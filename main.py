import pygame
import sys

print(pygame.__version__)

pygame.mixer.init()

#sound effect
audio_file = 'sound.mp3'
try:
    sound = pygame.mixer.Sound(audio_file)
    sound.set_volume(0.02)
except pygame.error as e:
    print(f"Could not load audio file: {e}")
    pygame.quit()
    sys.exit()

pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("What is wrong with you Dusty")

clock = pygame.time.Clock()

running = True

while running:
    clock.tick(144)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            try:
                sound.play()
                print("Playing audio file bruh.")
            except pygame.error as e:
                print(f"Error playing audio: {e}")

pygame.quit()
sys.exit()