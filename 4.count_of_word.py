line=input("enter a line of text : ")
words=line.split()
count={w:words.count(w) for w in words}
print(count)
