import subprocess
import platform

main_file = 'main.py'

# Ensure latest code is installed and cython compiled
subprocess.run(['pip', 'install', '-e', '.'], shell=True, check=True)
# Create exe
subprocess.run(['python', '-OO', '-m', 'PyInstaller', main_file], shell=True, check=True)

if platform.system() == 'Windows':
    # Create windows installer
    subprocess.run(['iscc', 'inno_folder_exe_setup.iss'], shell=True, check=True)

else:
    print(f'WARNING: skipping creating installer, unsupported system ({platform.system()})')