import sender_stand_request
import data



def positive_assert(name):
    kit_body = sender_stand_request.get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()['name'] == kit_body

def negative_assert(kit_body):
    kit_body_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_body_response.status_code == 400

def negative_assert_no_name(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.code == 400
    assert kit_response.json()["code"] == 400



# Тест 1 Допустимое количество символов (1)
def test_create_kit_2_letter_in_name_get_success_response():
    positive_assert("A")

# Тест 2 Допустимое количество символов (511)
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3 Количество символов меньше допустимого (0)
def test_create_kit_0_letter_in_name_get_success_response():
    negative_assert("")

    # Тест 4 Количество символов больше допустимого (512)
def test_create_kit_512_letter_in_name_get_success_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 5 Разрешены английские буквы
def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")

# Тест 6 Разрешены русские буквы
def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")

# Тест 7 Разрешены спецсимволы
def test_create_kit_simbol_in_name_get_success_response():
    positive_assert('"№%@",')

# Тест 8
def test_create_kit_empty_in_name_get_success_response():
    positive_assert(" Человек и КО ")

# Тест 9 Разрешены цифры
def test_create_kit_figure_in_name_get_success_response():
    positive_assert("123")

# Тест 10 Параметр не передан в запросе
def test_create_kit_not_in_name_get_success_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)

# Тест 11 Передан другой тип параметра (число)
def test_create_kit_int_in_name_get_success_response():
    kit_body = get_kit_body(123)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400
