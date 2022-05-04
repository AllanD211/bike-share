import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

    print("Hello! Let\'s explore some US bikeshare data!")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['Chicago', 'New York', 'Washington']
    while True:
          city = Input("Would you like to see data for Chicago, New York, or Washington?")
          if city in cities:
            city=city
            break
          elif city =="end":
            break
          else:
             print("Would you like to see data for Chicago, New York, or Washington?")
