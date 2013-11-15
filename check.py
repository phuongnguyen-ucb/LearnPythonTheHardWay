#def distance_from_zero(number):
	#if type(number) == int or type(number) == float:
	#	return abs(number)
	#else:
	#	return "Not an integer or float!"
#print distance_from_zero('abc')

from math import pi
def area_of_circle(radius):
	area = (radius**2)*pi
	return area
	
print area_of_circle(5)
