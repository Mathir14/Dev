Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0

the problem is about, finding the maximum number of times the string 'balloon' can be formed from the given main string,
to solve this problem,
we first build a count hash for the main string,

and count the maximum amount of balloons that can be formed using the simple logic,
min(), a function which returns the minimum value from the given.

return min( hash.get('b',0),hash.get('a',0),hash.get('l',0)//2,hash.get('o',0)//2,hash.get('n',0))

its basically checking how the count of each of these characters, but since we need two l and o, theyre whole divivded by 2,
so with this trick, the lacking value becomes the bottleneck and gets returned as the minimum,

for example,
for given string bbaalllloooon
every character is twice that of needed to form one balloon except the n,
so in logic it is,

2,2,4/2,4/2,1
if n were 2, then the numbers of balloons that can be formed would be 2, since the minimum value in that list of operands is 2,
but since n is 1, we also know that, only 1 balloon can be made and thus 1 is returned

time O(n)
space O(1)
