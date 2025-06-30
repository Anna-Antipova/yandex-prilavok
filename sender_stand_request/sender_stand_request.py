
import requests
from configuration import BASE_URL
from configuration import CREATE_USER_URL

def post_new_user():
    user_body = {
        "firstName": "Анатолий",
        "phone": "+79995553322",
        "address": "г. Москва, ул. Пушкина, д. 10"
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(CREATE_USER_URL, json=user_body, headers=headers)
    response.raise_for_status()

    return response.json()["authToken"]

def post_new_client_kit(kit_body, auth_token=None):
    headers = {"Content-Type": "application/json"}
    if auth_token:
        headers["Authorization"] = f"Bearer {auth_token}"
    return requests.post(BASE_URL, json=kit_body, headers=headers)

def get_new_user_token():
    return post_new_user()
