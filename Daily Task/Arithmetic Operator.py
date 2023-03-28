"""
My electricity biils for the  last three months have been $23,$32 and $64
What is the average monthly  electicity bill over the three month period ?
Write an expression to calculate the mean , and use print() to view thre result

"""

print(" Total 3 month electricity bill 23 + 32 + 64 = 119/3")
                                 #(119) / 3 = 39.66

#Use Arithmetic Operators ( + , / )


Mean= 119/3
print("Average Monthly  light bill is: ",Mean)







"""in this quiz you"re going to do some calculationn for a tiler Two parts of  a floor need tilling one  is 9 tile wide by 7  tile long.
the other is 5 tiles wide by 7 tile long tiles come in package of 6


1. how many tiles are needed
2. You buy 17 packages of tiles containing 6 tiles each .how man tile will be left over ?

"""

#The first floor of the floor has an area of 9 x 7
#The second floor of the floor has an area of 5 x 7 



# 1 - calculate total number of tiles needed

Floor1_width = 9
Floor1_length = 7
Floor1_area = Floor1_width * Floor1_length

Floor2_width = 5
Floor2_length = 7
Floor2_area = Floor2_width * Floor2_length

total_needed = Floor1_area + Floor2_area
print("total Needed tiles:",total_needed )


# 2 - calculate number of tiles left over
# Tiles come in package of 6

packages_bought = 17
total_tiles_bought = packages_bought * 6
tiles_left_over = total_tiles_bought - total_needed

print("Tiles left over:", tiles_left_over)

