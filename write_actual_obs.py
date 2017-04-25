from wu_utilities import *
import csv
import time



def get_actual_obs():

    # all of these variable could be passed to the function through other means
    output = 'c:\MyFiles\Weather\\actual_obs.csv'
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
    year = 2016
    start_month = 3
    start_day = 4
    end_month = 3
    end_day = 4
    # generate a formatted list of all the dates you would like to collect info for
    date_range = date_gen(year, start_month, start_day, end_month, end_day)

    with open(output, 'a', newline='') as history_log:
        history_writer = csv.writer(history_log)
        for day in date_range:
            # collect the actual high temp, low temp, and precip for each city/state pair for each date specified
            # sleep for 7 seconds to avoid the 10 calls/min WU API restriction for free account
            place1 = wu_actual_observations(city1, state1, day)
            time.sleep(7)
            place2 = wu_actual_observations(city2, state2, day)
            time.sleep(7)
            place3 = wu_actual_observations(city3, state3, day)
            time.sleep(7)
            place4 = wu_actual_observations(city4, state4, day)
            time.sleep(7)
            place5 = wu_actual_observations(city5, state5, day)
            time.sleep(7)
            place6 = wu_actual_observations(city6, state6, day)
            time.sleep(7)
            # write the place info to a csv which will appear as 'date, high temp, low temp, precipitation'
            history_writer.writerow(place1 + place2 + place3 + place4 + place5 + place6)

get_actual_obs()
