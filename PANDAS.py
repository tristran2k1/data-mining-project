class PANDAS:
	def __init__(self, data):
		self.data = data
		self.shape = (len(self.data),len(self.data[0]))

	def colnull(self):
		col =[]
		for i in range(self.shape[1]):
			for j in range(1,self.shape[0]):
				if self.data[j][i] == '':
					col.append(self.data[0][i])
					break
		return col
