from os.path import isfile
import argparse

FOSVGG_DEFAULT_WIDTH = 300
FOSVGG_DEFAULT_HEIGHT = 60

class foreignObjectSVGGenerator():
	"""
	Class for generating SVG files with foreignObject content (HTML/CSS/JS)
	from a source HTML and CSS file.
	"""
	def __init__(self,
		htmlFile: str = None,
		cssFile: str = None,
		outputFile: str = None,
		width: int = FOSVGG_DEFAULT_WIDTH,
		height: int = FOSVGG_DEFAULT_HEIGHT,
		verbose: bool = False,
		toString: bool = False):
		"""
		Constructor properties:
		htmlFile: path of input HTML file,
		cssFile: path of input CSS file,
		outputFile: desired path of output file (output),
		width: width of output image in px,
		height: height of output image in px,
		verbose: print output information,
		toString: instead of generating an output file, return data as a string
		"""

		if outputFile is not None and isfile(outputFile):
			if verbose:
				print(f"Sorry, output file {outputFile} already exists \
				and I won't be overwriting it.")
		else:
			self.output = outputFile

		if htmlFile is not None and isfile(htmlFile):
			with open(htmlFile, 'r') as file:
				self.html = file.read()
		else:
			self.html = ''
		
		if cssFile is not None and isfile(cssFile):
			with open(cssFile, 'r') as file:
				self.css = file.read()
		else:
			self.css = ''

		if len(self.css) == 0 and len(self.html) == 0:
			raise Exception("Both CSS and HTML files can't be empty")

		self.width = width
		self.height = height
		self.verbose = verbose
		self.toString = toString

	def generateSVG(self):
		"""
		Generate output file or return string depending on self.toString.
		"""
		self.svg = f'<svg fill="none" viewBox="0 0 {self.width} \
			{self.height}" width="{self.width}" height="{self.height}" \
			xmlns="http://www.w3.org/2000/svg">\n'
		self.svg += '<foreignObject width="100%" height="100%">\n'
		self.svg += '<div xmlns="http://www.w3.org/1999/xhtml">\n'
		self.svg += '<style>' + self.css + '</style>\n'
		self.svg += self.html
		self.svg += '</div></foreignObject></svg>'

		if self.toString:
			return self.svg

		if self.output is not None and not isfile(self.output):
			filename = self.output
		else:
			baseFilename = 'foreignObject.svg'
			filename = baseFilename
			i = 0
			# Find a filename that will work
			while isfile(filename):
				i += 1
				filenameArr = baseFilename.split('.')
				filenameArr[0] += str(i)
				filename = '.'.join(filenameArr)

		if (self.verbose):
			print(f"Writing to file '{filename}'")

		with open(filename, 'w') as file:
			file.write(self.svg)
	

if __name__ == '__main__':
	"""
	CLI use
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument('--html', metavar='file', type=str, help='filename of the input HTML file')
	parser.add_argument('--css', metavar='file', type=str, help='filename of the input CSS file')
	parser.add_argument('-o', '--out', metavar='file', type=str, help='desired filename of the output file', dest='output')
	parser.add_argument('-x', '--width', metavar='px', type=int, help='desired width of the image in pixels', default=FOSVGG_DEFAULT_WIDTH, dest='width')
	parser.add_argument('-y', '--height', metavar='px', type=int, help='desired height of the image in pixels', default=FOSVGG_DEFAULT_HEIGHT, dest='height')
	parser.add_argument('-v', '--verbose', action='store_false', help='print details relating to file names', default=True, dest='verbose')

	args = parser.parse_args()
	htmlFile = args.html
	cssFile = args.css
	outputFile = args.output
	width = args.width
	height = args.height
	verbose = args.verbose

	obj = foreignObjectSVGGenerator(
		htmlFile = htmlFile,
		cssFile = cssFile,
		verbose = verbose,
		width = width,
		height = height)
	obj.generateSVG()
