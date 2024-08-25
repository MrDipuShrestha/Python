import pandas

data = pandas.read_csv("Squirrel_Data.csv")
# color_count = data.groupby("Primary Fur Color").size()
# print(color_count)

gray_color_count = len(data["Primary Fur Color"] == "Gray")
cinnamon_color_count = len(data["Primary Fur Color"] == "Cinnamon")
black_color_count = len(data["Primary Fur Color"] == "Black")
print(gray_color_count)
print(cinnamon_color_count)
print(black_color_count)
data_dict = {
    "Fur Color": ["Gray", "Cinnemon", "Black"],
    "Total": [gray_color_count, cinnamon_color_count, black_color_count]
}

df = pandas.DataFrame(data_dict)

df.to_csv("squirrel_count.csv")

