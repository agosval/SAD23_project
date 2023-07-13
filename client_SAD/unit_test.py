import pytest
from project import app


def test_index():
    response = app.test_client().get('/index.html')
    assert response.status_code == 200
 


def test_stuff():
    response = app.test_client().get('/_stuff')
    lista = response.data.decode('utf-8').split(sep='],', maxsplit=-1)
    num_type_mes = len(lista)
    assert num_type_mes == 3


def test_stuff2():
    response = app.test_client().get('/_stuff2')
    lista = response.data.decode('utf-8').split(sep='},', maxsplit=-1)
    search_string = lista[0]
    all_words=['gpsFix','height','iTOW','lat','lon']
    found = True
    for word in all_words:
        if not word in search_string.split('"'):
            found = False  
    assert found

def test_stuff3():
    response = app.test_client().get('/_stuff3')
    lista = response.data.decode('utf-8').split(sep='},', maxsplit=-1)
    search_string = lista[0]
    all_words=['iTOW','lat','lon']
    found = True
    for word in all_words:
        if not word in search_string.split('"'):
            found = False  
    assert found