a = "a1v2b3b4n5m6,7,8.9"
s = 0
for i in a:
    if "0" <= i <= "9":
        s += int(i)
print(s)