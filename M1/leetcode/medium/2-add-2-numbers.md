You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.

Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

we are given 2 linked lists, where we have to return their sum, but in reverse,
for a linked list 1 3 4 we have to read it as 4 3 1

same for 2 4 5 as 5 4 2,
add both 4 3 1 and 5 4 2 which is 9 7 3
but instead return the reverse which is 3 7 9

the initial thought is to reverse both linked lists,
add the sum
form a new linked list with the sum as values,
reverse it and return,

so 1 2 3 as 3 2 1
4 5 6 as 6 5 4
sum both which is
3 2 1 + 6 5 4 so 9 7 5
reverse it, 5 7 9,
now return it,

there is a faster and better method,

the trick is to use carries,

the same 1 2 3 and 4 5 6 can be solved in a much simpler way,

1 2 3
4 5 6

1 and 4 which is 5,
2 and 5 which is 7,
3 and 7 which is 9,

return that as the new listnode,
and so , it is 5 7 9,
as required from the problem,

start with dummy node and current pointing at it

carry starts at 0

loop while either list has nodes

get current digit from l1 or 0 if none

get current digit from l2 or 0 if none

add both digits plus carry

update carry = sum divided by 10

create new node with sum mod 10 and link it

move current forward

move l1 and l2 forward if possible

after loop, if carry still there, add a new node with carry

return dummy.next as result linked list
