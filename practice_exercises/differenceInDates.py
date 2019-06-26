calendar_days = [31,28,31,30,31,30,31,31,30,31,30,31]

def isleapyr(yr):
	if yr%100 == 0:
		if yr%400==0:
			return True
		return False
	if yr%4==0:
		return True
	else:
		return False

def daysInyr(startmonth,yr,endmonth=12):
	if isleapyr(yr):
		calendar_days[1]=29
	else:
		calendar_days[1]=28
	return sum(map(lambda x:calendar_days[x],range(startmonth-1,endmonth)))


def diffDates(past_yr, future_yr):
	print(past_yr, future_yr)
	if past_yr[2] == future_yr[2]:
		yr_diff = 1
		month_diff = future_yr[1] - past_yr[1]
	else:
		yr_diff = abs(past_yr[2]-future_yr[2])
		month_diff = (12 - past_yr[1]) + future_yr[1]
	
	past_yr_days = calendar_days[future_yr[1]-2]-past_yr[0]
	days = past_yr_days + future_yr[0]

	if month_diff > 12:
		yr_diff+=1
		month_diff-=12
	elif month_diff == 12:
		month_diff=1
		yr_diff+=1

	num_days_yr=0
	for i in range(yr_diff-1):
		if i == 0:
			startmonth = past_yr[1]
		else:
			startmonth = 1
		num_days_yr+=daysInyr(startmonth,past_yr[2])
		print("No. of days in {} / {} = {}".format(startmonth,past_yr[2],daysInyr(startmonth,past_yr[2])))
		past_yr[2]+=1
	print(num_days_yr)

	num_days_month = daysInyr(1,future_yr[2],month_diff-1)
	print(num_days_month)

	total_num_Days = num_days_yr + num_days_month + days



	print('{} years , {} months and {} days OR Total {} days'.format(yr_diff-1,month_diff-1,days, total_num_Days))


d1 = list(map(int, input().split('/')))
d2 = list(map(int, input().split('/')))



'''
1/1/2013
1/10/2015
[1, 1, 2013] [1, 10, 2015]
2 years , 8 months and 30 days
'''

diffDates(d1,d2)