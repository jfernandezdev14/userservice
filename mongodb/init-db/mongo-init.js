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
print('END #################################################################');
