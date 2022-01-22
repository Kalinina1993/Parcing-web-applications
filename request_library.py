# Используя сервис https://fakerestapi.azurewebsites.net и requests библиотеку, написать запросы:
# GET: получение списка авторов, получение конкретного автора по его id
# POST: добавить новую книгу, добавить нового пользователя
# PUT: обновить данные для книги под номером 10
# DELETE: удалить пользователя под номером 4

import requests


def get_request():
    """Get authors list"""
    response_1 = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Authors")
    print("List of authors: ", response_1.text)
    print(response_1.url)

    """Get author with id 69"""
    response_2 = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Authors/69")
    print("Information about author with id 69: ", response_2.text)
    print(response_2.url)


def post_request():
    """Add new book"""
    response_1 = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Books", json={
        "id": 666,
        "title": "Book 666",
        "description": "Devil is come back",
        "pageCount": 999,
        "excerpt": "Boo",
        "publishDate": "2022-01-02T17:20:51.352Z"
    })
    print(response_1.text)

    """Add new User"""
    response_2 = requests.post("https://fakerestapi.azurewebsites.net//api/v1/Users", json={
        "id": 11,
        "userName": "Tom Raddle",
        "password": "Avadacedavra"
    })
    print(response_2.text)


def put_request():
    """Update datas for book 10"""
    r = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Books/10", data={"title": "Book 12"})
    print(r.status_code)


def delete_request():
    """Delete user 4"""
    d = requests.delete("https://fakerestapi.azurewebsites.net//api/v1/Users/4")
    print(d.status_code)


print(get_request())
print()
print(post_request())
print()
print(put_request())
print()
print(delete_request())
