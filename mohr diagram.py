import math
from random import randrange
import matplotlib.pyplot as plt

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


    #drawing the mohr circle
    radius = (sigma_max - sigma_min) / 2
    circle_center = sigma_max - radius

    fig = plt.figure()
    ax = fig.add_subplot()
    mohr_circle = plt.Circle((circle_center, 0), radius, fill = False)
    ax.add_patch(mohr_circle)
    ax.axis('equal')

    plt.title('wassup bejing')
    plt.show()

    return {
        "sigma_theta": sigma_theta,
        "sigma_y_prime": sigma_y_prime,
        "tau_theta": tau_theta,
        "sigma_max": sigma_max,
        "sigma_min": sigma_min,
        "radius": radius,
        "circle_center": circle_center,
        "mohr_circle": mohr_circle,
        "fig": fig,
        "ax": ax
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