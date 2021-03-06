# Python Package Test

## Tips for obfuscating code

- Compile core parts of proprietary code as cython modules.
    - It's important to compile cython with `--inplace` (done automatically as part of `pip install -e .`) so the resulting `.pyd` files will be automatically included instead of the `.py` files.

## Cython

To handle auto recompilation of cython files:
- use the file extension .pyx on files compiled with cython
- use `import pyximport; pyximport.install()`

This alone is enough to run the project as expected. However, autocompletion doesn't understand .pyx files, even if they only contain regular python. To fix this, we need to create stub files (.pyi).

### Generating stub files from .pyx files

Use `make_stub_files.py` from `deps/make-stub-files`.

```sh
python deps/make-stub-files/make_stub_files.py --force-pyx <file>
```

`.pyi` files are created inline.

> NOTE: vscode's "Run on Save" extension allows for this to be run on any .pyx file on save automatically.

`compile_cython.py` also generates stubs for any .pyx files it compiles.

## Building and Packaging

See `gen_exe.py`.

### Install the project as editable

> NOTE: Highly recommend doing this in a python virtual environment (`python -m venv venv`)!

Can work on the project with PYTHONPATH set correctly. Builds Cython files if needed.

```sh
# Install in editable mode and generate cython files
pip install -e .
```

### Package into exe

#### PyInstaller

```sh
# Create 'one folder' build with exe and all the deps of the given file
# Exe: ./dist/main/main.exe
#
# -OO: do optimizations + strip docstrings
#   - ref: https://pyinstaller.readthedocs.io/en/stable/usage.html#running-pyinstaller-with-python-optimizations
#   - optimizations include:
#     - __debug__ set to false
#     - assert statements are removed from bytecode
# NOTE: Use one folder mode to debug packaging
python -OO -m PyInstaller main.py
#
# NOTE: Windows defender sees the single exe as a trojan sometimes(?!)
# -F, --onefile: package into a single exe
#  - Increased startup time while it extracts into tmp.
```

Creating a reproducible build: https://pyinstaller.readthedocs.io/en/stable/advanced-topics.html#creating-a-reproducible-build
Encrypting Python Bytecode: https://pyinstaller.readthedocs.io/en/stable/advanced-topics.html#creating-a-reproducible-build
Supporting multiple operating systems: https://pyinstaller.readthedocs.io/en/stable/usage.html#supporting-multiple-operating-systems
- Need to bundle on each OS separately

##### Packaging the correct files

See this for packaging tips: https://github.com/pyinstaller/pyinstaller/wiki/How-to-Report-Bugs#make-sure-everything-is-packaged-correctly

Most useful:
- package it as a folder for debugging to see all the included files
- python files will be merged into the exe. Use `pyi-archive_viewer` (installed with pyinstaller) to view the exe archive.
    - check the `PYZ-*.pyz` archive, your code is likely there.

###### Packaging dependencies of cython files

Cython files (.pyx) can have imports. While pyinstaller follows and includes all of the imports of the provided file, it does not follow the imports of .pyx files. This becomes an issue when the cython file imports a dependency that is not imported by the rest of the non-cython parts of the application. This results in missing imports in the final exe.

There is a feature request, but it doesn't seem to be active: https://github.com/pyinstaller/pyinstaller/issues/1674

WARs:
- Include missing modules in a python file crawled by pyinstaller.
- Manually include missing modules.

##### Add Windows CRT

https://pyinstaller.readthedocs.io/en/stable/usage.html#windows

Download the runtime here: https://www.microsoft.com/en-US/download/details.aspx?id=48145

##### Optional: Compress the exe with UPX

https://upx.github.io/
https://pyinstaller.readthedocs.io/en/stable/usage.html#using-upx

Use `--upx-dir=' to point to the upx exe. If available pyinstaller will do it.

##### Optional: Populate exe version info

https://stackoverflow.com/a/54409096/3693388
https://pyinstaller.readthedocs.io/en/stable/usage.html#capturing-windows-version-data

Get a version info file generated from some arbitrary exe to get a template.

```sh
pyi-grab_version <some_exe>
```

Edit the generated file with the correct info.

Either pass the `--version-file=` arg to pyinstaller or use `pyi-set_version` to edit a created exe.

> NOTE: For some reason `--version-file=` path is relative to the spec file.

##### Optional: Create reproducible builds

https://pyinstaller.readthedocs.io/en/stable/advanced-topics.html#creating-a-reproducible-build

### Create Windows Installer exe

Create a Windows Installer EXE using Inno Setup (.iss files). Can use the Inno Wizard to create a setup script.

> NOTE: Using the single exe seems to have some untriaged run issues.

If using the Inno Setup VSCode extension:
- Have ISCC in PATH (Inno Setup's compiler)
- Open the .iss setup script as the active pane
- Run `> Inno Setup: Save & Compile Script`