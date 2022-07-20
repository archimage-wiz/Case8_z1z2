from pprint import pprint
import requests

HOST = "https://cloud-api.yandex.net"
UPLOAD_PATH = "/v1/disk/resources/upload"

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        req_headers = {
            "Content-Type" : "application/json",
            "Authorization" : F"OAuth {self.token}"
        }
        req_parameters = {
            "path" : file_path,
            "overwrite" : "True"
        }
        srv_response = requests.get(HOST + UPLOAD_PATH, headers=req_headers, params=req_parameters)
        pprint(srv_response)
        if(srv_response.status_code == 200):
            resp_json = srv_response.json()
            upload_link = resp_json['href']
            srv_response = requests.put(upload_link, data=open(file_path, "rb"))
            print(srv_response)
            srv_response.raise_for_status()
            # //


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    #path_to_file = "some_file.txt"
    path_to_file = input("Название файла: ")
    token = input("Токен: ")
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

    # eom

