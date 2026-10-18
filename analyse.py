with open('wards.csv') as f:
    lines = f.readlines()

for line in lines[1:]:  # Skip the header line
    parts = line.strip().split(',')
    ward = parts[0]
    area_km2 = float(parts[1])  # Convert area to float
    hectares = area_km2 * 100
    print(ward, "is", hectares, "hectares")

for line in lines[1:]:  # Skip the header line
    parts = line.strip().split(',')
    ward = parts[0]
    area_km2 = float(parts[1])  # Convert area to float
    if area_km2 > 10:
        size = "large"
    elif area_km2 < 10:
        size = "small"
    else:
        size = "medium"
    print(ward, "is", size) 