# cucheckargs
The idea behind this script is to check that one passes the correct number of arguments to a CuPY
RawKernel function. 

## Example
Use CuPy to construct a RawKernel function, e.g., 
```python
import checkargs
import cupy as cp
import numpy as np

source = """
extern "C" __global__ void copy(float *a, float *b) {
    a[i] = b[i];
}
"""
```
Before calling the kernel, call `checkargs`
```python
n = cp.int32(10)
block = (n,)
grid = (1,)
a = cp.random.rand(n ,dtype=cp.float32)
b = cp.random.rand(n, dtype=cp.float32)

# OK
checkargs.checkargs(source, "copy", (a, b)) 

# TypeError: copy takes 2 positional arguments but 3 were given.
#checkargs.checkargs(source, "copy", (a, b, b)) 

copy(grid, block, (a, b))
```

## TODO
* Add support for type checking.
