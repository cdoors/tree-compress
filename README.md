# TreeCompress

**TreeCompress** is a lightweight, open-source Python script that combines multiple text-based files from your local project into a single Markdown file for easy reference, context sharing, or large-scale text ingestion. Unlike Gitingest or Repomix, TreeCompress is designed for **local** use only, so you can keep your entire codebase or documentation private without uploading it to an external service.

## How It Works
1. **Directory Tree Generation**: It scans your project folder to build a tree-like structure of all files and folders, excluding any directories or files you choose to ignore.
2. **Content Packaging**: It then reads each text-based file (e.g., `.py`, `.js`, `.md`, `.txt`) in UTF-8 mode and writes their contents into a single Markdown file, `all_docs.md`.
3. **Code Block Formatting**: Files are included with Markdown code fences, preserving syntax highlighting for a wide array of languages and file types.

## Why TreeCompress?
- **Local-Only, No External Upload**: If you prefer not to push your codebase to online platforms like GitHub or GitLab, TreeCompress is an excellent choice to keep everything offline and under your control.
- **Open Source & Lightweight**: The script is a few lines of Python and can be modified easily to fit your needs.
- **Large Context Aggregation**: Perfect for local Large Language Model (LLM) workflows that benefit from having an entire repository’s text in a single file.
- **Customizable**: Add or remove file extensions, change ignore rules, or adapt the script for your specific environment.

## Installation
1. **Clone or Download** this repository (or copy the single script file `tree_compress.py` into your project’s root directory).
2. Ensure you have **Python 3.6+** installed on your system.

## Usage
From your project’s root directory:

```bash
python tree_compress.py
```

### Configuration
In the script, you can modify:
- **Ignore Directories**: (e.g., `.git`, `.venv`, `node_modules`, `__pycache__`)  
- **Ignore Files**: (e.g., the output Markdown `all_docs.md`, or any other you don’t want included)  
- **Extension to Language** Mapping: Tweak or extend the code-block language detection.  

After running, you’ll get `all_docs.md` in your project folder containing:
1. A directory tree overview.
2. The contents of every UTF-8 readable file wrapped in Markdown code blocks.

## Example
Here’s a condensed view of the output file’s structure:

```markdown
# Project Documentation

## Directory Structure

```
your_project/
├── src/
│   ├── app.py
│   └── helpers.js
├── docs/
│   └── README.md
└── requirements.txt
```

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
We welcome suggestions, bug reports, and feature requests! Feel free to open an issue or submit a pull request if you have ideas for improvement. Because this tool runs entirely locally, you can safely fork and modify it to fit your own security or workflow requirements.

## License
This project is licensed under the [MIT License](LICENSE). Feel free to use it in personal, academic, or commercial projects. 

---

Feel free to rename the script or adapt its functionality to match your exact needs!
