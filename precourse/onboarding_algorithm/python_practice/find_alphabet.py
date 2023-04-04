# 1. 116 ms

s = input()

list = [-1] * 26

i = 0
for l in s:
    if l.islower():
        if list[ord(l) - 97] == -1:
            list[ord(l) - 97] = i
    i += 1

for l in list:
    print(l, end = " ")

# 2. 204 ms

# import string

# s = input()

# def get_idx_naive(word):
#     result = [-1]*len(string.ascii_lowercase)
#     for i in range(len(word)):
#         char = word[i]
#         for j in range(len(string.ascii_lowercase)):
#             lo = string.ascii_lowercase[j]
#             if result[j] == -1 and char == lo:
#                 result[j] = i
#     print(' '.join([str(num) for num in result]))

# get_idx_naive(s)

# 3. 224 ms

# import string

# s = input()

# def get_idx(word):
#     # point 1. ord
#     # point 2. O(n^2) -> O(n)
#     result = [-1]*len(string.ascii_lowercase)
#     for i in range(len(word)):
#         idx = ord(word[i]) - 97
#         if result[idx] == -1:
#             result[idx] = i
#     print(' '.join([str(num) for num in result]))

# get_idx(s)