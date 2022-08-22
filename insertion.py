ll = [1,2,3,4,5,6,7,8,9,10,11,12,13]
l = len(ll) - 1
for j in range(l,12,-1):
    ll[j] = ll[j - 1]
print(ll)
