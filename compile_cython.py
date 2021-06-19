from glob import glob
import subprocess

subprocess.run(['python', 'setup.py', 'build_ext', '--inplace'], shell=True, check=True)

# Generate stubs to be compatible with autocomplete and other dev tooling
for file in glob('*.pyx'):
    subprocess.run(['python', 'deps/make-stub-files/make_stub_files.py', '--force-pyx', '-o', file], shell=True, check=True)
for file in glob('./src/**/*.pyx', recursive=True):
    subprocess.run(['python', 'deps/make-stub-files/make_stub_files.py', '--force-pyx', '-o', file], shell=True, check=True)