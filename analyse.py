def classify(area):
    if area > 9:
        return "large"
    else:
        return "small"

with open("wards.csv") as f:
    lines = f.readlines()

total = 0

for line in lines[1:]:
    parts = line.strip().split(",")
    ward = parts[0]
    area_km2 = float(parts[1])
    total = total + area_km2
    size = classify(area_km2)
    print(ward, "is", size)

print("Total area in sq.km:", total)