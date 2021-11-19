from functions import *

#3.8 Tính giá trị biểu thức thuộc tính
#format cmd line: python normalize.py house-prices.csv [output-file] [formula]


data = Load_data(sys.argv[1])

if sys.argv[2] == 'z-score':
	scale = Z_score(data)
else:
	scale = minmaxScaler(data)

print("Normalization by method:", sys.argv[2])
print(scale)
