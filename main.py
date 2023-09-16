def parse_cookie(query: str) -> dict:
    dic = {}
    arr = query.split(";")
    for parameter in arr:
        pair = parameter.split("=", 1)
        if len(pair) == 2:
            if len(pair[0]) > 0 and len(pair[1]) > 0:
                dic[pair[0]] = pair[1]

    return dic


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=User;age;') == {'name': 'Dima=User'}
    assert parse_cookie("name=Dima=User;word='';") == {'name': 'Dima=User', 'word': "''"}
    assert parse_cookie('=;=Buku') == {}
    assert parse_cookie('name=Dima;;age=28;;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie("name=Dima=User;word=") == {'name': 'Dima=User'}
    assert parse_cookie("name=Dima=User;word===;") == {'name': 'Dima=User', 'word': "=="}
