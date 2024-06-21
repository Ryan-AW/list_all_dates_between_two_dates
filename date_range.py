''' a script that lists all dates between two dates the user inputs (inclusive) '''
import argparse
from datetime import datetime, timedelta


def validate_date(date: str):
    ''' checks date is formated dd/mm/yyyy - dates with more than 4 year digits are not allow :( '''
    try:
        return datetime.strptime(date, '%d/%m/%Y')
    except ValueError as error:
        raise argparse.ArgumentTypeError('Invalid date format. Please use dd/mm/yyyy') from error


def calc_date_range(start_date: str, end_date: str, start_inclusive: bool, end_inclusive: bool):
    ''' calculates date range '''
    if start_date > end_date:
        raise ValueError('Start date cannot be after end date')

    dates = []
    cur_date = start_date

    if start_inclusive:
        dates.append(cur_date.strftime('%d/%m/%Y'))
    cur_date += timedelta(days=1)

    while cur_date < end_date:
        dates.append(cur_date.strftime('%d/%m/%Y'))
        cur_date += timedelta(days=1)

    if end_inclusive:
        dates.append(cur_date.strftime('%d/%m/%Y'))
    return dates




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a list of dates between two dates')
    parser.add_argument('start_date', help='Start date (dd/mm/yyyy)', type=validate_date)
    parser.add_argument('end_date', help='End date (dd/mm/yyyy)', type=validate_date)

    parser.add_argument('-i', '--inclusive', action='store_true', help='Includes both start and end dates in the range')
    parser.add_argument('-s', '--start-inclusive', action='store_true', help='Includes the start date in the range')
    parser.add_argument('-e', '--end-inclusive', action='store_true', help='Includes the end date in the range')
    args = parser.parse_args()

    try:
        date_list = calc_date_range(
                args.start_date,
                args.end_date,
                (args.inclusive or args.start_inclusive),
                (args.inclusive or args.end_inclusive)
            )

    except ValueError:
        print('Start date cannot be after end date')
    else:
        print('\n'.join(date_list))
