import math
import random

#Implementing the Archemedis formula for PIE value calculation
def archemedis_pie_calc(num_sides):
    #Calculate the inner angle a, which is half of the angle of a side, which has a radius of 1
    inner_half_angle_A = 360.0 / num_sides /2
    half_arc = math.sin(math.radians(inner_half_angle_A)) *1
    #Using arc size to calculate the circumferance of the circle
    circumferance = half_arc * 2 * num_sides
    #Estimated pie value pie = circumferance/ (2* radius)
    estimated_pie_archemedis = circumferance/ (2 * 1)
    return estimated_pie_archemedis

#Implementing the Lenbiz formula for PIE value calculation
def lenbiz_pie_calc(terms):
    estimated_pie_lenbiz = 0
    algebra_sign = 1
    #Looping through each term for calculation
    #Formula π/4=1−1/3+1/5−1/7+1/9−⋯
    for term in range(1, terms +1, 2):
        estimated_pie_lenbiz += 1/(term * algebra_sign)
        #Defining Alegebra sign
        algebra_sign = -1 * algebra_sign
    return estimated_pie_lenbiz * 4

def monte_carlo_pie_calc(num_tries):
    inside_the_circle = 0
    for tryies in range(num_tries):
        #Getting Random Coordinate Using x and y
        x = random.random()
        y = random.random()
        #Distance = Squre Root of (x-0)^2 + (y-0)^2
        distance_from_center = math.sqrt(x**2 + y**2)
        if distance_from_center <= 1:
            #If the distance is or lees than 1, then the point is inside the circle
            inside_the_circle = inside_the_circle + 1
    #Formula pie /4 = (total points incode the circle / total number of points tested)
    estimated_pie_monte = inside_the_circle / num_tries * 4
    return estimated_pie_monte

#Testing the functions for 5 random values.
for try_num in range(5):
    num_sides = random.randint(8,100)
    terms = random.randint(8,100)
    num_tries = random.randint(100, 200)
    print('For Value of Number of Sides ' + str(num_sides))
    print('Estimated PIE Value by the Archemedis Function is ' + str(archemedis_pie_calc(num_sides)) + '\n' + '\n')
    print('For Value of Terms ' + str(terms))
    print('Estimated PIE Value by the Lenbiz Function is ' + str(lenbiz_pie_calc(num_sides)) + '\n' + '\n')
    print('For Value of Terms ' + str(num_tries))
    print('Estimated PIE Value by the Wallis Function is ' + str(monte_carlo_pie_calc(num_tries))+ '\n' + '\n')
  
