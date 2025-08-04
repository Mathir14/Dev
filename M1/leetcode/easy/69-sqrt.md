Square Root Problem – Notes & Learnings

What I Tried:

Revisited the classic integer square root problem.
Solved it using different methods to compare performance, readability, and logic.

Methods Explored:

Built-in (Fastest but banned in interviews)

Fastest in practice
Uses float, banned in most DSA problems

Newton-Raphson (Purposeful and efficient)

Integer math only
Fastest custom method (log(log n) iterations)
Actually solves the equation x² = n
Feels like doing real math, not just logic

Binary Search (Tried, but felt roundabout)

Why am I squaring guesses instead of just solving it?
Works, but feels like a logic test, not a real solution.

Bitwise (Cool, low-level, but overkill in Python)

Slower than Newton in Python
Only shines in C or embedded work

Final Thoughts:

I’d rather use a method that actually solves the equation instead of playing hot/cold with guesses.

Dropped binary search because it felt too indirect.
Chose Newton-Raphson for its elegance + performance.
Kept built-in version for general use when no constraints.

Use builtin when allowed.
Use newton when it matters.
Forget the rest.
