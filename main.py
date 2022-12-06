import os
import random
import time
import sys
from colorama import Back, Fore, Style

# str bool
run = True
menu = True
status = False
play = False
batalha = False
safe = True
comprar = False
boss = False
chave = False
falar = True
instrucao = False
credito = False

# atributos do personagem
hp_personagem = 100
hp_max_personagem = 100
ATK = 10
gold = 8
pocao = 1
x = 0
y = 0

# mapa
#         x = 0       x = 1       x = 2       x = 3       x = 4       x = 5        x = 6
mapa = [['planices', 'planices', 'planices', 'planices', 'floresta', 'montanhas', 'caverna'],
        ['floresta', 'floresta', 'floresta', 'floresta', 'floresta', 'colinas',   'montanhas'],
        ['floresta', 'campos',   'ponte',    'floresta', 'colinas',  'floresta',  'colinas'],
        ['planices', 'loja',     'lider',    'floresta', 'planices', 'colinas',   'montanhas'],
        ['planices', 'campos',   'planices', 'floresta', 'colinas',  'montanhas', 'montanhas']]

y_len = len(mapa) - 1
x_len = len(mapa[0]) - 1

# dicionario do mapa
bioma = {
    "planices": {
        "nome": "PLANICES",
        "inimigos": True},

    "floresta": {
        "nome": "FLORESTA",
        "inimigos": True},

    "campos": {
        "nome": "CAMPOS",
        "inimigos": True},

    "cidade": {
        "nome": "CIDADE",
        "inimigos": False},

    "ponte": {
        "nome": "PONTE",
        "inimigos": True},

    "loja": {
        "nome": "LOJA",
        "inimigos": False},

    "colinas": {
        "nome": "COLINAS",
        "inimigos": True},

    "montanhas": {
        "nome": "MONTANHAS",
        "inimigos": True},

    "caverna": {
        "nome": "CAVERNA",
        "inimigos": True},

    "lider": {
        "nome": "CHEFE DA GUILDA",
        "inimigos": False},
}

lista_inimigos = ["Goblin", "Orc", "Slime", "Esqueleto"]
mobs = {
    "Goblin": {
        "HP": 20,
        "atk": random.randint(3, 12),
        "gold": 6
    },
    "Orc": {
        "HP": 25,
        "atk": random.randint(5, 15),
        "gold": 8
    },
    "Slime": {
        "HP": 25,
        "atk": random.randint(2, 8),
        "gold": 6
    },
    "Esqueleto": {
        "HP": 15,
        "atk": random.randint(4, 11),
        "gold": 4
    },
    "Dragão": {
        "HP": 700,
        "atk": random.randint(25, 40),
        "gold": 400
    }
}


# funcoes importantes
def limpaConsole():
    os.system("cls")


def desenhar():
    print("]-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-[")


def telaLogo():
    print(
        f'          {Fore.RED}  ^     \    /      ^        \n'
        '           / \    )\__/(     / \       \n'
        '          /   \  (_\  /_)   /   \      \n'
        '     ____/_____\__\@  @/___/_____\____ \n'
        '    |             |\../|              |\n'
        '    |              \VV/               |\n'
        f'    |         {Fore.RESET}Dragon´s Quest{Fore.RED}          |\n'
        '    |_________________________________|\n'
        '     |    /\ /      //       \ /\    | \n'
        '     |  /   V       ))        V   \  | \n'
        '     |/     `      //         `     \| \n'
        '     `             v                 \'\n'
        '          +=====================+\n'
        f'          |  {Fore.RESET}[{Fore.CYAN}1{Fore.RESET}] Novo jogo{Fore.RED}      |\n'
        f'          |  {Fore.RESET}[{Fore.CYAN}2{Fore.RESET}] Carregar jogo{Fore.RED}  |\n'
        f'          |  {Fore.RESET}[{Fore.CYAN}3{Fore.RESET}] Instruções{Fore.RED}     |\n'
        f'          |  {Fore.RESET}[{Fore.CYAN}0{Fore.RESET}] Sair{Fore.RED}           |\n'
        f'          +=====================+{Fore.RESET}\n')


def salvar():
    save = [
        nome,
        str(hp_personagem),
        str(hp_max_personagem),
        str(ATK),
        str(gold),
        str(pocao),
        str(x),
        str(y)
    ]
    arquivo = open("save.txt", "w")

    for item in save:
        arquivo.write(item + "\n")
    arquivo.close()


def loja():
    global comprar, gold, ATK, pocao, hp_max_personagem
    while comprar:
        limpaConsole()
        print(f"]-=-=-=-=-=-= {Fore.CYAN}LOJA{Fore.RESET} =-=-=-=-=-=-[")
        print(f"   [{Fore.CYAN}1{Fore.RESET}] Comprar Poção (8 de ouro)")
        print(f"   [{Fore.CYAN}2{Fore.RESET}] Comprar Espada + 10 ATK (25 de ouro)")
        print(f"   [{Fore.CYAN}3{Fore.RESET}] Melhorar Armadura + 20 HP (35 de ouro)")
        print(f"   [{Fore.CYAN}0{Fore.RESET}] Sair da loja")
        desenhar()
        print(f"   Moedas: {Fore.YELLOW}{gold}{Fore.RESET}")
        print(f"   Poções: {pocao}")
        print(f"   Dano de ATK: {ATK}")
        print(f"   HP Máximo: {hp_max_personagem}")
        desenhar()
        acao = input(f"{Fore.CYAN}>{Fore.RESET} ")

        if acao == "1":
            if gold >= 8:
                gold -= 8
                pocao += 1
            else:
                print("   Sem ouro suficiente!!")
                input(f"{Fore.CYAN}>{Fore.RESET} ")
        if acao == "2":
            if gold >= 25:
                gold -= 25
                ATK += 10
            else:
                print("   Sem ouro suficiente!!")
                input(f"{Fore.CYAN}>{Fore.RESET}")
        if acao == "3":
            if gold >= 35:
                gold -= 35
                hp_max_personagem += 20
            else:
                print("   Sem ouro suficiente!!")
                input(f"{Fore.CYAN}>{Fore.RESET} ")
        if acao == "0":
            comprar = False


def pocao_curar(curar):
    global hp_personagem
    if hp_personagem + curar < hp_max_personagem:
        hp_personagem += curar
    else:
        hp_personagem = hp_max_personagem
    print(f"   {Fore.CYAN}{nome}{Fore.RESET} usou poção!")
    desenhar()
    input(f"{Fore.CYAN}>{Fore.RESET} ")


def lider():
    global falar, ATK, chave
    while falar:
        limpaConsole()
        desenhar()
        print("   Olá nobre guerreiro!")
        input(f"{Fore.CYAN}>{Fore.RESET} ")
        if ATK >= 30:
            print(f'''   Você finalmente está pronto para derrotar o Dragão
   que assombra nossa vila a anos.
   E como você provou ser um guerreiro digno,
   te darei esta {Fore.YELLOW}CHAVE{Fore.RESET} para ir ao ninho e
   elimina-lo de uma vez por todas!!''')
            print('''
   Tome, leve com você!!
   Ele se esconde a leste daqui.''')
            chave = True
            desenhar()
            print(f"   [{Fore.CYAN}1{Fore.RESET}] Pegar chave e sair")
            desenhar()
        else:
            print("   Você ainda não está pronto para combater a fera")
            chave = False
            desenhar()
            print(f"   [{Fore.CYAN}1{Fore.RESET}] Sair")
            desenhar()
        acao = input(f"{Fore.CYAN}>{Fore.RESET} ")

        if acao == "1":
            falar = False


def chefe():
    global boss, chave, batalha
    while boss:
        limpaConsole()
        if chave:
            print(f"Você está prestes a entrar no ninho do feroz {Fore.RED}Smaug{Fore.RESET}!!\nTem certeza disso?")
            print(f"   [{Fore.CYAN}1{Fore.RESET}] Usar chave")
        if not chave:
            print("Você precisa de uma chave para entrar!")
            print(f"   [{Fore.CYAN}2{Fore.RESET}] Voltar ")

        acao = input(f"{Fore.CYAN}>{Fore.RESET} ")

        if acao == "1":
            if chave:
                batalha = True
                batalha_inimigos()

        elif acao == "2":
            boss = False


def batalha_inimigos():
    global batalha, play, run, hp_personagem, pocao, gold, boss, credito

    if not boss:
        inimigo = random.choice(lista_inimigos)
    else:
        inimigo = "Dragão"
    hp_mob = mobs[inimigo]["HP"]
    hp_max_mob = hp_mob
    atk = mobs[inimigo]["atk"]
    gold_inimigo = mobs[inimigo]["gold"]

    while batalha:
        limpaConsole()
        desenhar()
        print(f"   Derrote o {Fore.RED}{inimigo}{Fore.RESET}!")
        desenhar()
        print(f"   {Fore.RED}{inimigo} HP{Fore.RESET}: {str(hp_mob)} / {str(hp_max_mob)}")
        print(f"   {Fore.CYAN}{nome} HP{Fore.RESET}: {str(hp_personagem)} / {str(hp_max_personagem)}")
        print(f"   Poçoes: {str(pocao)}")
        desenhar()
        print(f"   [{Fore.CYAN}1{Fore.RESET}] Atacar")
        if pocao > 0:
            print(f"   [{Fore.CYAN}2{Fore.RESET}] Usar poção (30 HP)")
        desenhar()

        acao = input(f"{Fore.CYAN}>{Fore.RESET} ")

        if acao == "1":
            desenhar()
            hp_mob -= ATK
            print(f"   {Fore.CYAN}{nome}{Fore.RESET} deu {Fore.CYAN}{str(ATK)}{Fore.RESET} de dano")
            print(f"   ao {Fore.RED}{inimigo}{Fore.RESET}.")
            desenhar()
            if hp_mob > 0:
                hp_personagem -= atk
                print(
                    f"   {Fore.RED}{inimigo}{Fore.RESET} deu {Fore.RED}{str(atk)}{Fore.RESET} de dano a {Fore.CYAN}{nome}{Fore.RESET}.")
                desenhar()
            input(f"{Fore.CYAN}>{Fore.RESET} ")
        elif acao == "2":
            desenhar()
            if pocao > 0:
                pocao -= 1
                pocao_curar(30)
                hp_personagem -= atk
                desenhar()
                print(
                    f"   {Fore.RED}{inimigo}{Fore.RESET} deu {Fore.RED}{str(atk)}{Fore.RESET} de dano a {Fore.CYAN}{nome}{Fore.RESET}.")
                desenhar()
                input(f"{Fore.CYAN}>{Fore.RESET} ")
            else:
                print("    Sem poções!!")
                input(f"{Fore.CYAN}>{Fore.RESET} ")

        if hp_personagem <= 0:
            desenhar()
            print(f"{Fore.RED}{inimigo}{Fore.RESET} derrotou {Fore.CYAN}{nome}{Fore.RESET}....")
            desenhar()
            batalha = False
            play = False
            run = False
            print(f"   {Fore.LIGHTRED_EX}GAME OVER!!{Fore.RESET}")
            quit()

        if hp_mob <= 0:
            desenhar()
            print(f"   {Fore.CYAN}{nome}{Fore.RESET} derrotou {Fore.RED}{inimigo}{Fore.RESET}!")
            desenhar()
            batalha = False
            if random.randint(0, 100) <= 80:
                gold += gold_inimigo
                print(f"   Você achou {Fore.YELLOW}{str(gold_inimigo)}{Fore.RESET} moedas de ouro!")
                desenhar()
            if inimigo == "Dragão":
                gold += gold_inimigo
                print(f"   Você achou {Fore.YELLOW}{str(gold_inimigo)}{Fore.RESET} moedas de ouro!")
                desenhar()
                print("   Parabéns guerreiro você derrotou a\n criatura maligna que nos assombrava a décadas!")
                desenhar()
                input(f"{Fore.CYAN}>{Fore.RESET} ")
                boss = False
                play = False
                run = False
                credito = True
                creditos()

            if random.randint(0, 100) <= 10:
                pocao += 1
                print(f"   Você achou uma {Fore.GREEN}poção{Fore.RESET}!")
                desenhar()
            input(f"{Fore.CYAN}>{Fore.RESET} ")
            limpaConsole()


def instrucoes():
    global instrucao
    while instrucao:
        limpaConsole()
        print(f'''
  As ações serão feitas a partir da barra de "{Fore.RED}AÇÕES{Fore.RESET}" onde cada ação tera impacto em sua gameplay.
  Apos o sinal "{Fore.RED}>{Fore.RESET}" o jogador deverá prssionar "{Fore.RED}ENTER{Fore.RESET}"
  Sua localização se mostrará abaixo de "{Fore.RED}POSIÇÃO{Fore.RESET}" em "{Fore.RED}Localização:{Fore.RESET}"
  Logo abaixo de "{Fore.RED}POSIÇÂO{Fore.RESET}" será mosrado seu status do personagem. 
  O jogo terminará quando o seu personagem derrotar o boss principal,
  Boa sorte!!
        ''')

        print(f"  [{Fore.CYAN}0{Fore.RESET}] Voltar ao menu")

        acao = input(f"{Fore.CYAN}>{Fore.RESET} ")

        if acao == '0':
            instrucao = False


def creditos():
    global credito

    def escrever(texto):
        for letra in texto:
            sys.stdout.write(letra)
            sys.stdout.flush()
            time.sleep(0.09)
    while credito:
        limpaConsole()
        text = f"OBRIGADO POR JOGAR \nFEITO POR: {Fore.LIGHTGREEN_EX}MATHEUS HENRIQUE DE MACEDO{Fore.RESET} \n \nPressione {Fore.GREEN}ENTER{Fore.RESET} para sair"
        textfinal = "2 "
        escrever(text)
        input()
        quit()


# loop principal onde roda tudo
while run:

    while menu:
        # tela inicial de titulo
        limpaConsole()
        telaLogo()
        escolha = input(f"{Fore.CYAN}>{Fore.RESET} ")

        if escolha == '1':
            limpaConsole()
            print("   Qual seu nome nobre guerreiro? ")
            nome = input(f"{Fore.CYAN}>{Fore.RESET} ")
            menu = False
            play = True

        elif escolha == '2':
            try:
                arquivo = open("save.txt", "r")
                carregar_save = arquivo.readlines()
                if len(carregar_save) == 8:
                    nome = carregar_save[0][:-1]
                    hp_personagem = int(carregar_save[1][:-1])
                    hp_max_personagem = int(carregar_save[2][:-1])
                    ATK = int(carregar_save[3][:-1])
                    gold = int(carregar_save[4][:-1])
                    pocao = int(carregar_save[5][:-1])
                    x = int(carregar_save[6][:-1])
                    y = int(carregar_save[7][:-1])

                    limpaConsole()
                    desenhar()
                    print(f"  Bem vindo de volta {Fore.CYAN}{nome}{Fore.RESET} !")
                    print(f"  Pressione {Fore.CYAN}ENTER{Fore.RESET} para continuar")
                    desenhar()
                    input("> ")
                    menu = False
                    play = True
                else:
                    desenhar()
                    print(f"   Arquivo {Fore.RED}CORROMPIDO!{Fore.RESET}")
                    desenhar()
                    input(f"{Fore.CYAN}>{Fore.RESET} ")
            except OSError:
                desenhar()
                print(f"   Dados do  {Fore.RED}SAVE{Fore.RESET} não encontrado!")
                desenhar()
                input(f"{Fore.CYAN}>{Fore.RESET} ")
        elif escolha == '3':
            instrucao = True
            instrucoes()
        elif escolha == '0':
            quit()


        #loop do jogo
        while play:

            salvar()
            limpaConsole()

            # encontro de inimigos
            if not safe:
                if bioma[mapa[y][x]]["inimigos"]:
                    if random.randint(0, 100) <= 25:
                        batalha = True
                        batalha_inimigos()

            # tela principal de acoes

            print(f"]-=-=-=-=-=-{Fore.CYAN} POSIÇÃO {Fore.RESET}=-=-=-=-=-[")
            print("   Localização: " + Fore.CYAN, bioma[mapa[y][x]]["nome"], Fore.RESET)
            print(f"   Coordenadas: {Fore.CYAN}X{Fore.RESET}: {x}  {Fore.CYAN}Y{Fore.RESET}: {y}")
            print(f"]-=-=-=-=-=- {Fore.CYAN}STATUS{Fore.RESET} -=-=-=-=-=-[")
            print(f"   Nome: {nome}")
            print(f"   HP: {Fore.CYAN}{hp_personagem} / {hp_max_personagem}{Fore.RESET} ")
            print(f"   ATK: {ATK}")
            print(f"   Ouro: {gold}")
            print(f"   Poções: {pocao}")
            print(f"]-=-=-=-=-=-= {Fore.CYAN}AÇÃO{Fore.RESET} =-=-=-=-=-=-[")
            if y > 0:
                print(f"   [{Fore.CYAN}1{Fore.RESET}] Ir para o Norte")

            if y < y_len:
                print(f"   [{Fore.CYAN}2{Fore.RESET}] Ir para o Sul")

            if x < x_len:
                print(f"   [{Fore.CYAN}3{Fore.RESET}] Ir para o Leste")

            if x > 0:
                print(f"   [{Fore.CYAN}4{Fore.RESET}] Ir para o Oeste")

            if pocao > 0:
                print(f"   [{Fore.CYAN}5{Fore.RESET}] Usar poção (30 HP)")

            if mapa[y][x] == "loja" or mapa[y][x] == "caverna":
                print(f"   [{Fore.CYAN}6{Fore.RESET}] Entrar na " + Fore.RED + bioma[mapa[y][x]]["nome"] + Fore.RESET)
            if mapa[y][x] == "lider":
                print(f"   [{Fore.CYAN}6{Fore.RESET}] Falar com " + Fore.GREEN + bioma[mapa[y][x]]["nome"] + Fore.RESET)
            print(f"   [{Fore.CYAN}0{Fore.RESET}] Salvar e voltar ao menu")
            desenhar()
            destino = input(f"{Fore.CYAN}>{Fore.RESET} ")


            # destinos do input usuario
            if destino == "0":
                salvar()
                play = False
                menu = True
            elif destino == "1":
                if y > 0:
                    y -= 1
                    safe = False
            elif destino == "2":
                if y < y_len:
                    y += 1
                    safe = False
            elif destino == "3":
                if x < x_len:
                    x += 1
                    safe = False
            elif destino == "4":
                if x > 0:
                    x -= 1
                    safe = False
            elif destino == "5":
                desenhar()
                if pocao > 0:
                    pocao -= 1
                    pocao_curar(30)
                else:
                    print("  Sem poções!!")
                    input(f"{Fore.CYAN}>{Fore.RESET} ")
                safe = True
            elif destino == "6":
                if mapa[y][x] == "loja":
                    comprar = True
                    loja()
                elif mapa[y][x] == "lider":
                    falar = True
                    lider()
                elif mapa[y][x] == "caverna":
                    boss = True
                    chefe()
            else:
                safe = True
