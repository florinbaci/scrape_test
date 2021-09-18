# import pandas as pd
# import csv
# from pandas import DataFrame
import sqlite3

def race_data():
  date_01 = '26 SEPT'
  hour = '10:30'
  race = "['Swan', 'Hill']"
  country = '(AUS)'
  money = '175487'
  against_odds = '4.0'
  jokey = "Broadway Lane\nJarrod Fry"
  test(date_01, hour, race, country, money, against_odds, jokey)

  # individual_race = [date_01, hour, race, country, money, against_odds, jokey]
  # return date_01, hour, race, country, money, against_odds, jokey

def test(date_01, hour, race, country, money, against_odds, jokey):
  # print(date_01, hour, race, country, money, against_odds, jokey)

  # Connect to database
  db = sqlite3.connect('ex02.db')

  # Create a cursor
  cur = db.cursor()

  # Create a table
  # cur.execute("""CREATE TABLE IF NOT EXISTS ex02(
  #            Data text NOT NULL,
  #            Hour text NOT NULL,
  #            Race text NOT NULL,
  #            Country text NOT NULL,
  #            Money integer NOT NULL,
  #            Against_odds real NOT NULL,
  #            Jokey text NOT NULL)""")

  # Search into DB for the event and update table
  cur.execute("""INSERT INTO ex02(Data, Hour, Race, Country, Money, Against_odds, Jokey)
              VALUES(?,?,?,?,?,?,?)""", [date_01, hour, race, country, money, against_odds, jokey])

  # cur.execute("""UPDATE ex02(Data, Hour, Race, Country, Money, Against_odds, Jokey)
  #             VALUES(?,?,?,?,?,?,?)""", (date_01, hour, race, country, money, against_odds, jokey))
  #
  # cur.execute('SELECT * FROM ex02')


  db.commit()
  db.close()


race_data()

# def race_data():
#   date_01 = '10 SEPT'
#   hour = '07:30'
#   race = "['Swan', 'Hill']"
#   country = '(AUS)'
#   money = '175487'
#   against_odds = '4.0'
#   jokey = "Broadway Lane\nJarrod Fry"
#
#   individual_race = [date_01, hour, race, country, money, against_odds, jokey]
#   return date_01, hour, race, country, money, against_odds, jokey
  # print(date_01, hour, race, country, money, against_odds, jokey)
  # print(individual_race)

# print(race_data())
# race_f = race_data('1 SEPT', '08:30', "['Swan', 'Hill']", '(AUS)', '175487', '4.0', "Broadway Lane\nJarrod Fry")
# print(race_f)

# Connect to database
# db = sqlite3.connect('ex02.db')

#Create a cursor
# cur = db.cursor()

#Create a table
# cur.execute("""CREATE TABLE IF NOT EXISTS ex01(
#            Data text NOT NULL,
#            Hour text NOT NULL,
#            Race text NOT NULL,
#            Country text NOT NULL,
#            Money integer NOT NULL,
#            Against_odds real NOT NULL,
#            Jokey text NOT NULL)""")

# Search into DB for the event and update table
#
# cur.execute("""INSERT INTO ex02(Data, Hour, Race, Country, Money, Against_odds, Jokey)
#             VALUES(?,?,?,?,?,?,?)""", individual_race)

# cur.execute("""UPDATE ex01(Data, Hour, Race, Country, Money, Against_odds, Jokey)
#             VALUES(date_01, hour, race, country, money, against_odds, jokey)""")

# cur.execute('SELECT * FROM ex02')

# cur.execute("SELECT * FROM ex WHERE name = 'NEXT'")
# items = cur.fetchall()

# for item in items:
#   print(item)

# for item in cur.fetchall():
#   print(item[1])
  # if item[1]:
  #   print('in')
# print(cur.fetchall())


# db.commit()
# db.close()



# with open('data.csv', 'a+', newline='') as f:
# df = DataFrame(pd.read_csv('data.csv'))
#     print(df)
# df = pd.read_csv('data.csv')
# print(df)
    # , names = header_list

# print(last_seven_positions)

# with open('data.csv', 'r', newline='') as csv_file:
#   del csv_file['Unnamed: 0']
# date_01 = '26 Aug'
# hour = '20:52'
# race = "['Poalata']"
# country = '(Egipt)'
# money = '7807'
# against_odds = '2.1'
# jokey = "White Rhino\nGeorge"

# x = 0
# while x < 10:
#     df = DataFrame(pd.read_csv('data.csv'))
    # for i in range(len(last_seven_positions)):
    # if ((df.tail()['hour'] == hour) & (df.tail()['race'] == race)).any():
    #     pass
    # else:
    #     df = df.append({'date': date_01,
    #                     'hour': hour,
    #                     'race': race,
    #                     'country': country,
    #                     'money': money,
    #                     'against_odds': against_odds,
    #                     'jokey': jokey},
    #                     ignore_index=True)
    #
    #     df.to_csv('data.csv', index=False)
        # break
    # x += 1
# df = df.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'])
# df.to_csv('data.csv')
# print(df[['hour', 'race']])

# df['alt'].add((df.index+1)*400)

# df.to_csv('data.csv')

# with open('output_races.csv', 'a+', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',')
    # df = DataFrame('output_races.csv', columns=['Date', 'Hour', 'Race', 'Country', 'Money bet', 'Against odds', 'Jokey'])
    # df_final = pd.read_csv('output_races.csv', names=header_list)
    # last_seven_positions = df_final[-7:]
    
    # writer.writerow(['07:26', 'Here'])

# print(last_seven_positions)
# csv_file = csv.reader(open('output_races.csv', "r"), delimiter=",")

# header_list = ['Date', 'Hour', 'Race', 'Country', 'Money bet','Against odds', 'Jokey']
# list_df = pd.read_csv('output_races.csv', names=header_list)
# final_dataframe = DataFrame(list_df)
# # print(final_dataframe)
# tail_pos = final_dataframe[-7:]
#
# ev_time = tail_pos.iloc[-5][1]
# ev_race = tail_pos.iloc[-5][2]
#
# x = 0
# while 7 > x:
#
#     if ((tail_pos['Hour'] == ev_time) & (tail_pos['Race'] == ev_race)).any():
#       pass
#       # print('is in')
#     else:
#       print('not in')
#     # break
#
#     x += 1

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

