import pygame, sys
from pygame.locals import *

pygame.init()
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

win = pygame.display.set_mode((800,600))
pygame.display.set_caption('Animation')
win.fill((255,255, 255))

menuIMG = pygame.image.load('MainMenuBackground.png')
menuIMG = pygame.transform.scale(menuIMG, (800, 600))
clearBlack75 = pygame.image.load('transpBlack75.png')
clearBlack75 = pygame.transform.scale(clearBlack75, (800, 200))

pygame.mixer.music.load('Ancient, Desert, Thoughtful Song - Non Copyright, Royalty Free.ogg')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

fontGlobal = 'Arial'

spinP=[]

for pic in range(32):
    if pic <= 9:
        spin = pygame.image.load('pyramidSpinIMG/frame_0'+ str(pic)+ '_delay-0.06s.png')
    else:
        spin = pygame.image.load('pyramidSpinIMG/frame_' + str(pic) + '_delay-0.06s.png')
    spin = pygame.transform.scale(spin, (210, 160))
    spinP.append(spin)



class button():
    def __init__(self, x, y, font, font_size, text='', boldness=False):
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.font_size = font_size
        self.boldness = boldness

    def draw(self, win, outline=None):
        font = pygame.font.SysFont(self.font, self.font_size, bold=self.boldness)
        text = font.render(self.text, 1, (255, 255, 255))
        if outline:
             pygame.draw.rect(win, outline, (self.x, self.y, text.get_width(), text.get_height()),0)

        if self.text != '':
            font = pygame.font.SysFont(self.font, self.font_size, bold=self.boldness)
            text = font.render(self.text, 1, (255, 255, 255))
            win.blit(text, (self.x, self.y))

    def isOver(self, pos):
        font = pygame.font.SysFont(self.font, self.font_size, bold=self.boldness)
        text = font.render(self.text, 1, (255, 255, 255))
        if pos[0]>self.x and pos[0] < self.x + text.get_width():
            if pos[1] > self.y and pos[1] < self.y + text.get_height():
                return True

        return False

def redrawWindow():
    startButton.draw(win)
    storeButton.draw(win)
    optionsButton.draw(win)
    objectivesButton.draw(win)
    invButton.draw(win)
    statsButton.draw(win)

run = True
startButton = button(250, 470, fontGlobal, 18, 'Start Game')
storeButton = button(250, 535, fontGlobal, 18, 'Store')
optionsButton = button(435, 470, fontGlobal, 18, 'Options')
objectivesButton = button(435, 535, fontGlobal, 18, 'Objectives')
invButton = button(620, 470, fontGlobal, 18, 'Invite Friends')
statsButton = button(620, 535, fontGlobal, 18, 'Stats')


spinCount = 0
while run:
    win.blit(menuIMG, (0, 0))
    win.blit(clearBlack75, (0, 445))
    win.blit(spinP[spinCount], (0,445))
    spinCount += 1
    if spinCount == 32:
        spinCount = 0
    redrawWindow()
    pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if startButton.isOver(pos):
                print('clicked the start button')
            if storeButton.isOver(pos):
                print('clicked the store button')
            if optionsButton.isOver(pos):
                print('clicked the options button')
            if objectivesButton.isOver(pos):
                print('clicked the objectives button')
            if invButton.isOver(pos):
                print('clicked the invite friends button')
            if statsButton.isOver(pos):
                print('clicked the stats button')

        if event .type == pygame.MOUSEMOTION:
            if startButton.isOver(pos):
                startButton.boldness = True
            elif storeButton.isOver(pos):
                storeButton.boldness = True
            elif optionsButton.isOver(pos):
                optionsButton.boldness = True
            elif objectivesButton.isOver(pos):
                objectivesButton.boldness = True
            elif invButton.isOver(pos):
                invButton.boldness = True
            elif statsButton.isOver(pos):
                statsButton.boldness = True
            else:
                startButton.boldness = False
                storeButton.boldness = False
                optionsButton.boldness = False
                objectivesButton.boldness = False
                invButton.boldness = False
                statsButton.boldness = False

