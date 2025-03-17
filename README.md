# TreeCompress

**TreeCompress** is a lightweight, open-source Python script that combines multiple text-based files from your local project into a single Markdown file for easy reference, context sharing, or large-scale text ingestion. Unlike Gitingest or Repomix, TreeCompress is designed for **local use only**, keeping your codebase or documentation private.

## How It Works

1. **Directory Tree Generation**: Scans your project folder, building a tree structure of files and folders, excluding directories/files you specify.
2. **Content Packaging**: Reads each text-based file (e.g., `.py`, `.js`, `.md`, `.txt`) and compiles their contents into a single Markdown file (`all_docs.md`).
3. **Code Block Formatting**: Files are included with Markdown code fences for syntax highlighting.

## Why TreeCompress?

- **Local-Only, No External Upload**: Keeps your data offline and private.
- **Open Source & Lightweight**: Easily modifiable Python script.
- **Large Context Aggregation**: Ideal for local Large Language Model (LLM) workflows.
- **Customizable**: Modify file extensions, ignore rules, and language mappings.

## Installation

1. Clone or download this repository, or copy `tree_compress.py` directly into your project's root directory.
2. Ensure you have **Python 3.6+** installed.

## Usage

Run the script from your project's root directory:

```bash
python tree_compress.py
```

### Configuration

Modify within the script:
- **Ignored Directories**: e.g., `.git`, `.venv`, `node_modules`, `__pycache__`  
- **Ignored Files**: e.g., output file `all_docs.md`, or other specific files
- **Extension to Language Mapping**: Customize code-block language detection.

After running, you'll have `full_directory.md` containing:
- A directory tree overview
- Contents of each file wrapped in Markdown code blocks

## Example Output Structure

```markdown
# Project Documentation

## Directory Structure

your_project/
├── src/
│   ├── app.py
│   └── helpers.js
├── docs/
│   └── README.md
└── requirements.txt

## File Contents

# src/app.py

```python
print("Hello from app.py!")
```

---

# src/helpers.js

```javascript
function greet(name) {
    return `Hello, ${name}`;
}
```

---

...
```

## Contributing

Suggestions, bug reports, and feature requests are welcome! Open an issue or submit a pull request. Feel free to fork and modify the tool to fit your own workflow.

## License

Licensed under the [MIT License](LICENSE). Feel free to use it for personal, academic, or commercial projects.

---

Adapt the script freely to match your exact needs!

