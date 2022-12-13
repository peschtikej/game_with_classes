import random
class Hero:
    '''Этот класс описывает героя.'''
    
    
    BASE_HP=1000
    RANGE_ATTACK=(random.randint(75, 125)/100)
    DMG=100
    BASE_WP='GUN'



    def __init__(self, 
                name:str):
        self.name=name
    def info(self):
        return(f'Меня зовут {self.name}, \n'
        f'Я использую {self.BASE_WP} как оружие, \n'
        f'Я имею {self.BASE_HP} едениц здоровья \n'
        f'И наношу {self.DMG} урона')
    
    def attack(self):    
        return(f'{self.name} наносит {int(self.RANGE_ATTACK*self.DMG)+1} урона с помощью {self.BASE_WP}')


class Mage(Hero):
    '''Это класс Мага.'''


    DMG=400
    BASE_WP='Молнии'
    BASE_HP=500


class Warrior(Hero):
    '''Это класс Воина.'''
    
    
    DMG=100
    BASE_WP='Меча'
    BASE_HP=1500


class Hiler(Hero):
    '''Это класс Целителя.'''
    
    
    DMG=50
    BASE_WP='Исцеления'
    BASE_HP=1000

def choose_chel() -> Hero:
    c={
    'Маг':Mage,
    'Воин':Warrior,
    'Целитель':Hiler
    }
    ch=input('Здравствуй мудрый путник\n'
    'Ты начал игру The longest ECHPECHMAK(in HEGROPROM)\n'
    'Выбери класс:\n\n'
    'Маг — наносит много урона, но не имеет\n'
    'Много здоровья. Для выбора напиши Маг.\n\n'
    'Воин — сбалансирован\n'
    'Но не учён. Для выбора напиши Воин.\n\n'
    'Целитель — наносит много, но не имеет достаточно\n'
    'Здоровья. Для выбора напиши Целитель.\n\n'
    )   
    return c[ch](input('Введите имя: ')) 


def train(char1):
    att={
        'а': char.attack()
        }
    MANEKEN=500    
    
    print(f'Приветствую тебя {char1.name}! Рад познакомиться.\n'
    f'Тебе предстоит пройти подготовку боем.\n')
    actionx=input(f'Напишите\n "а" для атаки с помощью {char1.BASE_WP}\n\n\n')
    print(att[actionx])
if __name__ == '__main__':
    char = choose_chel()
    train(char)