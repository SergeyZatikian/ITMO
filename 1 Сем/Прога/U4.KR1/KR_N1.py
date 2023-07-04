s = ''
for i in range(12345):
    a = str(input())
    if a == '':
        print(s)
        break
    s = s + a[0]
