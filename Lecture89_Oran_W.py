import json
def readJson():
    # some JSON:
    x =  '{ "name":"John", "age":30, "city":"New York"}'

    # parse x:
    y = json.loads(x)

    # the result is a Python dictionary:
    print(y["age"])

def WriteJsons(): 
    #json as a stirng in python
    # a Python object (dict):
    x = {
    "name": "John",
    "age": 30,
    "city": "New York"
    }

    # convert into JSON:
    y = json.dumps(x)

    # the result is a JSON string:
    print(y)

def WriteJson(): 
    #json as a stirng in python
    # a Python object (dict):
    x = {
    "name": "John",
    "age": 30,
    "city": "New York"
    }

    with open ("test.json","w") as json_file:
        json.dump(x,json_file)  # เขียน Dirt(x) ลงในไฟล์ test.json

    # the result is a JSON string:
    print(type(x))

WriteJson()