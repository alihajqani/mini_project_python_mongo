def serializeDict(item) -> dict:
    return{
        'id':str(item['_id']),
        'name': item['name'],
        'email': item['email'],
        'password':item['password']
    }

def serializeList(entity) -> list:
    return [serializeDict(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'}, **{i:str(a[i]) for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return[serializeDict(a) for a in entity]