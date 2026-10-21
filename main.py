import random
import pgzrun
import time
import sys

WIDTH = 1200
HEIGHT = 600

bullets = []
ship = Actor("ship")
bug = Actor("bug")
screen.bgcolor("black")

ship.pos(WIDTH//2,HEIGHT//2)
enemies = []
for i in range (8):
    for k in range (4):
        enemies.append(Actor("bug"))

enemies[-1].i = 100 + 50*i
enemies[-1].k = 80 + 50*k

score = 0
direction = 1
ship.dead = False
ship.countdown = 90
speed = 5

def display_score():
    screen.draw.text(str(score), (50,30))
    color = "white"
    
    
def game_over():
      screen.draw.text(str("game_over"), (50,50))
      color = "white"


def on_key_down(key):
    if not ship.dead:
        if key == key.space:
            bullets.append(Actor("bullets"))
            bullets[-1].x=ship.x
            bullets[-1].y=ship.y-50
            
            
def update():
    global score, direction
    move_down = False
    
    if not ship.dead:
        if keyboard.left:
            ship.x = ship.x - speed
            
        elif keyboeard.right:
            ship.x = ship.x + speed
    
    
    if ship.x <= ship.WIDTH // 2:
        ship.x = ship.WIDTH // 2
         
    elif ship.x >= ship.WIDTH // 2:
        ship.x = WIDTH - ship.WIDTH // 2
        
for bullet in bullets[:]:
    bullet.y = bullet.y - 10
    
            
        


