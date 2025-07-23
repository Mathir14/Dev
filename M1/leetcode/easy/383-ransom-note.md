a hash map problem,

we are required to check whether, the ransomnote, a string of characters, can be formed within the string magazine
example, ransom is hello and magazine is heafasflaeoaflo,

we get the count of the characters in magazine string since it is equal or bigger than ransom, so it is the source string

then for each char in ransom,
we basically check if count of char in the hash of magazine, if it is 0, meaning that char doesnt exist, we return false
if it exists, we reduce count of that char by 1 in the magazine hash,
so when we encounter an extra char, the count will be 0 and we can return False

when the loop iterates till the end which means each char in ransom can be formed, we return True

time O(m + n) len of magazine + len of ransom note
space O(1)
