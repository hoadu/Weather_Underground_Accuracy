import csv
from wu_utilities import *


def write_forecast():

    output = 'c:\MyFiles\Weather\\three_day_forecast.csv'
    city1 = 'Seymour'
    state1 = 'CT'
    city2 = 'Miami'
    state2 = 'FL'
    city3 = 'Des Moines'
    state3 = 'IA'
    city4 = 'Denver'
    state4 = 'CO'
    city5 = 'Phoenix'
    state5 = 'AZ'
    city6 = 'Seattle'
    state6 = 'WA'

    with open(output, 'a', newline='') as forecast_log:
        forecast_writer = csv.writer(forecast_log)
        # collect the high temp, low temp, and expected precip for each city/state pair
        place1 = wu_three_day_forecast(city1, state1)
        place2 = wu_three_day_forecast(city2, state2)
        place3 = wu_three_day_forecast(city3, state3)
        place4 = wu_three_day_forecast(city4, state4)
        place5 = wu_three_day_forecast(city5, state5)
        place6 = wu_three_day_forecast(city6, state6)
        # write the place info to a csv
        forecast_writer.writerow(place1 + place2 + place3 + place4 + place5 + place6)

write_forecast()


