state = 'Oayo'
print(state)
state = 'Legos'
print(state)
print(5+5)
print('5'+'5')
wards = ['Ward 1', 'Ward 2', 'Ward 3']
print(wards)
wards.append('Ward 4')
print(wards)
wards.remove('Ward 2')
print(wards)
wards.insert(1, 'Ward 2')
print(wards)
wards.sort()
print(wards)
wards.reverse()
print(wards)
wards.pop()
print(wards)
print(len(wards))
print(wards[0])
print(wards[-1])
print(wards[1:3])
print(wards[:2])
print(wards[2])
for ward in wards:
    print('Checking',ward)
areas = [100, 200, 300]
for area in areas:
    hactars = area * 100
    print('Area in square killometers:', area)
    print('Area in hactars:', hactars)
area = 25869
if area > 20000:
    print('it is a larege area')
else:
    print('it is a small area')
aras = [12345, 21230, 25312]
for area in aras:
    if area > 20000:
        print('it is a larege area')
    else:
        print('it is a small area')
def km2_to_hectares(area):
    return area * 100
print(km2_to_hectares(25869))

def with_print(x):
    print(x*100)
def with_return(x):
    return x*100

a = with_print(5)
b = with_return(5)

print('a is', a)
print('b is', b)

import csv

with open('wards.csv', encoding='utf-8-sig') as f:
    reader =csv.DictReader(f)
    for row in reader:
        print(row['ward'], row['area_km2'])

print('-------------------')
ward ={"name": "Bodija", "area":8.1, "lga": "Ibadan North"}
print(ward["name"])
print(ward["area"])

with open("wards.csv", encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print("about_to_process", row)
        area = float(row["area_km2"])
        print("area is:", area)

print ('#####################')

with open("wards.csv", encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        raw = row["area_km2"].strip()
        if raw == "":
            continue
        area = float(raw)
        print("area is:", area)