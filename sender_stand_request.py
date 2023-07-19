import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())


def new_token():
    response = post_new_user(data.user_body)
    dict = response.json()  #
    auth_token = dict['authToken']
    current_headers_create_kit = data.headers.copy()
    current_headers_create_kit["Authorization"] = "Bearer " + auth_token
    return current_headers_create_kit


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def post_new_client_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=get_kit_body(kit_body),
                         headers=new_token())