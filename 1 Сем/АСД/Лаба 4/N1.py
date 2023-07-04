from random import choice
import timeit

def quicksort(n):
   if len(n) <= 1:
       return n
   else:
       a = choice(n)
       bolshe = []
       menshe = []
       ravno = []
       for i in n:
           if i < a:
               menshe.append(i)
           elif i > a:
               bolshe.append(i)
           else:
               ravno.append(i)
       return quicksort(menshe) + ravno + quicksort(bolshe)

def raschoska(l):
    st = int(len(l)/1.247)
    a = 1
    while st > 1 or a > 0:
        a = 0
        i = 0
        while i + st < len(l):
            if l[i] > l[i+st]:
                l[i], l[i+st] = l[i+st], l[i]
                a += 1
            i = i + 1
        if st > 1:
            st = int(st/1.247)
    return(l)

l = [1, 9, 2, 8, 3, 7, 4, 6, 5, 10, 20, 12, 19, 11, 18, 13, 17, 16, 14, 15]
print(quicksort(l))
print(123)
print(raschoska(l))

st = timeit.default_timer()
quicksort(l)
t1 = timeit.default_timer()-st
st = timeit.default_timer()
raschoska(l)
t2 = timeit.default_timer()-st

print(t1)
print(t2)
print(t1-t2)