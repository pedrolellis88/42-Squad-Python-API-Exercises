import requests

U = "UID"
S = "SECRET"
LOGIN_42 = "pdiniz-l"
PROJECTS_URL = f"https://api.intra.42.fr/v2/users/{LOGIN_42}/projects_users"
TOKEN_URL = "https://api.intra.42.fr/oauth/token"
data = {"grant_type": "client_credentials", "client_id": U, "client_secret": S}
auth_response = requests.post(TOKEN_URL, data=data, timeout=30)
if auth_response.status_code != 200:
    print("Error authenticating with 42 API")
    print(auth_response.text)
    exit()
access_token = auth_response.json()["access_token"]
headers = {"Authorization": f"Bearer {access_token}"}
auth_response = requests.post(TOKEN_URL, data=data, timeout=30)
page = 1
per_page = 100
projects = []
while True:
    params = {"page[number]": page, "page[size]": per_page}
    response = requests.get(
        PROJECTS_URL, headers=headers, params=params, timeout=30)
    if response.status_code != 200:
        print("Error")
        print(response.text)
        exit(1)
    data = response.json()
    if not data:
        break
    projects.extend(data)
    page += 1
print("---------------------------------------------------------------\n")
print("Progress of my projects at 42:\n")
for proj in projects:
    project_name = proj["project"]["name"]
    status = proj["status"]
    final_mark = proj["final_mark"]
    grade = final_mark if final_mark is not None else "-"
    print(f"{project_name:<25} | {status:<22} | grade: {grade}")
print("\n---------------------------------------------------------------")
