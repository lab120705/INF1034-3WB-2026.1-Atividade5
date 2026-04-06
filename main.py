from pygame import *
import sys

init()

spider_png = image.load("spider.png")

spider_png = transform.scale(spider_png, (100, 0))

spider_font = font.Font("spiderfont.ttf", 50)

mixer.music.load("spiderman-web-sound-effect.mp3")
mixer.music.play(-1)

window = display.set_mode((1200, 720))

window.fill((0, 0, 0))

while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
        
    #DESENHAR A PARTIR DAQUI


    draw.rect(window, (255, 0, 0), (200, 200, 200, 200), 0)
    draw.circle(window, (20, 50, 20), (500, 600), 200)
    draw.polygon(window, (0, 255, 0), ((200, 300), (250, 150), (300, 300)))
    draw.line(window, (255,0, 0), (100, 100), (200, 200), 3)

    #DESENHAR IMAGEM
    window.blit(spider_png, (-50, 0))



    display.update()
