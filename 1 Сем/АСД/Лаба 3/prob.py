from random import randint

def compl5(list, item):
  low = 0
  high = len(list) - 1
  i = 0
  while low <= high:
    mid = (low + high) // 2
    guess = list[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1
    i=i+1
  return None
a = range(20)
for i in range(len(a)):
    print(compl5(a, randint(0, 19)))
print()
for i in range(3):
    print(compl5(a, randint(0, 19)))