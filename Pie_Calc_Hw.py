import math
import random
import gspread
import time

gc = gspread.service_account('pi-cas-446ee5a764c2.json')

# Open a sheet from a spreadsheet in one go
wks = gc.open_by_key('1y6uHP-Pi-vMwPktfURhLJaLBhuaPeCxvqDZyszUo-RQ').sheet1


def archemedis(num_sides):
    inner_half_angle_A = 360.0 / num_sides / 2
    half_s = math.sin(math.radians(inner_half_angle_A)) * 1
    circumferance = half_s * 2 * num_sides
    estimated_pie_archemedis = circumferance / (2 * 1)
    return estimated_pie_archemedis


def lenbiz(terms):
    estimated_pie_lenbiz = 0
    algebra_sign = 1
    for term in range(1, terms + 1, 2):
        estimated_pie_lenbiz += 1 / (term * algebra_sign)
        algebra_sign = -1 * algebra_sign
    return estimated_pie_lenbiz * 4


def wallis(terms):
    estimated_pie_wallis = 1
    for i in range(1, terms):
        numerator = (i * 2) * (i * 2)
        denominator = (i * 2 - 1) * (i * 2 + 1)
        estimated_pie_wallis = estimated_pie_wallis * (numerator / denominator)
    return estimated_pie_wallis * 2


for i in range(8, 1000, 1):
    temp_list = []
    num_sides = i
    terms = i
    print('For Value of Number of Sides ' + str(num_sides))
    temp_list.append(num_sides)
    print('Estimated PIE Value by the Archemedis Function is ' +
          str(archemedis(num_sides)) + '\n' + '\n')
    temp_list.append(archemedis(num_sides))
    print('For Value of Terms ' + str(terms))
    temp_list.append(terms)
    print('Estimated PIE Value by the Lenbiz Function is ' +
          str(lenbiz(num_sides)) + '\n' + '\n')
    temp_list.append(lenbiz(terms))
    print('For Value of Terms ' + str(terms))
    temp_list.append(terms)
    print('Estimated PIE Value by the Wallis Function is ' +
          str(wallis(num_sides)) + '\n' + '\n')
    temp_list.append(wallis(terms))
    wks.append_row(temp_list)
    time.sleep(10)
