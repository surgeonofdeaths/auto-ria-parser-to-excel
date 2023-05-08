from environs import Env
from pydantic import Field, BaseSettings

# env = Env()
# env.read_env()

fields: list[str] = [
    'Назва машини', 'Рік', 'Посилання', 'Ціна UAH',
    'Ціна $', 'Пробіг (тис. км)', 'Місце', 'Бензин',
    'Коробка передач', 'Стан', 'Дата',
]

preferred_marks: list[str] = [
    'toyota', 'mercedes', 'bmw',
    'honda', 'volkswagen', 'ford',
    'audi', 'suzuki', 'mazda',
    'nissan', 'Hyundai',
]


class Settings(BaseSettings):
    URL: str
    FIELDS: list[str]
    CSV_NAME: str
    ANY: bool
    MIN_PRICE: int
    MAX_PRICE: int
    MAX_RACE: int
    MIN_YEAR: int
    LOCATION: list[str]
    PAGES: int
    SOLD: bool
    FIELDS: list[str] = fields
    PREFERRED_MARKS: list[str] = preferred_marks

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


# URL: str = env.str('URL')

# ANY: bool = env.bool('ANY', default=False)
# CSV_NAME: str = env.str('CSV_NAME', default='info_cars')
# MIN_PRICE: int = env.int('MIN_PRICE', default=0)
# MAX_PRICE: int = env.int('MAX_PRICE', default=1_000_000)
# MAX_RACE: int = env.int('MAX_RACE', default=1000)
# MIN_YEAR: int = env.int('MIN_YEAR', default=1900)
# LOCATION: str = env.str('LOCATION', default='__all__').split(',')
# PAGES: int = env.int('PAGES', default=10)
# SOLD: bool = env.bool('SOLD', default=False)
