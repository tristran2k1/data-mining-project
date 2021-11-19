from functions import *

#3.8 Tính biểu thức
#format cmd line: python cal-formula.py house-prices.csv [output-file] [formula]


data = Load_data(sys.argv[1])

if '=' not in sys.argv[3]:
	name = sys.argv[3]
	specialChars = '+-*/'
	for spec in specialChars:
		name = name.replace(spec,'_')

	parse = str(name+'='+sys.argv[3])
else:
	parse = sys.argv[3]

new_data = data.eval(parse)

Save_file(new_data,sys.argv[2])