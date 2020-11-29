from pygame import *
from random import *

init()

width = 800
height = 600

screen = display.set_mode((width,height))

endProgram = False

x = 800
x1 = 1200
y = 100
z = 0

gravity = True
up = False
coins = True
coins1 = True
score1 = False
gamescreen = True
gameover = False

barrier1 = draw.rect(screen,(0,0,0),(0,0,800,1))
barrier3 = draw.rect(screen,(0,0,0),(0,0,3,600))
bird = draw.rect(screen,(255,255,255),(375,y,50,50))

positions = [[[x,0,75,200],[x,400,75,200]],[[x,0,75,100],[x,300,75,300]],[[x,0,75,300],[x,500,75,100]]]
positions1 = [[[x1,0,75,200],[x1,400,75,200]],[[x1,0,75,100],[x1,300,75,300]],[[x1,0,75,300],[x1,500,75,100]]]

def DrawObstacles(first,second):
	one = draw.rect(screen,(255,0,0),(positions[first][0]))
	two = draw.rect(screen,(255,0,0),(positions[first][1]))
	three = draw.rect(screen,(255,0,0),(positions1[second][0]))
	four = draw.rect(screen,(255,0,0),(positions1[second][1]))
	return
	

first = randint(0,2)
second = randint(0,2)

score = 0

while endProgram == False:
	if gamescreen == True:
		positions = [[[x,0,75,200],[x,400,75,200]],[[x,0,75,100],[x,300,75,300]],[[x,0,75,300],[x,500,75,100]]]
		positions1 = [[[x1,0,75,200],[x1,400,75,200]],[[x1,0,75,100],[x1,300,75,300]],[[x1,0,75,300],[x1,500,75,100]]]
		for e in event.get():
			if e.type == QUIT:
				endProgram = True
			if e.type == KEYDOWN:
				if e.key == K_SPACE:
					z = y
					up = True
					gravity = False
		screen.fill((0,0,0))
		if score < 100:
			font1 = font.Font(None,50)
		else:
			font1 = font.Font(None,32)
		scoretext = font1.render(str(score),True,(0,0,0))
		if up == True:
			y -= 6
			if y == (z - 84) or bird.colliderect(barrier1):
				up = False
				gravity = True
		if gravity == True:
			y += 5
				
		DrawObstacles(first,second)
		
		if score <= 10:
			x -= 3
			x1 -= 3
		if score > 10 and score <= 25:
			x -= 4
			x1 -= 4
		if score > 25 and score <= 40:
			x -= 5
			x1 -= 5
		if score > 40 and score <= 55:
			x -= 6
			x1 -= 6
		if score > 55 and score <= 70:
			x -= 7
			x1 -= 7
		if score > 70 and score <= 85:
			x -= 8
			x1 -= 8
		if score > 85 and score <= 100:
			x -= 9
			x1 -= 9
		if score > 100:
			x -= 10
			x1 -= 10
			
		bird = draw.rect(screen,(255,255,255),(375,y,50,50))
		screen.blit(scoretext,(380,y+7))
		one = draw.rect(screen,(255,0,0),(positions[first][0]))
		two = draw.rect(screen,(255,0,0),(positions[first][1]))
		three = draw.rect(screen,(255,0,0),(positions1[second][0]))
		four = draw.rect(screen,(255,0,0),(positions1[second][1]))
		barrier3 = draw.rect(screen,(0,0,0),(0,0,3,600))
		barrier4 = draw.rect(screen,(0,0,0),(0,599,800,1))
		
		if coins == True:
			coin = draw.circle(screen,(255,255,0),(x+37,positions[first][0][3]+100),20)
		else:
			coin = draw.circle(screen,(255,255,0),(5000,positions[first][0][3]+100),20)
		if coins1 == True:
			coin1 = draw.circle(screen,(255,255,0),(x1+37,positions[second][0][3]+100),20)
		else:
			coin1 = draw.circle(screen,(255,255,0),(5000,positions[second][0][3]+100),20)
			
		if coin.colliderect(bird):
			coins = False
			score1 = True

		if bird.colliderect(coin1):
			coins1 = False
			score1 = True
			
		if score1 == True:
			score += 1
			score1 = False

		if one.colliderect(barrier3):
			x = 800
			first = randint(0,2)
			coins = True

		if three.colliderect(barrier3):
			x1 = 800
			second = randint(0,2)
			coins1 = True
		
		if bird.colliderect(one) or bird.colliderect(two) or bird.colliderect(three) or bird.colliderect(four) or bird.colliderect(barrier4):
			gamescreen = False
			gameover = True
	if gameover == True:
		for e in event.get():
			if e.type == QUIT:
				endProgram = True
			if e.type == KEYDOWN:
				if e.key == K_RETURN:
					gamescreen = True
					gameover = False
					score = 0
					x = 800
					x1 = 1200
					y = 100
					z = 0

					gravity = True
					up = False
					coins = True
					coins1 = True
					score1 = False
					gamescreen = True
					gameover = False
		screen.fill((0,0,0))
		font1 = font.Font(None,75)
		scoretext = font1.render("Score: "+str(score),True,(255,255,255))
		screen.blit(scoretext,(270,200))
		
	display.flip()
