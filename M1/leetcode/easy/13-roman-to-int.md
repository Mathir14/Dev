a clever problem which is about converting Roman numericals to it's integer equivalent
some info on how Roman numerals work from the problem description:

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

so subtracting in Roman numerals happen kinda opposite to how you would naturally do,
instead of a - b where you would subtract b from a, it's the opposite, in Roman numerals, 
a - b is subtracting a from b as you can see from it's description
so if we want to handle subtraction in Roman numerals, we would also have to go the opposite way,
in this case, traversing the Roman numerical string from the reverse,

we store the values in a dict for faster lookups,
there are two variables, total : to return the integer value and prev : to keep track of the last element iterated from the reverse
in a for loop, we reverse the string
we check if the current value is lesser than prev
which would be something like, IV
prev being V and current being I
and curr is lesser than prev, so to simulate Roman subtraction, we simply decrease the total by curr, total -= curr
which is just, adding V-5 and subtracting I-1 which is IV 4
exactly what we need,
now if the current is not lesser than prev,
like VI which is normal, then we simply add the value of the curr to total and assign prev = curr
this loop iterates till there is element left in the string,
after the operations, the total is returned