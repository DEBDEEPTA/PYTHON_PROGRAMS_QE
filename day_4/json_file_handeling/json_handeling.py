student = {
    "name": "Debdeepta",
    "age":  23,
    "skills":["java","python","c#"]
}


# NESTED OBJECT
student_nested = {
        "name": "Dev",
        "age":  23,
        "skills":{
            "java":  9,
            "python": 6,
            "SpringBoot": 8
        },
    }

# ACCESSING DICT <-> JSON OBJECT

print(student["name"])
print(student["age"])
print(student["skills"][2])

# ACCESSING NESTED OBJECT
print(student_nested["name"])
print(student_nested["skills"])
print(student_nested["skills"]["java"]) # 9


import  json

# SAVING STRUCTED DATA (DICT) AS JSON

# with open("sample_data.json", "x") as file_obj: # CREATES A JSON FILE WITH NAME sample_data.json & WRITES THE STUDENT NESTED OBJECT TO IT
#     json.dump(student_nested,file_obj)


# ACESSING A JSON FILE & READING IT
with open("sample_data.json", "r") as reader_obj:
    # LOADING DATA FROM JSON OBJECT
    data = json.load(reader_obj)
    print("Json File Loaded")
    print(data)
    print(data["name"]) #dev
    print(data["skills"]) #  {'java': 9, 'python': 6, 'SpringBoot': 8}
    print(data["skills"]["python"]) # 6

    """"
    note ->
            using read() will only give string representation, & doesn't allows json subscripting
    """

# CONEVIRT JSON FILE --> STRING
with open("sample_data.json","r") as reader_converter:
    data_file = json.load(reader_converter)
    json_string = json.dumps(data_file)
    print("data_file")
    print(type(data_file))    # type dict (now you can perform dict operation(subscripting)
    print("json string")       #            but you can't perform string operations)
    print(json_string)
    print(type(json_string))  # type string (now you can perform string operations
                              #              but cant perform dict operations)
                              # generally used for logging

# CONVERTING JSON STRING BACK TO JSON OBJECT (USE loads())
    json_file = json.loads(json_string)
    print(type(json_file))             # dict (changed from str ---> dict)
    print(json_file["skills"]["java"]) # 9






