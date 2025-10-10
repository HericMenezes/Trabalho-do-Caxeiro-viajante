import random
import math

def set_seed(s):
    """Sets the seed of the pseudo-random number generator."""
    random.seed(s)

def get_seed():
    """
    Returns the seed of the pseudo-random number generator.
    Note: Python's random module doesn't have a direct get_seed method.
    This functionality is not directly supported.
    """
    raise NotImplementedError("Python's random module does not support getting the seed.")

def uniform_int(a, b=None):
    """
    Returns a random integer uniformly in [0, a) or [a, b).
    """
    if b is None:
        if a <= 0:
            raise ValueError("Argument must be positive")
        return random.randrange(a)
    else:
        if not (a < b):
            raise ValueError(f"Invalid range: [{a}, {b})")
        return random.randrange(a, b)

def uniform_double(a=0.0, b=1.0):
    """
    Returns a random real number uniformly in [a, b).
    """
    if not (a < b):
        raise ValueError(f"Invalid range: [{a}, {b})")
    return random.uniform(a, b)

def bernoulli(p=0.5):
    """
    Returns a random boolean from a Bernoulli distribution with success
    probability p.
    """
    if not (0.0 <= p <= 1.0):
        raise ValueError("Probability p must be between 0.0 and 1.0")
    return random.random() < p

def gaussian(mu=0.0, sigma=1.0):
    """
    Returns a random real number from a Gaussian distribution with mean mu
    and standard deviation sigma.
    """
    return random.gauss(mu, sigma)

def discrete(probabilities):
    """
    Returns a random integer from the specified discrete distribution.
    """
    if abs(sum(probabilities) - 1.0) > 1e-9:
        raise ValueError("Probabilities must sum to 1")
    return random.choices(range(len(probabilities)), weights=probabilities, k=1)[0]

def shuffle(a):
    """Rearranges the elements of the specified list in uniformly random order."""
    random.shuffle(a)

def permutation(n, k=None):
    """
    Returns a uniformly random permutation of n elements, or k of n elements.
    """
    if k is None:
        k = n
    return random.sample(range(n), k)
