def liters_100km_to_miles_gallon(liters):
    #
    # Write your code here.
    #
    gallon = liters / 3.785411784
    miles = 100E3 / 1609.344
    return miles / gallon

def miles_gallon_to_liters_100km(miles):
    #
    # Write your code here.
    #
    liters = 100 * 3.785411784
    km = miles * 1.609344
    return liters / km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
