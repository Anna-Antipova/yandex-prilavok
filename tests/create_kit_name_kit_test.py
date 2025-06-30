
import pytest
from data.data import get_kit_body
from sender_stand_request.sender_stand_request import post_new_client_kit, get_new_user_token

token = get_new_user_token()

def positive_assert(kit_body):
    response = post_new_client_kit(kit_body, token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    response = post_new_client_kit(kit_body, token)
    assert response.status_code == 400

def test_create_kit_name_1_symbol():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)

def test_create_kit_name_511_symbols():
    kit_body = get_kit_body("x" * 511)
    positive_assert(kit_body)

def test_create_kit_name_0_symbols():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

def test_create_kit_name_512_symbols():
    kit_body = get_kit_body("x" * 512)
    negative_assert_code_400(kit_body)

def test_create_kit_name_english():
    kit_body = get_kit_body("QWErty")
    positive_assert(kit_body)

def test_create_kit_name_russian():
    kit_body = get_kit_body("Мария")
    positive_assert(kit_body)

def test_create_kit_name_special_chars():
    kit_body = get_kit_body("№%@\",")
    positive_assert(kit_body)

def test_create_kit_name_with_spaces():
    kit_body = get_kit_body(" Человек и КО ")
    positive_assert(kit_body)

def test_create_kit_name_with_numbers():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

def test_create_kit_without_name():
    kit_body = {}
    negative_assert_code_400(kit_body)

def test_create_kit_name_as_number():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)
