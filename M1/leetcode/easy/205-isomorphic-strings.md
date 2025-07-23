another hash map problem,

the problem requires us to check, where given two strings, can be mapped one to one
so one char from string 1 gets mapped to another char from string 2, this is called one to one mapping,

if this applies for every character in the strings, then it is isomorphic,
if a char from one string gets mapped to a char from another string while either being mapped to some other character
then it is broken and is not isomorphic

first we build a hash were we map these characters from both strings
and another set to store the chars which have already been mapped
initially the hash is empty,

if the char from string 1 is not in hash,
then we check if the char from string 2 is mapped previously,
if it is, then we return False as the char from string 1 cannot be paired as char from string 2
already has a pair

if char from string 2 is not mapped,
then we map the char from string 1 and char from string 2 together
and we mark the char from string 2 as mapped using mapped values set

if char from string 1 is already in hash,
then we check if the corresponding index char from string 2, is mapped to the corresponding index char from string 1

if theyre mapped together, the loop continues,
if they don't, then we return false as they are not mapped together

and hence the strings cannot be isomorphic

if the loop iterates through the end which means they passed as isomorphic strings
we return True
