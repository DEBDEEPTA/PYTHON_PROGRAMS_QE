import re
def validate_email(email_id:str):
    email_pattern = r"^[a-zA-Z0-9]{1}+[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})+$"
    compiled_pattern = re.compile(email_pattern)

    if(re.match(compiled_pattern,email_id)):
        return True

    return False

def validate_phone(phone_num:int):
    phone_pattern = r"^[6-9]{1}+[0-9]{9}$"   # + is redundant after a reputation range ends
    # or r"^[6-9]{1}/d{9}$"

    compiled_pattern = re.compile(phone_pattern)

    if(re.match(compiled_pattern,str(phone_num))):
        return True
    return False

if __name__ == "__main__":
    print(validate_email("deep.o8.2oo3.26@gmail.com"))
    print(validate_phone(1003496011))