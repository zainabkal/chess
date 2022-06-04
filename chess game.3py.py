import pygame
import os
import time
from client import Network
import pickle
pygame.font.init()

board = pygame.transform.scale(pygame.image.load(os.path.join('img','board_alt.png')), (750,750))
chessbg=pygame.image.load(os.path.join('img','chess.png'))
rect=(113,113,525,525)

turn = "w"

def menu_screen(win, name):
    global bo,chessbg
    run = True
    offline = False

    while run:
        win.blit(chessbg, (0,0))
        small_font= pygame.font.SysFont("comicsans",50)

if offline:
           off = small_font.render("Server Offline, Try Again Later...",1,(255,0,0))
           win.blit(off, (width/2-off.getwidth()/2,500))

pygame.display.update()

for event in pygame.event.get():
         if event.type == pygame.Quit:
                        pygame.quit()
                        run = False

if event.type==pygame.MOUSEBUTTONDOWN:
                        offline = False
                        try:
                            bo=connect()
                            run = False
                            main()
                            break
                        except:
                            print("Server Offline")
                            offline = True

        def redraw_gamewindow(win,bo,p1,p2,color,ready):
             win.blit (board,(0,0))
             bo.draw (win,color)

             formatTime1= str(int(p1//60)) + ":" + str(int(p1%60))
             formatTime2 = str(int(p2//60)) + ":" + str(int(p2%60))
             if int(p1%60) < 10:
                 formatTime1 = formatTime[:-1] + "0" + formatTime[-1]
             if int(p2%60) < 10:
                 formatTime2 = formatTime2[:-1] + "0" + formatTime[-1]

             font = pygame.font.SysFont('comicsans', 30)
             try:
                 txt = font.render(bo.p1Name + "\'s Time: " + str(formatTime2), 1 ,(255,255,255))
                 txt2 = font.render(bo.p2Name + "\'s Time: " +str(fomatTime1), 1,(255,255,255)
             except Exception as e:
                 print(e)
             win.blit(txt, (520,10))
             win.blit(txt2, (520,700))

             txt = font.render("Press q to quit", 1, (255,255,255))
             win.blit(txt, (10,20))

             if color == "s":
                 txt3 = font.render("SPECTATOR MODE", 1,(255,0,0))
                 win.blit(txt3,(width/2-txt3.get_width()/2,10))

              if not ready:
                  show = "Waiting for Player"
                  if color == "s"
                     show = "Waiting for players"
                  font= pygame.font.SysFont("comicsans", 80)
                  txt = font.render(show,1,(255,0,0))
                  win.blit(txt, (width/2 - txt.get_width()/2, 300))

                if not color =="s":
                    font = pygame.font.SysFont("comicsans",30)
                    if color =="w":
                        txt3 = font.render("YOU ARE WHITE",1,(255,0,0))
                        win.blit(txt3, (width/2 - txt3.get_width()/2,10))
                    else:
                        txt3= font.render("YOU ARE BLACK", 1 , (255,0,0))
                        win.blit(txt3, (width/2 - txt3.get_width()/2,10))

                    if bo.turn == color:
                        txt3 = font.render("YOUR TURN", 1, (255,0,0))
                        win.blit(txt3, (width/2 - txt3.get_width()/2,700))

                    else:
                        txt3= font.reader("THEIR TURN, 1,(255,0,0))
                        win.blit(txt3, (width/2 - txt3.get_width()/2,700))


                    pygame.display.update()


def end_screen(win,text):
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 80)
    txt = font.render(text,1,(255,0,0))
    win.blit(txt, (width/2 - txt.get_width()/2, 300))
    pygame.display.update()

    pygame.time.set_timer(pygame.USEREVENT+1, 3000)

     run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                run = False
            elif event.type == pygame.KEYDOWN:
                run = False
            elif event.type == pygame.USEREVENT+1:
                run = False
    










                  










                            













            
                                   








                            
    


















        
