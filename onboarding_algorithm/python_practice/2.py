# check if a number exists in an array of numbers

arr = [3, 5, 6, 1, 2, 4]

n = int(input())

def number_exists(n):
    for a in arr:
        if n == a:
           return True
    return False

if number_exists(n):
    print("True")
else:
    print("False")