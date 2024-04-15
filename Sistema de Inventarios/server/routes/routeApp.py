import json
from data.bd import connectBD

def routeApp(data, Hmode, Htype):
    query = ""
    Id = data['id']
    Nombre = data['nombre']
    Precio = data['precio']
    Stock = data['stock']
    Categoria = data['categoria']
    Marca = data['marca']
    Descuento = data['descuento']
    result = []
    if type(Id) == int and type(Nombre) == str and type(Precio) == float and type(Stock) == int and type(Categoria) == str and type(Marca) == str and type(Descuento) == int:
        if Htype == "insert" and Hmode == "unique":
            query = "INSERT IGNORE INTO producto (id, nombre, precio, stock, categoria, marca, descuento) VALUES (" + str(Id) + ", '" + Nombre + "', " + str(Precio) + ", " + str(Stock) + ", '" + Categoria + "', '" + Marca + "', " + str(Descuento) + ")"
            connectBD(query, True)
            status = "200 OK"
            sendMsg = "Producto Agregado"
        elif Htype == "update" and Hmode == "unique":
            query = "UPDATE producto SET nombre = '" + Nombre + "', precio = " + str(Precio) + ", stock = " + str(Stock) + ", categoria = '" + Categoria + "', marca = '" + Marca + "', descuento = " + str(Descuento) + " WHERE id = " + str(Id) 
            connectBD(query, True)
            status = "200 OK"
            sendMsg = "Producto Actualizado"
        elif Htype == "delete" and Hmode == "unique":
            query = "DELETE FROM producto WHERE id = " + str(Id)
            connectBD(query, True)
            status = "200 OK"
            sendMsg = "Producto Eliminado"
        elif Htype == "read" and Hmode == "unique":
            query = "SELECT * FROM producto WHERE id = " + str(Id)
            result = connectBD(query, False)
        elif Htype == "read" and Hmode == "all":
            query = "SELECT * FROM producto"
            result = connectBD(query, False)
        else:
            status = "400 Bad Request"
            sendMsg = "Error en la request"
        
        if Htype == "read" and (Hmode == "unique" or Hmode == "all"):
            if result != []:
                status = "200 OK"
                sendMsg = ""
            else:
                status = "400 Bad Request"
                sendMsg = "No se encontro el producto"
    else:
        status = "400 Bad Request"
        sendMsg = "Tipo de datos incorrectos"
    jsonRes = {
        "head": {
            "status": status,
            "msg": sendMsg,
        },
        "data": result
    }
    jsonData = json.dumps(jsonRes)
    jsonResult = jsonData.encode("utf-8")
    return jsonResult
    