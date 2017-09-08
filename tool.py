import csv

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

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

# x,y의 start end 구간 사이의 correlation 값 구하기
def pearson_for_sec(x,y,start_idx,end_idx) :	#0-2
	n = end_idx-start_idx + 1 #3
	vals = range(start_idx,end_idx+1)	#range(n) #start ~ end 	#0~2

	#sum
	sumx = sum([float(x[i]) for i in vals]) #x[0]~x[2]
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



# x,y의 po 기준 으로 좌측의 n 구간의 correlation 값 구하기
def corr_before_point(x,y,po_idx,n) :
	n = n
	vals = range(po_idx-n,po_idx)

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

# x,y의 po 기준 으로 우측의 n 구간의 correlation 값 구하기
def corr_after_point(x,y,po_idx,n) :
	n = n
	vals = range(po_idx+1,po_idx+n+1) 

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

# x,y의 po 기준 으로 좌측의 n 구간의 magnetometer 값 구하기 # 그 점은 포함 안함
def mag_before_point(x,y,po_idx,n) : 
	n = n
	vals = range(po_idx-n,po_idx) #po_idx-n~po_idx

	#sum
	sumx = sum([float(x[i]) for i in vals])
	sumy = sum([float(y[i]) for i in vals])

	avg=(sumx+sumy)/n/2

	return avg

# x,y의 po 기준 으로 좌측의 n 구간의 magnetometer 값 구하기
def mag_after_point(x,y,po_idx,n) :
	n = n
	vals = range(po_idx+1,po_idx+n+1) #po_idx~po_idx+n-1

	#sum
	sumx = sum([float(x[i]) for i in vals])
	sumy = sum([float(y[i]) for i in vals])

	avg=(sumx+sumy)/n/2

	return avg

def mag_before_point_each(x,po_idx,n) :
	n = n
	vals = range(po_idx-n+1,po_idx+1) #po_idx-n~po_idx

	#sum
	sumx = sum([float(x[i]) for i in vals])
	

	avg=(sumx)/n


	return avg

def mag_after_point_each(x,po_idx,n) :
	n = n
	vals = range(po_idx,po_idx+n) 

	#sum
	sumx = sum([float(x[i]) for i in vals])

	avg=(sumx)/n

	return avg



#data 저장할 배열들
x,y=[],[]	#개수 real_en-real_st+1 # x 는 index
x2,y2=[],[] #개수 real_en-real_st+1 

#input
total_st= 1	#total_index_start
total_en= 852	#total_index_end
real_st=  390#273	#real_index_start
real_en= 556#673	#real_index_end
out_p=	473	#out_point
point_sec= 25	#section 길이 


#tsv 읽고 그래프 그리기
f = open('log_sensors_white_test01.tsv', 'r', encoding='utf-8')			
rdr = csv.reader(f, delimiter='\t')
r = list(rdr)

for num in range(real_st,real_en+1):		#개수 real_en-real_st+1 
	x.append(r[num][0])
	y.append(r[num][21])

#plt.plot(x, y,'b')
plt.plot(x, y, color="#2E2E2E", linewidth=2, linestyle="-", label="S6_White")

f.close()


# tsv2 읽고 그래프그리기
f = open('log_sensors_gold_test01.tsv', 'r', encoding='utf-8')
rdr = csv.reader(f, delimiter='\t')
r = list(rdr)

for num in range(real_st,real_en+1): 	#개수 real_en-real_st+1 		 real_st가 index 0번임
	x2.append(r[num][0])
	y2.append(r[num][21])

plt.plot(x2, y2, color="#B7950B",  linewidth=2, linestyle="-", label="S6_Gold")

#f.close()

#outpoint line 그리기 in->out 의 경우
plt.axvline(x=out_p, color="#FF0000",  linewidth=2.5, linestyle="-", label="outPoint") 
plt.axvline(x=out_p-point_sec, color="#0080FF",  linewidth=2.5, linestyle=":", label="out_section_start") 
plt.axvline(x=out_p+point_sec, color="#0080FF",  linewidth=2.5, linestyle=":", label="out_section_end") 

#legend 표시
plt.legend(loc='upper right', frameon=False)

#label 표시
plt.xlabel(u'time (index)')
plt.ylabel(u'magnetometer (uT)') #단위는 마이크로 테슬라


print ("total correlation : ", pearson(y,y2))
print ("correlation of inside  : ", pearson_for_sec(y,y2,0,out_p-real_st+1)) #def pearson_for_sec(x,y,start_idx,end_idx)
print ("correlation of outside : ", pearson_for_sec(y,y2,out_p-real_st,real_en-real_st))

print ("correlation before point (25index) : ",corr_before_point(y,y2,out_p-real_st,point_sec))
print ("correlation after point (25index) : ",corr_after_point(y,y2,out_p-real_st,point_sec))


print ("magnetometer before point for S6white : ",mag_before_point_each(y,out_p-real_st,point_sec))
print ("magnetometer after point for S6white : ",mag_after_point_each(y,out_p-real_st,point_sec))


print ("magnetometer before point for S6gold : ",mag_before_point_each(y2,out_p-real_st,point_sec))
print ("magnetometer after point for S6gold : ",mag_after_point_each(y2,out_p-real_st,point_sec))


#그래프 출력
plt.show()
