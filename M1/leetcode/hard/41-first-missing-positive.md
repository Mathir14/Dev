we are given an array of n size consisting elements of any value including negatives

our goal is to find the smallest positive element missing in the array
the core problem is simple but doing it in O(n) time and O(1) space is what's real about it

our solution mainly relies on the logic,
if an array has size n
then the smallest missing number would be something from 1 to n+1

we first sort the array in a way where all the elements are in the index i-1
for example value 3 at index 2 and so on
we take a value, check if it's within the bounds 1 <= x <= n
then check if it is not equal to value at x-1 to avoid duplicates

if it satisfies, we place the current value at index current value - 1, and swap the value at that index with current index
if this isn't satisfied, then we move to the next index

once the array is sorted,
we loop through it again to check if all the elements are equal to i + 1 where i is the element value,
so for 3 we check if it's equal to 2 + 1 since 3 is stored at index 2
and we move i to the next value

if this doesnt satisfy, we return i+ 1 which is the missing positive value

if no element is missing in the n sized array, we return n+1, yeah, just, do
