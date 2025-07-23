a game theory problem, and an accidental solution
backstory at the problem,

to explain in simple terms, we are given an array of words,
we are given an n number of guesses, we can guess one word at a time,

and the game master will tell us how many characters in that word actually map with the secret word,
using this clue and some supposed brain thinking, we are supposed to find the secret word within the
amount of guesses allowed

the logic behind the solution is,
when game master tells us how many characters from guessed word matches with the secret word,
we can simply eliminate the words that do not match the said amount of characters with the guessed word,
by doing this, we can prune the element from n groups to only 1 group that matches,

and we repeat this iteratively until we prune everything we can and reach the final secret word.

how my solution differs:
to pick the guess word, the general community accept method is minmax,
basically grouping every element based on how it matches with every other element
an O(n^2) mapping, this is so that,

we can pick the word which matches the most with any other word,
so if it is wrong or on the lower side,
we can prune majority of the bad ones,

but since it is O(n^2) for choosing the right candidate as the guess word,
i refused to accept that as my solution and that I was not ready to invest my time on minmax or game theory when I am still in the foundation stage,

so instead of finding the best candidate,
I decided to pick a random element as the guess word and then prune using that, this is O(n) as
we only pick a random word instead of finding the best one using n^2 comparisons,

and the result is, this sub optimal method, beats 90% of the solutions submitted,
despite having it's worse case where every element is almost similar to each other so it's hard to prune elements
as the last test case.

the program logic:

we pick a random word as our guess,
we call the game master with that word,
we check if it matches every character with the secret word from the result,

if it does, we return True since it is the secret word,
if it doesn't, and instead, say it matches 4 character,

we group the words based on how many characters they match with the guessed word

words = [w for w in words if match(w, guess_word) == matches]

return sum(c1 == c2 for c1, c2 in zip(w1, w2))

these 2 lines handle the grouping,
for every word in words, we call the function match with the word and the guessed word,
inside the match function, it checks how many characters it matches using ==, and returns a sum of it,

when it returns an n value, we check if it is the same as the value the game master returned us,
if it matches, then the word is stored in words, otherwise skipped,

this way, we prune the words which do not match as game master said, and we also remove the guessed word from the words list so we dont randomly select it again since we know it is not the secret word

now the backstory // Ignore unless interested

I solved this method a few days ago, and it failed since the last test case is the worst case for this algorithm,
as I refused to pick an O(n^2) every iteration just to select a candidate, so I stuck to using random for O(n)
candidate selection,

since it failed, I thought there was no further way to go unless I used minmax which is currently out of my scope,
so I decided to put it on hold and moved on with slight frustration,

I decided to show it to my friend in class today since we were bored,
and as we were looking at the solution, I submitted it to show him it didn't work,
and as we thought, it failed the last test case,

except it showed allowedguesses as 30,
I knew of this when I submitted it the previous time too but my brain decided it was not important,
today when I saw it again, I glanced over to my code where it had
for \_ in range(10) basically, the amount of guesses hardcoded,

the catch? this specific last testcase has 30 allowed guesses because we need that,
so I simply remvoed that range statement and used while True
and let leetcode handle when it fails instead of hardcoding the guesses allowed

A single line from
for \_ in range(10) to while True
pushed this from from failing the last test case to beats 90% on runtime,

that was eye opening considering how I thought this will be on hold for a while since
I thought my method was not the one for this problem,
and a simple looping statement changed the entire thing,

it was a shocker when we both saw it work live, definitely something to keep in memory.
