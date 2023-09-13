def parse(query: str) -> dict:
    dic = {}
    print(query)
    arr = query.split("?")
    if len(arr)==2:
        query = arr[1]
        print(query)
        arr = query.split("&")
        for par in arr:
            pair = par.split("=")
            print(pair)
            if len(pair)==2:
                if len(pair[0])>0 and len(pair[1])>0:
                    dic[pair[0]]=pair[1]
                    print(dic)
    return dic


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('http://example.com/?name=') == {}
    assert parse('http://example.com/?name') == {}
    assert parse('http://example.com/?=Dima') == {}
    assert parse('http://example.com/?name==Dima') == {}
    assert parse('http://example.com/?name=Dima=Masha') == {}
    assert parse('http://example.com/?name=Dima&name=Masha') == {'name': 'Masha'}
    assert parse('http://example.com/?name=Dima&fuga=Dima') == {'name': 'Dima', 'fuga': 'Dima'}
