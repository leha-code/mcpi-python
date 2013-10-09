#!/usr/bin/env python

# mcpipy.com retrieved from URL below, written by  Jason Milldrum, NT7S
# http://www.nt7s.com/blog/2013/02/exploring-minecraft-pi-edition/

import mcpi.block as block



def sphere(mc):
	mc.postToChat("Hallo, here's your sphere")
	
	radius = 6
	
	playerPos = mc.player.getPos()
	
	for x in range(radius*-1,radius):
		for y in range(radius*-1, radius):
			for z in range(radius*-1,radius):
				if x**2 + y**2 + z**2 < radius**2:
					mc.setBlock(playerPos.x + x, playerPos.y + y + radius, playerPos.z - z - 10, block.GOLD_BLOCK)

if __name__ == "__main__":
	import server
	sphere(server.mc)