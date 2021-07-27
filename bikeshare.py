import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('HI! Let\'s explore some US bikeshare Cities!')
    while True:
        city = input("choose one city (chicago, new york city, washington) to explore ")
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Error")

    while True:    
        month = input("write done a  month to explore or just write all to see all the months")
        month = month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Error")

    while True:
        day = input("write the day name for example : monday to see monday only or all to see all the days")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Error")
    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        df = df[df['month'] == month]

    if day != 'all':
        
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n Calculating The Most Frequent Times of Travel \n')
    start_time = time.time()

    print("The usual month is \n ", df['month'].mode()[0], "\n")

    print("The usual day weakly  is \n", df['day_of_week'].mode()[0], "\n")

    df['hour'] = df['Start Time'].dt.hour
    print("The usual started hour is ", df['hour'].mode()[0])


    print("\n This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n Calculating The Most Popular Stations and Trip\n')
    start_time = time.time()

    print("The usual used start station is ", df['Start Station'].mode()[0], "\n")
    print("The usual used end station is ", df['End Station'].mode()[0], "\n")
    df['combination'] = df['Start Station'] + " " + df['End Station']
    print("The usual combination of start station and end station trip is: ", df['combination'].mode()[0])



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n Calculating Trip Duration...\n')
    start_time = time.time()


    print("Total travel time:", df['Trip Duration'].sum(), "\n")
    print("Total mean time is:", df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\n Calculating User Stats...\n')
    start_time = time.time()

    user_types = df.groupby(['User Type'])['User Type'].count()
    print(user_types, "\n")
    if city != 'washington':
        gen = df.groupby(['Gender'])['Gender'].count()
        print(gen)
        mryob = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
        eyob = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
        mcyob = df['Birth Year'].mode()[0]
        print("The earliest year of birth is ", eyob, "\n")
        print("The most recent year of birth is ", mryob, "\n")
        print("The most common year of birth is ", mcyob, "\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    x = 1
    while True:
        raw = input('\n  if you want to see 5 lines of raw data Enter yes \n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\n Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
