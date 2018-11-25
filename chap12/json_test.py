import json
from atmmanager import User

with open("atmusers.json") as f:
        data = json.load(f)

users = {}

for key, value in data['users'].items():
        print(value["userid"], value["pin"])
        user = User(value["userid"], value["pin"],value["checking"],value["savings"], value["name"])
        users['users'] = value['userid']
        users['users']
        print(users)

# data = {}
# data['users'] = {}
# for user in users:
#     json_str = (vars(user))
#     del json_str["user"]
#     userid = user.getID()
#     data['users'][userid] = json_str

# with open('new_atmusers.json', 'w') as f:
#     json.dump(data, f, indent=4)
        
