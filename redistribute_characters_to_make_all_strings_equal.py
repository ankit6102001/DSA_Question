# -*- coding: utf-8 -*-
"""Redistribute_Characters_to_Make_All_Strings_Equal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZG9BsP0MxHGtAKbDveO8ZlVj9A2spxAx
"""

# Leetcode : https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_cnt = defaultdict(int)

        for w in words:
            for c in w:
                char_cnt[c]+=1

        for c in char_cnt:
            if char_cnt[c] % len(words):
                return False
        return True