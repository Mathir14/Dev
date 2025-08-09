````markdown
# Python `typing` Module – Backlog Clearance (2025-08-04)

---

## 1. Basic Type Hinting & Syntax Updates

- Function annotations example:
  ```python
  def func(x: int) -> str:
      return str(x)
  ```
````

- Python 3.10+ improvements (PEP 604 & PEP 585):

  - Use `|` instead of `Optional` or `Union`:

    ```python
    def f(x: str | None) -> int | None:
        ...
    ```

  - Use built-in generics (`list`, `dict`) instead of `List`, `Dict` from `typing`:

    ```python
    def f(data: list[int]) -> dict[str, str]:
        ...
    ```

---

## 2. Common Type Hints (Python 3.10+ syntax)

| Purpose                          | Syntax Example               |        |
| -------------------------------- | ---------------------------- | ------ |
| List of integers                 | `list[int]`                  |        |
| Dict with string keys, int vals  | `dict[str, int]`             |        |
| Optional int (int or None)       | \`int                        | None\` |
| Union of types (int or str)      | \`int                        | str\`  |
| Callable with specific signature | `Callable[[str, int], bool]` |        |
| Generic type variable            | `TypeVar('T')`               |        |

---

## 3. Key Syntax Rules

- Capitalize `None` (never `none`).
- Use valid parameter names, **not type names** like `Dict` or `List`.
- Use lowercase built-in generics (`dict`, `list`) in Python 3.9+.
- Ensure balanced brackets and parentheses.
- Function signature ends with colon `:`.
- Arrow `->` has no spaces inside (spaces before/after allowed).

---

## 4. Tested Correct Signatures

### a) Dict with `str` keys and values as `int` or `list[float | None]`

```python
def func(d: dict[str, int | list[float | None]]) -> list[str]:
    ...
```

### b) List of dicts mapping `str` to `int` or callable `(str, int) -> bool`

```python
from typing import Callable

def func(var: list[dict[str, int | Callable[[str, int], bool]]]) -> dict[str, int]:
    ...
```

### c) Generic function returning last element of a list

```python
from typing import TypeVar
T = TypeVar('T')

def last_item(items: list[T]) -> T:
    return items[-1]
```

---

## 5. Conceptual Points

- `Optional[X]` is identical to `X | None`—modern style prefers `|`.
- Use built-in generics (`list`, `dict`) over `List`, `Dict` from `typing` in Python 3.9+.
- `Callable[[ArgTypes], ReturnType]` accurately types function parameters and return.
- `TypeVar` enables writing generic, type-safe functions.

---

## 6. Common Mistakes Fixed

- Using type names (`Dict`, `List`) as parameter names — use normal variable names instead.
- Missing or unbalanced brackets/parentheses.
- Incorrect capitalization (`none` vs `None`).
- Wrong arrow syntax (`- >` instead of `->`).
- Forgetting colon at end of function signature line.
- Not importing `Callable` when using it.
