import csv

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

#not used
# Pearson correlation coefficient
def pearson(x,y) :
	n = len(x)
	vals = range(n) #0~n-1

	#sum
	sumx = sum([float(x[i]) for i in vals])
	sumy = sum([float(y[i]) for i in vals])

	#sum double
	sumxSq = sum([float(x[i])**2.0 for i in vals])
	sumySq = sum([float(y[i])**2.0 for i in vals])

	#곱을 합함
	pSum = sum([float(x[i])*float(y[i]) for i in vals])

	#피어슨 점수 계산
	num = pSum - (sumx*sumy/n)
	den = ((sumxSq-pow(sumx,2)/n)*(sumySq-pow(sumy,2)/n))**.5
	if den==0: return 0

	r = num/den

	return r

#not used
# Pearson correlation coefficient for section (60 개 단위로)
def pearson_for_sec(x,y) :
	n = 10
	vals = range(0,9)

	#sum
	sumx = sum([float(x[i]) for i in vals])
	sumy = sum([float(y[i]) for i in vals])

	#sum double
	sumxSq = sum([float(x[i])**2.0 for i in vals])
	sumySq = sum([float(y[i])**2.0 for i in vals])

	#곱을 합함
	pSum = sum([float(x[i])*float(y[i]) for i in vals])

	#피어슨 점수 계산
	num = pSum - (sumx*sumy/n)
	den = ((sumxSq-pow(sumx,2)/n)*(sumySq-pow(sumy,2)/n))**.5
	if den==0: return 0

	r = num/den

	return r

#not used
# 60 개 단위의 상관계수를 평균내는 함수
def avg_person_for_sec(x,y):
	n = (int)(len(x)/60)
	#vals = range(n) #block 개수
	num = 0.0

	x_imm,y_imm=[],[]

	for i in range(0,n-1):
		for j in range(i*60,i*60+59):
			x_imm.append(x[j])
			y_imm.append(y[j])
		num = num + pearson_for_sec(x_imm,y_imm)

	r = num/n

	return r


dx,dy=[],[]

# 10 개 단위의 상관계수를 뽑아서 배열로 만드는 함수
def person_for_sec_conv_array(x,y):
	n = (int)(len(x)/10)
	#vals = range(n) #block 개수
	#num = 0.0

	x_imm,y_imm=[],[]

	for i in range(0,n-1):
		for j in range(i*10,i*10+9):
			x_imm.append(x[j])
			y_imm.append(y[j])
		dx.append(i)
		dy.append(pearson_for_sec_conv(x_imm,y_imm))

	#return r


x,y=[],[]
x2,y2=[],[] 
 

#tsv 읽고 그래프 그리기
f = open('S5white_log_sensors_out_02.tsv', 'r', encoding='utf-8')
rdr = csv.reader(f, delimiter='\t')
r = list(rdr)

for num in range(1,1000):
	#print("index=%s : revmagneticz=%s" % (r[num][0], r[num][21]))
	x.append(r[num][0])
	y.append(r[num][21])

#plt.plot(x, y,'b')
plt.plot(x, y, color="orange", linewidth=2.5, linestyle="-", label="Black")

f.close()


# tsv2 읽고 그래프그리기
f = open('S5white_log_sensors_out_01.tsv', 'r', encoding='utf-8')
rdr = csv.reader(f, delimiter='\t')
r = list(rdr)

for num in range(1,1000):
	#print("index=%s : revmagneticz=%s" % (r[num][0], r[num][21]))
	x2.append(r[num][0])
	y2.append(r[num][21])

#plt.plot(x2, y2,'r')
plt.plot(x2, y2, color="green",  linewidth=2.5, linestyle="-", label="White")


#legend 표시
plt.legend(loc='upper right', frameon=False)

#label 표시
plt.xlabel(u'time(index)')
plt.ylabel(u'revmagneticz')


#print (sim_distance(x,y))
print ("correlation of 1st try and 2nd try is ", pearson(y,y2))
print ("avg correlation of 1st try and 2nd try is ", avg_person_for_sec(y,y2))

#그래프 출력
plt.show()




