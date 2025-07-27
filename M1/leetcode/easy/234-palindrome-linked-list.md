Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

we are given a linked list, and are required to check where it is palindrome or not,

it is similar to the two pointer version of array based palindrome,
except different techniques to operate on a linked list,

here we can't come from both ends of a linked list like we can do in array using converging pointers,

and so we have to solve this differently,

we can split the linked list into 2 parts
and then check if all the values match,

to do this, we use floyd's tortoise hare algorithm
where we move slow one node at a time
and fast two nodes at a time
so when fast reaches the end of the linked list,
slow is at the middle,

this allows us to use slow as the
second half of the linked list,

and now we reverse the second half of the linked list using the same 3 pointer technique

prev at None, curr as slow which will be the head of the second half,
we use a temp pointer to hold curr's next node,

and assing prev as curr's next,
essentially swapping values

and now moving both forward using
prev as curr
and curr as the temp pointer which held its actual next node

with this, the second half is reversed,

now we compare both the first half and second half using two pointers,

we compare if each node val is same as the corresponding one from the other half,
and we move forward each node using
slow = slow.next
fast = fast.next

if they don't match, we return False,
if the while loop terminates which means it never returned False,

meaning the linked list is palindrome,
and so we return True

dry run:
consider a linked list
1 2 2 1

we find the middle using floyds algorithm
slow at 1 fast at 2
slow at 2 fast at 4
slow at 3 fast at None, this is so that we use the later half as the middle,

now slow at 3rd node which is 2,
now we reverse the second half,

so its 1 2
and now we compare both halfs,

1 and 1 at both 1st node, match
2 and 2 at both 2nd node, match
the linked lists are exhausted and so the while loop terminates without returning False,

which means its a palindrome and so we return True

time O(n)
space O(1)
