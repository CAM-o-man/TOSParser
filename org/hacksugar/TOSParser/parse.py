from org.hacksugar.TOSParser.exceptions import FileReadException


def read_from_file(filename):
	file = open(filename, "r")  # Open file in read mode
	if file.mode != "r":
		raise FileReadException  # If it isn't in read mode, something's gone wrong.
	
	content = file.read()
