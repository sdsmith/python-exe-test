# Python Package Test

## Building and Packaging

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
# NOTE: Windows defender sees the single exe as a trojan...
# -F: package into a single exe
#  - Increased startup time. Means it
# one exe install
```

#### py2exe

> NOTE: Having trouble with the current setup script. After it's packaged into a windows installer and installed it seems to be broken.

```sh
python setup.py py2exe
```

### Create Windows Installer exe

Create a Windows Installer EXE using Inno Setup (.iss files). Can use the Inno Wizard to create a setup script.

> NOTE: Using the single exe seems to have some untriaged run issues.

If using the Inno Setup VSCode extension:
- Have ISCC in PATH (Inno Setup's compiler)
- Open the .iss setup script as the active pane
- Run `> Inno Setup: Save & Compile Script`