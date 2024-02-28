import collections
import sys

word = sys.stdin.readline().rstrip()
check_word = collections.Counter(word)
cnt = 0
result = ''
mid = ''
print(check_word)
a = list(check_word.items())
print(a)