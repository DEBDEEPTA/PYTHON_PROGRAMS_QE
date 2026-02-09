import requests as req
from urllib.parse import urlparse, parse_qs
"""
    requests.get(url, params={...})
    requests.post(url, params={...})
    requests.put(url, params={...})
    requests.delete(url, params={...})
    
    Note -> obtaining (reading / extracting) query parameters is the SAME for all HTTP request types
            (GET, POST, PUT, PATCH, DELETE, etc.).

"""

def send_params(url):
    params = {
        "name": "Dev",
        "age": 23
    }

    response = req.get(url, params=params)
    """
        Adding Parameters to Query String
        Client → Server
        
        original_url 
                            -> "https://fakerestapi.azurewebsites.net/api/v1/Activities"
        after_adding_params 
                            -> "https://fakerestapi.azurewebsites.net/api/v1/Activities?name=dev&age=23"
    """


    "adding multiple values for a single parameter/key"
    params_roles = {
        "roles": ["user","admin"]
    }

    response2 = req.get(url, params = params_roles)
    """
            Adding Multiple values for a single parameters
            Client → Server

            original_url 
                                -> "https://fakerestapi.azurewebsites.net/api/v1/Activities"
            after_adding_params 
                                -> "https://fakerestapi.azurewebsites.net/api/v1/Activities?role=user&role=admin
        """


    """
        Obtaining url from the Response type Object
        syntax response.url   <-- return 'str' type url
    """
    print(response.url)  # https://fakerestapi.azurewebsites.net/api/v1/Activities?name=Dev&age=23

    print(response2.url) # https://fakerestapi.azurewebsites.net/api/v1/Activities?roles=user&roles=admin




def get_params(url):

    response = req.get(url)

    # print(response.url)
    # print(response.request.url)

    """
        To obtain all the query parameters ->
            use urllib.parse    
                        -> urlparse  # To obtain the parseResult object
                                     # parseResult(scheme ='' , netloc='' , path ='' , params ='', query = '', fragment) <-- parseResult object constructor
                        -> parse_qs(pareseResult_obj)  <-- extract dictionary of key : [val1,val2,..]
                                                                          string key : list of string values
                                                                          
        Obtaning values list for a specific key
        
        query_params = parse_qs(pareseResult_obj)
        
        value = query_params.get("key name")
        
        
    """
    parsed_url = urlparse(response.request.url)
    print(parsed_url)
    print(type(parsed_url))
    query_params = parse_qs(parsed_url.query)
    print(query_params)         # printing dict of query params
    print(type(query_params))   # dict type object
    print(query_params.get("postId"))  # printing value of specific query param

    print(query_params.get("postI"))   # for invalid key it returns None (No Key Error)



if __name__ == "__main__":
    url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

    url_with_params = "https://jsonplaceholder.typicode.com/comments?postId=1"
    send_params(url)

    get_params(url_with_params)





