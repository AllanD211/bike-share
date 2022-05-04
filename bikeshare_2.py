import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new york city', 'washington']
months = ["january", "february", "march", "april", "may", "june","all"]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        try:
          city = input("Would you like to see data for Chicago, New York City, or Washington?\n ")
          if city in cities:
            print("We are getting data for {}".format(city))
            break
        except KeyboardInterrupt:
            print("You can only choose between Chicago, New York City or Washington")
            break
        else:
            print("You can only choose between Chicago, New York City or Washington")

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Would you like to see data for the months: january, february, march, april, may, june or all?.\n").lower()
            if month in months:
                print("We are getting data for {}".format(month))
                break
        except KeyboardInterrupt:
            Print("Please input your chosen month")
            break
        else:
            print ("Please choose a month, or type all")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
         try:
            day = str(input("Would you like to see data for the weekdays monday, tuesday, wednesday, thursday, friday, saturday, sunday or all?\n ").lower())
            if day in days:
                print("We are getting data for {}".format(day))
                break
         except KeyboardInterrupt:
            print("Invalid Input")
            break
         else:
            print("You need to select one day or all")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # To load data file into dataframe
    df = pd.read_csv(CITY_DATA[city])
    # To convert start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # To extract month from Start Time to create new column
    df['month'] = df['Start Time'].dt.month
    # To extract day of week from Start Time to create new column
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # To extract hour from Start Time to create new column
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february','march', 'april', 'may', 'june']
        month = months.index(month) + 1
    # filter by month to create the new dataframe.
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df,month):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if df['month'].to_string() != month:
        common_month = df['month'].mode()[0]
        print ("The Most Popular Month Is: {}".format(months[common_month].title()))
    else:
        print ("The Most Popular Month: Not available since you have selected a specific month")

    # display the most common day of week
    common_day= df['day_of_week'].mode()[0]
    print ("The Most Popular Day of Week Is: {}".format(common_day.title()))

    # display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print ("The Most Popular Hour Is: {}".format(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print ("The Most Popular Start Station Is: {}".format(common_start_station))

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print ("The Most Popular End Station Is: {}".format(common_end_station))

    # display most frequent combination of start station and end station trip
    frequent_stations = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print ("\nThe Most Frequent Start/Stop Station Are: {}".format(frequent_stations))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print ("Total Travel Time in Seconds: ",total_travel_time)

    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print ('Average Travel Time in Seconds: ',average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user = df['User Type'].value_counts().to_frame()
    print ('User type:\n' ,count_user)

    # Display counts of gender
    try:
      gender_types = df['Gender'].value_counts().to_frame()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available.")

    # Display earliest, most recent, and most common year of birth
    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', int(Earliest_Year))
    except KeyError:
      print("\nEarliest Year:\nNo data available.")
    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', int(Most_Recent_Year))
    except KeyError:
      print("\nMost Recent Year:\nNo data available.")
    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', int(Most_Common_Year))
    except KeyError:
      print("\nMost Common Year:\nNo data available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df,month)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        i = 0
        raw = input("Would you like to see the first 5 rows of raw data? Type 'yes' or 'no'.\n").lower()
        pd.set_option('display.max_columns', 200)
        while True:
          if raw == 'no':
            break
          print(df[i:i+5])
          raw = input("Would you like to see the next 5 rows of raw data?\n").lower()
          i +=5
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
