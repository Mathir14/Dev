a two pointer problem where we use trigger pointers to iterate through the array in-place

the problem requires us to, 'remove' duplicates in a sorted array
[1,1,2,2,2,3,3,3]

it is specified we must do it in-place meaning we cannot use a seperate data structure, this forces us to use pointers
to iterate through the array since space complexity of pointers are O(1)

we use two pointers as mentioned, for this problem
stayer and finder

finder, freely iterates through the array and stops when it finds a value according to the condition 'nums[finder] > nums[stayer-1]'
the value at index stayer is replaced with the value finder finds and we move stayer by 1

the reason we go with this approach is because,
consider this array
[1,1,2,2,2,3,3,3]

we start at stayer = 1 because we know the first element is sorted/ unique as it is the original element of a value in the array
now finder moves till the end of range which is the length of the array,

when finder finds a value that satisfies this condition 
nums[finder] > nums[stayer-1]

we are basically checking for a new value that is greater than array[stayer-1] which is 1 as array[1-1] is array[0] -> 1
this is used to replace the duplicate with a value that is greater(next unique value) than the previous original value

this works because we only replace if we find a greater/new unique value, otherwise it means the array is sorted, and we return stayer which is the length of the valid array/ numbers of unique elements in the problem