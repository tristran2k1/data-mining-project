from functions import * 

#3.5 Xóa các cột bị thiếu dữ liệu với ngưỡng tỉ lệ thiếu cho trước 
#format cmd line: python drop-col.py house-prices.csv [output-file] [threshold-Na-%]


data = Load_data(sys.argv[1])
print("Size data before:",(len(data),len(data[0])))

new_data = Drop_col(data, int(sys.argv[3])/100)

print("Size data after:",(len(data),len(data[0])))
Save_file(new_data, sys.argv[2])

