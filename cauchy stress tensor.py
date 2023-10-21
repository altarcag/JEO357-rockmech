#rock mechanics
import math
from random import randrange

def stress_tensor(sigma_x, sigma_y, tau_xy, theta, twotheta):
        
    sigma_theta = sigma_x * math.cos(math.radians(theta))**2 + sigma_y * math.sin(math.radians(theta))**2 + tau_xy * math.sin(math.radians(twotheta))
    print("sigma theta =", sigma_theta)

    sigma_y_prime = sigma_x * math.sin(math.radians(theta))**2 + sigma_y * math.cos(math.radians(theta))**2 - tau_xy * math.sin(math.radians(twotheta))
    print("sigma y' =", sigma_y_prime)

    tau_theta = ((sigma_y - sigma_x)/2) * math.sin(math.radians(twotheta)) + tau_xy * math.cos(math.radians(twotheta))
    print("Tau theta =", tau_theta)

    sigma_max = 0.5 * (sigma_x + sigma_y) + math.sqrt(((sigma_x - sigma_y) / 2)**2 + (tau_xy)**2)
    print("sigma_1 =", sigma_max)

    sigma_min = 0.5 * (sigma_x + sigma_y) - math.sqrt(((sigma_x - sigma_y) / 2)**2 + (tau_xy)**2)
    print("sigma_3 =", sigma_min)

    return {
        "sigma_theta": sigma_theta,
        "sigma_y_prime": sigma_y_prime,
        "tau_theta": tau_theta,
        "sigma_max": sigma_max,
        "sigma_min": sigma_min
    }


def generator(sigma_x, sigma_y, tau_xy, theta, twotheta):
    
    print("sigma x =", sigma_x)
    print("sigma y =", sigma_y)
    print("tau xy =", tau_xy)
    print("theta =", theta)
    print("2 * theta = ", twotheta)

    result = stress_tensor(sigma_x, sigma_y, tau_xy, theta, twotheta)
    return result

print("Select operation.")
print("1. question generator")
print("2. stress tensor by inputs")

while True:
    #taking input
    choice = input("Enter choice (1/2): ")

    #checking the choice
    if choice == '1':
        sigma_x = randrange(0, 50)
        sigma_y = randrange(0, 50)
        tau_xy = randrange(0, 20)
        theta = randrange(1, 10) * 5
        twotheta = theta * 2
        qa = generator(sigma_x, sigma_y, tau_xy, theta, twotheta)
        print(qa)
        
    elif choice == '2':
        sigma_x = float(input("Enter sigma_x: "))
        sigma_y = float(input("Enter sigma_y: "))
        tau_xy = float(input("Enter tau_xy: "))
        theta = float(input("Enter theta: "))
        twotheta = theta * 2

        stress_tensor(sigma_x, sigma_y, tau_xy, theta, twotheta)
        print(stress_tensor)

    else:
        print("invalid input")
        break
