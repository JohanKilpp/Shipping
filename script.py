# Ground Shipping
def ground_shipping(weight):
  if weight <= 2:
    cost = weight * 1.50 + 20.00
    return cost
  
  elif weight > 2 and weight <= 6:
    cost = weight * 3.00 + 20.00
    return cost
  elif weight > 6 and weight <= 10:
    cost = weight * 4.00 + 20.00
    return cost
  else:
    cost = weight * 4.75 + 20.00
    return cost
  
#premium ground shipping
premium_ground_shipping = 125.00

#Drone shipping
def drone_shipping(weight):
  if weight <= 2:
    cost = weight * 4.5
    return cost
  elif weight > 2 and weight <= 6:
    cost = weight * 9.00
    return cost
  elif weight > 6 and weight <= 10:
    cost = weight * 12.00
    return cost
  else:
    cost = weight * 14.25
    return cost
  
def cheapest_shipping(weight):
  if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_ground_shipping:
    print(ground_shipping(weight))
    return "The ground shipping is the cheapest"
  
  if drone_shipping(weight) < ground_shipping(weight)  and drone_shipping(weight) < premium_ground_shipping:
    print(drone_shipping(weight))
    return "The drone shipping is the cheapest"
  
  else:
    print(premium_ground_shipping)
    return "The premium ground shipping is the cheapest"

print( cheapest_shipping(41.5))


  
