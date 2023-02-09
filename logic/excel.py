import pandas as pd
from parse_cars import get_cars_parsed, FIELDS, PAGES

data = get_cars_parsed(pages=PAGES)

new_df = pd.DataFrame(data=data, columns=FIELDS)
new_df.to_csv("../info_cars2.csv", sep=',')