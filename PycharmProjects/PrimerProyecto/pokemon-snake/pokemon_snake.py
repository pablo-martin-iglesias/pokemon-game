import os
from random import randint
import readchar


# entrenadores
# cuando pares en un entrenador, dar opcion de que se cree combate
# pokemon
# habilidades pokemon
# fase de combate

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
cont1 = 0
cont2 = 0
cont3 = 0

obstacle_map = """\
#####################
########            #
########   ##########
#          ##########
########   ##########
########            # 
########   ##########
#          ##########
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
        trainers.append(new_trainer)

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
            for tra in trainers:
                if tra[POS_X] == coordinate_x and tra[POS_Y] == coordinate_y:
                    char_to_draw = "😈"
                    hay_entrenador = tra

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

        if not vence1:
            ###################################### COMBAT 1 STARTS ###########################################
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
                    ataque_pikachu = input(
                        "Elige ataque : Ataque Rápido(A) , Bola Voltio(B), Onda Trueno(O), o no atacar(N) : ")
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
                if hay_entrenador:
                    trainers.remove(hay_entrenador)
                vence1 = True

            input("Enter para continuar...\n\n")
            os.system("cls")

            ########################################## COMBAT  1  ENDS ##########################################

            if not vence1:
                # Draw map 1
                print("▄" + "▄" * (MAP_WIDTH * 2) + "▄")
                for coordinate_y in range(MAP_HEIGHT):
                    print("║", end="")

                    for coordinate_x in range(MAP_WIDTH):
                        char_to_draw = "  "
                        hay_entrenador = None

                        # imprimimos el entrenador en pantalla
                        for tra in trainers:
                            if tra[POS_X] == coordinate_x and tra[POS_Y] == coordinate_y:
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

                # Add options to move
                direction = readchar.readchar()
                new_position = None

                if direction == "w" or direction == "W":
                    new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]
                elif direction == "s" or direction == "S":
                    new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]
                elif direction == "a" or direction == "A":
                    new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]
                elif direction == "d" or direction == "D":
                    new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]
                elif direction == "q" or direction == "Q":
                    endgame = True

                if new_position:
                    if obstacle_map[new_position[POS_Y]][new_position[POS_X]] != "#":
                        my_position = new_position

            # Draw map 1
            print("▄" + "▄" * (MAP_WIDTH * 2) + "▄")
            for coordinate_y in range(MAP_HEIGHT):
                print("║", end="")

                for coordinate_x in range(MAP_WIDTH):
                    char_to_draw = "  "
                    hay_entrenador = None

                    if vence1:
                        for tra in trainers:
                            if tra[POS_X] == my_position[POS_X] and tra[POS_Y] == my_position[POS_Y]:
                                trainers.remove(tra)
                    # imprimimos el entrenador en pantalla
                    for tra in trainers:
                        if tra[POS_X] == coordinate_x and tra[POS_Y] == coordinate_y:
                            char_to_draw = "😈"
                            hay_entrenador = tra

                    # imprimimos el jugador en pantalla
                    if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                        char_to_draw = "😎"
                        # if hay_entrenador:
                        #   hay_combate = True

                    # imprimios la pared en pantalla
                    if obstacle_map[coordinate_y][coordinate_x] == "#":
                        char_to_draw = "▒▒"

                    print("{}".format(char_to_draw), end="")
                print("║")
            print("▀" + "▀" * (MAP_WIDTH * 2) + "▀")

            ############################################################################################
        if cont1 == 0:
            cont1 += 1
            continue

        if vence1 and not vence2:
            ###################################### COMBAT 2 STARTS ###########################################
            inicial_pikachu = 100
            inicial_pidgey = 100
            actual_pikachu = inicial_pikachu
            actual_pidgey = inicial_pidgey
            vida_pikachu = inicial_pikachu
            vida_pidgey = inicial_pidgey
            TAM_BARRA = 20

            print("Vida Pikachu [{}] {}/{}\n"
                  "Vida Pidgey [{}] {}/{}\n".format("#" * TAM_BARRA, actual_pikachu, vida_pikachu,
                                                    "#" * TAM_BARRA, actual_pidgey, vida_pidgey))
            input("Enter para continuar...\n\n")
            os.system("cls")

            while vida_pidgey > 0 and vida_pikachu > 0:
                # Se resuelven los turnos de combate
                # Turno de Pidgey
                print("Turno de Pidgey")
                ataque_pidgey = randint(1, 2)
                if ataque_pidgey == 1:
                    print("Pidgey ataca con Ataque Arena")
                    vida_pikachu -= 9
                else:
                    print("Pidgey ataca con Tornado")
                    vida_pikachu -= 11

                graf_pikachu = int(vida_pikachu * TAM_BARRA / inicial_pikachu)
                graf_pidgey = int(vida_pidgey * TAM_BARRA / inicial_pidgey)

                if vida_pikachu < 0:
                    vida_pikachu = 0

                print("Vida de Pidgey = [{}{}] {}/{}\n""Vida de Pikachu = [{}{}] {}/{}"
                      .format("#" * graf_pidgey, " " * (TAM_BARRA - graf_pidgey), vida_pidgey, inicial_pidgey,
                              "#" * graf_pikachu, " " * (TAM_BARRA - graf_pikachu), vida_pikachu, inicial_pikachu))

                input("Enter para continuar...\n\n")
                os.system("cls")

                # Turno de pikachu
                print("Turno de Pikachu")
                ataque_pikachu = None
                while ataque_pikachu not in ["A", "B", "O", "N"]:
                    ataque_pikachu = input(
                        "Elige ataque : Ataque Rápido(A) , Bola Voltio(B), Onda Trueno(O), o no atacar(N) : ")
                if ataque_pikachu == "A":
                    print("Pikachu ataca con Ataque Rapido")
                    vida_pidgey -= 11
                elif ataque_pikachu == "B":
                    print("Pikachu ataca con Bola Voltio")
                    vida_pidgey -= 13
                elif ataque_pikachu == "O":
                    print("Pikachu ataca con Onda Trueno")
                    vida_pidgey -= 10
                elif ataque_pikachu == "N":
                    print("Pikachu no ataca este turno")

                graf_pikachu = int(vida_pikachu * TAM_BARRA / inicial_pikachu)
                graf_pidgey = int(vida_pidgey * TAM_BARRA / inicial_pidgey)

                if vida_pidgey < 0:
                    vida_pidgey = 0
                print("Vida de Pidgey = [{}{}] {}/{}\n""Vida de Pikachu = [{}{}] {}/{}"
                      .format("#" * graf_pidgey, " " * (TAM_BARRA - graf_pidgey), vida_pidgey, inicial_pidgey,
                              "#" * graf_pikachu, " " * (TAM_BARRA - graf_pikachu), vida_pikachu, inicial_pikachu))

                input("Enter para continuar...\n\n")
                os.system("cls")

            if vida_pikachu < vida_pidgey:
                print("Pidgey gana")
            elif vida_pikachu > vida_pidgey:
                print("Pikachu gana")
                if hay_entrenador:
                    trainers.remove(hay_entrenador)
                vence2 = True

            input("Enter para continuar...\n\n")
            os.system("cls")

            ########################################## COMBAT  2  ENDS ##########################################

            if not vence2:
                if not vence1:
                    # Draw map 1
                    print("▄" + "▄" * (MAP_WIDTH * 2) + "▄")
                    for coordinate_y in range(MAP_HEIGHT):
                        print("║", end="")

                        for coordinate_x in range(MAP_WIDTH):
                            char_to_draw = "  "
                            hay_entrenador = None

                            # imprimimos el entrenador en pantalla
                            for tra in trainers:
                                if tra[POS_X] == coordinate_x and tra[POS_Y] == coordinate_y:
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

                    # Add options to move
                    direction = readchar.readchar()
                    new_position = None

                    if direction == "w" or direction == "W":
                        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]
                    elif direction == "s" or direction == "S":
                        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]
                    elif direction == "a" or direction == "A":
                        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]
                    elif direction == "d" or direction == "D":
                        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]
                    elif direction == "q" or direction == "Q":
                        endgame = True

                    if new_position:
                        if obstacle_map[new_position[POS_Y]][new_position[POS_X]] != "#":
                            my_position = new_position

            # Draw map 2
            print("▄" + "▄" * (MAP_WIDTH * 2) + "▄")
            for coordinate_y in range(MAP_HEIGHT):
                print("║", end="")

                for coordinate_x in range(MAP_WIDTH):
                    char_to_draw = "  "
                    hay_entrenador = None

                    if vence2:
                        for tra in trainers:
                            if tra[POS_X] == my_position[POS_X] and tra[POS_Y] == my_position[POS_Y]:
                                trainers.remove(tra)
                    # imprimimos el entrenador en pantalla
                    for tra in trainers:
                        if tra[POS_X] == coordinate_x and tra[POS_Y] == coordinate_y:
                            char_to_draw = "😈"
                            hay_entrenador = tra

                    # imprimimos el jugador en pantalla
                    if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                        char_to_draw = "😎"
                        # if hay_entrenador:
                        #   hay_combate = True

                    # imprimios la pared en pantalla
                    if obstacle_map[coordinate_y][coordinate_x] == "#":
                        char_to_draw = "▒▒"

                    print("{}".format(char_to_draw), end="")
                print("║")
            print("▀" + "▀" * (MAP_WIDTH * 2) + "▀")

            ############################################################################################
        if cont2 == 0:
            cont2 += 1
            continue

        if vence1 and vence2 and not vence3:
            ###################################### COMBAT 3 STARTS ###########################################
            inicial_pikachu = 100
            inicial_mewtwo = 110
            actual_pikachu = inicial_pikachu
            actual_mewtwo = inicial_mewtwo
            vida_pikachu = inicial_pikachu
            vida_mewtwo = inicial_mewtwo
            TAM_BARRA = 20

            print("Vida Pikachu [{}] {}/{}\n"
                  "Vida Mewtwo [{}] {}/{}\n".format("#" * TAM_BARRA, actual_pikachu, vida_pikachu,
                                                    "#" * TAM_BARRA, actual_mewtwo, vida_mewtwo))
            input("Enter para continuar...\n\n")
            os.system("cls")

            while vida_mewtwo > 0 and vida_pikachu > 0:
                # Se resuelven los turnos de combate
                # Turno de Mewtwo
                print("Turno de Mewtwo")
                ataque_mewtwo = randint(1,3)
                if ataque_mewtwo == 1:
                    print("Mewtwo usa Recuperación")
                    vida_mewtwo += 8
                elif ataque_mewtwo == 2:
                    print("Mewtwo ataca con Rapidez")
                    vida_pikachu -= 11
                elif ataque_mewtwo == 3:
                    print("Mewtwo ataca con Psíquico")
                    vida_pikachu -= 15

                graf_pikachu = int(vida_pikachu * TAM_BARRA / inicial_pikachu)
                graf_mewtwo = int(vida_mewtwo * TAM_BARRA / inicial_mewtwo)

                if vida_pikachu < 0:
                    vida_pikachu = 0
                if vida_mewtwo > inicial_mewtwo:
                    graf_mewtwo = TAM_BARRA

                print("Vida de Mewtwo = [{}{}] {}/{}\n""Vida de Pikachu = [{}{}] {}/{}"
                      .format("#" * graf_mewtwo, " " * (TAM_BARRA - graf_mewtwo), vida_mewtwo, inicial_mewtwo,
                              "#" * graf_pikachu, " " * (TAM_BARRA - graf_pikachu), vida_pikachu, inicial_pikachu))

                input("Enter para continuar...\n\n")
                os.system("cls")

                # Turno de pikachu
                print("Turno de Pikachu")
                ataque_pikachu = None
                while ataque_pikachu not in ["A", "B", "O", "I"]:
                    ataque_pikachu = input(
                        "Elige ataque : Ataque Rápido(A) , Bola Voltio(B), Onda Trueno(O), o Impactotrueno(I) : ")
                if ataque_pikachu == "A":
                    print("Pikachu ataca con Ataque Rapido")
                    vida_mewtwo -= 12
                elif ataque_pikachu == "B":
                    print("Pikachu ataca con Bola Voltio")
                    vida_mewtwo -= 13
                elif ataque_pikachu == "O":
                    print("Pikachu ataca con Onda Trueno")
                    vida_mewtwo -= 11
                elif ataque_pikachu == "I":
                    print("Pikachu ataca con Impactotrueno")
                    vida_mewtwo -= 15

                graf_pikachu = int(vida_pikachu * TAM_BARRA / inicial_pikachu)
                graf_mewtwo = int(vida_mewtwo * TAM_BARRA / inicial_mewtwo)

                if vida_mewtwo < 0:
                    vida_mewtwo = 0
                print("Vida de Mewtwo = [{}{}] {}/{}\n""Vida de Pikachu = [{}{}] {}/{}"
                      .format("#" * graf_mewtwo, " " * (TAM_BARRA - graf_mewtwo), vida_mewtwo, inicial_mewtwo,
                              "#" * graf_pikachu, " " * (TAM_BARRA - graf_pikachu), vida_pikachu, inicial_pikachu))

                input("Enter para continuar...\n\n")
                os.system("cls")

            if vida_pikachu < vida_mewtwo:
                print("Mewtwo gana")
            elif vida_pikachu > vida_mewtwo:
                print("Pikachu gana")
                if hay_entrenador:
                    trainers.remove(hay_entrenador)
                vence3 = True

            input("Enter para continuar...\n\n")
            os.system("cls")

            if vence3:
                os.system("cls")
                print("🎖️🎖️🎖️  ¡¡¡ FELICIDADES, ERES EL NUEVO CAMPEON POKEMON !!!  🎖️🎖️🎖️\n")
                os.system("pause")
                exit()

            ########################################## COMBAT  3  ENDS ##########################################

            # Draw map 3
            print("▄" + "▄" * (MAP_WIDTH * 2) + "▄")
            for coordinate_y in range(MAP_HEIGHT):
                print("║", end="")

                for coordinate_x in range(MAP_WIDTH):
                    char_to_draw = "  "
                    hay_entrenador = None

                    if vence3:
                        for tra in trainers:
                            if tra[POS_X] == my_position[POS_X] and tra[POS_Y] == my_position[POS_Y]:
                                trainers.remove(tra)
                    # imprimimos el entrenador en pantalla
                    for tra in trainers:
                        if tra[POS_X] == coordinate_x and tra[POS_Y] == coordinate_y:
                            char_to_draw = "😈"
                            hay_entrenador = tra

                    # imprimimos el jugador en pantalla
                    if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                        char_to_draw = "😎"
                        # if hay_entrenador:
                        #   hay_combate = True

                    # imprimios la pared en pantalla
                    if obstacle_map[coordinate_y][coordinate_x] == "#":
                        char_to_draw = "▒▒"

                    print("{}".format(char_to_draw), end="")
                print("║")
            print("▀" + "▀" * (MAP_WIDTH * 2) + "▀")

            ############################################################################################

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