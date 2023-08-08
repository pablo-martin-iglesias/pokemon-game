import os
from random import randint
import readchar

# if gana desaparece ese entrenador
# else menu principal y ni desaparece
# while haya entrenadores ...
# si entrenadores = 3 sale del bucle

# variables
endgame = False
died = False
POS_X = 0
POS_Y = 1   
my_position = [3,3]
trainers = []
NUM_TRAINERS = 3

vence1 = False
vence2 = False
vence3 = False
eliminado1 = False
eliminado2 = False
eliminado3 = False
entrenador1 = False
entrenador2 = False
entrenador3 = False

obstacle_map = """\
#####################
########            #
########  ###########
#         ###########
########  ###########
########            # 
########  ###########
#         ###########
#####################\
"""

# Create walls map
obstacle_map = [list(row) for(row) in obstacle_map.split("\n")]
MAP_WIDTH = len(obstacle_map[0])
MAP_HEIGHT = len(obstacle_map)
print(obstacle_map)

# Create random trainers appearance
while len(trainers) < NUM_TRAINERS:
    new_trainer = [randint(0, MAP_WIDTH-1), randint(0, MAP_HEIGHT-1)]
    if (new_trainer not in trainers and obstacle_map[new_trainer[POS_Y]][new_trainer[POS_X]] != "#"
            and new_trainer != my_position):
        if not entrenador1:
            entrenador1 = new_trainer
            entrenador1 = True
            trainers.append(entrenador1)
        elif not entrenador2:
            entrenador1 = new_trainer
            entrenador1 = True
            trainers.append(entrenador1)
        elif not entrenador3:
            entrenador1 = new_trainer
            entrenador1 = True
            trainers.append(entrenador1)


# Main loop
while not endgame:
    hay_combate = False
    os.system("cls")
    # Draw map
    print("▄" + "▄" * (MAP_WIDTH * 2) + "▄")
    for coordinate_y in range(MAP_HEIGHT):
        print("║", end="")

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = "  "
            hay_entrenador = None

            # imprimimos el entrenador en pantalla
            for tr in trainers:
                if tr[POS_X] == coordinate_x and tr[POS_Y] == coordinate_y:
                    if (vence1 and not eliminado1):
                        trainers.remove(tr)
                        eliminado1 = True
                    if (vence2 and not eliminado2):
                        trainers.remove(tr)
                        eliminado1 = True
                    if (vence3 and not eliminado3):
                        trainers.remove(tr)
                        eliminado1 = True
                    char_to_draw = "😈"
                    hay_entrenador = tr

            # imprimimos el jugador en pantalla
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "😎"
                if hay_entrenador:
                    hay_combate = True

            #imprimios la pared en pantalla
            if obstacle_map[coordinate_y][coordinate_x] == "#":
                char_to_draw = "▒▒"

            print("{}".format(char_to_draw), end="")
        print("║")
    print("▀" + "▀" * (MAP_WIDTH * 2) + "▀")

    # Combat development
    if hay_combate:
        os.system("cls")
        print("PIKACHU se enfrenta a :")

        ##################################### COMBAT STARTS ####################################
        inicial_pikachu = 100
        inicial_squirtle = 90
        actual_pikachu = inicial_pikachu
        actual_squirtle = inicial_squirtle
        vida_pikachu = inicial_pikachu
        vida_squirtle = inicial_squirtle
        TAM_BARRA = 20

        print("Vida Pikachu [{}] {}/{}\n"
              "Vida Squirtle [{}] {}/{}\n".format("#" * TAM_BARRA, actual_pikachu, vida_pikachu,
                                                  "#" * TAM_BARRA, actual_squirtle, vida_squirtle))
        input("Enter para continuar...\n\n")
        os.system("cls")

        while vida_squirtle > 0 and vida_pikachu > 0:
            # Se resuelven los turnos de combate
            # Turno de Squirtle
            print("Turno de Squirtle")
            ataque_squirtle = randint(1, 2)
            if ataque_squirtle == 1:
                print("Squirtle ataca con Pistola de Agua")
                vida_pikachu -= 9
            else:
                print("Squirtle ataca con Burbuja")
                vida_pikachu -= 11

            graf_pikachu = int(vida_pikachu * TAM_BARRA / inicial_pikachu)
            graf_squirtle = int(vida_squirtle * TAM_BARRA / inicial_squirtle)

            if vida_pikachu < 0:
                vida_pikachu = 0

            print("Vida de Squirtle = [{}{}] {}/{}\n""Vida de Pikachu = [{}{}] {}/{}"
                  .format("#" * graf_squirtle, " " * (TAM_BARRA - graf_squirtle), vida_squirtle, inicial_squirtle,
                          "#" * graf_pikachu, " " * (TAM_BARRA - graf_pikachu), vida_pikachu, inicial_pikachu))

            input("Enter para continuar...\n\n")
            os.system("cls")

            # Turno de pikachu
            print("Turno de Pikachu")
            ataque_pikachu = None
            while ataque_pikachu not in ["A", "B", "O", "N"]:
                ataque_pikachu = input("Elige ataque : Ataque Rápido(A) , Bola Voltio(B), Onda Trueno(O), o no atacar(N) : ")
            if ataque_pikachu == "A":
                print("Pikachu ataca con Ataque Rapido")
                vida_squirtle -= 10
            elif ataque_pikachu == "B":
                print("Pikachu ataca con Bola Voltio")
                vida_squirtle -= 13
            elif ataque_pikachu == "O":
                print("Pikachu ataca con Onda Trueno")
                vida_squirtle -= 9
            elif ataque_pikachu == "N":
                print("Pikachu no ataca este turno")

            graf_pikachu = int(vida_pikachu * TAM_BARRA / inicial_pikachu)
            graf_squirtle = int(vida_squirtle * TAM_BARRA / inicial_squirtle)

            if vida_squirtle < 0:
                vida_squirtle = 0
            print("Vida de Squirtle = [{}{}] {}/{}\n""Vida de Pikachu = [{}{}] {}/{}"
                  .format("#" * graf_squirtle, " " * (TAM_BARRA - graf_squirtle), vida_squirtle, inicial_squirtle,
                          "#" * graf_pikachu, " " * (TAM_BARRA - graf_pikachu), vida_pikachu, inicial_pikachu))

            input("Enter para continuar...\n\n")
            os.system("cls")

        if vida_pikachu < vida_squirtle:
            print("Squirtle gana")
        elif vida_pikachu > vida_squirtle:
            print("Pikachu gana")
            vence1 = True

        input("Enter para continuar...\n\n")
        os.system("cls")

        ##################################### COMBAT ENDS ####################################

        # Draw map AFTER COMBAT
        print("▄" + "▄" * (MAP_WIDTH * 2) + "▄")
        for coordinate_y in range(MAP_HEIGHT):
            print("║", end="")

            for coordinate_x in range(MAP_WIDTH):
                char_to_draw = "  "
                hay_entrenador = None

                # imprimimos el entrenador en pantalla
                for tra in trainers:
                    if tra[POS_X] == coordinate_x and tra[POS_Y] == coordinate_y:
                        if (vence1 and not eliminado1):
                            trainers.remove(tra)
                            eliminado1 = True
                        char_to_draw = "😈"
                        hay_entrenador = tra

                # imprimimos el jugador en pantalla
                if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                    char_to_draw = "😎"

                # imprimios la pared en pantalla
                if obstacle_map[coordinate_y][coordinate_x] == "#":
                    char_to_draw = "▒▒"

                print("{}".format(char_to_draw), end="")
            print("║")
        print("▀" + "▀" * (MAP_WIDTH * 2) + "▀")

    ###############################################################################################
    # Add options to move
    direction = readchar.readchar()
    new_position = None

    if direction == "w" or direction == "W":
        new_position = [my_position[POS_X], (my_position[POS_Y] -1) % MAP_HEIGHT]
    elif direction == "s" or direction == "S":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]
    elif direction == "a" or direction == "A":
        new_position = [(my_position[POS_X] -1) % MAP_WIDTH, my_position[POS_Y]]
    elif direction == "d" or direction == "D":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]
    elif direction == "q" or direction == "Q":
        endgame = True

    if new_position:
        if obstacle_map[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position