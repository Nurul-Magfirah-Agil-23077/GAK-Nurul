import pygame
import sys
import random

pygame.init()

# Ukuran layar
lebar_layar = 800
tinggi_layar = 600
layar = pygame.display.set_mode((lebar_layar, tinggi_layar))
pygame.display.set_caption("Mini Game: Kelinci Makan Wortel")

# ==============================
# LOAD GAMBAR KELINCI
# ==============================
try:
    kelinci = pygame.image.load('p7-kelinci.webp').convert_alpha()
    kelinci = pygame.transform.scale(kelinci, (100, 100))
except pygame.error as e:
    print("Error memuat kelinci.webp")
    print(e)
    sys.exit()

# ==============================
# LOAD GAMBAR WORTEL
# ==============================
try:
    wortel = pygame.image.load('wortel.png').convert_alpha()
    wortel = pygame.transform.scale(wortel, (70, 70))
except pygame.error as e:
    print("Error memuat wortel.png")
    print(e)
    sys.exit()

# Posisi awal objek
x = 100
y = 100

# Posisi awal wortel (acak)
wortel_x = random.randint(0, lebar_layar - 70)
wortel_y = random.randint(0, tinggi_layar - 70)

kecepatan = 5
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ==========================
    # KONTROL KEYBOARD
    # ==========================
    tombol = pygame.key.get_pressed()

    if tombol[pygame.K_RIGHT]:
        x += kecepatan
    if tombol[pygame.K_LEFT]:
        x -= kecepatan
    if tombol[pygame.K_DOWN]:
        y += kecepatan
    if tombol[pygame.K_UP]:
        y -= kecepatan

    # Batas layar
    x = max(0, min(x, lebar_layar - 100))
    y = max(0, min(y, tinggi_layar - 100))

    # ==========================
    # CEK TABRAKAN (Collision)
    # ==========================
    kelinci_rect = kelinci.get_rect(topleft=(x, y))
    wortel_rect = wortel.get_rect(topleft=(wortel_x, wortel_y))

    if kelinci_rect.colliderect(wortel_rect):
        # Kelinci menyentuh wortel → pindahkan wortel ke posisi random
        wortel_x = random.randint(0, lebar_layar - 70)
        wortel_y = random.randint(0, tinggi_layar - 70)

    # ==========================
    # GAMBAR SEMUA OBJEK
    # ==========================
    layar.fill((230, 230, 230))

    layar.blit(wortel, (wortel_x, wortel_y))
    layar.blit(kelinci, (x, y))

    pygame.display.flip()
    clock.tick(60)