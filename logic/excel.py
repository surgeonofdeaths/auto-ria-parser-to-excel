import pandas as pd
from parse_cars import get_cars_parsed, FIELDS, PAGES

data = get_cars_parsed(pages=PAGES)

new_df = pd.DataFrame(data=data, columns=FIELDS)

csv_name = 'info_cars2.csv'
new_df.to_csv(f"../{csv_name}", sep=',')