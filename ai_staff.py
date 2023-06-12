data = []

my_dict = {
    'Apples': [10000, 5000, 8000, 6000],
    'Pears': [2000, 3000, 4000, 5000],
    'Bananas': [6000, 6000, 6500, 6000],
    'Oranges': [500, 300, 200, 700],
}

for key, values in my_dict.items():
    for index, value in enumerate(values):
        if index == 0:
            data.append([key, value])
        else:
            data.append(["", value])

for row in data:
    print(row)
