import bisect

'''
# from scipy.special import perm, comb
# from itertools import combinations,permutations
# a = [0,1,2,3,4,5]
# print("naozi")
# print(a[1:-1])
# print(comb(3,3))
'''
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