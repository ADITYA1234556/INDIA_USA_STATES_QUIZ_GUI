import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240502.csv")

grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
#TODO: To create a csv file
squirrels = {
    "colours": ["Grey", "Black", "Cinnamon"],
    "numbers": [grey_squirrels, black_squirrels, cinnamon_squirrels]
}
#TODO: Create a csv file from a dictionary using dataframe
squirrels_data = pandas.DataFrame(squirrels)
squirrels_data.to_csv("squirrel data")



