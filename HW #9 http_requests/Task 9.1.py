import requests

superhero_list = ['Hulk', 'Captain America', 'Thanos']


def test_request():
    url = "http://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(url)
    all_json = response.json()
    max_intelligence = 0
    for hero in all_json:
        if hero['name'] in superhero_list and hero['powerstats']['intelligence'] >= max_intelligence:
            max_intelligence = hero['powerstats']['intelligence']
            the_smartest_superhero = hero['name']
    print(f"{the_smartest_superhero} has the highest intelligence - {max_intelligence}")


if __name__ == '__main__':
    test_request()
