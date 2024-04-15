import mysql.connector as mysql

def connectBD(query, mode):
    try:
        conxBD = mysql.connect(
            user = "your_user",
            password = "your_password",
            host = "localhost",
            database = "your_name_database",
            port = "your_port"
        )
        cursor = conxBD.cursor()
        cursor.execute(query)
        if mode:
            conxBD.commit()
        result = cursor.fetchall()
        return result
    except Exception as e:
        print("Error connecting to database" + str(e))
        
