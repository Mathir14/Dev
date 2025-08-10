````markdown
# Regex + Dataclasses — Condensed Notes (2025-08-10)

---

## Dataclasses — What & Why

- **Goal:** Cut down boilerplate for classes that just hold data.
- `@dataclass` auto-creates methods like:

  - `__init__` — constructor (no more manual `self.x = x`)
  - `__repr__` — easy print/debug output
  - `__eq__` — compare objects by values, not memory
  - `__hash__` — lets you use instances as dict keys/sets (only if immutable/frozen)

- Use `field()` when:

  - You need default mutable values (like lists) without sharing them
  - You want to tweak how fields behave (exclude from `repr`, etc.)

- `frozen=True` makes class immutable (read-only) and hashable.

---

### Example:

```python
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Point:
    x: int
    y: int
    tags: list = field(default_factory=list)  # safe default list
```
````

---

### Why bother?

- Saves you from writing repetitive `__init__`, `__repr__`, `__eq__` manually
- Cleaner, less error-prone, consistent with type hints
- With `frozen=True`, object is hashable & immutable, so usable as dict key or in sets

---

## `__eq__` vs `__hash__`

- `__eq__`: compare two objects by their content (fields), not by memory. Needed for `==`.
- `__hash__`: returns an int hash value, needed if you want object as dict key/set member. Works reliably only if object is immutable.
- Dataclasses handle these automatically when you set `frozen=True`.

---

## Regex in Python — The Basics

- All regex stuff lives in `re` module:

  ```python
  import re
  ```

### Main functions

| Function       | What it does                       |
| -------------- | ---------------------------------- |
| `re.search()`  | Find first match anywhere          |
| `re.match()`   | Match only at start of string      |
| `re.findall()` | Return list of all matches         |
| `re.sub()`     | Replace matches with a replacement |

---

### Basic syntax symbols

| Symbol   | Meaning                          |
| -------- | -------------------------------- |
| `.`      | Any char except newline          |
| `^`      | Start of string/line             |
| `$`      | End of string/line               |
| `\d`     | Digit (0-9)                      |
| `\w`     | Word char (a-z, A-Z, 0-9, \_)    |
| `\s`     | Whitespace (space, tab, newline) |
| `[...]`  | Character class                  |
| `[^...]` | Negated class                    |
| `*`      | 0 or more repetitions            |
| `+`      | 1 or more repetitions            |
| `?`      | 0 or 1 (also non-greedy)         |
| `{m,n}`  | Between m and n repeats          |

---

### Capturing groups `( )`

- Group parts of a pattern and capture for extraction
- Use `.group(n)` or `re.findall()` to get captured pieces

Example:

```python
pattern = r'(\w+)@(\w+\.\w+)'
match = re.search(pattern, "test@example.com")
print(match.group(1))  # 'test'
print(match.group(2))  # 'example.com'
```

---

### Flags — tweak how regex works

| Flag                     | Effect                                   |
| ------------------------ | ---------------------------------------- |
| `re.I` / `re.IGNORECASE` | Ignore case                              |
| `re.M` / `re.MULTILINE`  | `^` and `$` match start/end of each line |
| `re.S` / `re.DOTALL`     | `.` matches newline too                  |
| `re.X` / `re.VERBOSE`    | Allow whitespace and comments in pattern |

Example:

```python
pattern = r'^hello'
text = "Hello\nhello"
re.findall(pattern, text, re.I | re.M)  # ['Hello', 'hello']
```

---

### Lookarounds (zero-width assertions)

- Assert something **ahead** or **behind** current position without consuming chars

| Type                | Syntax     | What it does                      |
| ------------------- | ---------- | --------------------------------- |
| Positive Lookahead  | `(?=...)`  | Assert next chars match pattern   |
| Negative Lookahead  | `(?!...)`  | Assert next chars don’t match     |
| Positive Lookbehind | `(?<=...)` | Assert previous chars match       |
| Negative Lookbehind | `(?<!...)` | Assert previous chars don’t match |

Example:

```python
text = "foo123 bar456"

# Positive lookahead: words followed by 3 digits
print(re.findall(r'\w+(?=\d{3})', text))  # ['foo', 'bar']

# Negative lookbehind: digits not preceded by 'foo'
print(re.findall(r'(?<!foo)\d+', text))   # ['456']
```

---

## Key points

- `==` compares object identity by default; with `__eq__` (dataclasses provide) it compares values.
- Hashable objects must be immutable; `@dataclass(frozen=True)` makes this easy.
- Regex groups let you grab parts of text easily.
- Flags and lookarounds add power and control without complicating core patterns.
- `re.search()` vs `re.match()` difference is scope of matching in string.
