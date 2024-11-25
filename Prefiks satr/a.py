s = input()

a = set()
b = ""
for c in s:
    b += c
    a.add(b)
    
print(len(a))