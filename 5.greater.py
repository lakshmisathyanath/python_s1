num=input("enter numbers list ")
num_list=num.split()
for n in num_list:
    numl=int(n)
    if numl>100:
        print("over")
    else:
        print(numl)
