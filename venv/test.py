# import csv
import openpyxl
from openpyxl import load_workbook
from openpyxl.workbook import Workbook

x = 0
while x < 6:

    workbook_name = 'data.xlsx'
    wb = load_workbook(workbook_name)
    ws = wb.active

    headers = ['Date', 'Hour', 'Race', 'Country', 'Money', 'Against_odds', 'Jokey']

    date_01 = '26 Aug'
    hour = '20:18'
    race = "['Palmas']"
    country = '(SPA)'
    money = '14021'
    against_odds = '3.1'
    jokey = 'Boy\nBlue'

    # wb = openpyxl.Workbook()
    # sheet = wb.active

    # sheet.title = 'races'
    # sheet.append(headers)

    race = [date_01, hour, race, country, money, against_odds, jokey]


    race_hour_list = []
    race_title_list = []

    for race_info in range(2, ws.max_row + 1):
        race_hour = ws.cell(row=race_info, column=2).value
        race_title = ws.cell(row=race_info, column=3).value
        # print(race_hour)
        race_hour_list.append(race_hour)
        race_title_list.append(race_title)
    # print(race_hour_list[-5:])

    if hour not in race_hour_list[-5:] and race not in race_title_list[-5:]:
        ws.append(race)

        wb.save(filename=workbook_name)
    # print(type(race_hour_list[-5]))
    # print('not in')
    # break
    x += 1

# wb.save(filename=workbook_name)


# wb.save('data.xlsx')

# sheet = wb['Sheet']
# sheet['A1'] = 'Data'
# print(sheet['A1'].value)
# print(sheet.title)

# with open('output_races.csv', 'r', newline='') as csv_file:
#     # writer = csv.writer(csv_file, delimiter=',')
#     # writer.writerow(['Date', 'Hour', 'Race', 'Country', 'Money', 'Against_odds', 'Jokey'])
#     # writer.writerow([date_01, hour, race, country, money, against_odds, jokey])
#     reader = csv.reader(csv_file, delimiter=',')
#     header = next(reader)
#     # print(reader)

# row01 = [date_01, hour, race, country, money, against_odds, jokey]
# with open('output_races.csv', 'r') as csv_file:
#     reader = csv.reader(csv_file, delimiter=',')
#     writer = csv.writer(csv_file, delimiter=',')
#     header = next(reader)

    # for index, column_header in enumerate(header):
    #     print(index, column_header)


    # hours = []
    # for row in reader:
        # print(row[2])
    #     hour02 = row[2]
    #     hours.append(hour02)
    # print(hours)
    # if hour in hours:
    #     print('is in')
        # pass
    # else:
    #     print('not in')
        # print(hours)
        # with open('output_races.csv', 'a+', newline='') as csv_file:

        # writer.writerow(row01)
        # csv_file.close()



    # for row in reader:
    #     # print(row)
    #     if row[1] == hour and row[2] == race:
    #         # pass
    #         print('in list')
    #     else:
    #         with open('output_races.csv', 'a+', newline='') as csv_file:
    #             writer = csv.writer(csv_file, delimiter=',')
    #             writer.writerow([date_01, hour, race, country, money, against_odds, jokey])
    #             csv_file.close()
    #         print('not in list')
    #         break


 # print(row['Hour'], row['Race'])
    # header = next(reader)
    # if header[1] == hour:
    #     print('Ola')
    # print(header[1:3])