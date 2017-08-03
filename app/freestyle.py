import pandas as pd
excel_file = pd.read_excel(r'C:\Users\Paloma\Desktop\jobs.xlsx')

# adapted with help from Professor Rossetti

chosen_skill = input("Please input one main skill you have: ")

results = excel_file[excel_file['Skills'].str.contains(chosen_skill)]

for index, row in results.iterrows():
    print("                  ")
    print("MATCHING POSITION:")
    print("   Position:", row["Position"])
    print("   Company:", row["Company"])
    print("   Location:", row["Location"])
    print("   Level:", row["Level"])
    print("   Status:", row["Status"])
    print("   Description:", row["Description"])

#print(type(rows))
#print("Position:")
#for jobs in rows.Position.tolist():
    #print(jobs)
#print("Company:")
#for Firm in rows.Company.tolist():
    #print(Firm)
#print("Location;")
#for Place in rows.Location.tolist():
    #print(Place)
#print("Level:")
#for Tenure in rows.Level.tolist():
    #print(Tenure)
#print("Status:")
#for Time in rows.Status.tolist():
    #print(Time)
#print("Description:")
#for Role in rows.Description.tolist():
    #print(Role)

for row in rows:
    print(type(row))
    print(row)
