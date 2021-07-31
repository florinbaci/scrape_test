import pandas as pd
import csv
from pandas import DataFrame

header_list = ['Date', 'Hour', 'Race', 'Country', 'Money bet','Against odds', 'Jokey']
list_df = pd.read_csv('output_races.csv', names=header_list)
final_dataframe = DataFrame(list_df)
# print(final_dataframe)

last_seven_positions = final_dataframe[-10:]

# print(last_seven_positions.iloc[-1][1])
# print(last_seven_positions.iloc[0][1])
# print(last_seven_positions.iloc[-1][2])
# print(last_seven_positions.iloc[0][2])

for i in last_seven_positions:
    if last_seven_positions.iloc[0][2] in last_seven_positions:
        # pass
        print('in list')
    else:
        print('not in list')

# for i in range(len(last_seven_positions)):
#     hour_comparison = (last_seven_positions.iloc[-1][1] == last_seven_positions.iloc[i][1])
#     race_comparison = (last_seven_positions.iloc[-1][2] == last_seven_positions.iloc[i][2])
#     if hour_comparison and race_comparison:
#         pass
#     else:
#         print('add to list')

# for i in range(len(last_seven_positions)):
#     if last_seven_positions.iloc[-1][1:3].all() == last_seven_positions.iloc[i][1:3].all():
#         print('ok')
#     else:
#         print('not')

# print(last_seven_positions)
# print(last_seven_positions.iloc[0][1:3])
# print('\n')
# print(last_seven_positions.iloc[3][1:3])
# print('\n')
# print(last_seven_positions.iloc[0][1:3].all() == last_seven_positions.iloc[3][1:3].all())
# print('\n')
# print(last_seven_positions.iloc[-1][1] == last_seven_positions.iloc[1][1])
# print('\n')
# print(last_seven_positions.iloc[-1][2] == last_seven_positions.iloc[1][2])

