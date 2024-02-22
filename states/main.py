# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
    # print(stripped_data)

import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         # print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd


data = pd.read_csv("weather_data.csv", index_col="day")
# temp_list = data["temp"].to_list()
# # avg = data["temp"].mean()
# max = data["temp"].max()
# print(max)

# print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])
# print(data.temp)
# print(data["temp"])
# print(data[["temp"]])
# print(data)
# print(data[data.temp > 20])
# print(data.temp.max())
# print(data.temp > 20)
# print(data.condition.value_counts())
# print(data[data.condition == "Rain"])
