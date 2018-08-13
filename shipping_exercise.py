#Cost of the ground shipping. Weight in pounds.
def ground_shipping(weight):
  if weight <= 2:
    cost = 1.50 * weight + 20
  elif weight <= 6:
    cost = 3.00 * weight + 20
  elif weight <= 10:
    cost = 4.00 * weight + 20
  else:
    cost = 4.75 * weight + 20
  return cost
#Cost of the Drone Shipping.
def drone_shipping(weight):
  if weight <= 2:
    cost = 4.50 * weight
  elif weight <= 6:
    cost = 9.00 * weight
  elif weight <= 10:
    cost = 12.00 * weight
  else:
    cost = 14.25 * weight
  return cost
#Cost of the Premium Ground Shipping.  
def premium_ground_shipping():
  return 125
#Deciding the Cheapest method depending of the weight.
def cheapest_method(weight):
  if premium_ground_shipping()<=drone_shipping(weight) and premium_ground_shipping()<=ground_shipping(weight):
    return "Premium Ground Shipping is the cheapest method of shipping and the coast of the operations would be $125."
  elif drone_shipping(weight)<=ground_shipping(weight):
    drone_shipping(weight)
    return "Drone Shipping is the cheapest method of shipping and the cost of the operation would be $"+str(drone_shipping(weight))+"."
  else:
    return "Ground Shipping is the cheapest method of shipping and the cost of the operation would be $"+str(ground_shipping(weight))+"."

#Testing
print(cheapest_method(4.8))
print(" ")
print(cheapest_method(41.5))
