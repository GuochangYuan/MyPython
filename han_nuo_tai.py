#encoding:utf-8
#汉诺塔问题
#对圆盘排序，最上面为n,n-1,n-2,....1
#三根柱子分别是A,B,C
step=1
def move(disks_num,N,M):#N,M代表柱子，disks_num代表圆盘编号
	global step
	print('第',step,'次移动：把',disks_num,'号圆盘从',N,'移动到',M)
	step=step+1
	
	
	
#递归实现汉诺塔的函数
def hanoi(n,A,B,C):#四个参数分别是n代表圆盘个数，A,B,C代表三根柱子
	if n==1:
		move(1,A,C)
	else:
		hanoi(n-1,A,C,B)#递归，把A塔上编号1～n-1的圆盘移动到B上，以B为辅助塔
		move(n,A,C)#把A塔上编号为n的圆盘移动到C上
		hanoi(n-1,B,A,C)#递归，把B塔上编号1~n-1的圆盘移动到C上，以A塔为辅助塔

disk_num=int(input('请输入圆盘个数：'))
#执行的步数
#定义三根柱子
A='A'
B='B'
C='C'
hanoi(disk_num,A,B,C)
		
