from fastapi import FastAPI, HTTPException
import mysql.connector
import schemas
import db

app = FastAPI()

@app.get("/stores")
def get_products():
    mysql_db = mysql.connector.connect(host=db.host_name, port=db.port_number, user=db.user_name, password=db.password_db, database=db.database_name)
    cursor = mysql_db.cursor()
    cursor.execute("SELECT * FROM stores")
    result = cursor.fetchall()
    mysql_db.close()
    cursor.close()
    return {"stores": result}

@app.get("/stores/{id}")
def get_products_by_id(int: id):
    mysql_db = mysql.connector.connect(host=db.host_name, port=db.port_number, user=db.user_name, password=db.password_db, database=db.database_name)
    cursor = mysql_db.cursor()
    cursor.execute(f"SELECT * FROM stores WHERE id = {id}")
    result = cursor.fetchone()
    mysql_db.close()
    cursor.close()

    if result:
        return {"stores": result}
    else:
        raise HTTPException(status_code=404, detail="Store not found")


@app.post("/stores")
def create_products(store:schemas.Store):
    mysql_db = mysql.connector.connect(host=db.host_name, port=db.port_number, user=db.user_name, password=db.password_db, database=db.database_name)
    cursor = mysql_db.cursor()

    cursor.execute("SELECT id FROM stores WHERE id = %s", (store.id,))
    existing_product = cursor.fetchone()
    if existing_product:
        mysql_db.close()
        cursor.close()
        raise HTTPException(status_code=400, detail="ID already exist")


    id : store.id
    name : store.name
    opening_time : store.opening_time
    closing_time : store.closing_time
    address : store.address
    number : store.number
    payment_method : store.payment_method
    image_url : store.image_url

    sql = "INSERT INTO products (id, name, opening_time, closing_time, address, number, payment_method, image_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (id, name, opening_time, closing_time, address, number, payment_method, image_url)
    cursor.execute(sql, val)
    mysql_db.commit()
    mysql_db.close()
    cursor.close()
    return {"message": "Store added successfully"}


@app.put("/stores/{id}")
def change_products(id:int, store:schemas.Store):
    mysql_db = mysql.connector.connect(host=db.host_name, port=db.port_number, user=db.user_name, password=db.password_db, database=db.database_name)
    cursor = mysql_db.cursor()

    name : store.name
    opening_time : store.opening_time
    closing_time : store.closing_time
    address : store.address
    number : store.number
    payment_method : store.payment_method
    image_url : store.image_url

    cursor = mysql_db.cursor()
    sql = "UPDATE stores set name=%s, opening_time=%s, closing_time=%s, address=%s, number=%s, payment_method=%s ,image_url=%s where id=%s"
    val = (id, name, opening_time, closing_time, address, number, payment_method, image_url)
    cursor.execute(sql, val)
    mysql_db.commit()
    mysql_db.close()
    cursor.close()
    return {"message": "Store modified successfully"}

@app.delete("/stores/{id}")
def delete_products(id : int):
    mysql_db = mysql.connector.connect(host=db.host_name, port=db.port_number, user=db.user_name, password=db.password_db, database=db.database_name)
    cursor = mysql_db.cursor()

    cursor.execute("SELECT id FROM stores WHERE id = %s", (id,))
    existing_product = cursor.fetchone()
    if not existing_product:
        mysql_db.close()
        cursor.close()
        raise HTTPException(status_code=404, detail="Store not found")

    cursor.execute(f"DELETE FROM stores WHERE id = {id}")
    mysql_db.commit()
    mysql_db.close()
    cursor.close()
    return {"message": "Store deleted successfully"}
