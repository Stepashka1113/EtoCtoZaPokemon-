from random import randint
import requests
import random
class Pokemon:
    pokemons = {}
    hunger = random.randint(20,100)
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = self.get_hp()
        self.power = self.get_attack()

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
    
    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"

        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "


    def info(self):
        return f"Имя твоего покеомона: {self.name}\n Хп твоего покемна: {self.hp}\n Сила атаки твоего покемона: {self.power}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        result = super().attack(enemy)
        return result + f"\nБоец применил супер-атаку силой:{super_power} "
    
class Wizard(Pokemon):
    pass


    # Метод класса для получения информации
if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))
