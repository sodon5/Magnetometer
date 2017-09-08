def corr_before_point(x,y,po) :
	n = 50
	vals = range(po-49,po+1) #50개 구간

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

def corr_after_point(x,y,po) :
	n = 50
	vals = range(po,po+51) #50개 구간

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


def mag_before_point(x,y,po) :
	n = 50
	vals = range(po-49,po+1) #50개 구간

	#sum
	sumx = sum([float(x[i]) for i in vals])
	sumy = sum([float(y[i]) for i in vals])

	avg=(sumx+sumy)/100

	return avg

def mag_after_point(x,y,po) :
	n = 50
	vals = range(po,po+51) #50개 구간

	#sum
	sumx = sum([float(x[i]) for i in vals])
	sumy = sum([float(y[i]) for i in vals])

	avg=(sumx+sumy)/100

	return avg

