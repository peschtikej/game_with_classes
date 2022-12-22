import text

import random
import time

import pygame

pygame.init()
class Hero:
    '''Этот класс описывает героя.'''
    
    
    SKIN=pygame.image.load('pics\просто красивый замок.jpg').convert()
    BASE_HP=1000
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
        return int((random.randint(75, 125)/100)*self.DMG)+1
    def ulta(self) -> int:
        return int((random.randint(75, 125)/100)*self.ULTA_DMG)+1


class Mage(Hero):
    '''Это класс Мага.'''


    SKIN=pygame.image.load('pics\маг.jpg').convert()
    DMG=400
    BASE_WP='Молния'
    BASE_HP=500
    ULTA='Мега удар фугасом'
    ULTA_DMG=1000


class Warrior(Hero):
    '''Это класс Воина.'''
    
    
    SKIN=pygame.image.load('pics\воин с мечом в замке смотрит на солнце.jpg').convert()
    DMG=100
    BASE_WP='Меч'
    BASE_HP=1500
    ULTA='Прыжок с протыканием'
    ULTA_DMG=350

class Hiler(Hero):
    '''Это класс Целителя.'''
    
    
    SKIN=pygame.image.load('pics\аниме с палкой на фоне реки и леса.jpg').convert()
    DMG=50
    BASE_WP='Палкой в животик'
    BASE_HP=1000
    ULTA='Палкой в глаз'
    ULTA_DMG=100


class Badmalaj(Hero):
    '''Это класс врага.'''
    
    SKIN=pygame.image.load('pics\бэдбой.jpg').convert()
    DMG=100
    BASE_WP='Камень в лицо'
    BASE_HP=250


def choose_chel() -> Hero:
    c={
    'Маг':Mage,
    'Воин':Warrior,
    'Целитель':Hiler
    }
    ch=input(text.START_TEXT)   
    return c[ch](input('Введите имя: \n'))


def train(char1):
    MANEKEN=500
    print(f'Приветствую тебя {char1.name}! Рад познакомиться.\n'
        f'Тебе предстоит пройти подготовку боем.\n')
        
    print(f'Напишите\n "а" для атаки\n'
        f'"уу" для ульты\n'
        f'Если вы уже знаете как играть\n'
        f'То напишите "skip"\n\n\n'
        )
    actionx=None
    while actionx != 'skip':
        att={
            'а': char.attack(), 
            'уу': char.ulta()
        }
        actionx=input()
        if actionx in att:
            print(att[actionx])

if __name__ == '__main__':
    char = choose_chel()
    train(char)