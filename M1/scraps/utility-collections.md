# 📦 Python Standard Library – `collections` Module

**Topics:** `Counter`, `defaultdict`, `deque`

---

## 🔹 Counter

### ✅ What it is:

A subclass of `dict` for counting hashable items. Behaves like `defaultdict(int)` with added features for counting, frequency analysis, and arithmetic.

### 🔧 Syntax:

```python
from collections import Counter

c = Counter("aabbbc")
print(c)  # {'a': 2, 'b': 3, 'c': 1}
```

### 🔑 Behavior:

- Accessing a missing key returns `0`, not KeyError

  ```python
  c = Counter("abc")
  print(c['z'])  # 0
  ```

- Counting elements from iterables:
  ```python
  Counter([1,2,2,3])  # {1:1, 2:2, 3:1}
  ```

### 🧪 Useful Methods:

| Method            | Description                                    |
| ----------------- | ---------------------------------------------- |
| `.most_common(n)` | Returns list of top n most frequent elements   |
| `.elements()`     | Iterator over elements, repeating as per count |
| `.update()`       | Adds counts from another iterable or mapping   |
| `c1 + c2`         | Adds counts per key                            |
| `c1 - c2`         | Subtracts, removes non-positive results        |

### ✍️ Examples:

```python
Counter("aabb") - Counter("ab")
# Output: Counter({'a': 1, 'b': 1})
```

```python
Counter([1,2,3,2,1,1]).most_common(1)
# Output: [(1, 3)]
```

---

## 🔹 defaultdict

### ✅ What it is:

A dict subclass that auto-creates missing keys with a default value, defined by a factory (like `int`, `list`, `set`, or custom `lambda`).

### 🔧 Syntax:

```python
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)  # No KeyError even though 'a' was missing
```

### 🔑 Behavior:

- **No need to check for key existence.**
- Useful for:
  - Frequency counting (`int`)
  - Grouping data (`list`)
  - Unique item sets (`set`)
  - Custom fallback (`lambda`)

### ✍️ Examples:

#### Count letters (like Counter):

```python
from collections import defaultdict

d = defaultdict(int)
for ch in "aabbcc":
    d[ch] += 1
```

#### Group anagrams:

```python
words = ["bat", "tab", "tap", "pat", "cat"]
grouped = defaultdict(list)
for word in words:
    grouped["".join(sorted(word))].append(word)

print(list(grouped.values()))
# [['bat', 'tab'], ['tap', 'pat'], ['cat']]
```

#### Custom fallback:

```python
d = defaultdict(lambda: "N/A")
print(d['missing'])  # 'N/A'
```

---

## 🔹 deque

### ✅ What it is:

Double-ended queue. Supports fast appends and pops from both ends. Great for implementing queues, stacks, and sliding windows.

### 🔧 Syntax:

```python
from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)
dq.pop()
```

### 🔑 Performance:

- `append`, `pop`, `appendleft`, `popleft` → **O(1)**
- Faster than list for left-end operations

### 🧪 Useful Methods:

| Method           | Description                                             |
| ---------------- | ------------------------------------------------------- |
| `.append(x)`     | Add to right                                            |
| `.appendleft(x)` | Add to left                                             |
| `.pop()`         | Remove from right                                       |
| `.popleft()`     | Remove from left                                        |
| `.rotate(n)`     | Rotate elements right (positive n) or left (negative n) |
| `.clear()`       | Remove all items                                        |

### ✍️ Examples:

```python
dq = deque([1, 2, 3, 4])
dq.rotate(2)
print(dq)  # deque([3, 4, 1, 2])
```

```python
dq = deque([1, 2, 3, 4])
dq.pop()       # removes 4
dq.popleft()   # removes 1
print(dq)      # deque([2, 3])
```

---

## 🧠 Quizzes (and answers)

### Counter Quiz

1. `Counter('aabbbc')` → `{'a': 2, 'b': 3, 'c': 1}`
2. Get top 2 elements: `Counter(...).most_common(2)`
3. `Counter("aabb") - Counter("ab")` → `{'a': 1, 'b': 1}`
4. Supports arithmetic (`+`, `-`, `&`, `|`) → **True**
5. `Counter([1,2,3,2,1,1]).most_common(1)` → `[(1, 3)]`
6. Accessing `Counter("abc")['z']` → `0`

---

### defaultdict Quiz

1. `defaultdict(list)`, `d['x'].append(10)` → `{'x': [10]}`
2. `defaultdict(int)` auto-creates keys with 0
3. Fill in:
   ```python
   from collections import defaultdict
   d = defaultdict(int)
   d['missing'] += 1
   ```
4. Can use custom factories like lambda → **True**
5. `list` allows duplicates, `set` doesn't
6. Grouping example → 3 keys with grouped anagrams

---

### deque Quiz

1. `.popleft()` is **O(1)** → **Correct**
2. `dq.appendleft(0)` → adds to the left
3. `.rotate(2)` → rotates right by 2 (e.g., `[1,2,3,4]` → `[3,4,1,2]`)
4. deque faster than list for queue ops → **True**
5. After `pop()` and `popleft()` on `[1,2,3,4]` → `[2,3]`
6. Clear a deque: `dq.clear()`

---
