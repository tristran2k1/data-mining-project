from functions import * 

#3.4 Xóa các dòng bị thiếu dữ liệu với ngưỡng tỉ lệ thiếu cho trước 
#format cmd line: python drop-row.py house-prices.csv [output-file] [threshold-Na-%]


data = Load_data(sys.argv[1])

new_data = Drop_row(data, (100-int(sys.argv[3]))/100)

print("Shape of table: ", new_data.shape)
Save_file(new_data, sys.argv[2])