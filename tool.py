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
def pearson_for_sec(x,y,start,end) :	
	n = end-start + 1
	vals = range(start,end+1)#range(n) #st ~ st+m

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


# x,y의 po 기준 으로 좌측의 n 구간의 correlation 값 구하기
def corr_before_point(x,y,po,n) :
	n = n
	vals = range(po-n+1,po+1)

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
def corr_after_point(x,y,po,n) :
	n = n
	vals = range(po,po+n) 

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

# x,y의 po 기준 으로 좌측의 n 구간의 magnetometer 값 구하기
def mag_before_point(x,y,po,n) :
	n = n
	vals = range(po-n+1,po+1)

	#sum
	sumx = sum([float(x[i]) for i in vals])
	sumy = sum([float(y[i]) for i in vals])

	avg=(sumx+sumy)/n/2

	return avg

# x,y의 po 기준 으로 좌측의 n 구간의 magnetometer 값 구하기
def mag_after_point(x,y,po,n) :
	n = n
	vals = range(po,po+n) 

	#sum
	sumx = sum([float(x[i]) for i in vals])
	sumy = sum([float(y[i]) for i in vals])

	avg=(sumx+sumy)/n/2

	return avg

def mag_before_point_each(x,po,n) :
	n = n
	vals = range(po-n+1,po+1)

	#sum
	sumx = sum([float(x[i]) for i in vals])
	

	avg=(sumx)/n

	return avg

def mag_after_point_each(x,po,n) :
	n = n
	vals = range(po,po+n) 

	#sum
	sumx = sum([float(x[i]) for i in vals])

	avg=(sumx)/n

	return avg



#data 저장할 배열들
x,y=[],[]
x2,y2=[],[] 


#input
total_st= 1	#total_index_start
total_en= 346	#total_index_end
real_st= 91#83	#real_index_start
real_en= 270#278	#real_index_end
out_p=	178	#out_point
point_sec= 25	#section 길이 

#tsv 읽고 그래프 그리기
f = open('white_filname.tsv', 'r', encoding='utf-8')			
rdr = csv.reader(f, delimiter='\t')
r = list(rdr)

for num in range(real_st,real_en):		 
	x.append(r[num][0])
	y.append(r[num][21])

#plt.plot(x, y,'b')
plt.plot(x, y, color="#2E2E2E", linewidth=2, linestyle="-", label="S6_White")

f.close()


# tsv2 읽고 그래프그리기
f = open('gold_filname.tsv', 'r', encoding='utf-8')
rdr = csv.reader(f, delimiter='\t')
r = list(rdr)

for num in range(real_st,real_en):		 
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
print ("correlation of inside  : ", pearson_for_sec(y,y2,1,out_p-real_st))
print ("correlation of outside : ", pearson_for_sec(y,y2,out_p-real_st,real_en-real_st-1))

print ("correlation before point : ",corr_before_point(y,y2,out_p-real_st,point_sec))
print ("correlation after point : ",corr_after_point(y,y2,out_p-real_st,point_sec))


print ("magnetometer before point : ",mag_before_point(y,y2,out_p-real_st,point_sec))
print ("magnetometer after point : ",mag_after_point(y,y2,out_p-real_st,point_sec))


print ("magnetometer before point for S6white : ",mag_before_point_each(y,out_p-real_st,point_sec))
print ("magnetometer after point for S6white : ",mag_after_point_each(y,out_p-real_st,point_sec))


print ("magnetometer before point for S6gold : ",mag_before_point_each(y2,out_p-real_st,point_sec))
print ("magnetometer after point for S6gold : ",mag_after_point_each(y2,out_p-real_st,point_sec))


#그래프 출력
plt.show()
