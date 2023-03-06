from __future__ import annotations
from dataclasses import dataclass, field
from random import randint

@dataclass 
class Tank:
    
    model:str
    armor:int
    health:float
    min_damage:int
    max_damage:int
    damage:int=field(init=False)
    mes:str=field(init=False)

    def __post_init__(self)->None:
        if self.armor<=0: 
            self.armor=1
        if self.health<=0:
            self.health=5
        if self.min_damage<=0:
            self.min_damage=1
        if self.max_damage <= self.min_damage:
            self.max_damage=self.min_damage+1
        self.damage = randint(self.min_damage,self.max_damage)
        
    def print_info(self)->None:
        self.mes = f"«{self.model}» имеет лобовую броню «{self.armor}»"\
                    f"мм. при «{self.health}» ед. здоровья и урон в "\
                    f"«{self.damage}» единиц"
        print(self.mes)

    def shot(self, some_tank: Tank) -> None: 
        some_tank.health_down(self.damage)
        if some_tank.health<=0:
            self.mes = f"Экипаж танка «{some_tank.model}» уничтожен"
            print(self.mes)
        else:
            self.mes = f"«{self.model}»: Точно в цель, у противника "\
                        f"«{some_tank.model}» осталось «{some_tank.health}»"\
                        f"единиц здоровья"
            print(self.mes)
    
    def health_down(self,damage_taken: int) -> None:
        self.health-=damage_taken/self.armor
        if self.health>0:
            self.mes = f"«{self.model}»: Командир, по экипажу «{self.model}» "\
                        f"попали, у нас осталось «{self.health}» очков здоровья"
        else:
            self.mes = f"«{self.model}»: Командир, по экипажу «{self.model}» "\
                        f"попали, у нас не осталось очков здоровья"
            print(self.mes)

if __name__== "__main__":
    a=Tank("T34",10,10.,10,15)
    b=Tank("T35",10,10.,10,15)
    b.shot(a)
    a.print_info()
# https://t.me/+nfQXgqbMAzo3YjAy
