"""String terminator module."""

import numpy as np

def terminator(string):
    """Terminate a string."""
    return string + "."

def mod_v2(x,n):
    """Return x mod n, but with no pesky zeros."""

    output = np.array(np.mod(x,n))
    output[output == 0] = n
    return output