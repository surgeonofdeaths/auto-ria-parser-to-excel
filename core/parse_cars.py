import requests
from bs4 import BeautifulSoup

from core.settings import *


def _is_title_in_car(title):
    for mark in PREFERRED_MARKS:
        if mark.lower() in title.lower():
            return True
    return False


def _print_to_console(*args):
    for i in range(len(FIELDS)):
        print(f'{FIELDS[i]}: "{args[i]}"')
    print()


def _check_fields(title, year, price, race, location, sold):
    if _is_title_in_car(title) and \
            sold is SOLD and \
            MIN_YEAR < int(year) and \
            MIN_PRICE <= price <= MAX_PRICE and \
            (isinstance(race, str) or int(race) < MAX_RACE) and \
            (LOCATION == '__all__' or location.lower() in list(LOCATION)):
        return True
    return False


def _get_fields(car, *, console=False):
    title, year = car.find('div', class_='ticket-title').text.strip().rsplit(maxsplit=1)
    price = int(car.find('span', class_='i-block').find('span', attrs={'data-currency': 'UAH'}).text.replace(' ', ''))
    dollar_price = int(
        car.find('span', attrs={'data-currency': 'USD'}).text.replace(' ', '')
    )
    href = car.find('a', class_='m-link-ticket')['href'].strip()
    date = car.find('div', class_='footer_ticket').find('span')
    characteristic = car.find('ul', class_='characteristic')

    race = characteristic.find('li', class_='js-race')
    location = race.next_sibling.next_sibling
    fuel = location.next_sibling.next_sibling
    transmission = fuel.next_sibling.next_sibling

    race, location = race.text.split(maxsplit=1)[0], location.text.replace('( від )', '').strip()
    fuel, transmission = fuel.text.strip(), transmission.text.strip()

    race = int(race) if race.isdecimal() else race
    if date.has_attr('data-add-date'):
        sold = False
        date = date['data-add-date'].split()[0]
    else:
        sold = True
        date = date['data-sold-date'].split()[0]

    if not ANY and not _check_fields(title, year, dollar_price, race, location, sold):
        return

    sold = 'Продано' if sold else 'В наявності'
    data_fields = [title, year, href, price, dollar_price, race, location, fuel, transmission, sold, date]

    if console:
        _print_to_console(*data_fields)
    else:
        return data_fields


def get_cars_parsed(pages=PAGES, *, console=False):
    result_cars = []

    for page in range(pages):
        if not console:
            print(f'Сторінка №{page + 1} у процесі..')
        next_url = URL % page
        response = requests.get(next_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        search_results = soup.find('div', id='searchResults')
        car_content = search_results.select('div .content-bar')

        for car in car_content:
            filled_fields = _get_fields(car, console=console)
            if not console and filled_fields:
                result_cars.append(filled_fields)
    return result_cars if not console else None


def main():
    get_cars_parsed(console=True)


if __name__ == '__main__':
    main()
