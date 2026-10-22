import csv
with open('Shebelle_waterpoints.csv', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    print("Number of rows:", len(rows))
    print("columns:", list(rows[0].keys()))
print('#################################################')
import csv
with open('Shebelle_waterpoints.csv', encoding='utf-8-sig') as f:
    rows = list(csv.DictReader(f))

values = []
for row in rows:
    raw = row["SWL_elv"].strip()
    if raw == "":
        continue
    values.append(float(raw))
print("Smallest:", min(values))
print("Largest:", max(values))
print("Average:", sum(values) / len(values))
print("Count:", len(values))

import csv
def inspect_column(filename, column):
    with open(filename, encoding='utf-8-sig') as f: 
        rows = list(csv.DictReader(f))
    values = []
    non_numeric_count = 0
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        try:
            values.append(float(raw))
        except ValueError:
            non_numeric_count=non_numeric_count + 1
            continue
    if len(values) == 0:
        return "Thre are no values in the column."
    else:
        if non_numeric_count > 0:
            print(f"There are {non_numeric_count} non-numeric values in the column '{column}'.")
            return {
        "smallest" : min(values) ,
        "largest": max(values) ,
        "average": sum(values) / len(values) ,
        "count": len(values)}
        else:
            return { "smallest" : min(values) ,
        "largest": max(values) ,
        "average": sum(values) / len(values) ,
        "count": len(values)}
SWL_result = inspect_column('Shebelle_waterpoints.csv', 'SWL_elv')
TDS_result = inspect_column('Shebelle_waterpoints.csv', 'TDS')
Transmissivity_result = inspect_column('Shebelle_waterpoints.csv', 'Transmissi')
SWL_mbgl_result = inspect_column('Shebelle_waterpoints.csv', 'SWL(m)')
print("SWL masl.:",SWL_result)
print("TDS mg/L.:",TDS_result)
print("Transmissivity:",Transmissivity_result)
print("SWL(m).:",SWL_mbgl_result)