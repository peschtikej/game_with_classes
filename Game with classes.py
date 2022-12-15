import random, time, text
class Hero:
    '''Этот класс описывает героя.'''
    
    
    BASE_HP=1000
    RANGE_ATTACK=(random.randint(75, 125)/100)
    DMG=100
    BASE_WP='GUN'
    ULTA='ULTIMATE_UDAR'
    ULTA_DMG=200



    def __init__(self, 
                name:str):
        self.name=name
    def info(self):
        return(f'Меня зовут {self.name}, \n'
        f'Я использую {self.BASE_WP} как оружие, \n'
        f'Я имею {self.BASE_HP} едениц здоровья \n'
        f'И наношу {self.DMG} урона')
    
    def attack(self) -> int:    
        return int(self.RANGE_ATTACK*self.DMG)+1
    def ulta(self) -> int:
        return int(self.RANGE_ATTACK*self.ULTA_DMG)+1


class Mage(Hero):
    '''Это класс Мага.'''


    DMG=400
    BASE_WP='Молния'
    BASE_HP=500
    ULTA='Мега удар фугасом'
    ULTA_DMG=1000


class Warrior(Hero):
    '''Это класс Воина.'''
    
    
    DMG=100
    BASE_WP='Меч'
    BASE_HP=1500
    ULTA='Прыжок с протыканием'
    ULTA_DMG=350

class Hiler(Hero):
    '''Это класс Целителя.'''
    
    
    DMG=50
    BASE_WP='Палкой в животик'
    BASE_HP=1000
    ULTA='Палкой в глаз'
    ULTA_DMG=100


def choose_chel() -> Hero:
    c={
    'Маг':Mage,
    'Воин':Warrior,
    'Целитель':Hiler
    }
    ch=input(text.START_TEXT)   
    return c[ch](input('Введите имя: \n\n')) 


def train(char1):
    actionx=None
    while actionx != 'skip':
        att={
            'а': char.attack(), 
            'уу': char.ulta()
            }
        MANEKEN=500    
        
        print(f'Приветствую тебя {char1.name}! Рад познакомиться.\n'
        f'Тебе предстоит пройти подготовку боем.\n')
        actionx=input(f'Напишите\n "а" для атаки\n'
        f'"уу" для ульты\n'
        f'Если вы уже знаете как играть\n'
        f'То напишите "skip"\n\n\n'
        )
        if actionx in att:
            print(att[actionx])

if __name__ == '__main__':
    char = choose_chel()
    train(char)