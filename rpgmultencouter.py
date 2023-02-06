#@title RPG com mult encouter

from google.colab import output
import time
import random
from IPython.display import display
import ipywidgets as widgets

class numero :
  def __init__(self, soma):
    self.soma = soma

  def aumentar(self):
    indicador.soma = indicador.soma + 1

indicador = numero(0)

class hero :
  def __init__(self, vida, ataque, defesa, mana, nivel, xp):
    self.vida = vida
    self.ataque = ataque
    self.defesa = defesa
    self.mana = mana
    self.nivel = nivel
    self.xp = xp

  def atacar(self):
    aleat = random.choice(range(5))
    if aleat == 0 :
      print('Você errou o ataque\n')
    if aleat >= 1 and aleat <= 3 :   
      dano = heroi.ataque - escolhido.defesa
      escolhido.vida = int(escolhido.vida - dano)
      print(f'Você ataca causando {int(dano)} de dano em {escolhido.nome}.\n')
    if aleat == 4 :
      dano = heroi.ataque*2 - escolhido.defesa
      escolhido.vida = int(escolhido.vida - dano)
      print(f'Você causou dano critico de {int(dano)} de dano.\n')
    time.sleep(2)
    if escolhido.vida <= 0 :
      print(f'Você matou {escolhido.nome} e pode continuar a viagem')
      time.sleep(2)
      heroi.xp = heroi.xp + escolhido.givenxp
      if heroi.xp >= 100 :
        print(f'Você subio de nivel! Nivel atual = {heroi.nivel +1}')
        heroi.up()
      output.clear()
      escolhido.vida = escolhido.vidamax
      templateviagem()
    else:
      if escolhido.vida <= escolhido.vidamax * 0.1:
        escolhido.atacarvampirico()
        output.clear()
      else:
        escolhido.atacar()
        output.clear()

  def defender(self):
    probabilidade = random.choice(range(2))
    if probabilidade == 1: 
      dano = int(heroi.ataque*1.3) - escolhido.defesa
      escolhido.vida = int(escolhido.vida - dano)
      print(f'Você defendeu o ataque e aproveitou para contra atacar causando {int(dano)} de dano.\n')
      time.sleep(2)
      if escolhido.vida <= 0 :
        print(f'Você matou {escolhido.nome}')
        time.sleep(2)
        heroi.xp = heroi.xp + escolhido.givenxp
        if heroi.xp >= 100 :
          print(f'Você subio de nivel! Nivel atual = {heroi.nivel +1}')
          heroi.up()
        output.clear()
        escolhido.vida = escolhido.vidamax
        templateviagem()
        output.clear()
    else:
      print(f'Você reduz o dano dobrando sua defesa para {int(heroi.defesa*2)}.\n')
      dano = escolhido.ataque - heroi.defesa*2
      if dano <= 0 :
        dano = 0
      heroi.vida = int(heroi.vida - dano)
      time.sleep(2)
      print(f'O {escolhido.nome} te causou {int(dano)} de dano.\n')
      time.sleep(2)
      output.clear()

  def curar(self):
    if heroi.mana < heroipadrao.mana*0.2 :
      heroi.mana = heroipadrao.mana*0.45
      print(f'Você não tem mana para se curar. Você descançou por essa rodada recuperando {int(heroipadrao.mana*0.45)} de mana.\n')
      time.sleep(2)
      escolhido.atacar()
      output.clear()
    else:
      if heroi.vida*1.25 >= heroipadrao.vida :
        print('Sua vida está completa')
        heroi.vida = heroipadrao.vida
        heroi.mana = heroi.mana - heroipadrao.mana*0.2
        print(f'Te resta {int(heroi.mana)} de mana.\n')
        time.sleep(2)
      else:
        print(f'Você restaurou {int(heroipadrao.vida*0.25)} de vida.')
        heroi.vida = int(heroi.vida + heroipadrao.vida*0.25)
        heroi.mana = heroi.mana - heroipadrao.mana*0.2
        print(f'Te resta {int(heroi.mana)} de mana.\n')
        time.sleep(2)
      escolhido.atacar()
      output.clear()
  
  def desca(self):
    aleater = random.choice(range(10))
    if aleater == 0 :
      escolhidorerrolar()
      print(f'Enquanto descançava, um {escolhido.nome} te encontra no acampamento.')
      time.sleep(2)
      output.clear()
      batalha()
      return 
    else:
      heroi.vida = heroi.vida + heroipadrao.vida*1.2
      if heroi.vida > heroipadrao.vida:
        heroi.vida = heroipadrao.vida
      heroi.mana = heroi.mana*1.25
      print('Você recuperou um pouco de vida e mana antes de seguir viagem.')
      time.sleep(3)
      output.clear()
      templateviagem()
      return 

  def up(self):
    time.sleep(2)
    escolhidorerrolar()
    for x in range(len(lista)) :
      lista[x].vida = lista[x].vida * 1.5
      lista[x].ataque = lista[x].ataque * 1.5
      lista[x].defesa = lista[x].defesa * 1.5
      lista[x].vidamax = lista[x].vidamax * 1.5
    heroi.vida = heroipadrao.vida * 1.3
    heroi.ataque = heroipadrao.ataque * 1.3
    heroi.defesa = heroipadrao.defesa * 1.3
    heroi.mana = heroipadrao.mana * 1.3
    heroi.nivel = heroi.nivel + 1
    heroi.xp = 0
    heroipadrao.vida = heroipadrao.vida * 1.3
    heroipadrao.ataque = heroipadrao.ataque * 1.3
    heroipadrao.defesa = heroipadrao.defesa * 1.3
    heroipadrao.mana = heroipadrao.mana * 1.3

heroipadrao, heroi = hero(100, 20, 10, 50, 1, 0), hero(100, 20, 10, 50, 1, 0)

class monster :
  def __init__(self, nome, vida, ataque, defesa, vidamax, givenxp):
    self.nome = nome
    self.vida = vida
    self.ataque = ataque
    self.defesa = defesa
    self.vidamax = vidamax
    self.givenxp = givenxp

  def atacar(self):
    aleat = random.choice(range(5))
    if aleat == 0 :
      print(f'{escolhido.nome} errou o ataque.\n')
      time.sleep(2)
      if heroi.vida <= 0 :
        return
    if aleat >= 1 and aleat <= 3 :
      dano = escolhido.ataque - heroi.defesa
      if dano <= 0 :
        dano = 0
      heroi.vida = int(heroi.vida - dano)
      print(f'O {escolhido.nome} te causou {int(dano)} de dano.\n')
      time.sleep(2)
      if heroi.vida <= 0 :
        return
    if aleat == 4 :
      dano = escolhido.ataque*2 - heroi.defesa
      if dano <= 0 :
        dano = 0
      heroi.vida = int(heroi.vida - dano)
      print(f'CRITICO!!\n\nO {escolhido.nome} te causou {int(dano)} de dano.\n')
      time.sleep(2)
      if heroi.vida <= 0 :
        return

  def atacarvampirico(self):
    aleat = random.choice(range(5))
    if aleat == 0 :
      print(f'{escolhido.nome} errou o ataque.\n')
      time.sleep(2)
    if aleat >= 1 and aleat <= 3 :
      dano = escolhido.ataque - heroi.defesa
      if dano <= 0 :
        dano = 0
      heroi.vida = int(heroi.vida - dano)
      escolhido.vida = escolhido.vida + dano
      print(f'O {escolhido.nome} te causou {int(dano)} de dano se curando.\n')
      time.sleep(2)
      if heroi.vida <= 0 :
        return
    if aleat == 4 :
      dano = escolhido.ataque*2 - heroi.defesa
      if dano <= 0 :
        dano = 0
      heroi.vida = int(heroi.vida - dano)
      escolhido.vida = escolhido.vida + dano
      print(f'CRITICO!!\n\nO {escolhido.nome} te causou {int(dano)} de dano se curando.\n')
      time.sleep(2)
      if heroi.vida <= 0 :
        return

def escolhidorerrolar():
    numerador = random.choice(range(len(lista)))
    escolhido.nome = lista[numerador].nome
    escolhido.vida = lista[numerador].vida
    escolhido.ataque = lista[numerador].ataque
    escolhido.defesa = lista[numerador].defesa
    escolhido.vidamax = lista[numerador].vidamax
    escolhido.givenxp = lista[numerador].givenxp


def templateviagem():
  if heroi.vida <= 0 :
    return
  anim = ["   🧙‍♂️🌳🌳🌳🌳","   🌳🧙‍♂️🌳🌳🌳","   🌳🌳🧙‍♂️🌳🌳","   🌳🌳🌳🧙‍♂️🌳","   🌳🌳🌳🌳🧙‍♂️"]
  print('Você está passeando pelas planícies. O que será que você pode encontrar?\n')
  z = 0
  for y in range(50):
    indicador.aumentar()
    with output.use_tags('viagem'):
      print(f'Você já viajou {indicador.soma}km.')
      if z == 5:
        z = 0
        print(anim[z])
        z = z+1
      else:
        print(anim[z])
        z = z+1
    time.sleep(1)
    output.clear(output_tags='viagem')
    conbate = random.choice(range(10))
    if conbate == 9:
      print(f'Você encontrou um monstro!!')
      escolhidorerrolar()
      time.sleep(2)
      output.clear()
      escolhido.vida = escolhido.vidamax
      if heroi.vida <= 0 :
        return
      batalha()
      return
    if conbate == 8 :
      camping()
      return

def batalha():
  if heroi.vida <= 0 :
    morreu()
    return 
  output.clear()
  with output.use_tags('batalinha'): 
    print(f'''
  Nivel {heroi.nivel} 
 XP = {heroi.xp}/100

  🧙‍♂️Você🧙‍♂️       x         👾{escolhido.nome}👾
💓={int(heroi.vida)}/{int(heroipadrao.vida)}             
  ⚔️={int(heroi.ataque)}                   💓= {int(escolhido.vida)}/{int(escolhido.vidamax)}
  🛡️={int(heroi.defesa)}                    ⚔️= {int(escolhido.ataque)}
  ✨={int(heroi.mana)}                   🛡️= {int(escolhido.defesa)}
  ''')
    display(atk, defend, heal)
    
def morreu():
  print('''
              VOCE MORREU
    ……..……..$…………….……………..$…………..
     ……..……$$……………………………..$$…………
     ……….…$$……………………..………..$$…………
     ………..$$s………………..………………s$$…………..
    …………….$$$$………...……………….$$$$…………….
   ………………³$$$$..¶¶¶¶¶¶¶¶..$$$$³………………
  ………………..³$$$$..¶¶¶¶¶¶..$$$$³………………..
  ………………¶..$$$$$..¶¶¶¶..$$$$$..¶………………
 …………….¶¶¶..$$$..¶¶¶¶¶¶..$$$..¶¶………………
   …………….¶¶¶….¶¶¶¶¶¶¶¶¶¶….¶¶¶¶………………
   …………….¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶………………
   ………………..¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶………………..
    ……………………¶¶....¶¶¶¶....¶¶…………………
    ……………………¶¶....¶¶¶¶....¶¶………………….
   ………………..¶¶¶¶¶¶¶¶..¶¶¶¶¶¶¶¶………………….
     ………………….¶¶¶¶¶¶……¶¶¶¶¶¶…………………….
     ………….…………….¶¶¶¶¶¶¶¶¶…………………………
    ……………………….¶..¶..¶..¶..¶…………………………
     …………,…………..,…………..,…………..,…………..''')

def camping():
  print('''
    Você encontrou um acampamento.⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠠⣤⣤⣤⣴⣶⣶⣾⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣿⢹⣷⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⡿⠸⣿⣷⡀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⣿⣿⡇⠀⣿⣿⣷⡄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀
⠀⠀⠀⠀⣰⣿⣿⣿⠃⠀⢿⣿⣿⣿⣦⡘⢿⣿⣿⣿⣿⣿⡻⣿⣿⣿⡿⠛⠀⠀
⠀⠀⠀⣴⣿⣿⣿⡿⠀⠀⢸⣿⣿⣿⣿⣷⣄⠙⣿⣿⣿⣿⣿⣤⡙⠻⠀⠀⠀⠀
⠀⢀⣾⣿⣿⣿⣿⠇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣦⠈⢿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        O que deseja fazer?⠀
''')
  display(rest, nrest)
  return
  

#funções de botão para template
#------------------------------

#ataque
atk = widgets.Button(description="Atacar!")
def buttonatk(a):
  output.clear()
  heroi.atacar()
  batalha()
atk.on_click(buttonatk)
#------

#defesa
defend = widgets.Button(description="Defender!")
def buttondef(b): 
  output.clear()
  heroi.defender()
  batalha()
defend.on_click(buttondef)
#------

#cura
heal = widgets.Button(description="Curar!")
def buttonheal(c):   
  output.clear() 
  heroi.curar()
  batalha()
heal.on_click(buttonheal)
#------

#descançar
rest = widgets.Button(description="Descançar.")
def buttonrest(e): 
  output.clear()
  heroi.desca()
rest.on_click(buttonrest)
#------

#ndescançar
nrest = widgets.Button(description="Seguir viagem.")
def buttonnrest(f): 
  output.clear()
  templateviagem()
nrest.on_click(buttonnrest)
#------
#--------------------------------------

goblin = monster('Goblin', 25, 15, 10, 25, 15)
morcego = monster('Morcego', 10, 5, 5, 10, 2)
minotauro = monster('Minotauro', 50, 20, 5, 50, 20)
ladrao = monster('Ladrão', 60, 25, 10, 60, 30)
rato = monster('Rato', 5, 1, 1, 5, 1)
golem = monster('Golem de Vidro', 15, 40, 0, 15, 20)
lista = [goblin, minotauro, morcego, ladrao, rato, golem]
escolhido = monster('', 0, 0, 0, 0, 0)
templateviagem()