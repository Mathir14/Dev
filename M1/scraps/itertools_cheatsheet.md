# 🧠 `itertools` Cheat Sheet

## 1. `product()`

- Cartesian product of input iterables.
- Think: all combinations from nested loops.

```python
from itertools import product
list(product([1, 2], ['a', 'b']))
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

list(product([0, 1], repeat=3))
# [(0, 0, 0), ..., (1, 1, 1)]
```

## 2. `permutations()`

- All possible **ordered** arrangements (no repeats unless duplicates in input).

```python
from itertools import permutations
list(permutations([1, 2], 2))
# [(1, 2), (2, 1)]

list(permutations([1, 2, 2], 2))
# [(1, 2), (1, 2), (2, 1), (2, 2), (2, 1), (2, 2)]
```

## 3. `combinations()`

- All **unordered** unique groups, **without replacement**.

```python
from itertools import combinations
list(combinations([1, 2, 2], 2))
# [(1, 2), (1, 2), (2, 2)]
```

## 4. `combinations_with_replacement()`

- Same as `combinations()`, but allows same-element pairs like `(1, 1)` or `(2, 2)`.

```python
from itertools import combinations_with_replacement
list(combinations_with_replacement([1, 2, 2], 2))
# [(1, 1), (1, 2), (1, 2), (2, 2), (2, 2)]
```

## 5. `groupby()`

- Groups **consecutive identical values**.
- Doesn't merge values unless they’re next to each other.

```python
from itertools import groupby

for key, group in groupby([1, 2, 2, 1, 4, 4, 4, 3, 3]):
    print(key, list(group))

# Output:
# 1 [1]
# 2 [2, 2]
# 1 [1]
# 4 [4, 4, 4]
# 3 [3, 3]
```

```python
groupby('aaabbbccaadd')
# a ['a', 'a', 'a']
# b ['b', 'b', 'b']
# c ['c', 'c']
# a ['a', 'a']
# d ['d', 'd']
```

⚠️ Don’t wrap `groupby()` in `list()` before using it — group iterators get exhausted.

---

## 🧪 Mini Challenge Recap Answers

### `combinations([1, 2, 2], 2)`

```
[(1, 2), (1, 2), (2, 2)]
```

### `permutations([1, 2, 2], 2)`

```
[(1, 2), (1, 2), (2, 1), (2, 2), (2, 1), (2, 2)]
```

### `combinations_with_replacement([1, 2, 2], 2)`

```
[(1, 1), (1, 2), (1, 2), (2, 2), (2, 2)]
```

### `product(['a', 'b'], repeat=2)`

```
[('a', 'a'), ('a', 'b'), ('b', 'a'), ('b', 'b')]
```
