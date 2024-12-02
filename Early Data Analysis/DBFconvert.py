
import csv
from dbfread import DBF


dbf_file = '../Data/wa_lrg_fires.dbf'
csv_file = '../Data/wa_lrg_fire.csv'  # Output CSV file

# Read the DBF file
table = DBF(dbf_file)

# Convert to CSV
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write header (field names)
    writer.writerow(table.field_names)
    
    # Write rows
    for record in table:
        writer.writerow(list(record.values()))

print(f"Converted {dbf_file} to {csv_file}")