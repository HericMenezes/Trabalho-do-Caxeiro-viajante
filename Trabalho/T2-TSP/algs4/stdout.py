import sys

def println(x=""):
    """Prints the given argument to standard output, followed by a newline."""
    print(x)
    sys.stdout.flush()

def print_(x):
    """Prints the given argument to standard output, without a newline."""
    sys.stdout.write(str(x))
    sys.stdout.flush()

def printf(format_string, *args):
    """Prints a formatted string to standard output."""
    # Python's % formatting is similar to C's printf
    sys.stdout.write(format_string % args)
    sys.stdout.flush()
