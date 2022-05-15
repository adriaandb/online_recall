import mysql.connector
from mysql.connector import (connection)

db = connection.MySQLConnection(user='sql11491613', password='eWFcPv5Ndt',
                                host='35.157.16.43',
                                database='sql11491613')

mycursor = db.cursor()
db_name = "sql11491613"

users = mycursor.execute("SHOW columns FROM users;")
for x in mycursor:
    print(*x)

users = mycursor.execute("SELECT * FROM users;")
for x in mycursor:
    print(x)


# ----------------------------------------------
# admin functies

def voeg_user_toe():
    str_a = ""
    print("geef de RoleID van de nieuwe user:")
    print("1:geregistreerde gebruiker")
    print("2:admin")
    print("3:muzikant")
    nu_roleID = input()
    nu_lastName = input("geef de achternaam van de nieuwe user:")
    nu_firstName = input("geef de voornaam van de nieuwe user:")
    nu_mail = input("geef email adres in:")
    nu_password = input("geef paswoord van de nieuwe user:")
    nu_stageName = input("geef de artiestennaam van de nieuwe user:")
    str_a = str(
        "INSERT INTO `sql11491613`.`users` (roleID, lastName, firstName, emailAddress, password, stageName)  VALUES  ('" + nu_roleID + "','" + nu_lastName + "','" + nu_firstName + "','" + nu_mail + "','" + nu_password + "','" + nu_stageName + "'); ")
    mycursor.execute(str_a)
    db.commit()


def alter_user():
    print("alter user:")
    print("all users:")
    mycursor.execute("SELECT * FROM users;")
    for x in mycursor:
        print(*x)
    au_userID = input("geef ID van de aan te passen user:")
    antw = ""
    while not antw == "y":
        print("ben je zeker dat je de volgende user wilt aanpassen:")
        mycursor.execute("SELECT * FROM users WHERE userID=" + au_userID + ";")
        for x in mycursor:
            print(x)
        antw = input("y/n")
        if not antw == "y":
            au_userID = input("geef ID van te wissen user:")

    str_aa = ""
    print("geef de RoleID van de aan te passen user:")
    print("1:geregistreerde gebruiker")
    print("2:admin")
    print("3:muzikant")
    au_roleID = input()
    au_lastName = input("geef de achternaam van de aan te passen user:")
    au_firstName = input("geef de voornaam van de aan te passen user:")
    au_mail = input("geef email adres in:")
    au_password = input("geef paswoord van de aan te passen user:")
    au_stageName = input("geef de artiestennaam van de aan te passen user:")
    str_aa = str(
        "UPDATE `sql11491613`.`users` SET `roleID` = '" + au_roleID + "', `lastName` = '" + au_lastName + "', `firstName` = '" + au_firstName + "', \
    `emailAddress` = '" + au_mail + "', `password` = '" + au_password + "', `stageName` = '" + au_stageName + "' WHERE (`userID` = '" + au_userID + "'); ")
    mycursor.execute(str_aa)
    db.commit()
    print("user aangepast")


def wis_user():
    print("delete user:")
    print("all users:")
    mycursor.execute("SELECT * FROM users;")
    for x in mycursor:
        print(x[0], "", x[3], "", x[2])
    userID = input("geef ID van te wissen user:")
    antw = ""
    while not antw == "y":
        print("ben je zeker dat je de volgende user wilt wissen:")
        mycursor.execute("SELECT * FROM users WHERE userID=" + userID + ";")
        for x in mycursor:
            print(x)
        antw = input("y/n")
        if not antw == "y":
            userID = input("geef ID van te wissen user:")
    str_b = str("DELETE FROM `sql11491613`.`users`WHERE(`userID` = '" + userID + "');")
    mycursor.execute(str_b)
    db.commit()
    print("user met user ID '" + userID + "' is gewist")


def alter_permissions():
    print("permissies:")
    mycursor.execute("SELECT * FROM sql11491613.roles;")
    for x in mycursor:
        print(*x)
    print("users:")
    mycursor.execute("SELECT * FROM users;")
    for x in mycursor:
        print(x[0], "", x[3], "", x[2], " RoleID=", x[1])
    ap_roleID = input("geef role ID in:")
    ap_userID = input("geef ID van user:")
    antw = ""
    while not antw == "y":
        print("ben je zeker dat je de volgende user de permissie wilt veranderen?:")
        mycursor.execute("SELECT * FROM users WHERE userID=" + ap_userID + ";")
        for x in mycursor:
            print(x)
        antw = input("y/n")
        if not antw == "y":
            ap_userID = input("geef ID van te wissen user:")
    str_c = str(
        "UPDATE `sql11491613`.`users` SET `roleID` = '" + ap_roleID + "' WHERE (`userID` = '" + ap_userID + "');")
    mycursor.execute(str_c)
    db.commit()


# user functies-----------------------------------------------------------------
# steps:

# register=maak user
# maak project
# maak sessie
# maak setup
# kies gearunit
# write controls
# read controls
#

def make_project():
    np_name = input("geef naam nieuw project in:")


def make_session():
    pass


def make_chain():
    pass


def run_write_controls():
    # -kies project
    # -kies sessie
    # -haal lijst gearunits op
    # -kies gearunit
    # -haal controls gearunit op
    # -vul values voor controls van gearunit in
    pass


def run_read_controls():
    pass


alter_user()

db.close()
