alist=input("enter a list of colours seprated by',': ").strip()
blist=input("enter 2nd list of clours: ").strip()
set_a={col.strip().lower() for col in alist.split(',')}
set_b={col.strip().lower() for col in blist.split(',')}

exclu= set_a - set_b
print(exclu)
