import serial
import pygame
import sys

# Configuración inicial de pygame
pygame.init()
screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption('Lectura del Potenciómetro')
font = pygame.font.Font(None, 24)
clock = pygame.time.Clock()

# Configuración de la comunicación serial
puertoSerie = serial.Serial('COM6', 9600, timeout=1)

# Variables
valorPotenciometro = 0

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Leer datos del puerto serial
    if puertoSerie.in_waiting > 0:
        line = puertoSerie.readline().decode('utf-8').strip()
        if line:
            try:
                valorPotenciometro = int(line)
                print(valorPotenciometro)
            except ValueError:
                pass  # En caso de que la conversión falle

    # Lógica de visualización
    screen.fill((255, 255, 255))  # Fondo blanco
    text = font.render(f'Valor del potenciómetro: {valorPotenciometro}', True, (0, 0, 0))
    screen.blit(text, (50, 100))
    
    # Dibujar rectángulo
    #agregar "// 2" para hacer que aumente arriba y abajo
    pygame.draw.rect(screen, (0, 120, 120), (200 - 15, 400 - valorPotenciometro, 30, valorPotenciometro), 0)
    #                           RGB                Posición                            
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
puertoSerie.close()