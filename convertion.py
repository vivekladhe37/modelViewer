import requests
import json

#forge creds and bim details
client_id = "i3ubGGn8qrTaI8FYNsQtljBkGkTnz9Cv"
client_secret = "WwII1a1WWbvkaTVb"
bim360_project_id = "94de07a7-033a-4a3a-9009-ad7f6874610d"
rvt_file_id = "urn:adsk.wipprod:dm.lineage:cUkVSaFKQwONvxNJfmdg4g"
derivative_id = "dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLmNVa1ZTYUZLUXdPTnZ4TkpmbWRnNGc_dmVyc2lvbj0xMA"

#auth
def get_access_token():
    url = "https://developer.api.autodesk.com/authentication/v1/authenticate"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
        "scope": "data:read data:write"
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()["access_token"]

#svf auth
def get_token():
    url = "https://developer.api.autodesk.com/authentication/v2/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
        "scope": "data:read data:create"
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json()["access_token"]


#bim details
def get_bim360_file_details(access_token):
    url = f"https://developer.api.autodesk.com/data/v1/projects/b.{bim360_project_id}/items/{rvt_file_id}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json()

#simple-vector-format
def convert_to_svf(token):
    url = "https://developer.api.autodesk.com/modelderivative/v2/designdata/job"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    data = {
        "input": {
            "urn": derivative_id
        },
        "output": {
            "formats": [
                {
                    "type": "svf",
                    "views": ["3d"]
                }
            ]
        }
    }
    response = requests.post(url, headers=headers, json=data)
    print(response)

    return response.json()

#manifest
def check_status(token):
    url =  f"https://developer.api.autodesk.com/modelderivative/v2/designdata/{derivative_id}/manifest"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    print(response.json())

#main function
if __name__ == "__main__":
    #auth
    access_token = get_access_token()
    #print("Access Token is : {}".format(access_token))

    #bim
    file_details = get_bim360_file_details(access_token)
    #print("RVT file details are : {}".format(file_details))

    #svf token
    token = get_token()
    print("SVF Token is : {}".format(token))

    #SVF
    #svf_urn = convert_to_svf(token)
    #print("SVF URN:", svf_urn)

    #check status
    #check_status(token)

