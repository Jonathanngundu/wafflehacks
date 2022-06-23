import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="food_waste"
)

sql_student = "INSERT INTO student (name, address, phonenumber, city) VALUES (%s, %s, %s, %s)"
sql_resturant = "INSERT INTO resturants (name, address) VALUES (%s, %s)"
sql_foodbanks = "INSERT INTO foodbanks (name, address, city, email) VALUES (%s, %s, %s, %s)"
sql_events = "INSERT INTO events (start, end, foodtype, name, city, location) VALUES (%s, %s, %s, %s, %s, %s)"
#need to make events database I think


foodbank_names = [
    ("Food Kitchen For All", "702 Modale Drive", "Lane, GA", "NJ12jonathan@gmail.com"),
    ("Jacksonville Food Bank", "361 Richison Lane", "Auckland, FN", "NJ12jonathan@gmail.com"),
    ("Fresno Food Kitchen", "2675 Timber Ridge Road", "Perry, ZR", "NJ12jonathan@gmail.com"),
    ("Richardson Pantry", "1410 Spirit Drive", "Capalaba, OH", "NJ12jonathan@gmail.com"),
    ("Harrisburg Food Bank", "3275 Ingram Road", "Centurain, GA", "NJ12jonathan@gmail.com"),
    ("Alcoa Food Bank", "2962 Highland View Drive", "New york city, NY", "NJ12jonathan@gmail.com"),
    ("Port Lavaca Kitchen", "2489 George Avenue", "Atlanta, GA", "NJ12jonathan@gmail.com"),
    ("Port Martin Pantry", "4338 Brannon Lane", "New jersey, OH", "NJ12jonathan@gmail.com"),
    ("Huntington Kitchen", "3419 Virgil Street", "Milane, IL", "NJ12jonathan@gmail.com"),
    ("Fort Rye Kitchen", "3504 Goosetown Avenue", "Seal, SK", "NJ12jonathan@gmail.com")

]

event_names = ("June 5th 2022, 14:00", "June 5th 2022, 16:00", "Vegan", "New York" "Harrison Food Drive", "702 Modale Drive")


mycusor = mydb.cursor()

    

#mycusor.execute(sql_events, event_names)
#mydb.commit()


#sql = "SELECT phonenumber FROM student WHERE city = 'centurion'"
#mycusor.execute(sql)

#myresult = mycusor.fetchall()
#for x in myresult:
    #print(x)


# def add_events(name,start_date, end_date, location, city, food_types):
#     sql = "INSERT INTO events (name,start_date, end_date, location, city, food_types) VALUES (%s, %s, %s, %s, %s)"
#     val = ("{name1}", "{start_date1}", "{end_date1}", "{location1}", "{city1}", "{food_types1}")
#     mycursor.execute(sql, val)
#     mydb.commit()
#     return 1


#mycusor.execute("CREATE TABLE events (start VARCHAR(255), end VARCHAR(255), foodtype VARCHAR(255), name VARCHAR(255), city VARCHAR(255))")



# CREATE TABLE MyUsers ( firstname VARCHAR(30) NOT NULL,  lastname VARCHAR(30) NOT NULL);
# you can ignore this for now. I just created a Fname Lname in "index.html"

# DELETE FROM sql_events [WHERE Clause]
