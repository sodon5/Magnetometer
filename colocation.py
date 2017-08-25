import csv
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

# Pearson correlation coefficient for section 거꾸로 뒤집어서 (10 개 단위로)
def pearson_for_sec_conv(x,y) :
	n = 10
	vals = range(10) # 0부터 9까지 [0.1.2.3.4.5.65.]

	#sum
	sumx = sum([float(x[i]) for i in vals]) # 0~9
	sumy = sum([float(y[9-i]) for i in vals]) # 9~0

	#sum double
	sumxSq = sum([float(x[i])**2.0 for i in vals])
	sumySq = sum([float(y[9-i])**2.0 for i in vals])

	#곱을 합함
	pSum = sum([float(x[i])*float(y[9-i]) for i in vals])

	#피어슨 점수 계산
	num = pSum - (sumx*sumy/n)
	den = ((sumxSq-pow(sumx,2)/n)*(sumySq-pow(sumy,2)/n))**.5

	if den==0: return 0

	r = num/den

	return r

def pearson_for_sec_conv_array_x(x,y):
	n = (int)(len(x)/10)
	num_im=0
	x_imm,y_imm=[],[] #10칸만 쓸 것임
	dx,dy=[],[]

	for i in range(0,n): #0~n-1
		for j in range(i*10,i*10+10): # i*10 ~ i*10+9
			x_imm.append(x[j])
			y_imm.append(y[j])
			num_im =pearson_for_sec_conv(x_imm,y_imm)

		dx.append(i)
		dy.append(num_im)

	return dx


def pearson_for_sec_conv_array_y(x,y):
	n = (int)(len(x)/10)
	num_im=0
	x_imm,y_imm=[],[] #10칸만 쓸 것임
	dx,dy=[],[]

	for i in range(0,n): #0~n-1
		for j in range(i*10,i*10+10): # i*10 ~ i*10+9
			x_imm.append(x[j])
			y_imm.append(y[j])
			num_im =pearson_for_sec_conv(x_imm,y_imm)

		dx.append(i)
		dy.append(num_im)

	return dy

#배열선언
x,y=[],[]
x2,y2=[],[] 
dx,dy=[],[] 

#tsv 읽고 그래프 그리기
f = open('mydata_w.tsv', 'r', encoding='utf-8')
rdr = csv.reader(f, delimiter='\t')
r = list(rdr)

for num in range(1,1000):
	#print("index=%s : revmagneticz=%s" % (r[num][0], r[num][21]))
	x.append(r[num][0])	#index
	y.append(r[num][21]) # revmagneticz

f.close()

# tsv2 읽고 그래프그리기
f = open('mydata_w2.tsv', 'r', encoding='utf-8')
rdr = csv.reader(f, delimiter='\t')
r = list(rdr)

for num in range(1,1001):
	#print("index=%s : revmagneticz=%s" % (r[num][0], r[num][21]))
	x2.append(r[num][0])
	y2.append(r[num][21])

f.close()

#dx.append(pearson_for_sec_conv(y,y2))
#print(dx)

#def pearson_for_sec_conv_array_x(x,y):
n = 130
num_im=0
x_imm,y_imm=[],[] #10칸만 쓸 것임
dx,dy=[],[]

for i in range(0,n): #0~n-1
	x_imm,y_imm=[],[]
	for j in range(0,10)#(i*10,i*10+10): # i*10 ~ i*10+9
		print (j)
		x_imm.append(y[j])
		y_imm.append(y2[j])
		print (x_imm)
		print (y_imm)
		#num_im =pearson_for_sec_conv(x_imm,y_imm)

	dx.append(i)
	dy.append(num_im)

print (dx)
print (dy)

#dx.extend(pearson_for_sec_conv_array_x(y,y2))
#dy.extend(pearson_for_sec_conv_array_y(y,y2))


plt.plot(dx,dy,color="black",  linewidth=1.5, linestyle="-", label="d")

plt.xlabel(u'd')
plt.ylabel(u'correlation of section')

#그래프 출력
plt.show()




