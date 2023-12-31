l=[1,2,65]
l.reverse()
print(l)

l.remove(1)

print(l)

del(l[0:1])

l[0:1]=[]
print(l)
print(len(l))

s={1,2,"hello"}

s.add(3)

print(s)
# s.clear()
print(s)

t={1,"你好"}

# 返回 s-t 
print(s.difference(t)) 


