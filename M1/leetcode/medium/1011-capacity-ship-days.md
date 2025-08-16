A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

Example 2:
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

Example 3:
Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1

we need smallest ship capacity to ship all weights in given days.
capacity must be at least max(weights) and at most sum(weights).

binary search on capacity.
for each mid capacity, simulate shipping:

start with empty ship, add weights until exceeding mid.

if exceed, start next day, reset current.
count days_taken.

if days_taken > days, capacity too small → low=mid+1.
else, capacity enough or more → high=mid.
loop until low=high. answer=low.

dry run
weights=[1,2,3,1,1], days=4

low=max=3, high=sum=8

mid=5 → simulate:
day1: 1+2+3=6>5 → stop at 1+2=3, new day.
day2: 3 → ok.
day3: 1+1=2 → ok.
total 3 days ≤ 4. so high=5.

low=3, high=5 → mid=4.
simulate:
day1: 1+2=3, next 3 → exceeds 4. stop.
day2: 3.
day3: 1+1=2.
total 3 days ≤4 → high=4.

low=3, high=4 → mid=3.
simulate:
day1: 1+2=3, next 3 → exceeds. stop.
day2: 3.
day3: 1.
day4: 1.
total 4 days =4 → ok. high=3.

low=3, high=3 → stop.
answer=3.
