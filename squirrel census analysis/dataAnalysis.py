import pandas

data = pandas.read_csv("Beginner-Python-Projects\squirrel census analysis\Squirrel_Data.csv")

grey_squirrels = len(data[data["Primary Fur Color"] == 'Gray'])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == 'Cinnamon'])
black_squirrels = len(data[data["Primary Fur Color"] == 'Black'])

data_dict = {
    'Fur color':['Gray','Cinnamon','Black'],
    'Count':[grey_squirrels, cinnamon_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv('new_data')