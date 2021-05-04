print('Start #################################################################');
db = db.getSiblingDB('userservice');
db.createUser(
        {
            user: "api_user",
            pwd: "api_pwd",
            roles: [
                {
                    role: "readWrite",
                    db: "userservice"
                }
            ]
        }
);
db.createCollection('users', { capped : true, size : 5242880, max : 5000 } );
db.users.insert({"user_id": "105398891", "pin": 2090})
db.users.insert({"user_id": "105398892", "pin": 2091})
db.users.insert({"user_id": "105398893", "pin": 2092})
print('END #################################################################');
