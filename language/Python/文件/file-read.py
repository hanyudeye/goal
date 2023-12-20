fd=open("./test","r",encoding="utf-8")
line=fd.readline()

res=fd.seek()

print(res)

fd.close()