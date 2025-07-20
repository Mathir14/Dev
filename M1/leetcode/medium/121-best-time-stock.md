an easy problem to solve,
we are given an array,
we pick a value which is the date to buy,
we pick a value after that as the date we sell,
the goal is to get the max profit obtainable.

we set initial buy as the first element
and max profit as 0
then we iterate through the array from the 2nd element since buy is as first element first,
we compare buy value and value of the element in array, whichever is lowest is now buy

then to count the profit we use, current price - buy, if it is greater than max profit seen so far,
max profit is updated

the loop is closed once i has iterated through the array, the max profit obtained is returned

time complexity O(n)
space complexity O(1)