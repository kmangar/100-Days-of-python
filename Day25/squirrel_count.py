import pandas as pd

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))

# data = pd.read_csv("weather_data.csv")

# average = sum(data["temp"])/len(data["temp"])
#
# print(data["temp"].max())
#
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp = monday_temp *(9/5)+32
# print(monday_temp)
#

# MAKE A CSV FILE WITH ALL THE COLORS AND COUNT MANY THERE ARE
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrel = data[data["Primary Fur Color"] == "Gray"]
cinnamon_squirrel = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrel = data[data["Primary Fur Color"] == "Black"]

data_dict= {
    "Fur Color": ["Grey", "Black", "Cinnamon"],
    "Count": [len(gray_squirrel), len(black_squirrel), len(cinnamon_squirrel)]
}

# TURN THE DICT TO A DataFrame
df = pd.DataFrame(data_dict)
# Convert the DataFrame to a csv file
df.to_csv("squirrel_count.csv")
