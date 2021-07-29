import pandas as pd
import csv
from pandas import DataFrame

header_list = ['Date', 'Hour', 'Race', 'Country', 'Money bet','Against odds', 'Jokey']
list_df = pd.read_csv('output_races.csv', names=header_list)
final_dataframe = DataFrame(list_df)
# print(final_dataframe)

last_seven_positions = final_dataframe[-7:]
# for i in range(len(final_dataframe)):
#     if final_dataframe.iloc[-1][1:3].all() == final_dataframe.iloc[i][1:3].all():
#         print('ok')
#     else:
#         print('not')

# print(last_seven_positions)
print(last_seven_positions.iloc[-1][1:3])
print('\n')
print(last_seven_positions.iloc[2][1:3])
# # print('\n')
# # print(last_seven_positions.iloc[0][1:3].all() == last_seven_positions.iloc[3][1:3].all())
#
print(last_seven_positions.iloc[-1][1:3] == last_seven_positions.iloc[3][1:3])

