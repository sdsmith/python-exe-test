if __debug__:
    # Use pyximport to avoid having to recompile cython modules every code change. Only triggers compilation for .pyx files.
    import pyximport
    # NOTE: install(pyimport=True) runs cython on all python files and falls back to the original python file on error
    pyximport.install()

from hello import hello
from hello import foo

if __name__ == '__main__':
    hello()