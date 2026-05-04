import pygame
import random

pygame.init()
# Initierar Pygame själva spelet
pygame.font.init()
# Initierar Pygame fonts

#pygame.mixer.init()
# Initierar Pygame ljud (kommenterad för nu)
run = True
clock = pygame.time.Clock()
# Klocka för att styra FPS

font = pygame.font.Font('C:\Users\25dmtr\OneDrive - Stockholm Kommun\pythoncode\pythonPygameproject\Sansita-Regular (1).ttf', 50)
title_font = pygame.font.Font('C:\Users\25dmtr\OneDrive - Stockholm Kommun\pythoncode\pythonPygameproject\Sansita-Regular (1).ttf', 150)
# Laddar ett typsnitt

#pygame.mixer.music.load('')
#pygame.mixer.music.play(loops=-1)
# Laddar och startar musik i loop (kommenterad för nu)h

screen_width = 2920
screen_height = 2200
screen = pygame.display.set_mode((screen_width, screen_height))
# Skapar spelfönstret
pygame.display.set_caption('2P TRIPLE T')
# Sätter fönstertitel
icon = pygame.image.load('C:\Users\25dmtr\OneDrive - Stockholm Kommun\pythoncode\pythonPygameproject\tic-tac-toe-icon-illustration-free-vector.jpg')
pygame.display.set_icon(icon)
# Sätter fönsterikon
grip = pygame.image.load('C:\Users\25dmtr\OneDrive - Stockholm Kommun\pythoncode\pythonPygameproject\gripp (1) (1).jpg')
# Laddar bilder

cell = 280
grid_offset_x = 800
grid_offset_y = 695
# Storlek och position av spelplanens celler

cells = {i: None for i in range(9)}
grid = {}
winner = None
whos_turn = random.randint(1, 2)
# Speldata: celler, vems tur, vinnare

textfornewgame = font.render("Ny spel", True, (255, 255, 255))
textforstopgame = font.render("Stänga spel", True, (255, 255, 255))
textnewgamerect = textfornewgame.get_rect(center=(screen_width//2, screen_height//2))
textrectstop = textforstopgame.get_rect(center=(screen_width//2, screen_height//2 + 100))
# Skapar text och position för menyknappar

start_button = textnewgamerect
exit_button = textrectstop
# Lagrar knapp-rektanglar för kollisionstest

x_img = pygame.Surface((cell, cell), pygame.SRCALPHA)
pygame.draw.line(x_img, (0,0,0), (20,20), (cell-20, cell-20), 10)
pygame.draw.line(x_img, (0,0,0), (cell-20,20), (20,cell-20), 10)
# Skapar bild för X-symbol

o_img = pygame.Surface((cell, cell), pygame.SRCALPHA)
pygame.draw.circle(o_img, (0,0,0), (cell//2, cell//2), cell//2-20, 10)
# Skapar bild för O-symbol

textx = font.render("X", True, (255,0,0))
texto = font.render("O", True, (25,0,255))
textxrect = textx.get_rect(topleft=(1815, 695))
textorect = texto.get_rect(topleft=(1815, 695))
# Text som visar vems tur det är

drawn = font.render("Ingen vinner!", True, (0,0,0))
drawnrect = drawn.get_rect(topleft=(1700,1000))
tryckx = font.render("Tryck X för mainmenu", True, (0,0,0))
tryckrect = tryckx.get_rect(topleft=(1700,1200))
# Text vid oavgjort

winning_combinations = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
]
# Lista över vinnande kombinationer

text = font.render("Turn: ", True, (0,0,0))
text_rect = text.get_rect(topleft=(1700,695))
# Textlabel för "Turn"

for row in range(3):
    for col in range(3):
        index = row*3 + col
        x = grid_offset_x + col*cell
        y = grid_offset_y + row*cell
        grid[index] = pygame.Rect(x, y, cell, cell)
# Skapar rektanglar för varje cell för kollisionstest

screen_state = 1
# 1 = huvudmeny, 2 = spel, 3 = avsluta (inte använd)

def check_winner(cells):
    for combo in winning_combinations:
        a, b, c = combo
        if cells[a] == cells[b] == cells[c] and cells[a] is not None:
            return cells[a], combo  
    if all(value is not None for value in cells.values()):
        return "Draw", None
    return None, None
# Funktion för att kontrollera vinnare eller oavgjort

color = [255, 255, 255]
target_color = [255, 0, 0]
# Färg-animation för menyknappar
title_text = title_font.render("2P TicTacToe", True, (0, 255, 0))
title_rect = title_text.get_rect(center=(screen_width//2, screen_height//2.5))

while run:
    
    for i in range(3):
        if color[i] < target_color[i]:
            color[i] += 1
        elif color[i] > target_color[i]:
            color[i] -= 1
    if color == target_color:
        target_color = [random.randint(0,255) for _ in range(3)]
    # Ljus-animation för knappar

    mouse_pos = pygame.mouse.get_pos()
    # Hämta musposition

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Stäng fönster



        if event.type == pygame.KEYDOWN and winner:
            if event.key == pygame.K_x:
                cells = {i: None for i in range(9)}
                winner = None
                whos_turn = random.randint(1, 2)
                screen_state = 1
            elif event.key == pygame.K_f:
                run = False
        # Hantering av knapptryck efter vinst

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                run = False 
            # Högerklick avslutar spelet

            if screen_state == 1:
                if start_button.collidepoint(mouse_pos):
                    cells = {i: None for i in range(9)}
                    winner = None
                    whos_turn = random.randint(1, 2)
                    screen_state = 2
                elif exit_button.collidepoint(mouse_pos):
                    run = False
            # Menyknappar klickhantering

            elif screen_state == 2 and not winner:
                for index, rect in grid.items():
                    if rect.collidepoint(mouse_pos) and cells[index] is None:
                        cells[index] = "X" if whos_turn == 1 else "O"
                        whos_turn = 2 if whos_turn == 1 else 1
                        winner, winning_combo = check_winner(cells)
                # Placera X eller O i spelrutan

    if screen_state == 1:
        if start_button.collidepoint(mouse_pos):
            textfornewgame = font.render("Ny spel", True, color)
        else:
            textfornewgame = font.render("Ny spel", True, (255,255,255))

        if exit_button.collidepoint(mouse_pos):
            textforstopgame = font.render("Stänga spel", True, color)
        else:
            textforstopgame = font.render("Stänga spel", True, (255,255,255))
        
        screen.fill((0,0,0))
        screen.blit(title_text, title_rect)
        screen.blit(textfornewgame, textnewgamerect)
        screen.blit(textforstopgame, textrectstop)
    # Rita huvudmeny

    elif screen_state == 2:
        screen.fill((255,255,255))
        screen.blit(grip, (800,695))
        screen.blit(text, text_rect)
        # Rita spelplan och info

        if whos_turn == 1:
            screen.blit(textx, textxrect)
        else:
            screen.blit(texto, textorect)
        # Visa vems tur det är

        for rect in grid.values():
            pygame.draw.rect(screen, (0,0,0), rect, 3)
        # Rita cellramar

        for index, rect in grid.items():
            if cells[index] == "X":
                screen.blit(x_img, rect.topleft)
            elif cells[index] == "O":
                screen.blit(o_img, rect.topleft)
        # Rita X och O på spelplanen

        if winner:
            if winner == "Draw":
                screen.blit(drawn, drawnrect)
            else:
                won = font.render(f"Vinnare {winner}!", True, (0,0,0))
                wonrect = won.get_rect(topleft=(1700,1000))
                screen.blit(won, wonrect)
            screen.blit(tryckx, tryckrect)
            if winning_combo: 
                start_cell = grid[winning_combo[0]]
                end_cell = grid[winning_combo[2]]
                start_pos = (start_cell.x + cell//2, start_cell.y + cell//2)
                end_pos = (end_cell.x + cell//2, end_cell.y + cell//2)
                pygame.draw.line(screen, (255, 0, 0), start_pos, end_pos, 40)  
        # Visa vinnare eller oavgjort, och om det finns vinnare då strycks det linje

    pygame.display.update()
    clock.tick(60)
#pygame.mixer.music.stop()
pygame.quit()
# Avslutar spelet