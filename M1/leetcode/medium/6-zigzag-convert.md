we are given a string, which we have to return zig zag

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P I N
A L S I G
Y A H R
P I

Example 3:

Input: s = "A", numRows = 1
Output: "A"

we have to return it in zigzag form for n rows,

first we assign '' as placeholders for the rows
and a go_down flag,

now for each element in string,
we append the current char to the current row

we check if currrent row is at the top, which is 0 , if yes,
go_down is true

else, we check if current row is at the bottom which is numRows-1,
then go_down is false as it's already at the bottom

if go_down is true,
we increase current row by 1
else we decrease curreny row by 1

and we finally return the entire string using .join(rows)
