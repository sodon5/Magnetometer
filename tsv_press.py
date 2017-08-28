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
def pearson_for_sec(x,y,st,n) :
	n = n
	vals = range(st,st+n)#range(n) #0~n-1

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

def pearson_for_sec_print(x,y):
	n=100
	for num in range(n):
		print (num+1," section correlation of white and gold is ", pearson_for_sec(x,y,num*n,n))

#not used
# 60 개 단위의 상관계수를 평균내는 함수
def avg_person_for_sec(x,y,n):
	n = n
	#vals = range(n) #block 개수
	num = 0.0

	#x_imm,y_imm=[],[]

	for i in range(0,len(x)):
		for j in range(i*n,i*n+n-1):
			x_imm.append(x[j])
			y_imm.append(y[j])
		num = num + pearson_for_sec(x_imm,y_imm)

	r = num/n

	return r


x,y=[],[]
x2,y2=[],[] 
 

#tsv 읽고 그래프 그리기
f = open('log_sensors_white.tsv', 'r', encoding='utf-8')
rdr = csv.reader(f, delimiter='\t')
r = list(rdr)

for num in range(100,10001):																		#끝점정하기
	#print("index=%s : revmagneticz=%s" % (r[num][0], r[num][21]))
	x.append(r[num][0])
	y.append(r[num][26])

#plt.plot(x, y,'b')
plt.plot(x, y, color="green", linewidth=2.5, linestyle="-", label="S5_White")

f.close()


# tsv2 읽고 그래프그리기
f = open('log_sensors_silver.tsv', 'r', encoding='utf-8')
rdr = csv.reader(f, delimiter='\t')
r = list(rdr)

for num in range(100,10001):																		#끝점정하기
	#print("index=%s : revmagneticz=%s" % (r[num][0], r[num][21]))
	x2.append(r[num][0])
	y2.append(r[num][26])

#plt.plot(x2, y2,'r')
plt.plot(x2, y2, color="orange",  linewidth=2.5, linestyle="-", label="S5_Gold")

#f.close()

#legend 표시
plt.legend(loc='upper right', frameon=False)

#label 표시
plt.xlabel(u'time(index)')
plt.ylabel(u'pressx')


#print (sim_distance(x,y))
#print ("correlation of 1st and 2nd is ", pearson(y,y2))
#print ("1st section correlation of 1t and 2nd is ", pearson_for_sec(y,y2,0,100))
pearson_for_sec_print(y,y2)
#print ("avg correlation of 1t and 2nd is ", avg_person_for_sec(y,y2))

#for num in range(0,100):
#	print ("  correlation of 1t and 2nd is ", pearson_for_sec(y,y2,100))

#그래프 출력
#plt.show()




