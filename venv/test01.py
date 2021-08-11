import pandas as pd
import csv
from pandas import DataFrame

# csv_file = csv.reader(open('output_races.csv', "r"), delimiter=",")

header_list = ['Date', 'Hour', 'Race', 'Country', 'Money bet','Against odds', 'Jokey']
list_df = pd.read_csv('output_races.csv', names=header_list)
final_dataframe = DataFrame(list_df)
# print(final_dataframe)
tail_pos = final_dataframe[-7:]

ev_time = tail_pos.iloc[-5][1]
ev_race = tail_pos.iloc[-5][2]

x = 0
while 7 > x:

    if ((tail_pos['Hour'] == ev_time) & (tail_pos['Race'] == ev_race)).any():
      pass
      # print('is in')
    else:
      print('not in')
    # break

    x += 1

# for row in csv_file:
#     #if current rows 2nd value is equal to input, print that row
#     if ev_race == row[2]:
#          print (row)

# header_list = ['Date', 'Hour', 'Race', 'Country', 'Money bet','Against odds', 'Jokey']
# list_df = pd.read_csv('output_races.csv', names=header_list)
# final_dataframe = DataFrame(list_df)
# print(final_dataframe)


#
# last_seven_positions = final_dataframe[-5:]

# print(last_seven_positions.iloc[-1][1])
# print(last_seven_positions.iloc[0][1])
# print(last_seven_positions.iloc[-1][2])
# print(last_seven_positions.iloc[0][2])
# x = 0
# while 5 > x:
# for i in range(len(last_seven_positions)):
#     if ev_time in last_seven_positions.iloc[i][1] and ev_race in last_seven_positions.iloc[i][2]:
#         print('in list')
#         break
#     else:
#         print('ad to list')
#         break
    # x += 1

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

