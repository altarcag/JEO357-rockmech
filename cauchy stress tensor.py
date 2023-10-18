#rock mechanics

import math
from random import randrange

sigma_x = randrange(0, 50)
 
print("sigma x =", sigma_x)

sigma_y = randrange(0, 50)

print("sigma y =", sigma_y)

tau_xy = randrange(0, 20)

print("tau xy =", tau_xy)

theta = randrange(1, 10) * 5
twotheta = theta * 2

print("theta =", theta)
print("2 * theta = ", twotheta)

sigma_theta = sigma_x * math.cos(math.radians(theta))**2 + sigma_y * math.sin(math.radians(theta))**2 + tau_xy * math.sin(math.radians(twotheta))

print("sigma theta =", sigma_theta)

tau_theta = ((sigma_y - sigma_x)/2) * math.sin(math.radians(twotheta)) + tau_xy * math.cos(math.radians(twotheta))

print("Tau theta =", tau_theta)
