name=input("enter file name (eng:hey.jpg)")
part=name.split('.')
if len(part)>1:
    exe=part[-1]
    print("extention of the file is .",exe)
else:
    print("there is no extention for this file")
