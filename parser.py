#File that parse the input file

def getInput(input_file):
	f = open(input_file, 'r')
	input = f.read().split('\n')
	headers = input[0]
	grid = input[1:]
	grid.pop()
	grids = []
	headers = headers.split(' ')
	i=0
	for element in grid:
		aux = element.split(' ')
		aux.append(i)
		grids.append(aux)
		i=i+1
	grids.sort(key=lambda x: x[4])
	return (headers,grids)

def writeOutput(vehicles):
	print "gatos"
