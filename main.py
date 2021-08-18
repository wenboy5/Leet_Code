import random
import math
from collections import Counter

l = [1,2,3,4,1]
d = Counter(l)
for i in d:
  print(i,d[i])

print(1==1) # True
print(True + True) #2
print(True + False) #1

'''
l.remove(1)
print(l)
l.remove(1)
print(l)

for i in range(8,-19,-1):
  print(i)
print((['1', '2']))
print()
for i in range(2,2):
  print(i,"haha")
print()
print(5//3)
a = {1,2,3}
b = {1}
print(a-b)

a = set()

b = set()
b.add(2)
print(a)

a.update(b)
print(a)

def count(num):
  if num == 10:
    return True
if count(5):
  print("hahahah")
print("----")
if count(10):
  print("woc")
a = 1 
b =a 
print(b)
a= 5
print(b)
c = set()
c.add(1)
d = c
print(d)
c.add(2)
print(d)

s = "dsfsf"
print(s[0:2])
# a= 1
# b=0
# c=0
# if (a and b and c) == 0:
#   print("yes")
# for x,y in [(1,3)]:
#   print(x,y)
# print(type({0}))

print(int(math.sqrt(12)))

for i in [0,1,2][:-1:-1]:
  print(i)
print(int(3/2))

print(['a'] + ["b"])
print("a" < "asbdf")
print("a" < "b")
if int("s"):
  print("ok")
if None:
  print("1")
print(10//3)
print(10%3)
s= "cbd"
b = sorted(list(s))
print(tuple(list(s)))
print(b)
print(['a','b'] == ['b','a'])
c = set()
if 'a' not in c:
  c.add('a')
print(c)

print("0".lstrip("0") != "")

print(s[0:3])
a = set()
a.add((1,2,3))
print(list(a))

print(int(s))
print(-2**31)
num = 4321
print( (num //100) %10 )

print('a' > '`')

a= ["abd","bsd","csa","baa"]
print(a.index("abd"))
print(len("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxt"))
print(len("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtxxxxxxxxxxxxxxxxxxxxw"))

print(a.remove("csa"))
print(a.remove("ssss"))
print(a)



s = 'a'
print(s*2)


a= ["abd","bsd","csa","baa"]

print(a[1:])
print(min(a))
print("abd"<"bsd")
print("csa"<"baa")
if not 0:
  print("ok")

index = "abc".find('d',0)
print(index)

print(index)

class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None

ListNode.check = False
a = ListNode()
a.check = True
print(a.check)
b = ListNode()
print(b.check)


a = [21,12,12,3,4,5,3]
print(a)
print(len(a))
a.pop(7)
print(a)

b = a[:2]
print(b)
print(sorted(a,reverse = True))
print(random.randint(0, 1))
'''
'''
a = [21,12,12,3,4,5,3]
for i in range(4,7):
  print(i)


a = {2:1,4:2}
print(2 in a)

for i in range(4,7):
  print(i)
print()
for i in range(7):
  print(i)

a = [21,12,12,3,4,5,3]
for i in range(0,len(a)):
  print(-i-1)
  print(a[-i-1])
  print()

print(len(str(123)))

for i in range(2):
  print(i)


a = 5
b = 4
a,b = b,a
print(a)
print(b)
s ="hello"
s[0] = 'o'
print(s)
'''