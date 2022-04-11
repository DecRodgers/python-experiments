from datetime import datetime

datetime_format = datetime.now().strftime("%d%m%y-%H%M%S")
logfilename = 'log-'+str(datetime_format)+'.txt'

print(datetime_format)
print(logfilename)