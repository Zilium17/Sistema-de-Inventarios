import mysql.connector as mysql

def connectBD(query, mode):
    try:
        conxBD = mysql.connect(
            user = "root",
            password = "Berylm762",
            host = "localhost",
            database = "inventario",
            port = "3306"
        )
        cursor = conxBD.cursor()
        cursor.execute(query)
        if mode:
            conxBD.commit()
        result = cursor.fetchall()
        return result
    except Exception as e:
        print("Error connecting to database" + str(e))
        