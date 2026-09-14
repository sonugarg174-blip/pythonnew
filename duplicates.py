s = "geeksforgeeks"
seen = set()  
res = ""      
for char in s:
    if char not in seen:
        seen.add(char)
        res += char

print(res)
