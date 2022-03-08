import contextlib
import os
import shutil


@contextlib.contextmanager
def create_output_directory():
    """
    Create and enter an output directory; used as context manager.

    Args:
        rm_dir: bool
            Remove the directory when finished
    """
    if os.path.isdir("output"):
        shutil.rmtree("output")
    cwd = os.getcwd()
    os.mkdir(os.path.join(cwd, "output"))
    os.chdir(os.path.join(cwd, "output"))
    yield
    os.chdir(cwd)
