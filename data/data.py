
kit_body = {
    "name": "Мария"
}

def get_kit_body(name):
    from copy import copy
    body = copy(kit_body)
    body["name"] = name
    return body

user_body = {
        "firstName": "Анатолий",
        "phone": "+79995553322",
        "address": "г. Москва, ул. Пушкина, д. 10"
    }
