Capitals = [0,1,2]
Profits = [1,2,3]
d = dict()
for i,j in zip(Capitals,Profits):
    if i in d:
        d[i] = max(d[i],j)
    else:
        d[i] = j
        
# print(d)
ans = 0
def find_profit(c, n):
    nonlocal ans
    
    if n == 0:
        ans = max(ans,c)
    else:
        for k in d.keys():
            if k <= c and d[k] > 0:
                v = d[k]
                d[k] = 0
                find_profit(c+v,n-1)
                d[k] = v
find_profit(1,2)
print(ans)
# def find_profit(c, n):
#     if n == 0:
#         return c
#     else:
#         ans = c
#         for k in d.keys():
#             if k <= c and d[k] > 0:
#                 v = d[k]
#                 d[k] = 0
#                 localmax = find_profit(c+v,n-1)
#                 if localmax > ans:
#                     ans = localmax
#                 d[k] = v
#         return ans

'''
l = [1,2,3,4,5]
a = [1,2]
print(all(i in l for i in a))


a = None
a = 1
print(a)
print(2/3)
if []:
  print("1")


s = []
if s:
  print(1)

if not s:
  print(2)

a = [1,2,3,4,5,6,7,8]
print(a[:-2])

import bisect


# from scipy.special import perm, comb
# from itertools import combinations,permutations
# a = [0,1,2,3,4,5]
# print("naozi")
# print(a[1:-1])
# print(comb(3,3))

print(701//26)
print(701%26)

new_res = ["0" for _ in range(8)]
print(new_res)
l = [1]
for i in range(len(l)):
  l[i] = str(l[i])
print(l)

l = [1,2,3,5,1]
print(l)
index = bisect.bisect_left(l,2)
print(index)
print()
print(bisect.bisect_left([0, 0, 1, 6, 8],1))
print(bisect.bisect_right([0, 0, 1, 6, 8],1))
print()
for i in reversed(range(1,5)):
  print(i)

'''