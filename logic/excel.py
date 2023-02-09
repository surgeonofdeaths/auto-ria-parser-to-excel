import pandas as pd
from parse_cars import get_cars_parsed, preferred_marks, url

cols = ['Назва машини', 'Рік', 'Посилання', 'Ціна', ]
data = get_cars_parsed(url, car_marks=preferred_marks)

new_df = pd.DataFrame(data=data, columns=cols)
new_df.to_csv("../info_cars.csv", sep=',')