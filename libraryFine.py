# 1 -> getiriliş
# 2 -> son tarih
#https://www.hackerrank.com/challenges/library-fine/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=30-day-campaign
#Kutay KELEŞ 14 Kasım 2021

def solve(d1,m1,y1,d2,m2,y2):
	if(y1-y2 == 0 and m1-m2 == 0):
		if(d1 > d2):
			return((d1-d2)*15)
		else:
			return(0)
	elif(y1>y2):
		return(10000)
	elif(y1 == y2):
		if(m1>m2):
			return((m1-m2) * 500)
		else:
			return(0)
	else:
		return(0)


solve(6,6,2019,6,6,2015)


