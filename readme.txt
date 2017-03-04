This project is meant to collect data over a period of time using the write_3_day_forecast.py file.
This file will record the forecasted conditons 3 days out and will record the expected high temperature, low temperature
and QPF (quantitative precipitation forecast).  This script can be run on Linux as a cron job or on Windows using
Task Scheduler.

The write_actual_obs.py file is meant to be used at the end of the data collection period.  You can specify the dates
you ran the project through and it will collect the observed weather conditions for each day and for each location.

Coming soon will be an analysis script using PANDAS which will seek identify deviations between the forecast and
observed conditions.

Also, I would like to include other weather data providers to this project as well, such as AccuWeather and the
National Weather Service.