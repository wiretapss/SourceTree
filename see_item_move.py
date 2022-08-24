###Hero sees item and moves to it's coord
item = hero.findNearestItem()
if item:
	pos = item.pos
	x = pos.x
	y = pos.y
	hero.moveXY(x, y)
#cleaner version
item = hero.findNearestItem
if item and item.type == "coin":
    hero.moveXY(item.pos.x, item.pos.y)