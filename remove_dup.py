from functions import *

#3.8 Xóa mẫu trùng lặp
#format cmd line: python remove_dup.py house-prices.csv [output-file]


data = Load_data(sys.argv[1])
print("Size data before:",(len(data),len(data[0])))

data = remove_dup_row(data)
print("Size data after:",(len(data),len(data[0])))

Save_file(data,sys.argv[2])