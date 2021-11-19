from functions import *

#3.2. Đếm số dòng bị thiếu dữ liệu
#format cmd line: python missing-col.py house-prices.csv 


data = Load_data(sys.argv[1])
count = 0

#all values in row are null
"""
for i in range(len(data.index)):
	if data.iloc[i].isnull().sum() == len(data.columns):
		count+=1
"""

#row has at least 1 null
count = data.shape[0] - data.dropna().shape[0]


print("Number of lines with missing data: ", count)