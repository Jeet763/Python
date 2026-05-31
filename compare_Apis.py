api1 = [
    {"id":1,"name":"A"},
    {"id":2,"name":"B"}
]

api2 = [
    {"id":1,"name":"A"},
    {"id":2,"name":"C"}
]

api1_dict = {}
for record in api1:
    api1_dict[record['id']] = record

# api1_dict = {record["id"]: record for record in api1} ->(Dict comprehension)
# Trying to make it like - 
# {
#     1: {"id":1,"name":"A"},
#     2: {"id":2,"name":"B"}
# }

api2_dict = {}
for record in api2:
    api2_dict[record['id']] = record

changed_records = []
missing_Records = []

for id, record in api1_dict.items():

    if id not in api2_dict:
        missing_Records.append(record)

    elif record['name'] != api2_dict[id]['name']:

        changed_records.append({
            'id': id,
            'old_name': record['name'],
            'new_name': api2_dict[id]['name']
        })

print('changed:' , changed_records)
print('missing:' , missing_Records)
