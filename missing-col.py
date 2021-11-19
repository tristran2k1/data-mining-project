from functions import *

#3.1. Liệt kê các cột bị thiếu dữ liệu.
#format cmd line: python missing-col.py house-prices.csv 


data = Load_data(sys.argv[1])
print("List columns with missing data: ")
print(Missing_col(data))