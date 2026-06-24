s="engineering"
vowels="aeiou"
freq={}
for ch in s:
    if ch in vowels:
        freq[ch]=freq.get(ch,0)+1

print(freq)        
