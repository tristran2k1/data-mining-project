#block warnings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


import pandas as pd
import numpy as np
import sys
import csv

#All functions 

def Load_data(path):
	path = './data/' + path
	file = open(path)
	csvreader = csv.reader(file)
	data = []
	for row in csvreader:
		data.append(row)
	#data = pd.read_csv(path)
	return data


def Save_file(data, filename):
	path = './data/' + filename
	#data.to_csv(path, index=False)
	print("New file is saved at: ",path)

	fields = data[0]
	rows = data[1:]
	with open(path, 'w',newline='') as f:
		write = csv.writer(f)
		write.writerow(fields)
		write.writerows(rows)

def Missing_col(data):
	missing_list =[]
	for i in range(len(data[0])):
		for j in range(1,len(data)):
			if data[j][i] == '':
				missing_list.append(data[0][i])
				break
	return missing_list

def count_missing_row(data):
	count = 0
	for i in range(1,len(data)):	
		for j in range (len(data[0])):
			if data[i][j] == '':
				count +=1
				break
	return count

def remove_dup_row(data):
	removed = []
	[removed.append(x) for x in data if x not in removed]
	return removed


def Fillna_data_mean(df):
	df1 = df.select_dtypes(np.number)
	df2 = df.select_dtypes(exclude = ['float64','int64'])
	mode = df2.mode()
	df3 = df1.fillna(df.mean())
	df4 = df2.fillna(mode.iloc[0,: ])
	new_df = [df3, df4]
	df5 = pd.concat(new_df, axis = 1)
	new_cols = list(df.columns)
	df6 = df5[new_cols]
	return df6

def Fillna_data_median(df): 
	df1 = df.select_dtypes(np.number)
	df2 = df.select_dtypes(exclude = ['float64','int64'])
	mode = df2.mode()
	df3 = df1.fillna(df.median())
	df4 = df2.fillna(mode.iloc[0,: ])
	new_df = [df3, df4]
	df5 = pd.concat(new_df, axis = 1)
	new_cols = list(df.columns)
	df6 = df5[new_cols]
	return df6

def Drop_row(data, threshold):
	max_val = int(threshold*len(data[0]))
	for i in range(1,len(data)):
		count = 0
		j = 0
		while (count<=max_val) and (j<len(data[0])):
			if data[i][j]=='':
				count+=1
			j +=1

		if count>max_val:
			data.pop(i)
			i -= 1
	return data

def Drop_col(data, threshold):
	max_val = int(threshold*(len(data)-1))
	lst = []
	for j in range(len(data[0])-1):
		count = 0
		i = 1
		while((count<=max_val) and (i<len(data))):
			if data[i][j] == '':
				count +=1
			i +=1

		if count > max_val:
			lst.append(int(j))
		
	for d in range(len(lst)-1,-1,-1):
		for row in data:
			del row[lst[d]]
	return data

def minmaxScaler(df):
	df = df.select_dtypes(np.number)
	X = df.sample(n=1,axis='columns',replace=True)
	X = X.iloc[:,0]
	df1 = []
	for i in range(len(X)):
		df1.append([(X[i] - min(X)) / (max(X) - min(X))])
	return df1

def Z_score(df):
	data_numeric = df.select_dtypes(np.number)
	X = data_numeric.sample(n=1,axis='columns',replace=True)
	X = X.iloc[:,0]
	X_for_zcore = X.to_numpy()
	z_score_formula = (X_for_zcore - np.mean(X_for_zcore, axis=0)) / np.std(X_for_zcore, axis=0)
	return z_score_formula
