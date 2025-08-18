You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.

Example 1:

Input: arr = [0,1,0]

Output: 1

Example 2:

Input: arr = [0,2,1,0]

Output: 1

Example 3:

Input: arr = [0,10,5,2]

Output: 1

low = 0, high = len(arr) - 1 → search boundaries.

While loop runs until low == high.

At each step:

If arr[mid] < arr[mid+1] → slope is increasing, so peak is to the right → move low = mid + 1.

Else → slope is decreasing or at peak → move high = mid.

When loop ends, low == high → that’s the peak index.

Correct time complexity: O(log n).
Space complexity: O(1).

Note : same as 162-peak-index-element
