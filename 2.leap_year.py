cyear=int(input("enter current year"))
fyear=int(input("enter final year"))
for year in range(cyear,fyear,+1):
    if(year%4==0)or(year%400==0):
        if year%100!=0:
            print(year)
      
