from pprint import pprint
import requests
import json


ACCESS_TOKEN = "2619421814940190"
API_URL = "https://superheroapi.com/api/" # "/"" at the end is obligatory


def try_get_character(url: str, character: str):
    return_val = None
    try:
        print(F"Trying to parse {character}..")
        request_uri = F"{url}/search/{character}"
        return_val = requests.get(request_uri).json()["results"][0]
    except Exception as e:
        print("Error: ", character, e)
    return return_val
   

def main() -> None: # This is main

    url_base = F"{API_URL}{ACCESS_TOKEN}"
    characters_dict = dict()

    #Задача №1
    characters_list = ["Thanos", "Captain America", "Hulk"]

    for character_name in characters_list:
        characters_dict[character_name] = try_get_character(url_base, character_name)

    iq_dict = dict()
    for character_name in characters_dict:
        try:
            iq_dict[character_name] = int(characters_dict[character_name]["powerstats"]["intelligence"])
        except Exception as e:
            print("Error: ", character_name, e)

    for item_index, item in enumerate(sorted(iq_dict.items(), key=lambda x: x[1], reverse=True)):
        print(F"Самый умный (iq:{item[1]})", item[0]) if item_index == 0 else None
        print(F"Обычный (iq:{item[1]})", item[0]) if item_index >= 1 and item_index <= 3 else None
        print(F"Не очень умный (iq:{item[1]})", item[0]) if item_index > 3 else None
    
    return None
    # end of main

if __name__ == "__main__":
    main()
