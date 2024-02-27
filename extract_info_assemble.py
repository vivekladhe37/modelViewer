import requests

# Forge API credentials
client_id = 'i3ubGGn8qrTaI8FYNsQtljBkGkTnz9Cv'
client_secret = 'WwII1a1WWbvkaTVb'
project_id = '94de07a7-033a-4a3a-9009-ad7f6874610d'
hub_id = '82456a78-de16-4ccb-8b95-5bf550f1908e'
hj_folder_id = 'urn:adsk.wipprod:fs.folder:co.EHVvPO-oTtSdUR3KSaAJ9w'
hj_version_id = 'urn:adsk.wipprod:fs.file:vf.cUkVSaFKQwONvxNJfmdg4g?version=10'
hj_item_id = 'urn:adsk.wipprod:dm.lineage:cUkVSaFKQwONvxNJfmdg4g'
file_id = 'urn:adsk.wipprod:dm.lineage:cUkVSaFKQwONvxNJfmdg4g'


def authenticate(client_id, client_secret):
    url = "https://developer.api.autodesk.com/authentication/v1/authenticate"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
        "scope": "data:read"
    }

    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print("Authentication Error: ", response.status_code)
        return None
    
def get_project_details(hub_id, project_id, access_token):
    url = f"https://developer.api.autodesk.com/data/v1/projects/b.{project_id}/items/{hj_item_id}/versions"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error getting project details: ", response.status_code)
        print("Response content: ", response.content)
        return None

access_token = authenticate(client_id, client_secret)
print("Access Token is", access_token)
if access_token:
    project_details = get_project_details(hub_id, project_id, access_token)
    if project_details:
        print("Project Details:", project_details)
    else:
        print("Failed to retrieve project details.")
