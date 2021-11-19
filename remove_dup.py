from functions import *

#3.8 Xóa mẫu trùng lặp
#format cmd line: python remove_dup.py house-prices.csv [output-file]


data = Load_data(sys.argv[1])

print("Size data before:",data.shape)
data = data.drop_duplicates()
print("Size data after:",data.shape)
Save_file(data,sys.argv[2])