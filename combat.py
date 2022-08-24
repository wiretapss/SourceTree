### Generic Combat with flags
while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()

    if flag:
        # What happens when I find a flag?
        flagPos = flag.pos
        flagX = flagPos.x
        flagY = flagPos.y
        hero.moveXY(x, y)
        hero.pickUpFlag(flag)
    elif enemy:
        # What happens when I find an enemy?
        if hero.isReady("power-up"):
            hero.powerUp(enemy)
        else:
            hero.attack(enemy)