# with traditional method
# List = []
#
# with open("weather_data.csv") as data_list:
#     # for content in data_list:
#     #     List.append(content)
#     data = data_list.readlines()

# using csv library
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     next(data)
#
#     temperature = []
#     for row in data:
#         temperature.append(int(row[1]))
#
# print(temperature)

# using pandas library
import pandas
data = pandas.read_csv("weather_data.csv")
# print(data)
# data_dict = data.to_dict()
#
# average = data["temp"].mean()
# print(average)
#
# maximum = data["temp"].max()
# print(maximum)
#
# # get data of column
# print(data["condition"])
# print(data.condition)

# get data of Row

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])
