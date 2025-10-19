from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = self.get_hp()
        self.attack = self.get_attack()

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API

    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
            

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "https://upload.wikimedia.org/wikipedia/ru/7/77/Pikachu.png"
        

    def get_hp(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data["stats"][0]["base_stat"])
        else:
            return "https://yandex.ru/images/search?pos=0&from=tabbar&img_url=https%3A%2F%2Fpolinka.top%2Fpics2%2Fuploads%2Fposts%2F2024-02%2F1706896995_polinka-top-p-dulya-risunok-vkontakte-19.jpg&text=abu+nt%2Ct+ajnj&rpt=simage&lr=213"
        
        
    def get_attack(self):
            url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return (data["stats"][1]["base_stat"])
            else:
                return "https://yandex.ru/images/search?pos=0&from=tabbar&img_url=https%3A%2F%2Fpolinka.top%2Fpics2%2Fuploads%2Fposts%2F2024-02%2F1706896995_polinka-top-p-dulya-risunok-vkontakte-19.jpg&text=abu+nt%2Ct+ajnj&rpt=simage&lr=213"



    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def show_hp(self):
        return f"Хп твоего покемна: {self.hp}"

    def show_attack(self):
        return f"Сила атаки твоего покемона: {self.attack}"



