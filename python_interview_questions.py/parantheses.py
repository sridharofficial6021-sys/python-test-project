s="()[]"
pairs={')':'(',
       ']':'[',
       '}':'{'
       
}
stake=[]
for ch in s:
    if ch in "{([":
        stake.append(ch)

    else:
        stake.pop()!=pairs [ch]
        print("Invalid")
        break

else:
     if not stake:
        print("Valid")
     else:
        print("invalid")
   
