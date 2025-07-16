problem statement:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

the problem requires us to,
skip the non alpha numeric characters
and only compare the valid characters and return whether it forms a palindrome or not

this problem and palindromes in general are favored by two pointers
as this is a converging method,

we, as usual, have two pointers left and right
and as usual left is at 0 and right is at the end
we use while left <= right for the loop,

if the char at index left is not alpha numeric,
we skip it by moving left inwards to the array

if the char at index right is not alpha numeric,
we skip it by moving right inwards to the array

if valid chars at index left and right do not match
we return false,
else we move both left and right inwards to the array

if it completes the while loop successfuly, meaning no not match was successful,
we return True
