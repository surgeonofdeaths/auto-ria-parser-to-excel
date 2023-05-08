import pandas as pd

from .settings import config


def generate_csv(data: list | None) -> None:
    if data is None:
        print('Done!\nAll cars are parsed')
        return

    new_df = pd.DataFrame(data=data, columns=config.FIELDS)
    csv_name = f'{config.CSV_NAME}.csv'
    new_df.to_csv(f"../{csv_name}", sep=',')
    print('Your csv file is ready!')
