import time
import pandas as pd
import numpy as np

# Indexing the CITY_DATA dictionary to get the corresponding filename for the given city name
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Defining a function to get the filters

def get_filters():
    welcome_string = """ Hello! Let\'s explore some US bikeshare data! 
 
  |* * * * * * OOOOOOOOOOOO|
  | * * * * *  ::::::::::::|         _@     
  |* * * * * * OOOOOOOOOOOO|      _`\<,_   
  |::::::::::::::::::::::::|     (*)/ (*) 
  |OOOOOOOOOOOOOOOOOOOOOOOO|

"""
    print(welcome_string)
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = ''
    while city not in ['chicago','new york city','washington']:

        city = input("\nIf you had to choose, would you choose Chicago, New York City, or Washington?").lower()
        print("\nYou have chosen to look at {}.".format(city))
        print()
        
        # get user input for month (all, january, february, ... , june)
        
    month = ''
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:

        month = input("Pick a month - January - June or all").lower()
        print("\nYou have chosen to look during {}.".format(month))
        print()
   
        # get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = ''
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']:
        
        day = input("Pick a day of the week - Monday - Friday or all").lower()
        print("\nYou have chosen to look on {}.".format(day))
            
        print("\nYou have chosen to look at {}, during {}, on a {}.".format(city, month, day))
        print('*'*120)
        print()
        
    return city, month, day

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Defining a function to load the data
    
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month/week/hour and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Defining a function to get the time stats

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # find the most popular month
    
    popular_month = df['month'].mode()
    
    print("\nThe most popular month is: {}".format(popular_month))

    # find the most popular week
    
    day_of_week = df['day_of_week'].mode()
    
    print("\nThe most popular week is: {}.".format(day_of_week))

    # find the most popular hour
    
    popular_hour = df['hour'].mode()
    
    print("\nThe most popular hour is: {}.".format(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*120)
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Defining a function to get the station stats

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()
    
    print("\nThe most commonly used start station is: {}.".format(start_station))

    # display most commonly used end station
    end_station = df['End Station'].mode()
    
    print("\nThe most commonly used end station is: {}.".format(end_station))

    # display most frequent combination of start station and end station trip
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*120)
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Defining a function to get the trip duration stats

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print("\nThe total travel time is: {}.".format(total_travel_time))
    
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    
    print("\nThe mean travel time is: {}.".format(mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*120)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Defining a function to get the user stats

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of User types
    if "User Type" in df:
        user_types = df['User Type'].value_counts()
        print("\nCounts of User Types is {}.".format(user_types))

    # Display counts of Gender
    if "Gender" in df:
        gender = df['Gender'].value_counts()
        print("\nCounts of Genders are: {}.".format(gender))
        
    # Display counts of Birth Year
    if "Birth Year" in df:
        birth_year = df['Birth Year'].value_counts()
        print("\nCounts of Birth Year's are: {}.".format(birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*120)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Defining a function to get the source data

def raw_data(df):
    """Displays source data."""
    start_time = time.time()
    
    raw_data = input('\nDo you want to see the first 5 rows of the source data? Enter yes or no.\n').lower()
    i=5
    while raw_data in ['yes','y','yep','yea'] and i+5 < df.shape[0]:
        print(df.iloc[i:i+5])
        i += 5
        raw_data = input('Do you want to see more source data? Enter yes or no.\n').lower()
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*120)
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
