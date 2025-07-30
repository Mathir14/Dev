You’re given a binary array and an integer k. The task is to return the maximum number of consecutive 1’s in the array if you’re allowed to flip at most k zeroes to ones.

Let’s break it down.

You want the longest subarray possible where at most k zeros exist. So for example, if k = 2, and you see three zeros in a subarray, that subarray is invalid. You’re allowed to flip only two.

So how do we handle this?
Sliding window. Two pointers. Left and right.

We start both at the beginning of the array. The right pointer expands the window — goes one step at a time.
Every time we see a zero at `nums[right]`, we increment a counter. This counter keeps track of how many zeros are in the current window.

Now, if that count ever goes above k, we shrink the window from the left side until it's valid again — that is, until the zero count drops back to k or below. That means moving the `left` pointer and checking if the thing you're removing from the left is a zero — if yes, decrease the counter.

At every step, while moving the right pointer, you keep track of the longest window you’ve seen so far that fits the rule (zeroes <= k). That’s your answer.

why this works:
because the window always expands when it's valid and only shrinks when it breaks the rule. This ensures that all valid subarrays are being considered, and we never re-check anything unnecessarily.

let’s say the input is:
nums = [1,1,0,0,1,1,1,0,1], k = 2

you start scanning from left to right
every time you hit a 0, you’re spending one flip.

the moment you overspend (i.e., zero count > k), you shift the window from the left until you're within budget again.
while doing this, you keep tracking the max window length seen so far.

this second one works because it treats k as the number of 0s you can afford to flip.
every 0 costs 1 flip.

when you run out of flips (k < 0), you move the left pointer to shrink the window.
if you’re removing a 0, you refund one flip back to k.

it’s cleaner but same logic.

space complexity is O(1)
time complexity is O(n)
