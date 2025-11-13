data={'bread':4,'milk':2,'egg':10}
asc=dict(sorted(data.items(),key=lambda item:item[0]))
desc=dict(sorted(data.items(),key=lambda item:item[0],reverse=True))
print("ascending data: ",asc)
print("decending data: ",desc)


