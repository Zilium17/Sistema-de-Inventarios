import json
from data.bd import connectBD

def routeLogin(data):
    User = data["user"]
    Password = data["password"]
    
    query = "SELECT name FROM usuario WHERE user = '" + User + "' AND password = '" + Password + "'"
    result = connectBD(query, False)
    
    if len(result) == 0:
        msg = "Usuario o Contraseña Incorrecta"
        status = "403 No authorization"
    else:
        msg = "Iniciando sesion..."
        status = "200 Authorization"
    
    jsonRes = {
        "Head": {
            "status": status,
            "msg": msg,
            "name": result,
        }
    }
    jsonRes = json.dumps(jsonRes)
    return jsonRes.encode("utf-8")