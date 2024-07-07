from datetime import datetime, timedelta


def display_current_datetime():
    #get the current date
    current_date = datetime.now()
    #format current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%m:%S")
    
    #print formated date and time
    print(f'current date and time {formatted_date}')

def calculate_future_date():
    number_of_days = int(input('Enter the number of days to add to the current date: '))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)

    #format and print future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f'Future date: {formatted_future_date}')

#main fuction to execute the script
def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == '__main__':
    main()





