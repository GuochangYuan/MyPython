import math

pi=math.pi

xs=[pi/24,pi/8,5*pi/24,7*pi/24,3*pi/8,11*pi/24]
ys=[pi/12,pi/6,pi/4,pi/3,5*pi/12,pi/2]

sum1=0
sum2=0

for x in xs:
	rel=(math.sin(x))/x
	print(rel)
	sum1=sum1+rel

print()

for y in ys:
	#print(str(y)+"\n")
	rel2=(math.sin(y))/y
	print(rel2)
	sum2=sum2+rel2

print('sum1=',sum1)

print('sum2=',sum2)

print('s6=',(pi/72)*(4*sum1+2*sum2))


