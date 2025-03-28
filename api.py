import requests
api_url = 'https://api.api-ninjas.com/v1/motorcycles?make=kawasaki&model=ninja'
response = requests.get(api_url, headers={'X-Api-Key': 'H5uuK9HJbSZ2To1kXkXAPA==gquaHst56MQtBG0E'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)
