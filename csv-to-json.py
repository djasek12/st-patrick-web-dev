import csv, json, re
fileName = 'C:\\Users\\dj125\\Downloads\\st-patrick-ministry-responses - Sheet1.tsv'

with open(fileName, encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter="\t")
    data = list(reader)

json_data = json.dumps(data)
print(json_data)

emailRegex = r'([\w\.-]+)@([\w\.-]+)\.([\w\.-]+)'
encodedEmailRegex = r'\1%\2!\3'
json_data = re.sub(emailRegex, encodedEmailRegex, json_data)

with open('organizationInfo.js', 'w') as outfile:
    outfile.write("var data=")
    json.dump(json_data, outfile)