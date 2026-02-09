import requests as req
import json

def get_url(url):

    """
        python  <----------equivalent-->   springBoot
        requests.get(url) <-------> @GetMapping(url)
    """
    response = req.get(url) # stores the response from the url
    """
        response includes -> header
                          -> status code
                          -> payload  
    """
    header_data = response.headers # returns header data as dictionary
    print(header_data)             # CaseInsensitiveDict
    print("--------------------------")

    """
     (note) -> response.headers returns a  CaseInsensitiveDict 
            -> NormalDict + (Key can be case Insensitive)
    below, e.g 
    """
    print(header_data["Content-Type"])     #
    print(header_data["content-type"])     # # -> All three are considered as same key
    print(header_data["contEnt-type"])     #
    #print(header_data["cont-type"])        # -> throws (except) keyError if key Doesn't Exists
    print(header_data.get("cont-type","key_not_found"))  # Handling key Not Found
    """
        Best Practise to Avoid key Error
            -> give default value if key is not present
            -> syntax  header_data.get("key_name", "key_not_found/default_value") 
    """
    print("--------------------------")
    print(type(header_data))       # <class 'requests.structures.CaseInsensitiveDict'>

    """
        Converting CaseInsensitiveDict type to Json
            approcah ->
            Dict -> jsonString
            jsonString -> json
    """
    # Dict to JSON String
    print("-----------------Conversion from Dict (Json-Obj) to jsonString----------------------")
    """
        note -> header data is of Type CaseInsensitiveDict which doesn't support json conversion
             -> type cast header data to dict first pass it as parameter to the dumps() method
                eg., below
    """
    header_json_string_data =  json.dumps(dict(header_data))
    print(header_json_string_data)
    print(type(header_json_string_data))

    print("-----------------Conversion from jsonString to Dict (Json-Obj)----------------------")
    # JsonString To Dict ( -> JSON Object)
    json_dict_obj = json.loads(header_json_string_data)
    print(json_dict_obj)
    print(type(json_dict_obj))


def sending_custom_header_to_server(url):
    """
        we can define custom headers to send meta data to the server
        They do not send the main data, but they control, describe, and secure the request.
        GENERALLY CONSISTS INFORMATION SUCH AS ->
            -> Who is sending the request
            -> What format the client expects
            ->  Whether the request is authenticated
            ->  How to interpret the body
            ->  Whether the request can be cached
            ->  Whether compression is supported

        USED IN ->  (Without this will cause 401(Unauthorized) satus code)
                -> JWT
                -> OAuth
                -> API Keys
        APPROACH ->
                -> define a dict with the re
    """
    headers = {
        "Authorization": "Bearer abc123",
        "Accept": "application/json",
        "custom_meta_test": "demo_test_key_12345"
    }

    """
        🔹 Are only these headers sent?
        ❌ No
        🔹 What is sent?
            ✔ Your custom headers
            ✔ PLUS default headers automatically added by requests

        🧠 Important Concept: requests MERGES headers
           1. requests does not replace headers — it adds/overrides them.
           2. Default headers added by requests
           3. Even if you don’t specify any headers, requests sends:

          

    """

    response = req.get(url, headers=headers) # CUSTOM/REQUEST HEADER SEND
    print(response.request.headers)  # PRINTING ALL CUSTOM/REQUEST HEADERS  -> Your headers dict + Requests default headers
    print(response.headers) # PRINTING ALL RESPONSE HEADERS


    """Printing/Acessing Specific key:value from header
       syntax ->  response.request.headers.get("key name") 
    """

    val = response.request.headers.get("custom_meta_test") # Case Insensitive Dict
    print(val) # Doesn't throw key error, if doesn't match it returns None

def get_status_code(url):
    response = req.get(url)
    status_code = response.status_code
    print(status_code)
    print(type(response))

    print(response.reason)

def main():
    get_faker_rest_api_url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

    #get_url(get_faker_rest_api_url)
    get_status_code(get_faker_rest_api_url)
    sending_custom_header_to_server(get_faker_rest_api_url)


if __name__=="__main__":
    main()