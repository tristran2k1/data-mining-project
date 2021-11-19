from functions import *

#3.3 Điền giá trị bị thiếu bằng phương pháp mean, median
#format cmd line: python fill-missing.py house-prices.csv [output-file] [median/mean]


data = Load_data(sys.argv[1])

if sys.argv[3] == 'median':
	new_data = Fillna_data_median(data)
else:
	new_data = Fillna_data_mean(data)

#saving
Save_file(new_data, sys.argv[2])

print("Top 5 rows:") 
print(new_data.head(5))
print("List columns with missing data: ", Missing_col(new_data))


#EXPAND:
#mode 1: fill all missing values
#mode 2: fill specify mode and col