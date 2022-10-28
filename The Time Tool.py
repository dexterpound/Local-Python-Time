import datetime

now = datetime.datetime.now() 

print (now.strftime("%d-%m-%Y %H:%M:%S"))
print (now.strftime("%d/%m/%Y"))
print (now.strftime("%H:%M:%S %p"))
print (now.strftime("%a, %d %b %Y"))





import pandas as pd
import datetime
timestamp = pd.Timestamp(datetime.datetime(2021, 10, 10))
#from datetime import datetime
#import pandas as pd

res = timestamp.today()



# Given timestamp in string
time_str = '24/7/2021 11:13:08.230010'
date_format_str = '%d/%m/%Y %H:%M:%S.%f'
# create datetime object from timestamp string
given_time = now.strptime(time_str, date_format_str)
print('Given Time: ', given_time)
n = 3
# Add 3 hours to datetime object
final_time = given_time + pd.DateOffset(hours=n)
print('Final Time (3 hours after given time ): ', final_time)
# Convert datetime object to string in specific format 
final_time_str = final_time.strftime('%d/%m/%Y %H:%M:%S.%f')
print('Final Time as string object: ', final_time_str)
