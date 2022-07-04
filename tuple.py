tupleFruits = ("apple","banana","cherry") #Tuple
listFruits = ("apple","banana","cherry") #list
print("original tuple:",tupleFruits)
print("original tuple:",listFruits)
#เปลี่ยนค่าในtuple
x=list(tupleFruits)#แปลงเป็นlistแล้วเก็บในตัวแปรx
x[1]="blueberry"
tupleFruits=tuple(x)
print("เปลี่ยนค่าtuple:",tupleFruits)
#เพิ่มค่าในtuple
x=list(tupleFruits)
x.append("melon")
tupleFruits=tuple(x)
print("เพิ่มค่าtuple",tupleFruits)
#ลบtuple
x=list(tupleFruits)
x.remove("cherry")
tupleFruits=tuple(x)
print("ลบค่าtuple",tupleFruits)
#join tuple
vege=("tomato","cucumber","onion")
fruitvege=tupleFruits+vege
print(fruitvege)
x = range(3, 6)
for n in x:
    print("range x:",n)
y = range(3,20,2)
for m in y:
    print("range x:",m)
#วีรภัทร พงษ์เกาะ ชั้นม.6/11 เลขที่13