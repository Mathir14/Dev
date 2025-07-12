in place:
modifying the original data structure without using extra space or copying it to another data structure

this problem requires removing of the elements in list nums that matches with the given value val
without creating a new list

and the problem requires us to return k, which is the count of elements not equal to val in list nums

decided to use two pointers to solve this problem

pointer i starts from the beginning and pointer k at the end (len(nums))

use while i < k to make sure they don't overlap each other

used i to check the element with val, if it matches
replaced it with the element from k-1
and reduce k by 1 moving k to the left

if it doesnt match increment i by 1 moving i to the right

note: 
i isn't incremented when it matches in-case of the value k-1 assinged to i being matched with val too,
at the next iteration i is still in same index and is checked with val to make sure it does not match 
before moving i to the right

and finally we return the k as required
the concept of in place is new to me and made me realize there are other ways to deal with problemsinstead of just hashmaps or building new data structures 