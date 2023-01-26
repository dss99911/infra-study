import yaml

#%% write
obj = {'Vegetables': ['Pepper', 'Tomato', 'Garlic']}
with open('vegetables.yml', 'w') as f:
    yaml.dump(obj, f)

#%% read
with open('vegetables.yml') as f:
    vegetables = yaml.load(f, Loader=yaml.FullLoader)
    print(vegetables)

