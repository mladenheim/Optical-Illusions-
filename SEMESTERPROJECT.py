import Draw

pink = Draw.color(187, 43, 149)
dark = Draw.color(100, 187, 135)
light = Draw.color(181, 217, 69)

Draw.setCanvasSize(680, 680)

# takes in color and flower center point, draws diamonds coming out of the center
# to make a flower shape
def flower(color, x, y):
  half = 10
  quart = half / 2
  eigth = quart / 2
  left = [(x, y), (x-quart, y+eigth), (x-half, y), (x-quart, y-eigth)]
  right = [(x, y), (x+quart, y+eigth), (x+half, y), (x+quart, y-eigth)]
  top = [(x, y), (x-eigth, y-quart), (x, y-half), (x+eigth, y-quart)]
  bottom = [(x, y), (x-eigth, y+quart), (x, y+half), (x+eigth, y+quart)]
  # the dimensions of the flower
  if color == "pink":
    Draw.setColor(pink)
  else:
    Draw.setColor(Draw.WHITE)
  Draw.filledPolygon(left)
  Draw.filledPolygon(right)
  Draw.filledPolygon(top)
  Draw.filledPolygon(bottom)

def squaresFlowers(rows, cols):
  x = 0
  y = 0  
  for j in range(rows):
    for i in range(cols):
      if (j + i) % 2 == 0:
        # setting every other sqaure to different colors
        Draw.setColor(light)
      else:
        Draw.setColor(dark)
      Draw.filledRect(x, y, 40, 40)
      if j != 0 and i != 0:
        v = (i - j) % 8 
        # v is configuring the pattern to the correct colors because every every 
        #set of 8 follows the same pattern so we can use mod
        if v == 0 or v == 3 or v == 5 or v == 6 or (j == 16 and i == 1):
          # pattern does not include te last row and col so the last condition 
          # was added
          flower("WHITE", x, y)
        else:
          flower("pink", x, y)
      x += 40
    y += 40
    # how far we are moving from each flower because that is the size of the squares
    x = 0  
  
def main():
  Draw.show()
  Draw.clear()
  rows = 17
  cols = 17
  squaresFlowers(rows, cols)
  
  Draw.show()

main()