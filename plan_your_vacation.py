# Calculate hotel cost based on number of days:
def hotel_cost(days):
	cost = 140*days
	return cost

# Calculate plane cost based on the destination:
def plane_ride_cost(city):
	if city == "los angeles":
		return 183
	elif city == "las vegas":
		return 220
	elif city == "san francisco":
		return 222
	elif city == "texas":
		return 475
	else:
		return 0

# Calculate rental car cost based on number of days:
def rental_car_cost(days):
	price = 40*days
	if 3 <= days < 7:
		new_price = price - 20
		return new_price
	elif days >= 7:
		new_price = price - 50
		return new_price
	else:
		return price
		
# Calculate total cost:
def trip_cost(city, days, spending_money):
	cost = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
	return cost

# Ask users information about their trip:
city = raw_input("What's your destination? ").lower() # to bypass case sensitive
if city in ('las vegas', 'los angeles', 'san francisco', 'texas'):
	days = int(raw_input("How many days are you going to stay? ")) # use int() to convert a string to a number, so it can be calculated
	spending_money = float(raw_input("How much do you want to spend? "))# use float() for non-interger number
	# Display total cost for users:
	#total = days + spending_money
	total = trip_cost(city, days, spending_money)
	print "Your total cost to %r for %r days with an extra of $%r is: %r" % (city, days, spending_money, total)
else:
	print "No fun going there! Try somewhere else!"
	







