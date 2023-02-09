from bs4 import BeautifulSoup
from settings import *
import requests


def _is_title_in_car(car_marks, title):
    for mark in car_marks:
        if mark.lower() in title.lower():
            return True
    return False


def _print_to_console(*args):
    fields = ['Назва машини', 'Рік', 'Посилання', 'Ціна', 'Пробіг (тис. км)']
    for i in range(len(fields)):
        print(f'{fields[i]}: "{args[i]}"')
    print()


def _get_fields(car, car_marks, console):
    title, year = car.find('div', class_='ticket-title').text.strip().rsplit(maxsplit=1)
    if not _is_title_in_car(car_marks, title):
        return

    price = int(car.find('span', class_='i-block').text.strip().replace(' ', '').rsplit(maxsplit=1)[0].replace(' ', ''))
    characteristic = car.find('ul', class_='characteristic')
    race = int(characteristic.find('li', class_='js-race').text.split(maxsplit=1)[0])
    if MIN_YEAR > int(year) or not MIN_PRICE <= price <= MAX_PRICE \
            or race > MAX_RACE:
        return

    href = car.find('a', class_='m-link-ticket')['href'].strip()

    if console:
        _print_to_console(title, year, href, price, race)
    else:
        return [title, year, href, price]


def get_cars_parsed(url, pages=10, *, car_marks=None, console=False):
    result_cars = []

    for page in range(pages):
        next_url = url % page
        response = requests.get(next_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        search_results = soup.find('div', id='searchResults')
        car_content = search_results.select('div .content-bar')

        for car in car_content:
            filled_fields = _get_fields(car, car_marks, console)
            if not console:
                result_cars.append(filled_fields)
    return result_cars if not console else None


def main():
    print(get_cars_parsed(url, car_marks=preferred_marks, console=True))


if __name__ == '__main__':
    main()
