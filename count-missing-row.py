from functions import *

#3.2. Đếm số dòng bị thiếu dữ liệu
#format cmd line: python count-missing-row.py house-prices.csv 


data = Load_data(sys.argv[1])
#count no. rows have at least 1 nan value
print("Number of lines with missing data: ", count_missing_row(data))




#all values in row are nan
"""
for i in range(len(data.index)):
	if data.iloc[i].isnull().sum() == len(data.columns):
		count+=1
"""
