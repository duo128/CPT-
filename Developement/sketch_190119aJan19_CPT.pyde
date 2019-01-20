import random
screen = "menu"
ballx = 500
bally = 300
ball_diameter = 10
xmovement = 0
ymovement = 0
ball_diameter_increase = 0
zoneX = 0
zoneY = 0
strikes = 0
balls = 0
pitches = 0
check_swing = False
score = 0
draw_frames = 0

def setup():
    global welcome
    global gonzalez
    global ichiro
    global stadium
    global wainright
    global baez
    size(1366, 768)
    welcome = loadImage("welcome.png")
    gonzalez = loadImage("gonzalez.png")
    ichiro = loadImage("ichiro.png")
    stadium = loadImage("stadium.png")
    wainright = loadImage("wainright.png")
    baez = loadImage("baez.png")
    
def draw():
    global screen, ballx, bally, ball_diameter, xmovement, ymovement, ball_diameter_increase, zoneX, zoneY, strikes, balls, pitches, check_swing, score, welcome, gonzalez, ichiro, stadium, wainright, baez
    
    if screen == "menu":
        background(0)
        imageMode(CENTER)
        image(ichiro, 220, 400, 636, 768)
        image(welcome, width/2, height/3, 960, 540)
        image(gonzalez, 1100, 390)
        fill(0)
        ellipse(1000, 400, 50, 50)
        fill(255)
        textAlign(CENTER)
        textSize(30)
        text("Press P to Play", width/2, 600)
        text("Press I for Intructions", width/2, 650)

    elif screen == "instructions":
        background(135, 206, 260)
        textSize(100)
        textAlign(CENTER)
        text("Intructions", width/2, 200)
        textSize(30)
        text("Press M to go back", width/2, 600)
        textAlign(LEFT)
        text("Controls:", 500, 300)
        text("Space Bar - Ready for Pitch", 550, 350)
        text("Right Click - Swing", 550, 400)

    elif screen == "game":
   
    #Background
        background(135, 206, 260)
        image(stadium, 600, 350)
        image(wainright, 545, 380, 113, 172)
        image(baez, 800, 350)
   
    #StrikeZone    
        stroke(255)
        fill(135, 206, 260, 0)
        rect(600, 350, 200, 250)
   
    #Baseball
        fill(255)
        noStroke()
        ellipse(ballx, bally, ball_diameter, ball_diameter)
        bally += ymovement
        ballx += xmovement
        ball_diameter += ball_diameter_increase
        if ball_diameter > 30:
            ball_diameter_increase = 0
            xmovement = 0
            ymovement = 0
        if ball_diameter <= 0:
            ballx = 500
            bally = 300
            ball_diameter = 10
            xmovement = 0
            ymovement = 0
            ball_diameter_increase = 0
   
    #Strikes
        stroke(255, 255, 0)
        strokeWeight(3)
        fill(135, 206, 260, 0)
        ellipse(1050, 100, 50, 50)
        ellipse(1150, 100, 50, 50)
        ellipse(1250, 100, 50, 50)

    #Balls
        stroke(50, 205 ,50)
        strokeWeight(3)
        fill(135, 206, 260, 0)
        ellipse(950, 175, 50, 50)
        ellipse(1050, 175, 50, 50)
        ellipse(1150, 175, 50, 50)
        ellipse(1250, 175, 50, 50)
        strokeWeight(2)
        
    #Miss/Strike
        global draw_frames
        if ball_diameter >= 30 and strikes <= 2:
            if ballx in range(600, 800) and bally in range(350, 600):        
                ballx = 500
                bally = 300
                ball_diameter = 10
                xmovement = 0
                ymovement = 0
                ball_diameter_increase = 0
                strikes += 1
                draw_frames = 60
            elif ballx not in range(600, 800) or bally not in range(350, 600):
                if check_swing == False:
                    ballx = 500
                    bally = 300
                    ball_diameter = 10
                    xmovement = 0
                    ymovement = 0
                    ball_diameter_increase = 0
                    balls += 1
                    draw_frames = 60
                if check_swing == True:
                    ballx = 500
                    bally = 150
                    ball_diameter = 10
                    xmovement = 0
                    ymovement = 0
                    ball_diameter_increase = 0
                    strikes += 1
                    draw_frames = 60
        if draw_frames > 0:
            textSize(100)
            fill(255)
            if strikes == 0 and balls == 1:
                text("COUNT 1 - 0", 500, 250)
            elif strikes == 0 and balls == 2:
                text("COUNT 2 - 0", 500, 250)
            elif strikes == 0 and balls == 3:
                text("COUNT 3 - 0", 500, 250)
            elif strikes == 1 and balls == 0:
                text("COUNT 0 - 1", 500, 250)
            elif strikes == 1 and balls == 1:
                text("COUNT 1 - 1", 500, 250)
            elif strikes == 1 and balls == 2:
                text("COUNT 2 - 1", 500, 250)
            elif strikes == 1 and balls == 3:
                text("COUNT 3 - 1", 500, 250)
            elif strikes == 2 and balls == 0:
                text("COUNT 0 - 2", 500, 250)
            elif strikes == 2 and balls == 1:
                text("COUNT 1 - 2", 500, 250)
            elif strikes == 2 and balls == 2:
                text("COUNT 2 - 2", 500, 250)
            elif strikes == 2 and balls == 3:
                text("COUNT 3 - 2", 500, 250)
            elif strikes == 3:
                text("STRIKE 3", 500, 250)
            elif balls == 4 and strikes == 0:
                text("WALK", 500, 250)
                draw_balls(950, 175)
                draw_balls(1050, 175)
                draw_balls(1150, 175)
                draw_balls(1250, 175)
            elif balls == 4 and strikes == 1:
                text("WALK", 500, 250)
                draw_balls(950, 175)
                draw_balls(1050, 175)
                draw_balls(1150, 175)
                draw_balls(1250, 175)
                draw_strikes(1050, 100)
            elif balls == 4 and strikes == 2:
                text("WALK", 500, 250)
                draw_balls(950, 175)
                draw_balls(1050, 175)
                draw_balls(1150, 175)
                draw_balls(1250, 175)
                draw_strikes(1050, 100)
                draw_strikes(1150, 100)
            draw_frames -= 1
        else:
        #BALLFOUR
            if balls == 4:
                balls = 0
                strikes = 0
        
        if draw_frames != 61:
            textSize(100)
            fill(255)
            if strikes == 0 and balls == 1:
                draw_balls(950, 175)
            elif strikes == 0 and balls == 2:
                draw_balls(950, 175)
                draw_balls(1050, 175)
            elif strikes == 0 and balls == 3:
                draw_balls(950, 175)
                draw_balls(1050, 175)
                draw_balls(1150, 175)
            elif strikes == 1 and balls == 0:
                draw_strikes(1050, 100)
            elif strikes == 1 and balls == 1:
                draw_strikes(1050, 100)
                draw_balls(950, 175)
            elif strikes == 1 and balls == 2:
                draw_strikes(1050, 100)
                draw_balls(950, 175)
                draw_balls(1050, 175)
            elif strikes == 1 and balls == 3:
                draw_strikes(1050, 100)
                draw_balls(950, 175)
                draw_balls(1050, 175)
                draw_balls(1150, 175)
            elif strikes == 2 and balls == 0:
                draw_strikes(1050, 100)
                draw_strikes(1150, 100)
            elif strikes == 2 and balls == 1:
                draw_strikes(1050, 100)
                draw_strikes(1150, 100)
                draw_balls(950, 175)
            elif strikes == 2 and balls == 2:
                draw_strikes(1050, 100)
                draw_strikes(1150, 100)
                draw_balls(950, 175)
                draw_balls(1050, 175)
            elif strikes == 2 and balls == 3:
                draw_strikes(1050, 100)
                draw_strikes(1150, 100)
                draw_balls(950, 175)
                draw_balls(1050, 175)
                draw_balls(1150, 175)
            elif strikes == 3 and balls == 0:
                draw_strikes(1050, 100)
                draw_strikes(1150, 100)
                draw_strikes(1250, 100)
            elif strikes == 3 and balls == 1:
                draw_strikes(1050, 100)
                draw_strikes(1150, 100)
                draw_strikes(1250, 100)
                draw_balls(950, 175)
            elif strikes == 3 and balls == 2:
                draw_strikes(1050, 100)
                draw_strikes(1150, 100)
                draw_strikes(1250, 100)
                draw_balls(950, 175)
                draw_balls(1050, 175)
            elif strikes == 3 and balls == 3:
                draw_strikes(1050, 100)
                draw_strikes(1150, 100)
                draw_strikes(1250, 100)
                draw_balls(950, 175)
                draw_balls(1050, 175)
                draw_balls(1150, 175)
           
    #Zone
        noStroke()
        fill(255, 200)
        zoneX = mouseX
        zoneX = constrain(zoneX, 600, 800)
        zoneY = mouseY
        zoneY = constrain(zoneY, 350, 600)
        ellipse(zoneX, zoneY, 100, 100)
   
    #Score
        fill(255)
        textAlign(LEFT)
        textSize(50)
        text("Score: " + str(score), 50, 100)
    
    #Pitches
        textSize(50)
        text("Pitches: " + str(pitches), 50, 170)
    
    #GameOver
        if strikes == 3:
            screen = "gameover"
    
    elif screen == "gameover":
        filter(BLUR, 6)
        textSize(100)
        textAlign(CENTER)
        text("Game Over!", width/2, height/2)
        textSize(30)
        text("Press R to Retry", width/2, 500)
        text("Press M to return to Menu", width/2, 550)
 
def draw_strikes(x, y):
    noStroke()
    fill(255, 255, 0)
    ellipse(x, y, 50, 50)
 
def draw_balls(x, y):
    noStroke()
    fill(50, 205 ,50)
    ellipse(x, y, 50, 50)
 
def mousePressed():
    global screen, ballx, bally, ball_diameter, xmovement, ymovement, ball_diameter_increase, zoneX, zoneY, strikes, balls, pitches, score
 
#timing is based on baseball size at time of swing
 
#Swing
    check_swing = True
 
#Contact
    if dist(mouseX, mouseY, ballx, bally) < 30:
        if ball_diameter >= 12 and ball_diameter <= 25:
            xmovement = random.randint(-10, -2)
            ymovement = -10
            ball_diameter_increase = -1.2
            score += 200
        if ball_diameter >= 26 and ball_diameter <= 29:
            xmovement = random.randint(2, 10)
            ymovement = -16
            ball_diameter_increase = -1.2
            score += 200
    elif dist(mouseX, mouseY, ballx, bally) < 50:
        if ball_diameter >= 12 and ball_diameter <= 25:
            xmovement = -10
            ymovement = 2
            ball_diameter_increase = -1
            score += 100
        if ball_diameter >= 25 and ball_diameter <= 29:
            xmovement = 10
            ymovement = -3
            ball_diameter_increase = -1
            score += 100
 
def keyPressed():
    global screen, ballx, bally, ball_diameter, xmovement, ymovement, ball_diameter_increase, zoneX, zoneY, strikes, balls, pitches, score

    if screen == "menu":
        if key == "i":
            screen = "instructions"
        if key == "p":
            screen = "game"
    if screen == "instructions":
        if key == "m":
            screen = "menu"
    if screen == "gameover":
        if key == "r":
            screen = "game"
            strikes = 0
            balls = 0
            score = 0
            pitches = 0
        if key == "m":
            screen = "menu"
    
    if screen == "game":
        if keyCode == 32:
            if ball_diameter == 10:
                if strikes < 3 and draw_frames <= 0:
                    ballx = 500
                    bally = 300
                    ball_diameter = 10
                    xmovement = random.randint(3, 10)
                    ymovement = random.randint(4, 8)
                    ball_diameter_increase = 0.5
                    pitches += 1
                    check_swing = False
                    if pitches > 25:
                        ball_diameter_increase = 1
                        xmovement = random.randint(5, 12)
                        ymovement = random.randint(4, 18)
                    elif pitches > 20:
                        ball_diameter_increase = 0.9
                        xmovement = random.randint(5, 12)
                        ymovement = random.randint(4, 16)
                    elif pitches > 15:
                        ball_diameter_increase = 0.8
                        xmovement = random.randint(4, 12)
                        ymovement = random.randint(4, 14)
                    elif pitches > 10:
                        ball_diameter_increase = 0.7
                        xmovement = random.randint(3, 10)
                        ymovement = random.randint(4, 12)
                    elif pitches > 5:
                        ball_diameter_increase = 0.6
                        xmovement = random.randint(3, 10)
                        ymovement = random.randint(4, 10)
