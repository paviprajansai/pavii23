ab,ac=map(int,input().split())
vp=[]
for i in range(0,ab):
    mn=[int(sv) for sv in input().split()]
    vp.append(sorted(mn))
for i in range(0,len(vp[0])):
  #print(vp[i])
  for j in range(0,len(vp)-1):
    if vp[j][i]>vp[j+1][i]:
      vp[j][i],vp[j+1][i]=vp[j+1][i],vp[j][i]
for i in vp:
  print(*i)
