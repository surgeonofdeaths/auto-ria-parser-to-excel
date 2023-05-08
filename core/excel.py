import pandas as pd

from core.parse_cars import FIELDS, PAGES, get_cars_parsed

data = get_cars_parsed(pages=PAGES)

new_df = pd.DataFrame(data=data, columns=FIELDS)

csv_name = 'info_cars2.csv'
new_df.to_csv(f"../{csv_name}", sep=',')
