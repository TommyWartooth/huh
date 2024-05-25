import pygame
import random

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Pantalla Completa")

screen_width, screen_height = screen.get_size()

#imagenes
fondo = pygame.image.load('tableroof2.png')
circulo = pygame.image.load('circulosf.png')
equis = pygame.image.load('equissf.png')

#escalando imagenes
fondo = pygame.transform.scale(fondo,(1500,900))
circulo = pygame.transform.scale(circulo,(180,180))
equis = pygame.transform.scale(equis,(180,180))

# Fuente para los mensajes
font = pygame.font.Font(None, 36)


#matriz
coor = [[(410,110),(583,110),(750,110)],
        [(410,295),(583,295),(750,295)],
        [(410,467),(583,467),(750,467)]]
tablero = [['','',''],
           ['','',''],
           ['','','']]

#turnos
turno = 'X'

#la wea para que funcione
game_over = False
clock = pygame.time.Clock()

#proceso para graficar en el tablero
def  graficar_board():
    screen.blit(fondo, (0,0))
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == 'X':
                dibujar_x(fila,col)
            elif tablero[fila][col] == 'O':
                dibujar_o(fila,col)
            
def dibujar_x(fila,col):
    screen.blit(equis, coor[fila][col])
    
def dibujar_o(fila,col):
    screen.blit(circulo, coor[fila][col])            

def verificar_ganador():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != '':
            return True
        elif tablero [0][i] == tablero[1][i] == tablero[2][i] != '':
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != '':
            return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != '':
            return True
    return False

def verificar_empate():
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == '':
                return False
    return True

def movimiento_computadora():
    # Buscar posición ganadora
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == '':
                tablero[fila][col] = 'O'
                if verificar_ganador():
                    return
                tablero[fila][col] = ''
    
    # Bloquear posición ganadora del usuario
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == '':
                tablero[fila][col] = 'X'
                if verificar_ganador():
                    tablero[fila][col] = 'O'
                    return
                tablero[fila][col] = ''
    
    # Mover a una posición aleatoria
    while True:
        fila = random.randint(0, 2)
        col = random.randint(0, 2)
        if tablero[fila][col] == '':
            tablero[fila][col] = 'O'
            return

#lo principal a
while not game_over:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            if  (mouseX >= 410 and mouseX <932 ) and (mouseY >= 110 and mouseY < 647):
                fila = (mouseY - 110) // 180
                col = (mouseX - 410) // 180
                if tablero[fila][col] == '':
                    tablero[fila][col] = 'X'
                    fin_juego = verificar_ganador()
                    if fin_juego:
                        print(f"El jugador ha ganado!!")
                        game_over = True
                    elif verificar_empate():
                        print("Empate")
                        game_over = True
                    else:
                        movimiento_computadora()
                        fin_juego = verificar_ganador()
                        if fin_juego:
                            print(f"La computadora ha ganado!!")
                            game_over = True
                        
    graficar_board()
    pygame.display.update()

#pygame.quit()

