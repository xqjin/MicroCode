import re
import sys
import os

def findAll():
	"""
	find all the pattern in the given string
	Notice:  the result only give the group result, if not given the whole match result will give
	You can read the example below carefully !
	"""

	demo = "justinxqjin, 2018-01-01, go to beijing"
	pattern = re.compile("((\d+)-(\d+)-(\d+))")
	print pattern.findall(demo)
	#[('2018-01-01', '2018', '01', '01')] 

	pattern = re.compile("(\d+)-\d+-\d+")
	print pattern.findall(demo)
	#['2018']

	pattern = re.compile("\d+-\d+-\d+")
	print pattern.findall(demo)
	#['2018-01-01']


if __name__ == "__main__":
	findAll()
