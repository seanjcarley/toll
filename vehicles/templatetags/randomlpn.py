import json
import random


def generate_vehicle():
    ''' 
        generate json file with 100 random vehicles 
        Irish LPS are in the following format:
            YYPCCXXXXX
            YY: last 2 digits of the year (ie: 2022 -> 22)
            P: the period the vehicle was first registered (
                    ie: 1 if within the first 6 months of the year
                    or 2 if within the last 6 months of the year)
            CC: The 1-2 character county code where the vehicle was 
            first registered
            XXXXX: This number is derived from the number of vehicles
                    registered in a county area (ie: the first vehicle 
                    registered will be 1, second will be 2, etc...)
    '''
    LPN = []
    vehicles = {}
    year = 2013
    county = ('C', 'CE', 'CN', 'CW', 'D', 'DL', 'G', 'KE', 'KK', 'KY', 'L', 
                'LD', 'LH', 'LM', 'LS', 'MH', 'MN', 'MO', 'OY', 'RN', 'SO', 
                'T', 'W', 'WH', 'WX', 'WW')
    makes = ['BMW', 'Audi', 'Citroen', 'Fiat', 'Ford', 'Honda', 'Hyundai', 
            'Kia', 'Land Rover', 'Mazda', 'Mercedes', 'Nissan', 'Opel', 
            'Seat', 'Volkswagen']
    models = ['MDL01','MDL02','MDL03','MDL04','MDL05']
    colors = ['Red', 'Green', 'Blue', 'White', 'Black', 'Grey', 'Yellow', 
            'Multi']
    
    # generate 10 random LPNs for the years 2013 -> 2022 
    while year < 2023:
        temp_year = str(year)[2:]
        for i in range(0, 10):
            if i < 5:
                toy = 1
            else:
                toy = 2
            lpn = temp_year + str(toy) + county[random.randint(0, 25)] + \
                    str(random.randint(1000, 99999))
            LPN.append(lpn)
            i += 1
        year += 1

    # assign a random make, model, color, and vehicle class
    for i in LPN:
        vehicles[i] = {
            'make': makes[random.randint(0, len(makes) - 1)],
            'model': models[random.randint(0, len(models) - 1)],
            'color': colors[random.randint(0, len(colors) - 1)],
            'class': random.randint(1, 7),
        }

    with open('random_lpns.json', 'w', encoding='utf-8') as f:
        json.dump(vehicles, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    generate_vehicle()

'''
for i in data:
    VehicleDetails.objects.create(
        owner=VehicleOwnerDetails.objects.get(id=random.randint(1,20)),
        lpn=i,
        make=data[i]["make"],
        model=data[i]["model"],
        color=data[i]["color"],
        lpn_class=data[i]["class"]
    )

# JSON file
f = open ('<file>.json', "r")

# Reading from file
data = json.loads(f.read())

# Iterating through the json list
for i in data['emp_details']:
	print(i)

# Closing file
f.close()
'''
