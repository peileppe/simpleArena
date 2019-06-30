#!/usr/bin/python3
# simpleArena (pygame)
# ===================================================================
import pygame
import random
import shelve
import sa_menu

class unit(object):
    def __init__(self, lbl = 'name', vl = 0):
        self.name=lbl # name
        self.hp=vl # hit points 
        self.mxvalue=vl # max hp
        return
    def display(self):
        return self.name+' '+str(self.hp)

class opponent(unit):
    def __init__(self, lbl, vl):
        l=(1,2,3)
        self.level = random.choice(l)
        unit.__init__(self, lbl, vl*self.level)
        return
    def damage(self):
        d=(5,6,7)
        dmg=random.choice(d)*self.level
        sa_menu.show_Text('D:'+str(dmg),460,400)
        pygame.display.update()
        return dmg
    def show(self):
        bgc=(105,175,205)
        sa_menu.show_Zone(bgc,380,350,250,150)
        sa_menu.show_Text('MONSTER:'+self.name,370,400,(200,200,200),200)
        sa_menu.show_Text('HP',400,400)
        sa_menu.show_Text('LV',400,440)
        sa_menu.show_Text(str(self.hp),430,400)
        sa_menu.show_Text(str(self.level),430,440)
        pygame.display.update()
        return
    
class hero(unit):
    def __init__(self, lbl, vl):
        unit.__init__(self, lbl,vl)
        self.level = 0
        self.xp = 0
        self.name_pos=(170,400)
        self.hp_pos=(230,400)
        self.level_pos=(230,420)
        self.xp_pos=(230,440)
        self.txt_pos=(230,440)
        self.live=True
        return
    def levelUp(self):
        self.level=int(self.xp/10)
        self.hp=int(self.level)*4+self.mxvalue
        return
    def damage(self):
        d=(5,6,7)
        dmg=random.choice(d)*(self.level+1)
        sa_menu.show_Text('D:'+str(dmg),260,400)
        pygame.display.update()
        return dmg
    def show(self):
        bgc=(105,175,205)
        sa_menu.show_Zone(bgc,380,150,250,150)
        sa_menu.show_Text('NAME:'+self.name,170,400,(200,200,200),200)
        sa_menu.show_Text('HP',200,400)
        sa_menu.show_Text('LV',200,440)
        sa_menu.show_Text('XP',200,480)
        sa_menu.show_Text(str(self.hp),230,400)
        sa_menu.show_Text(str(self.level),230,440)
        sa_menu.show_Text(str(self.xp),230,480)
        pygame.display.update()
        return

def New():
    global h
    global n
    h = hero('Hero-'+str(n),30)
    return h

def Load():
    global h #super important!
    db=shelve.open('saves/sa_saves')
    h=db['Hero']
    db.close()
    return('load')

def Save():
    db=shelve.open('saves/sa_saves')
    db['Hero']=h
    db.close()
    return('Save')

def Display():
    r=h.display()+' '+str(h.level)
    return r

def Fight():
    global h
    global dead
    global listm
    opponent_l=('gladiator','troglodyte','orc','barbarian')
    o=opponent(random.choice(opponent_l),8)
    roundr=1
    while o.hp>=0 and roundr<10:
        o.show()
        if (h.hp<=0):
            h.live=False
            return 'Hero is dead'
        else:
            h.xp+=1
            o.hp-=h.damage()
            h.hp-=o.damage()
        roundr+=1
    dead+=1
    listm.append(o.name+' is dead')
    h.levelUp()
    return 

def Quit():
    return('Bye')

def main():
    pygame.init()
    display_width = 800
    display_height = 600
    winDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('simple Arena')
    Font = pygame.font.Font(None, 26)
    white = (205,205,205)
    winDisplay.fill(white)
    clock = pygame.time.Clock()
    sa_menu.set_Display(winDisplay, clock, Font)
    turn = 0
    i = (0,'?')
    global n
    n=0
    global h
    h=New()
    global dead
    dead=0
    global listm
    listm=[]
    MENU= ['New','Load','Save','Display','Fight','Quit']
    CMD = [New,Load,Save,Display, Fight, Quit]
    while i[1] != ('Quit'):
        h.show()
        i=sa_menu.menu_loop(MENU)
        CMD[i[0]]()
        if(h.live==False):
                n+=1
                h=New()
        turn+=1
        sa_menu.show_Text('Turn'+str(turn),100,400)
        #pygame.display.update()
    pygame.quit()
    for i in (listm):
        print(i)
    quit()
    return

if __name__ == "__main__":
    main()

