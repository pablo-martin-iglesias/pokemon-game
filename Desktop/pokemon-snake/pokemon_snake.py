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
        print("PIKACHU se enfrenta a :")

        ################################################################################################
        inicial_pikachu = 80
        inicial_squirtle = 90
        actual_pikachu = inicial_pikachu
        actual_squirtle = inicial_squirtle
        vida_pikachu = inicial_pikachu
        vida_squirtle = inicial_squirtle
        TAM_BARRA = 20

        print("Vida Pikachu [{}] {}/{}\n"
              "Vida Squirtle [{}] {}/{}\n".format("#" * TAM_BARRA, actual_pikachu, vida_pikachu,
                                                  "#" * TAM_BARRA, actual_squirtle, vida_squirtle))

        while vida_squirtle > 0 and vida_pikachu > 0:
            # Se resuelven los turnos de combate
            # Turno de pikachu

            print("Turno de Pikachu")
            ataque_pikachu = randint(1, 2)
            if ataque_pikachu == 1:
                print("Pikachu ataca con Bola Voltio")
                vida_squirtle -= 10
            else:
                print("Pikachu ataca con Onda Trueno")
                vida_squirtle -= 11

            graf_pikachu = int(vida_pikachu * TAM_BARRA / inicial_pikachu)
            graf_squirtle = int(vida_squirtle * TAM_BARRA / inicial_squirtle)

            if vida_squirtle < 0:
                vida_squirtle = 0

            print("Vida de pikachu = [{}{}] {}/{}\n""Vida de squirtle = [{}{}] {}/{}"
                  .format("#" * graf_pikachu, " " * (TAM_BARRA - graf_pikachu), vida_pikachu, inicial_pikachu,
                          "#" * graf_squirtle, " " * (TAM_BARRA - graf_squirtle), vida_squirtle, inicial_squirtle))

            input("Enter para continuar...\n\n")
            os.system("cls")

            # Turno de squirtle

            print("Turno de Squirtle")
            ataque_squirtle = None
            while ataque_squirtle not in ["P", "A", "B", "N"]:
                ataque_squirtle = input("Elige ataque : Placaje(P) , Pistola agua(A), Burbuja(B), o no atacar(N) : ")
            if ataque_squirtle == "P":
                print("Squirtle ataca con Placaje")
                vida_pikachu -= 10
            elif ataque_squirtle == "A":
                print("Squirtle ataca con Pistola agua")
                vida_pikachu -= 12
            elif ataque_squirtle == "B":
                print("Squirtle ataca con Burbuja")
                vida_pikachu -= 9
            elif ataque_squirtle == "N":
                print("Squirtle no ataca este turno")

            graf_pikachu = int(vida_pikachu * TAM_BARRA / inicial_pikachu)
            graf_squirtle = int(vida_squirtle * TAM_BARRA / inicial_squirtle)

            if vida_pikachu < 0:
                vida_pikachu = 0
            print("Vida de pikachu = [{}{}] {}/{}\n""Vida de squirtle = [{}{}] {}/{}"
                  .format("#" * graf_pikachu, " " * (TAM_BARRA - graf_pikachu), vida_pikachu, inicial_pikachu,
                          "#" * graf_squirtle, " " * (TAM_BARRA - graf_squirtle), vida_squirtle, inicial_squirtle))

            input("Enter para continuar...\n\n")
            os.system("cls")

        if vida_pikachu < vida_squirtle:
            print("Squirtle gana")
        elif vida_pikachu > vida_squirtle:
            print("Pikachu gana")
    ###############################################################################################

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
                    #if hay_entrenador:
                    #   hay_combate = True

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

    if direction == "w" or direction == "S":
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