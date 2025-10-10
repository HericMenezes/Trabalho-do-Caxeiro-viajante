import sys
import urllib.request

class In:
    def __init__(self, source=None):
        """Initializes an input stream from standard input, a file, or a URL."""
        self._buffer = []
        self._source_iter = None
        
        if source is None:
            self._source_iter = iter(sys.stdin.readline, '')
        else:
            try:
                # Try to open as a URL
                with urllib.request.urlopen(source) as f:
                    lines = [line.decode('utf-8') for line in f.readlines()]
                self._source_iter = iter(lines)
            except (ValueError, urllib.error.URLError):
                # Fallback to file
                try:
                    # open() returns an iterator directly
                    self._file = open(source, 'r', encoding='utf-8')
                    self._source_iter = self._file
                except IOError as e:
                    raise ValueError(f"Could not open source: {source}") from e
    
    def _fill_buffer(self):
        if self._buffer:
            return True
        try:
            line = next(self._source_iter)
            self._buffer.extend(line.strip().split())
            return True
        except StopIteration:
            return False

    def is_empty(self):
        return not self._fill_buffer()

    def read_string(self):
        if not self._fill_buffer():
            raise EOFError("Attempt to read from empty input stream")
        return self._buffer.pop(0)

    def read_int(self): return int(self.read_string())
    def read_double(self): return float(self.read_string())
    def read_float(self): return float(self.read_string())
    
    def read_boolean(self):
        s = self.read_string().lower()
        if s in ['true', '1']: return True
        if s in ['false', '0']: return False
        raise ValueError(f"Could not parse '{s}' as a boolean")

    def close(self):
        """Closes this input stream if it's a file."""
        if hasattr(self, '_file'):
            self._file.close()
