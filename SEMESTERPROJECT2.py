import Draw
import math

Draw.setCanvasSize(850, 550)

def _rotatePoint(x, y, angle):
    r = math.sqrt(x*x + y*y)
    theta = math.atan2(y, x)
    theta += angle
    newx = math.cos(theta) * r
    newy = math.sin(theta) * r
    return newx, newy

def filledPartialOval(x, y, wide, high, degStart, degEnd, rot):
    coords = []
    rot = math.radians(rot)
    
    for angle in range(degStart, degEnd+1, 1):
        rad = math.radians(angle)
        newx = math.cos(rad) * wide/2
        newy = math.sin(rad) * high/2

        newx, newy = _rotatePoint(newx, newy, rot)
        coords += [x+newx, y-newy]
        
    Draw.filledPolygon(coords)
    
def border(x, y, width, height, col):
    # draws the border around the circles in different colors depending on rotation
    if col >= 8 and col <= 15:  rot = [0,180]
    else:   rot = [180,0]
    Draw.setColor(Draw.BLACK)
    filledPartialOval(x + width / 2 - 1, y + height / 2 - 1, width + 4, height + 4, 90, 270, rot[1])
    Draw.setColor(Draw.WHITE)
    filledPartialOval(x + width/2, y + height / 2 - 1, width + 4, height + 4, 90, 270, rot[0])   

    
def circles(rows, cols):
    for row in range(rows):
        x = 20
        # how far left the circles start from the border
        for col in range(cols):
            # for each of the three rollers, the width was same and is dependent
            # how far from the middle each circle is within its set of 8
            if col % 8 == 7 or col % 8 == 0:
                width = 8
            elif col % 8 == 1 or col % 8 == 6:
                width = 13
            elif col % 8 == 2 or col % 8 == 5:
                width = 18
            else:
                width = 28
            height = 50
    
  
            y = (row)*(height+15) + 20
            # 20 is how far from the top the circles start
            # rest of "y" is how far the frpm the above circle the new one is drawn
    
    
            border(x, y, width+2, height, col) 
            Draw.setColor(blue)
    
            Draw.filledOval(x+1, y, width, height)
    
            x += (width*2)
            # spacing between circles depends on how wide the previous circle is     

def main():
    Draw.show()
    Draw.clear()
    Draw.setBackground(greenYellow)
    rows = 8
    cols = 24
    circles(rows, cols)
    
    Draw.show()

greenYellow = Draw.color(211, 209, 68)
blue = Draw.color(33, 105, 245)
        
main()