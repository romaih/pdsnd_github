import time
import pandas as pd

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city = input("Which city would you like to check (Chicago, New york or Washington): ").title()
    while city not in CITY_DATA:
        city = input("Please choose a city from the list(Chicago, New york or Washington): ").title()

    #months used is this program are limited to the first six months
    month_filter = ['All', 'January', 'February' , 'March' , 'April', 'May' , 'june']
    month = input("Type month name to filter by or all : ").title()
    while month not in month_filter:
        month = input("Type correct month name or all : ").title()


    day_filter = ['All' , 'Monday' , 'Tuesday' , 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday ' , 'Sunday']
    day = input("Type day to filter by or all : ").title()
    while day not in day_filter :
        day = input("Type day correctly or all : ").title()

    print('-'*40)
    return city , month, day


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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    #day_name method gets day of week name
    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is : ', common_month)
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day is : ', common_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour is : ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most common start station is : ',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most common end station is : ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination station'] = df['Start Station'] + ' -AND- '+ df['End Station']
    print('Most common combination of stations is : ',df['Combination station'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time is :  ', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean travel time is :  ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types :\n',df['User Type'].value_counts())

    # TO DO: Display counts of gender
    # Not all files contain Gender column
    if 'Gender' in df.columns:
        print('Counts of gender :\n', df['Gender'].value_counts())
    else:
        print("No gender information of this city.")


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest year of birth is : ', df['Birth Year'].min())
        print('Most recent year of birth is : ', df['Birth Year'].max())
        print('Most common year of birth is : ', df['Birth Year'].mode()[0])
    else:
        print('No year of birth information of this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        count = 0

        while True:
            sample_data = input("\nWould you like to see sample data: yes/no \n")
            if sample_data.lower() != 'yes':
                break
            else:
                for i in range(5):
                    print(df.loc[count,:])
                    count += 1
                    print('-'*15)

        restart = input('\nWould you like to restart? Enter yes/no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
