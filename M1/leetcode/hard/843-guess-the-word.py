# https://leetcode.com/problems/guess-the-word/description/

import random


class Solution:
    def findSecretWord(self, words: List[str], master: "Master") -> None:

        def match(w1, w2):
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        while True:
            guess_word = random.choice(words)
            matches = master.guess(guess_word)
            if matches == len(guess_word):
                return
            words.remove(guess_word)
            words = [w for w in words if match(w, guess_word) == matches]
