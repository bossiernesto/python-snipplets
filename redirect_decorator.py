from os import dup, open, close, O_WRONLY, O_CREAT
from functools import wraps
import sys


def exit_with_error(error="Non Specified Error"):
    """
        Terminates with an error
    """
    print(error)
    sys.exit(1)


def open_if_exists(filename, mode='rb'):
    """Returns a file descriptor for the filename if that file exists,
    otherwise `None`.
    """
    try:
        return open(filename, mode)
    except IOError as e:
        exit_with_error('Cant open file {0}. Reason {1}'.format(filename, e.msg))


def redirect_fork(filename):
    """
        Decorates a function with a forked process
    """

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            old = dup(1)
            open_if_exists(filename,
                           O_WRONLY | O_CREAT)  # It exists if an error occurs, if you want to throw an exception on error, refactor this method
            try:
                func(*args, **kwargs)
            finally:
                sys.stdout.flush()
                close(1)
                dup(old)
                close(old)

        return wrapper

    return decorate


if __name__ == "__main__":
    file = 'test.txt'
    input = "Hello World\n"

    @redirect_fork(file)
    def printToFile():
        print(input)

