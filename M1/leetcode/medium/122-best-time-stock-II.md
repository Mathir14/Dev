sequel to the best time to buy and sell stock problem
in the original problem we were asked to return the most profit attainable in a single transaction -
buy and sell

in this problem, we are asked to return the total profit that can be made if we bought low and sold high every single time
we can sell a stock and buy it again the same day,

we used a single for loop,
with i starting from the element at idx 1,
we check if the current value is greater than previous value of i using i-1
if it is,
we buy at i-1 and sell at i and store this in the total profit
the profit is the sell price - buy price

time O(n)
space O(1)
