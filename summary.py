import csv
def read_rows(filename):
    with open(filename, encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))
def clean_values(rows, column):
    values = []
    non_numeric_count = 0
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        try:
            values.append(float(raw))
        except ValueError:
            non_numeric_count += 1
            continue
    if non_numeric_count > 0:
        print(f"There are {non_numeric_count} non-numeric values in the column '{column}'.")
    return values
def summarize(values):
    if len(values) == 0:
        return {"count": 0, "smallest": None, "largest": None, "average": None}
    return {
        "count": len(values),
        "smallest": min(values),
        "largest": max(values),
        "average": sum(values) / len(values), }
def summarize_all(filename, columns):
    rows = read_rows(filename)
    report = {}
    for column in columns:
        values = clean_values(rows, column)
        report[column] = summarize(values)
    return report

report = summarize_all('Shebelle_waterpoints.csv', ["SWL_elv", "TDS", "Transmissi", "SWL(m)"])
for column, stats in report.items():
    print(f"Summary for {column}:", stats)

with open('summary_report.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['Column', 'Count', 'Smallest', 'Largest', 'Average'])
    for column, stats in report.items():
        writer.writerow([column, stats['count'], stats['smallest'], stats['largest'], stats['average']])