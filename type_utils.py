# Copyright (c) 2017 Chao Ji

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==============================================================================
import numpy as np


def isint(i):
  """Returns if input is of integer type."""
  return isinstance(i, (int, np.int8, np.int16, np.int32, np.int64))

def is_variable(v):
  """Returns if input is of variable type."""
  return type(v).__name__ == 'Variable'

def to_numpy(val):
  """Converts input to a numpy array."""
  if not isinstance(val, np.ndarray):
    val = np.array(val).astype(np.float32)
  if np.isnan(val) is True or np.isnan(val).any():
    raise ValueError('ALL value passed as input to `Constant` node must be '
        'determined at graph construction type')
  return val

def is_numeric(val):
  """Returns if input is of numeric type."""
  return isinstance(val, (int, float,
                          np.int8, np.int16, np.int32, np.int16, np.int64,
                          np.float16, np.float32, np.float64))
