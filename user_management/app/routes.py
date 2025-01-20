from flask import Blueprint, jsonify, request
from app.database import get_db_connection

routes = Blueprint('routes', __name__)

@routes.route('/user_list', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data")
    users = cursor.fetchall()
    conn.close()

    user_list = [{
        "id": row["user_id"],
        "name": row["full_name"],
        "email": row["contact_email"],
        "address": {
            "street": row["street_address"],
            "suite": row["apt_number"],
            "city": row["town"],
            "zipcode": row["postal_code"]
        },
        "phone": row["phone_number"],
        "company": row["employer"]
    } for row in users]

    return jsonify(user_list)

@routes.route('/find_user', methods=['GET'])
def search_user():
    query = "SELECT * FROM user_data WHERE 1=1"
    values = []

    filters = {
        "name": "full_name",
        "email": "contact_email",
        "street": "street_address",
        "phone": "phone_number",
        "zip": "postal_code",
        "company": "employer"
    }

    for param, column in filters.items():
        if param in request.args:
            query += f" AND {column} LIKE ?"
            values.append(f"%{request.args[param]}%")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    results = cursor.fetchall()
    conn.close()

    user_results = [{
        "id": row["user_id"],
        "name": row["full_name"],
        "email": row["contact_email"],
        "address": {
            "street": row["street_address"],
            "suite": row["apt_number"],
            "city": row["town"],
            "zipcode": row["postal_code"]
        },
        "phone": row["phone_number"],
        "company": row["employer"]
    } for row in results]

    return jsonify(user_results)