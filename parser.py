#File that parse the input file

def getInput(input_file):
	f = open(input_file, 'r')
	input = f.read().split('\n')
	headers = input[0]
	grid = input[1:]
	grid.pop()
	grids = []
	headers = headers.split(' ')
	for element in grid:
		grids.append(element.split(' '))
	return (headers,grids)
