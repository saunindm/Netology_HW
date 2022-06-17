import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, file_path: str, file_name: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        href = response.json().get("href", "")
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print(f'''File "{file_name}" has been successfully uploaded to Yandex.Disk''')


if __name__ == '__main__':
     token = ""
     file_path = "Netology/test 9.2.txt"
     file_name = "test 9.2.txt"
     uploader = YaUploader(token)
     result = uploader.upload(file_path, file_name)
