import random

class puchamons:
    def __init__(self,nombre,vida,ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def atacar(self,otro):
        daño = random.randint(0, self.ataque)
        otro.vida -= daño
        print(f"{self.nombre} ataca a {otro.nombre} y le causa {daño} de daño")
        print(f"ps actuales de {otro.nombre}: {otro.vida} ")

    def vivo(self):
        return self.vida > 0
    
def batalla(puchamon1, puchamon2):
    turno = 0
    while puchamon1.vivo() and puchamon2.vivo():
        if turno % 2 == 0:
            puchamon1.atacar(puchamon2)
        else:
            puchamon2.atacar(puchamon1)
        turno += 1
        print()

    if puchamon1.vivo():
        print(f"gana {puchamon1.nombre}")
    else:
        print(f"gana {puchamon2.nombre}")

l = puchamons("l",10,1)
d = puchamons("d",10,2)
batalla(l,d)

 