from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import re
# import openpyxl
# from openpyxl import load_workbook
# from openpyxl.workbook import Workbook
import sqlite3
# import csv
# import pandas as pd
# from pandas import DataFrame

# setting up the environment and getting the web page raddy to scrap

# workbook_name = 'data.xlsx'
# wb = load_workbook(workbook_name)
# ws = wb.active

driver = webdriver.Chrome('C:/Users/User/AppData/Local/Programs/Python/Python38/Scripts/chromedriver.exe')
driver.maximize_window()
url = "https://www.betfair.ro/exchange/plus/ro/curse-de-cai-pariuri-7/next"
driver.get(url)

# print(driver.page_source)

# x = 0
# while x < 100:

# get the list of events and some other tabs from the page
race_list = []
races_class = WebDriverWait(driver, 30).until(ec.presence_of_all_elements_located((By.CLASS_NAME, "node")))
for race in races_class:
    race_list.append(race.text)
#     print(race.text)
# print(race_list)

# because the list is in the second element it had to be separated and then use re library to select each event
# the re library is to select only te time "tag", the rest of the elements don't have the hour pattern
# THINGS TO SOLVE IN HERE:
# SOMETIMES THE PAGE DOESEN'T LOAD PROPERLY AND FOR THIS REASON CAN'T FIND THE SECOND ELEMENT
# THERE IS TRY AND EXCEPT BUT DOESEN'T WORK PROPERLY, WHEN CAN'T FIND THE SECOND ELEMENT
# THE PROBLEM GOES DOWN TO THE NEXT STATEMENT AND GIVES AN ERROR BECAUSE IT CAN'T FIND THE EVENTS
# VARIABLE
try:
    race_list = race_list[2].split()
    scheduled_hours = [i for i in race_list if re.search(r'\d\d:\d\d', i)]
    events = scheduled_hours[:7]  # only 10 events
    # print(events)
except:
    "IndexError: list index out of range"

# preparing each event for the scrap: obtaining the sum that it's been bet on the event, the title and the buttons
# obtaining all the links from the horse racing page
# PROBLEM TO BE DEALT WITH:
# WHEN IT LOOPS THROUGH ALL THE LINKS, IT TAKES THOSE RACEAS WITH THE SAME NAMES THAT ARE A DAY APART
# FOR NOW THIS ISN'T A PROBLEM BEACUSE THE RACEAS THAT ARE ON THE NEXT DAY DON'T MEET THE REQUIREMENT
# OF HAVING THE TOTAL SUM OF MONEY OVER 5000 LEI, BUT JUST A SMALL BUG TO HAVE IN MIND
race_title = []
race_link = []
for event in events:
    races = driver.find_elements_by_partial_link_text(event)
    for race in races:
        race_title.append(race.text)
        race_link.append(race.get_attribute('href'))

# print(race_title)
# for link in race_link:
#     print(link)

# find the race winner
# HERE IS A DELAY IMPLEMENTED, AFTER EACH ROW CHECKED WAITS 5 SEC FOR THE JOKEY TO BE
# IDENTIFIED, SO SAY IF THE WINNER IS AT POSITION 5, IT WILL TAKE 20 TO 25 SEC GET
# THE CORECT ANSWER
def race_finished():
    jockey_names = WebDriverWait(driver, 30).until(ec.presence_of_all_elements_located((By.CLASS_NAME, "name")))
    jockey_names_list = []
    for jockey in jockey_names:
        jokey_01 = jockey.text
        jockey_names_list.append(jokey_01)
        race_winner = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, "runner-winner")))
        race_win01: str = '//*[@id="main-wrapper"]/div/div[2]/div/ui-view/div/div/div[1]/div[3]/div/div[' \
                          '1]/div/bf-main-market/bf-main-marketview/div/div[2]/bf-marketview-runners-list[' \
                          '2]/div/div/div/table/tbody/tr['
        race_win02: str = ']/td/div[1]/div[2]/div'
    # print(jockey_names_list)
    position_final = []

    for position in range(len(jockey_names)):
        race_w = race_win01 + str(position + 1) + race_win02
        try:
            winner = WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, race_w)))
            if winner.text == "Câştigător":
                position_final.append(position)
            break
        except:
            "TimeoutException"

    venue_name = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CLASS_NAME, "venue-name")))
    venue_name_final = venue_name.text
    winner_final = jockey_names_list[int(position_final[0])]

    print(venue_name_final)
    print(winner_final)

# this function takes the raceas that meet the requirements
# IN HERE SHOULD BE THE "PRESSING OF THE BUTTONS ACTION"
# AFTER ALL CONDITIONS ARE CHECKED TO PLACE THE BET AND CALCULATE IF IT DOES HAVE TO
# INCREASE THE MONEY THAT HAVE TO BE PALCED ON A BET OR CO REVERSE TO THE "BASE"
# FOR NOW THIS COME SECOND ORDER OF IMPORTANCE DUE TO THE FACT THE WE WANT TO TEST
# THE HYPOTESIS FIRST


def race_to_start():
    jockey_names = WebDriverWait(driver, 30).until(ec.presence_of_all_elements_located((By.CLASS_NAME, "name")))
    jockey_names_list = []
    for jockey in jockey_names:
        jokey_01 = jockey.text
        jockey_names_list.append(jokey_01)

    combined = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CLASS_NAME, "total-matched")))
    event_money = combined.text
    event_money_int = int(event_money.split()[1].replace(',', ''))

    if event_money_int > 5000:
        venue_name = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CLASS_NAME, "venue-name")))
        venue_name_final = venue_name.text

        venue_date = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CLASS_NAME, "event-date")))
        venue_date_final = venue_date.text
        venue_date_final01 = venue_date_final[3:]
        print(venue_date_final01)

        venue_time = venue_name_final.split()[0]
        print(venue_time)
        # print(type(venue_time))

        venue_name_final01 = venue_name_final.split()[1:-1]
        print(venue_name_final01)
        # print(type(venue_name_final01))

        venue_country = venue_name_final.split()[-1]
        # print(venue_country)

        venue_total_sum = event_money_int
        print(venue_total_sum)

        jockey_names = WebDriverWait(driver, 30).until(ec.presence_of_all_elements_located((By.CLASS_NAME, "name")))

        # pro_quote01 = '//*[@id="main-wrapper"]/div/div[2]/div/ui-view/div/div/div[1]/div[3]/div/div[1]/div/bf-main-market/bf-main-marketview/div/div[
        # '2]/bf-marketview-runners-list[' \ '2]/div/div/div/table/tbody/tr[' pro_quote02 = ']/td[4]/button/div/span[1]'

        against_quote01 = '//*[@id="main-wrapper"]/div/div[2]/div/ui-view/div/div/div[1]/div[3]/div/div[1]/div/bf-main-market/bf-main-marketview/div/div[' \
                          '2]/bf-marketview-runners-list[' \
                          '2]/div/div/div/table/tbody/tr['
        against_quote02 = ']/td[5]/button/div/span[1]'

        quotes_final_against = []

        try:
            for jockey_place in range(len(jockey_names)):
                jokey = jockey_names[jockey_place]

                # pro_q = pro_quote01 + str(jockey_place + 1) + pro_quote02
                against_q = against_quote01 + str(jockey_place + 1) + against_quote02

                # quotes = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH, pro_q)))
                quotes01 = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH, against_q)))

                # print(jokey.text)
                # print(quotes.text)
                quotes_final_against.append(float(quotes01.text))
                # print(quotes01.text)

        except:
            'TimeoutException'

        # print(quotes_final_against)
        favorite_index = min(quotes_final_against)
        print(favorite_index)

        favorite_jokey_name = jockey_names_list[quotes_final_against.index(favorite_index)]
        print(favorite_jokey_name)

        # Calling the Test funtion to write the event in the DB
        test(venue_date_final01, venue_time, venue_name_final01, venue_country, venue_total_sum, favorite_index, favorite_jokey_name)

    else:
        pass

# The function that writes the values in the DB
def test(venue_date_final01, venue_time, venue_name_final01, venue_country,
         venue_total_sum, favorite_index, favorite_jokey_name):

    # The PROBLEM:
    # it does sees the variables but for some reason doesen't write them in the DB
    print(venue_date_final01, venue_time, venue_name_final01, venue_country,
          venue_total_sum, favorite_index, favorite_jokey_name)

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

    cur.execute("""INSERT INTO ex02(Data, Hour, Race, Country, Money, Against_odds, Jokey)
                  VALUES(?,?,?,?,?,?,?)""", [venue_date_final01, venue_time, venue_name_final01, venue_country, venue_total_sum, favorite_index, favorite_jokey_name])

    # Save and close DB
    db.commit()
    db.close()



    # headers = ['Date', 'Hour', 'Race', 'Country', 'Money', 'Against_odds', 'Jokey', 'Race W/L', 'Bank']
    #
    # workbook_name = 'data01.xlsx'
    # # wb = load_workbook(workbook_name)
    # wb = Workbook()
    # ws = wb.active
    # ws.title = "Races"
    # ws.append(headers)

    # workbook_name = 'data.xlsx'
    # wb = load_workbook(workbook_name)
    # ws = wb.active
    # print(ws.title)
    # headers = ['Date', 'Hour', 'Race', 'Country', 'Money', 'Against_odds', 'Jokey', 'Race W/L', 'Bank']


    # Got empty list - don't know why, maybe some reading of xl problem
    # race_row = [venue_date_final01, venue_time, venue_name_final01, venue_country, venue_total_sum, favorite_index, favorite_jokey_name]
    # print(race_row)
    # race_hour_list = []
    # print(race_hour_list)
    # race_title_list = []
    # print(race_title_list)

    # for race_info in range(2, ws.max_row + 1):
    #     race_hour = ws.cell(row=race_info, column=2).value
    #     race_title = ws.cell(row=race_info, column=3).value
    #     # print(race_hour)
    #     race_hour_list.append(race_hour)
    #     race_title_list.append(race_title)
    # print(race_hour_list[-5:])
    # print(race_title_list[-5:])
    # print('Loop')
    # print(venue_time)
    # print(race_hour_list[-5])
    # print(venue_name_final01)
    # print(race_title_list[-5])
    # print('loop end')
    # if venue_time not in race_hour_list[-5:] and venue_name_final01 not in race_title_list[-5:]:
    #     # add the betting button
    #     print(race_row)
    #     ws.append(race_row)
    #     # ws.append(race_row)
    #
    #     wb.save(filename=workbook_name)

    # else:
    #     pass








            # for events_checked in last_seven_positions:
            # if ((last_seven_positions['Hour'] == venue_time) & (last_seven_positions['Race'] == venue_name_final01)).any():
            #     pass
            # else:
            #     writer.writerow([venue_date_final01, venue_time, venue_name_final01, venue_country, venue_total_sum, favorite_index, favorite_jokey_name])
                # break


        # list01 = csv.reader(open('output_races.csv', 'r'))
        # list(csv.reader(open('output_races.csv', 'r')))
        # last_five_rows = list01[-5:]

        # header_list = ['Date', 'Hour', 'Race', 'Country', 'Money bet', 'Against odds', 'Jokey']
        # list01 = pd.read_csv('output_races.csv', names=header_list)
        # final_dataframe = DataFrame(list_01)
        # print(final_dataframe)

        # last_seven_positions = final_dataframe[-7:]
        # print(last_seven_positions)
        # no aici ma impotmolesc big time, am crezut aseara ca am gasit pb, insa nu merge
        # trebuie sa compar ora de start si numele cursei daca sunt in csv
        # daca sunt in csv, sare peste, in caz contrar le scrie in csv

        # for events_checked in last_seven_positions:
        #     if ((last_seven_positions['Hour'] == venue_time) & (last_seven_positions['Race'] == venue_name_final01)).any():
        #         pass
        #         # print('in list')
        #     else:
        #         output_races = open('output_races.csv', 'a+', newline='')
        #         output_writer = csv.writer(output_races)
        #         output_writer.writerow([venue_date_final01, venue_time, venue_name_final01, venue_country, venue_total_sum, favorite_index, favorite_jokey_name])
        #         output_races.close()
        #     break



        # if [venue_date_final01, venue_time, venue_name_final01, venue_country, favorite_jokey_name] in last_five_rows:
        #     pass
        # else:
        #     output_races = open('output_races.csv', 'a+', newline='')
        #     output_writer = csv.writer(output_races)
        #     output_writer.writerow([venue_date_final01, venue_time, venue_name_final01, venue_country, venue_total_sum, favorite_index, favorite_jokey_name])
        #
        #     output_races.close()
    # else:
    #     pass

# break


# while True:
try:
    for race in race_link:
        driver.get(race)
        race_status = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CLASS_NAME, "market-status-label")))
        if race_status.text == "Intră în desfăşurare":
            race_to_start()
            # csv_write()
        elif race_status.text == 'Închis':
            race_finished()
        elif race_status.text == "În desfăşurare":
            pass

except:
    'TimeoutException'

    # x += 1
driver.quit()
