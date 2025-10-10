import time

class Stopwatch:
    """
    The Stopwatch data type is for measuring the time that elapses 
    between the start and end of a programming task.
    """

    def __init__(self):
        """Initializes a new stopwatch."""
        self._start = time.perf_counter()

    def elapsed_time(self):
        """
        Returns the elapsed time (in seconds) since the stopwatch was created.
        """
        now = time.perf_counter()
        return now - self._start
