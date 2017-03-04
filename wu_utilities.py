import datetime as dt
import requests
from api_key import *



def wu_history_url(city, state, day):
    # must use correct capitalization for city/state (City, ST)
    # YYYYMMDD
    url = 'http://api.wunderground.com/api/' + api_key + '/history_' + day + '/q/' + state + '/' + city + '.json'

    return url


def wu_forecast_url(city, state):
    url = 'http://api.wunderground.com/api/' + api_key + '/forecast/q/' + state + '/' + city + '.json'

    return url


def date_gen(year, start_month, start_day, end_month, end_day):
    d1 = dt.date(year, start_month, start_day)
    d2 = dt.date(year, end_month, end_day)
    delta = d2 - d1
    # generate list of all dates in sepcified date range
    unformatted_dates = [str(d1 + dt.timedelta(days=i)) for i in range(delta.days + 1)]
    # remove hyphens so dates can be inserted into url
    formatted_dates = [x.replace('-', '') for x in unformatted_dates]

    return formatted_dates


def wu_actual_observations(city, state, focus_day):
    weather_data = (requests.get(wu_history_url(city, state, focus_day))).json()
    # access the observed max and min temps using dict keys and list indices
    max_temp = weather_data['history']['dailysummary'][0]['maxtempi']
    min_temp = weather_data['history']['dailysummary'][0]['mintempi']
    precip = weather_data['history']['dailysummary'][0]['precipi']

    return focus_day, max_temp, min_temp, precip



def wu_three_day_forecast(city, state):
    today = dt.date.today()
    this_day = str(today + dt.timedelta(days=2))
    location_data = (requests.get(wu_forecast_url(city, state))).json()
    high = location_data['forecast']['simpleforecast']['forecastday'][2]['high']['fahrenheit']
    low = location_data['forecast']['simpleforecast']['forecastday'][2]['low']['fahrenheit']
    precip = location_data['forecast']['simpleforecast']['forecastday'][2]['qpf_allday']['in']

    return this_day, high, low, precip








