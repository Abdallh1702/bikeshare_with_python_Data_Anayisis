import time
import pandas as pd


CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def check_input_user(user_str, input_name):
    while True:
        user_input = input(user_str).lower()
        try:
            if user_input in ['chicago', 'new york city', 'washington'] and input_name == 'city':
                break
            elif user_input in ['january', 'february', 'march', 'april', 'may', 'june', 'all']\
                    and input_name == 'month':
                break
            elif user_input in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
                                'all'] and input_name == 'day':
                break
            else:
                if input_name == 'city':
                    print("Sorry Wrong city")
                if input_name == 'month':
                    print("Sorry wrong month")
                if input_name == 'day':
                    print("Sorry wrong day")
        except ValueError:
            print("The entry is wrong")

    return user_input


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    city = check_input_user("Would you like to see the data for chicago, new york city or washington?", 'city')
    # TO DO: get user input for month (all, january, february, ... , june)
    month = check_input_user("Which Month (all, january, ... june)?", 'month')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = check_input_user("Which day? (all, monday, tuesday, ... sunday)", 'day')
    print('-' * 40)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month :', df['month'].mode()[0])
    # TO DO: display the most common day of week
    print('The most common day of week :', df['day_of_week'].mode()[0])
    # TO DO: display the most common start hour
    print('The most common start hour:', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    print('Most commonly used start station : ', df['Start Station'].mode()[0])
    # TO DO: display most commonly used end station
    print(' Most commonly used end station : ', df['End Station'].mode()[0])
    # TO DO: display most frequent combination of start station and end station trip
    start_to_end = df.groupby(['Start Station', 'End Station'])
    print('Most frequent combination of start station and end station trip : ',
          start_to_end.size().sort_values(ascending=False).head(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    print('Total travel time : ', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean travel time : ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    print('Counts of user types : ')
    print(df['User Type'].value_counts())
    print('-' * 20)
    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('Counts of gender : ')
        print(df['Gender'].value_counts())
        print('-' * 20)
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('Earliest year:', df['Birth Year'].min())
        print('Most recent year:', df['Birth Year'].max())
        print('Most common year : ', df['Birth Year'].mode()[0])
        print('-' * 20)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
