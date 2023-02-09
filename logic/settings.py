from environs import Env

env = Env()
env.read_env()

url = 'https://auto.ria.com/uk/search/?indexName=auto,order_auto,newauto_search&year[0].gte=2005&categories.main.id=1&country.import.usa.not=-1&price.USD.gte=3000&price.USD.lte=5500&price.currency=1&gearbox.id[0]=1&mileage.lte=300&abroad.not=0&custom.not=1&page=%s&size=20'
preferred_marks = [
    'toyota', 'mercedes', 'bmw', 'honda',
    'volkswagen', 'ford', 'audi', 'suzuki',
    'mazda', 'nissan',
]

MIN_PRICE = env.int('MIN_PRICE', default=0)
MAX_PRICE = env.int('MAX_PRICE', default=1_000_000)
MAX_RACE = env.int('MAX_RACE', default=1000)
MIN_YEAR = env.int('MIN_YEAR', default=1900)