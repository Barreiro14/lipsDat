import argparse
from pathlib import Path
from readFile import read


def main():
	parser = argparse.ArgumentParser(description='Description of your program')
	parser.add_argument('-f','--path', help='Path for the data file', required=True)
	args = vars(parser.parse_args())

	file = Path(args['path'])
	if file.is_file():
		i = 0
		f = open("result.dat", "a")
		while i < len(read(args['path'])):
			f.write("{} ".format(read(args['path'])[i] + 1))
			i = i + 1
		f.close()
		print("Listo")
	else:
		print("Introduce un archivo valido miloco")
	#main function

if __name__ == '__main__':
	main()
