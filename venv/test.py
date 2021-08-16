import pandas as pd
import csv
from pandas import DataFrame

header_list = ['Date', 'Hour', 'Race', 'Country', 'Money bet','Against odds', 'Jokey']
list_df = pd.read_csv('output_races.csv', names=header_list)
final_dataframe = DataFrame(list_df)
# print(final_dataframe)

last_seven_positions = final_dataframe[-7:]
for i in range(len(last_seven_positions)):
    if last_seven_positions.iloc[-2][2] == last_seven_positions.iloc[i][2]:
        print('ok')
    else:
        print('not')

# print(last_seven_positions)
# print(last_seven_positions.iloc[-1][2])
# print('\n')
# print(last_seven_positions.iloc[3][2])
# print('\n')
# print(last_seven_positions.iloc[-1][2] == last_seven_positions.iloc[3][2])

# ((df['hour'] == '07:24') & (df['race'] == "['Sunshine', 'Coast']")).any()

x = 0
while x < 10:

    date_01 = '17 Aug'
    hour = '09:22'
    race = "['Budapest']"
    country = '(HUN)'
    money = '5807'
    against_odds = '3.8'
    jokey = "White Rhino\nGeorge"

    for i in range(len(df)):
        if ((df['hour'] == hour) & (df['race'] == race)).any():
            pass
        else:
            df = df.append({'date': date_01,
                            'hour': hour,
                            'race': race,
                            'country': country,
                            'money': money,
                            'against_odds': against_odds,
                            'jokey': jokey},
                           ignore_index=True)
        break

    x += 1