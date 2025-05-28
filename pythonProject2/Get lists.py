import requests

url = "https://api.clickup.com/api/v2/folder/90156767371/list"

payload = {}
headers = {
  'Authorization': '••••••'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)