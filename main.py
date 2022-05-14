import mysql.connector
from mysql.connector import (connection)

db = connection.MySQLConnection(user='sql11491613', password='eWFcPv5Ndt',
                                 host='35.157.16.43',
                                 database='sql11491613')

mycursor = db.cursor()
db_name= "sql11491613"


users=mycursor.execute("SHOW columns FROM users;")
for x in mycursor:
    print(*x)

users=mycursor.execute("SELECT * FROM users;")
for x in mycursor:
    print(x)



#----------------------------------------------
#admin functies

def voeg_user_toe():
    str_a=""
    print("geef de RoleID van de nieuwe user:")
    print("1:geregistreerde gebruiker")
    print("2:admin")
    print("3:muzikant")
    nu_roleID=input()
    nu_lastName=input("geef de achternaam van de nieuwe user:")
    nu_firstName=input("geef de voornaam van de nieuwe user:")
    nu_mail=input("geef email adres in:")
    nu_password=input("geef paswoord van de nieuwe user:")
    nu_stageName=input("geef de artiestennaam van de nieuwe user:")
    str_a=str("INSERT INTO `sql11491613`.`users` (roleID, lastName, firstName, emailAddress, password, stageName)  VALUES  ('"+nu_roleID+"','"+nu_lastName+"','"+nu_firstName+"','"+nu_mail+"','"+nu_password+"','"+nu_stageName+"'); ")
    mycursor.execute(str_a)
    db.commit()

def alter_user():
    pass

def wis_user():
    pass

def alter_permissions():
    pass

def make_project():


#user functies-----------------------------------------------------------------
#steps:

#register=maak user
#maak project
#maak sessie
#maak setup
#kies gearunit
#write controls
#read controls
#

def make_project():
    np_name=input("geef naam nieuw project in:")



def make_session():

def make_chain():


def run_write_controls():
    #-kies project
	#-kies sessie
    #-haal lijst gearunits op
    #-kies gearunit
	#-haal controls gearunit op
	#-vul values voor controls van gearunit in

def run_read_controls():







db.close()
