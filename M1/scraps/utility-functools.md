# functools Quick Reference

## lru_cache

Cache function results to speed up repeated calls (memoization).

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(40))
print(fib.cache_info())  # hits, misses, maxsize, currsize
fib.cache_clear()        # clears cache
```

## reduce

Apply a function cumulatively to items in an iterable.

```python
from functools import reduce
import operator

nums = [1, 2, 3, 4]
product = reduce(operator.mul, nums)  # 24
```

- Raises `TypeError` if iterable is empty and no initializer given.
- To avoid error:

```python
reduce(lambda x, y: x + y, [], 0)  # returns 0
```

## partial

Create a new callable by pre-filling some arguments of a function.

```python
from functools import partial

def greet(name, punctuation):
    return f"Hello {name}{punctuation}"

exclaim = partial(greet, punctuation='!')
print(exclaim("Alice"))  # Hello Alice!
```

---

**Summary:**

- `lru_cache`: memoize expensive pure functions.
- `reduce`: cumulative folding; needs initializer on empty iterables.
- `partial`: fix arguments, get simplified callable.

```

```
