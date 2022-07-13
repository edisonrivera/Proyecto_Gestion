from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel

# ? Realizar la conexión con la BD
def conecction():
    # ! Modificar con tus propios datos
    
    server = ""
    database = ""
    username = ""
    password = ""

    global db
    if (QSqlDatabase.contains("qt_sql_default_connection")):
        db = QSqlDatabase.database("qt_sql_default_connection")
    else:
        db = QSqlDatabase.addDatabase("QODBC")
        db.setDatabaseName('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        db.open()

# ? Usado en 'cargar_datos' para mostrar todos los productos actuales
def show_data(sql : str):
    conecction()
    qry = QSqlQuery(db)
    qry.prepare(sql)
    qry.exec()
    model = QSqlQueryModel()
    model.setQuery(qry)
    return model

# ? Usado en 'agregar_producto' para ingresar productos
def request_query(sql_str, args):
    conecction()
    qry2 = QSqlQuery(sql_str,db)
    qry2.prepare(sql_str)
    for arg in args:
        qry2.addBindValue(str(arg))
    return qry2.exec()