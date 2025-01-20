import requests
from app.database import create_user_table, insert_users
from app.config import API_URL

def import_users():
    response = requests.get(API_URL)
    if response.status_code == 200:
        users = response.json()
        create_user_table()
        insert_users(users)
        print("User data imported successfully.")
    else:
        print("User data failed to import.")

if __name__ == "__main__":
    import_users()