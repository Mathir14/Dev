# ✅ Python Standard Library Summary (Mastered)

**Modules**: `math`, `random`, `datetime`, `time`  
**Status**: ✔️ Learned, Quizzed, and Understood

---

## 📐 `math` — Mathematical Functions

| Function            | Purpose                         |
| ------------------- | ------------------------------- |
| `math.sqrt(x)`      | Square root                     |
| `math.pow(x, y)`    | x to the power y (float result) |
| `math.floor(x)`     | Round down to nearest int       |
| `math.ceil(x)`      | Round up to nearest int         |
| `math.trunc(x)`     | Chop off decimal (toward 0)     |
| `math.fabs(x)`      | Absolute value (float result)   |
| `math.factorial(x)` | Compute x! (x ≥ 0, int only)    |
| `math.gcd(a, b)`    | Greatest common divisor         |
| `math.pi`, `math.e` | Math constants                  |
| `math.sin(x)`       | Sine (radians)                  |
| `math.cos(x)`       | Cosine                          |
| `math.tan(x)`       | Tangent                         |
| `math.radians(x)`   | Degrees → Radians               |
| `math.degrees(x)`   | Radians → Degrees               |

---

## 🎲 `random` — Pseudo-Random Generators

| Function                   | Purpose                                  |
| -------------------------- | ---------------------------------------- |
| `random.random()`          | Float in [0.0, 1.0)                      |
| `random.randint(a, b)`     | Int in [a, b] (inclusive)                |
| `random.randrange(a, b)`   | Int in [a, b) (exclusive upper bound)    |
| `random.uniform(a, b)`     | Float in [a, b]                          |
| `random.choice(seq)`       | Random 1 item from list/str/tuple        |
| `random.choices(seq, k=n)` | List of k items, **with** replacement    |
| `random.sample(seq, k=n)`  | List of k items, **without** replacement |
| `random.shuffle(list)`     | Shuffle a list in place (Fisher-Yates)   |
| `random.seed(x)`           | Set seed for repeatable randomness       |

---

## 📅 `datetime` — High-Level Date and Time

| Function                    | Purpose                      |
| --------------------------- | ---------------------------- |
| `datetime.now()`            | Current local datetime       |
| `date.today()`              | Today's date only            |
| `datetime.strptime(s, fmt)` | Convert string → datetime    |
| `datetime.strftime(fmt)`    | Convert datetime → string    |
| `timedelta(days=7)`         | Time delta object            |
| `datetime.timestamp()`      | Seconds since epoch as float |
| `datetime.fromtimestamp(x)` | Convert timestamp → datetime |
| `date(YYYY, MM, DD)`        | Create a date manually       |
| `time(HH, MM, SS)`          | Create a time manually       |

**Common Format Codes**:

- `%Y` = year, `%m` = month, `%d` = day
- `%H` = 24h, `%I` = 12h, `%p` = AM/PM
- `%M` = minute, `%S` = second, `%b` = month abbrev

---

## ⏱️ `time` — System Time & Low-Level Ops

| Function                          | Purpose                            |
| --------------------------------- | ---------------------------------- |
| `time.time()`                     | Current time as timestamp (float)  |
| `time.sleep(n)`                   | Pause execution for n seconds      |
| `time.ctime()`                    | Timestamp → readable string        |
| `time.localtime()`                | Get `struct_time` (local timezone) |
| `time.gmtime()`                   | Get `struct_time` (UTC)            |
| `time.strftime(fmt, struct_time)` | Format structured time → string    |
| `time.strptime(s, fmt)`           | String → `struct_time`             |

**`struct_time` fields**:

- `tm_year`, `tm_mon`, `tm_mday`
- `tm_hour`, `tm_min`, `tm_sec`
- `tm_yday` = day of year
- `tm_wday` = weekday (0 = Monday)
- `tm_isdst` = daylight saving flag

---

## ✅ Final Notes:

- `math` is for **pure math** with floats.
- `random` is for **simulations, games, randomness**.
- `datetime` is for **working with real-world date/time logic**.
- `time` is for **system-level timing, sleeping, timestamps**.

All modules fully covered, understood, and tested through quizzes.
