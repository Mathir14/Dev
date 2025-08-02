**os module**

- `os.getcwd()`
  Get current working directory

- `os.chdir('scripts')`
  Change current directory

- `os.listdir()`
  List contents of current directory

- `os.remove('file.txt')`
  Delete a file

- `os.mkdir('folder')`
  Create a new folder

- `os.rmdir('folder')`
  Remove a folder (only if empty)

- `os.makedirs('parent/child')`
  Create nested folders

- `os.path.join('backup', 'log.txt')`
  Join folder and file into valid path

- `os.path.exists('path/to/file')`
  Check if path exists

---

**sys module**

- `sys.argv[1]`
  Access command line argument at index 1 (0 is script name)

- `sys.exit(1)`
  Exit program with status code (0 = success, 1 = failure)

- `sys.path.append('/my/custom/modules')`
  Add custom module directory for imports

- `sys.version`
  Get current Python version as a string

- `sys.stdout = open('out.txt', 'w')`
  Redirect all print output to file

- `sys.stderr = open('err.txt', 'w')`
  Redirect error messages to file

---

**pathlib module**

- `from pathlib import Path`
  Import the modern path interface

- `Path('folder') / 'file.txt'`
  Join paths (cross-platform, cleaner than string concat)

- `Path('notes.txt').exists()`
  Check if file exists

- `Path('notes.txt').unlink()`
  Delete file (like `os.remove`)

- `Path('folder').mkdir(parents=True, exist_ok=True)`
  Create folder and any necessary parent folders

- `for file in Path('.').glob('*.txt'):`
  List all `.txt` files in current directory

- `for file in Path('.').rglob('*.py'):`
  Recursively list all `.py` files in subfolders

- `Path('notes.txt').resolve()`
  Return absolute path, resolving symlinks/relative parts

- `Path('greet.txt').write_text('hello')`
  Write text to file

- `text = Path('greet.txt').read_text()`
  Read text from file
