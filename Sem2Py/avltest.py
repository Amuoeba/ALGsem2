# -*- coding: utf-8 -*-

class Number:
    def __init__(self,name,value):
        self.value = value
        self.name = name
    
    def __repr__(self):
        return "Name: " + self.name + " Value: " + str(self.value)
    


a = Number("Ena",1)
c = Number("Three",3)


dc = {a:c,c:a}

print(a)
b = a
b.name = "Dva"
print(a)
l = [a]
print(a)
b.value += 1
print("List before",l[0],id(l[0]))
print("a:",id(a),"c:",id(c))
print("A",a)
print("C",c)
a,c = c,a
print("List After",l[0],id(l[0]))
print("a:",id(a),"c:",id(c))
print("A",a)
print("C",c)


print(a)
print(c)
c.value,a.value = a.value,c.value
print(a)
print(c)
print(l[0])
print(dc[a])

st = set()
st.add((a,c))
print((c,a) in st or (a,c) in st)
a.value = 5
print((c,a) in st or (a,c) in st)