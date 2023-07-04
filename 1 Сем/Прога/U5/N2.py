a = "вфшпОАОроррыоваЫВЫА"
b = str()
for i in a:
    if i.isupper(): b += i.lower()
    else: b += i.upper()
print(b)