import datetime
S = str(input())
date_format = datetime.datetime.strptime(S,'%Y/%m/%d')
print('2018/'+str(date_format.strftime("%m/%d")))