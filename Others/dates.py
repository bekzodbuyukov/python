from datetime import datetime, timedelta


def generate_list() -> iter:
    dates = []

    for i in range(100):
        dates.append(datetime.now() + timedelta(minutes=i))
    
    return dates


def get_every_tenth(dates: iter) -> iter:
    every_tenth_minutes = []

    for index, date in enumerate(dates):
        if index % 10 == 0:
            every_tenth_minutes.append(date)
    
    return every_tenth_minutes


if __name__ == "__main__":
    dates = generate_list()

    for date in dates:
        print(date, end="\n")
    
    print("\n\n\n")
    
    for date in get_every_tenth(dates):
        print(date, end="\n")
