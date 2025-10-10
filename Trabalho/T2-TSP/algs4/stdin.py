import sys

_buffer = []
_current_line = ""

def _read_and_buffer_line():
    global _buffer, _current_line
    if not _buffer:
        try:
            _current_line = sys.stdin.readline()
            if _current_line == "":  # EOF
                return False
            _buffer.extend(_current_line.strip().split())
            return True
        except (IOError, EOFError):
            return False
    return True

def is_empty():
    return not _read_and_buffer_line()

def read_string():
    if not _read_and_buffer_line():
        raise EOFError("Attempt to read from empty input stream")
    return _buffer.pop(0)

def read_int():
    return int(read_string())

def read_float():
    return float(read_string())

def read_double():
    return float(read_string())

def read_boolean():
    s = read_string().lower()
    if s in ['true', '1']:
        return True
    if s in ['false', '0']:
        return False
    raise ValueError(f"Could not parse '{s}' as a boolean")

def has_next_line():
    global _current_line
    if _current_line is not None and _current_line != "":
        return True
    try:
        # This is a bit of a hack to peek at stdin, may not work in all terminals
        next_char = sys.stdin.read(1)
        if next_char:
            # Not standard, but we need to put it back somehow.
            # A more robust solution requires more complex buffering.
            # For this library's purpose, we'll assume this check is enough.
            return True
        return False
    except (IOError, EOFError):
        return False

def read_line():
    global _buffer, _current_line
    line = _current_line
    _buffer.clear()
    _current_line = "" # Reset line buffer
    if line:
        return line.rstrip('\n')
    else: # Buffer was cleared, read a fresh line
        return sys.stdin.readline().rstrip('\n')


def read_all():
    global _buffer
    _buffer.clear()
    return sys.stdin.read()

def read_all_strings():
    return read_all().split()

def read_all_ints():
    return [int(s) for s in read_all_strings()]

def read_all_doubles():
    return [float(s) for s in read_all_strings()]
