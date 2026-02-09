import requests as req

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiQ1MwMzMiLCJ1c2VyX25hbWUiOiJERUJERUVQVEEgU0FNVUkiLCJyb2xlIjoic3R1ZGVudCIsImV4cCI6MTc3MDQ3Mjg0NX0.m7XsvP4BemNLMVvKwAasDrIGcdg_V6MDlmIoaZwbmow"
T_ID = "TKT-57AA45529C"

def login(l_url):
    payload = {
            "email": "askdev2003@gmail.com",
            "password": "Dev2oo3"
        }

    response = req.post(url=l_url,json=payload)

    print(response.status_code)

    print(response.json()['token'])

def c_ticket_gen(url):

    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    payload = {
            "title": "D1",
            "desc": "D2"
        }

    response =  req.post(url=url, json=payload, headers= headers)
    print(response.status_code)

    print(response.json()['ticket'])


def get_tick_by_id(url,id):
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    final_url = f"{url}{id}"
    test = "http://127.0.0.1:8000/tickets/TKT-57AA45529C"
    response = req.get(url=final_url,headers=headers)
    print(response.status_code)
    print(response.json())


if __name__=="__main__":
    login_url = "http://127.0.0.1:8000/login/"
    c_ticket_url = "http://127.0.0.1:8000/tickets/create"
    t_id_url = "http://127.0.0.1:8000/tickets/"

    #login(login_url)

    #c_ticket_gen(c_ticket_url)

    get_tick_by_id(t_id_url,T_ID)