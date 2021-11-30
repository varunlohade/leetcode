import json
with open("script.json") as data_files:
    data = json.load(data_files)
    for v in data.values():
        for leng in range(len(v)):
            print("id: ",v[leng]["id"])
            print("Employee_ID: ",v[leng]['Employee_ID'])
            print("Designation: ",v[leng]['Designation'])
            print("Salary: ",v[leng]['Salary'])
            print("Experience: ",v[leng]['experience'])

#this was useless works thou