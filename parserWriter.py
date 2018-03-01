#File that parse the input file


"""This methods returns two lists:
	--headers: Contains info about the file
	--rides: Contains N lists with every ride in the problem
"""
def getInput(input_file):
	f = open(input_file, 'r')
	input = f.read().split('\n')
	headers = input[0]
	grid = input[1:]
	grid.pop()
	rides = []
	headers = headers.split(' ')
	i=0
	for element in grid:
		aux = element.split(' ')
		aux.append(i)
		rides.append(aux)
		i=i+1
	rides.sort(key=lambda x: x[4])
	f.close()
	return (headers,rides)

"""This methods writes the result according to the problem statement
"""
def writeOutput(vehicles):
	f = open("r",'w')
	for element in vehicles:
		f.write(str(len(element)))
		for i in element:
			f.write(" "+str(i))
		f.write("\n")
	f.close()
