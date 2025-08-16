Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

search space = [1 .. max(piles)].
mid = possible eating speed.

simulate hours: each pile takes ceil(pile/mid) hours. break early if > h.
if total hours > h → too slow → increase low.

else possible → try smaller → decrease high.
final low = minimum eating speed that finishes in h hours.

dry run
piles=[3,6,7,11], h=8

low=1, high=11
mid=6 → hours=1+1+2+2=6 ≤ 8 → high=5
mid=3 → hours=1+2+3+4=10 > 8 → low=4
mid=4 → hours=1+2+2+3=8 ≤ 8 → high=3
low=4, high=3 → stop

ans=4
