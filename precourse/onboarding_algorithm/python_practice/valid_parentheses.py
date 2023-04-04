import sys

s = sys.stdin.readline().strip()

def is_valid_parentheses(s):
  opener = "([{"
  pair = {
    ")": "(",
    "]": "[",
    "}": "{"
  }

  stack = []
  i = -1

  for c in s:
    if c in opener:  
      stack.append(c)
    else:
      if not stack:
        return False
      top = stack.pop()
      if top != pair[c]:
        return False

  return not stack

print(is_valid_parentheses(s))