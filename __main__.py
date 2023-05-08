from core.excel import generate_csv
from core.parse_cars import get_cars_parsed
from core.settings import config

if __name__ == "__main__":
    data = get_cars_parsed(console=config.CONSOLE)
    generate_csv(data)
