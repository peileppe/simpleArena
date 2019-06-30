#!/usr/bin/python
# sa_menu.py 
# ===================================================================
import pygame, time

def set_Display( w,c,f ):
    global winDisplay
    global clock
    global Font
    winDisplay=w
    clock=c
    Font=f
    return

def show_Zone(color, x, y, wh, hh):
    pygame.draw.rect(winDisplay, color, [x, y, wh, hh])
    return

def show_Text(msg, y=0, x=0, color= (205,205,205), wh=100):
    global Font
    black = (10,10,10)
    show_Zone(color, x,y,wh,15)
    font = pygame.font.SysFont(None, 25)
    text = font.render(msg, True, black)
    winDisplay.blit(text,(x,y))
    y+=Font.get_height()
    pygame.display.update()
    return y, x

def menu_loop(menu):
    global winDisplay
    global black
    global red
    global blue
    global white
    white = (205,205,205)
    global Font
    Font = pygame.font.Font(None, 26)
    black = (10,10,10)
    red = (195,110,50)
    blue = (105,175,205)
    menuExit = False
    posx = 50
    posy = 55
    r=0
    num_menu=[]
    for i in range(len(menu)):
        num_menu.append(48+i)
    while not menuExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    r-=1
                if event.key == pygame.K_DOWN:
                    r+=1
                if event.key in (13, 32):
                    menuExit=True
                if event.key in (27, 113):
                    r=len(menu)-1
                    menuExit=True
                if event.key in num_menu:
                    r=event.key-48
                    menuExit=True
        if r<=0: r=0
        if r>=len(menu):r=0
        pygame.draw.rect(winDisplay, black , [posx, posy, len(max(menu,key=len))*8+40, 15*len(menu)+10])
        r=display_menu(posx+5,posy+5,menu,r)
        clock.tick(5)
    return r, menu[r]

def display_menu(x1,y1,menu1, current_option):
    wh=len(max(menu1,key=len))*8+30
    for i,o in enumerate(menu1):
        o=str(i)+". "+o
        if i==current_option:
            show_Text(o,y1,x1,white,wh)
        else:
            show_Text(o,y1,x1,blue, wh)
        y1+=15
    return current_option

def main():
    global winDisplay
    global clock
    global white
    global Font
    pygame.init()
    Font = pygame.font.Font(None, 26)
    display_width = 800
    display_height = 600
    winDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('mokinator')
    white = (205,205,205)
    winDisplay.fill(white)
    clock = pygame.time.Clock()
    i=[0,'new']
    turn=0
    MENU=['new','load','save','combat','help','Quit']
    while i[1] != ('Quit'):
        i=menu_loop(MENU)
        turn+=1
    pygame.quit()
    quit()
    return

if __name__ == "__main__":
    main()

