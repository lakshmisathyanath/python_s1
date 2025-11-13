list_a=input("enter the first list").split(',')
list_b=input("enter the second list").split(',')
rep=0
sum_a=0
sum_b=0
for a in list_a:
    for b in list_b:
        if a==b:
            rep=rep+1
print("repetation=",rep)
for a in list_a:
    sum_a+=int(a)
for b in list_b:
    sum_b+=int(b)
if sum_a==sum_b:
    print("both list have equal sum that is , ",sum_a)
else:
    print("diffrent sum")
    print("sum of 1st list, ",sum_a)
    print("sum of 2nd list, ",sum_b)
if len(list_a)==len(list_b):
    print("both list have eqaul size")
else:
    print("list have differnt size")
