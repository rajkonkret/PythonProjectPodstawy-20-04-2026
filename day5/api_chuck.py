import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)

data = response.json()
print(data)
# {'categories': [],
# 'created_at': '2020-01-05 13:42:30.480041',
# 'icon_url': 'https://api.chucknorris.io/img/avatar/chuck-norris.png',
# 'id': 'Fjgy_hibS9CobSVTJv3NOQ',
# 'updated_at': '2020-01-05 13:42:30.480041',
# 'url': 'https://api.chucknorris.io/jokes/Fjgy_hibS9CobSVTJv3NOQ',
# 'value': 'Chuck Norris ones fought Chuck Norris. the world exploded the only person that survived was Chuck Norris no one kills Chuck Norris!!!'}


print(f"Kawał na dzisiaj:", data['value'])
# Kawał na dzisiaj: You can't beat Chuck Norris at poker ever. He always has the better hand...and the better fist.

icon_url = data['icon_url']
print(icon_url)  # https://api.chucknorris.io/img/avatar/chuck-norris.png

response_img = requests.get(icon_url)

with open('icon.png', "wb") as f:
    f.write(response_img.content)
