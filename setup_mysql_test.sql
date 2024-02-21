-- a script that prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
"""Good comment"""
"""New Good commit"""
# Badass commit
Love = ["shit", "Date", "shit2","time waste", "masterbation"]
for element in Love:
    print("shit")

i = 0
Life = ["ah", "eh", "oh"]
while Life[i] != "oh":
    Love[i] = "S*x"
    i += 1
