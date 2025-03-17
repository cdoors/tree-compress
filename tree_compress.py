import os

# --------------------------------------------------------------------------------
# A dictionary mapping common file extensions to a language identifier that
# can be used in Markdown code blocks. This ensures syntax highlighting
# for the most common languages and file types.
# --------------------------------------------------------------------------------
extension_to_lang = {
    '.py': 'python',
    '.js': 'javascript',
    '.ts': 'typescript',
    '.java': 'java',
    '.c': 'c',
    '.cpp': 'cpp',
    '.h': 'c',
    '.hpp': 'cpp',
    '.html': 'html',
    '.css': 'css',
    '.md': 'markdown',
    '.txt': 'text',
    '.json': 'json',
    '.xml': 'xml',
    '.yml': 'yaml',
    '.yaml': 'yaml',
    # Add more extensions as needed
}

def get_tree(dir_path, prefix='', ignore_dirs=None, ignore_files=None):
    """
    Recursively generates a string representing a tree-like view
    of the directory structure starting from `dir_path`.

    Args:
        dir_path (str): The root directory to scan.
        prefix (str): Used internally for nested calls to handle indentation.
        ignore_dirs (list[str]): Directories to ignore while building the tree.
        ignore_files (list[str]): Files to ignore while building the tree.

    Returns:
        str: A string containing the tree representation of the directory.
    """
    # Set default ignore lists if not provided
    if ignore_dirs is None:
        ignore_dirs = []
    if ignore_files is None:
        ignore_files = []

    # Initialize the resulting tree string
    tree_str = ''

    # Retrieve a list of items (files + directories), excluding ignored ones.
    # Sorting ensures a consistent order in the output.
    items = sorted([
        item for item in os.listdir(dir_path)
        if not (os.path.isdir(os.path.join(dir_path, item)) and item in ignore_dirs)
        and not (os.path.isfile(os.path.join(dir_path, item)) and item in ignore_files)
    ])

    # Loop through each item and build the tree representation
    for i, item in enumerate(items):
        item_path = os.path.join(dir_path, item)

        # Connector is '└── ' for the last item or '├── ' otherwise
        connector = '└── ' if i == len(items) - 1 else '├── '
        # For nested levels, we adjust the prefix so it lines up nicely in the output
        new_prefix = prefix + ('    ' if i == len(items) - 1 else '│   ')

        # If it's a directory, recurse into it
        if os.path.isdir(item_path):
            tree_str += f"{prefix}{connector}{item}/\n"
            tree_str += get_tree(item_path, new_prefix, ignore_dirs, ignore_files)
        else:
            # Otherwise, it's a file, so just append it
            tree_str += f"{prefix}{connector}{item}\n"

    return tree_str

if __name__ == "__main__":
    # --------------------------------------------------------------------------------
    # Configuration Section
    # --------------------------------------------------------------------------------

    # 1. The directory from which we start collecting files.
    #    Using os.getcwd() means "use the current working directory."
    root_dir = os.getcwd()

    # 2. Directories to ignore (e.g., virtual environments, Git folders, etc.)
    ignore_dirs = ['.git', '.venv', 'node_modules', '__pycache__']

    # 3. Name of the output file that will contain all the docs
    output_file = 'full_directory.md'

    # 4. Any files to ignore. We definitely ignore the output file itself to avoid
    #    reading and duplicating it infinitely.
    ignore_files = [output_file, 'tree_compress.py']

    # --------------------------------------------------------------------------------
    # Building the Directory Tree
    # --------------------------------------------------------------------------------
    # This section uses the get_tree function above to create a human-readable
    # directory tree of everything under root_dir (except ignored items).
    root_name = os.path.basename(root_dir)
    tree_str = f"{root_name}/\n" + get_tree(
        root_dir,
        ignore_dirs=ignore_dirs,
        ignore_files=ignore_files
    )

    # --------------------------------------------------------------------------------
    # Writing the Output File (all_docs.md)
    # --------------------------------------------------------------------------------
    # We open all_docs.md in write mode, so existing content is overwritten.
    # The encoding is set to 'utf-8' to handle non-ASCII characters.
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write a title and the directory structure
        f.write("# Project Documentation\n\n")
        f.write("## Directory Structure\n\n")
        f.write("```\n")
        f.write(tree_str)
        f.write("\n```\n\n")
        f.write("## File Contents\n\n")

        # --------------------------------------------------------------------------------
        # Walking through all sub-directories and files
        # --------------------------------------------------------------------------------
        # os.walk() recursively iterates over all subdirectories and files starting at root_dir.
        for root, dirs, files in os.walk(root_dir):
            # Filter out ignored directories (so we don't descend into them)
            dirs[:] = [d for d in dirs if d not in ignore_dirs]

            # Go through each file in the current directory
            for file in files:
                # Skip ignored files, including our own output_file
                if file in ignore_files:
                    continue

                # Construct the full path to the file
                file_path = os.path.join(root, file)
                # Build a relative path for display in the Markdown
                relative_path = os.path.relpath(file_path, root_dir).replace('\\', '/')

                try:
                    # Attempt to open the file as text in UTF-8. If it fails, it's likely binary.
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        # Determine the code block language based on the file extension
                        ext = os.path.splitext(file)[1].lower()
                        lang = extension_to_lang.get(ext, 'text')  # Default to plain text if unknown

                        # Write a header for the file (using the relative path)
                        f.write(f"# {relative_path}\n\n")

                        # Write the opening code fence with the determined language
                        f.write(f"```{lang}\n")

                        # Write the file's contents line by line
                        for line in infile:
                            f.write(line)

                        # Close the code fence
                        f.write("\n```\n\n")
                        # Add a horizontal rule for visual separation
                        f.write("---\n\n")

                except UnicodeDecodeError:
                    # If we hit a UnicodeDecodeError, it's probably a binary file.
                    # We skip it because we only want to include text-based files.
                    pass
                except Exception as e:
                    # Print any other errors to help with debugging.
                    print(f"Error reading {file_path}: {e}")
