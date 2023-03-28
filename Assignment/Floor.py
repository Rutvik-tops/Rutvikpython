"""in this quiz you"re going to do some calculationn for a tiler Two parts of  a floor need tilling one  is 9 tile wide by 7  tile long.
the other is 5 tiles wide by 7 tile long tiles come in package of 6


1. how many tiles are needed
2. You buy 17 packages of tiles containing 6 tiles each .how man tile will be left over ?

"""

FW1=9
FL1=7

Total1=FW1*FL1

print("Floor 1 Total tiles : ",Total1)


FW2=5
FL2=7

Total2=FW2*FL2

print("Floor 2 Total tiles : ",Total2)



Tiles= Total1 + Total2
print("Two Floor Total tiles : " , Tiles)

Buy_tiles = 17 * 6

print(Buy_tiles)

Home=Buy_tiles - Tiles
print("Left over tiles",Home)
