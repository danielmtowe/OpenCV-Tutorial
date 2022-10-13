## OpenCV - 3. Draw a shape

This article will demonstrate how to draw shapes on an image.

### Draw a straight line
Prepare a white image, such as a sheet of blank sketching paper, as illustrated below. (blank 500.jpg) Here, we will draw multiple straight lines.

Using the cv2.line(img, start, end, color, thickness, lineType) function, you may draw various lines. The stipulations are as follows:

- img: image file
- to draw from: line start coordinates (ex; (0,0))
- end: Line end coordinates (ex; (500. 500))
- color: BGR-shaped line color (ex; (255, 0, 0) -> Blue)
- thickness (int): The thickness of the line. pixel (default=1)
- lineType: Line drawing format (cv2. LINE_4, cv2. LINE_8, cv2. LINE_AA)


Note that the representation of color is BGR, not RGB. It is essential to observe that the order is opposite. When the code below is executed, several straight lines are drawn on the empty image blank 500.jpg.

```
# Draw various straight lines (draw_line.py)

import cv2

img = cv2.imread('../img/blank_500.jpg')

cv2.line(img, (50, 50), (150, 50), (255,0,0)) # blue 1-pixel line
cv2.line(img, (200, 50), (300, 50), (0,255,0)) # green 1-pixel line
cv2.line(img, (350, 50), (450, 50), (0,0,255)) # red 1-pixel line

# sky blue (blue+green) 10px line
cv2.line(img, (100, 100), (400, 100), (255,255,0), 10)
# Pink (blue+red) 10px line
cv2.line(img, (100, 150), (400, 150), (255,0,255), 10)
# yellow (green+red) 10px line
cv2.line(img, (100, 200), (400, 200), (0,255,255), 10)
# gray (blue+green+red) 10px line
cv2.line(img, (100, 250), (400, 250), (200,200,200), 10)
# black 10px line
cv2.line(img, (100, 300), (400, 300), (0,0,0), 10)

# 4 connecting wire
cv2.line(img, (100, 350), (400, 400), (0,0,255), 20, cv2.LINE_4)
#8 connecting wire
cv2.line(img, (100, 400), (400, 450), (0,0,255), 20, cv2.LINE_8)
# anti-aliasing line
cv2.line(img, (100, 450), (400, 500), (0,0,255), 20, cv2.LINE_AA)
# diagonal across the image
cv2.line(img, (0,0), (500,500), (0,0,255))

cv2.imshow('lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

LINE 4 of cv2 and cv2 If LINE 8 parameters are passed in, the pixels appear fractured. (second line from the bottom, third red) cv2.LINE AA constructs a connecting line that minimizes the stair-like effect of pixel breaking. (red line positioned at the bottom)


### Draw a rectangle

Rectangles can be drawn by using the cv2.rectangle(img, start, end, color, thickness, lineType) function. The parameters are as follows:

- img: image file
- to draw start: square start vertex coordinates (ex; (0,0))
- end: square ending vertex coordinates (ex; (500. 500))
- color: BGR-shaped line color (ex; (255, 0, 0) -> Blue)
- thickness (int): The thickness of the line. pixel (default=1, fill the entire rectangle with color=-1)
- lineType: Line drawing format (cv2. LINE_4, cv2. LINE_8, cv2. LINE_AA)

```
# Draw a rectangle (draw_rect.py)

import cv2

img = cv2.imread('../img/blank_500.jpg')

# Draw a rectangle with upper-left and lower-right coordinates, line thickness defaults to 1
cv2.rectangle(img, (50, 50), (150, 150), (255,0,0) )
# Draw a rectangle with lower right and upper left coordinates, line thickness 10
cv2.rectangle(img, (300, 300), (100, 100), (0,255,0), 10 )
# Draw a rectangle filled with upper-right and lower-left coordinates ---①
cv2.rectangle(img, (450, 200), (200, 450), (0,0,255), -1 )

cv2.imshow('rectangle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Drawing a polygon
The cv2.polylines(img, pts, isClosed, color, thickness, lineType) function can be used to draw polygons.

- img: image file
- pts: vertex coordinates to connect to, Numpy array
- isClosed: closed shape, True/False
- color: BGR-shaped line color (ex; (255, 0, 0) -> Blue)
thickness (int): The thickness of the line. pixel (default=1)
- lineType: Line drawing format (cv2. LINE_4, cv2. LINE_8, cv2. LINE_AA)

The isClosed option specifies whether a closed or open form should be drawn. If True, it draws a closed form that connects the initial and last vertices. If it is False, it draws an open shape and does not associate the first vertex with the end vertex.

```
# draw polygon (draw_poly)

import cv2
import numpy as np # numpy module for representing coordinates ---①

img = cv2.imread('../img/blank_500.jpg')

# Create coordinates with numpy array ---②
# Lightning line coordinates
pts1 = np.array([[50,50], [150,150], [100,140],[200,240]], dtype=np.int32)
# triangle coordinates
pts2 = np.array([[350,50], [250,200], [450,200]], dtype=np.int32)
# triangle coordinates
pts3 = np.array([[150,300], [50,450], [250,450]], dtype=np.int32)
# pentagonal coordinates
pts4 = np.array([[350,250], [450,350], [400,450], [300,450], [250,350]],\
                 dtype=np.int32)

# Draw polygon ---③
cv2.polylines(img, [pts1], False, (255,0,0)) # draw lightning lines
cv2.polylines(img, [pts2], False, (0,0,0), 10) # Draw triangle open lines ---④
cv2.polylines(img, [pts3], True, (0,0,255), 10) # Draw a triangle closed shape ---⑤
cv2.polylines(img, [pts4], True, (0,0,0)) # Draw a pentagon closed shape

cv2.imshow('polyline', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Draw a circle, ellipse, arc

The functions cv2.circle(img, center, radius, color, thickness, lineType) and cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness, lineType) make circles and ellipses, respectively.


The cv2.circle() function's parameters are self-explanatory. center is the coordinate of the circle's center (x,y), and radius is the circle's radius. The color is the color, the thickness is the thickness, and the lineType is the linetype. The cv2.ellipse() function's parameters can be perplexing. First and foremost, img, color, thickness, and lineType are the same as in cv2.line (). The remaining parameters are as follows:



center: the ellipse's center coordinates (x,y)

axes: the length of the longest axis in the center of the ellipse and the length of the shortest axis: the reference ellipse's angle of rotation axis start Angle: the degree of inclination



the point at which the ellipse's arc begins

endAngle: the angle at which the ellipse's arc terminates.




```
# Draw circles, ellipses, arcs (draw_circle.py)

import cv2

img = cv2.imread('../img/blank_500.jpg')

# Origin (150,150), radius 100 ---①
cv2.circle(img, (150, 150), 100, (255,0,0))
# Origin (300,150), radius 70 ---②
cv2.circle(img, (300, 150), 70, (0,255,0), 5)
# origin (400,150), radius 50, fill ---③
cv2.circle(img, (400, 150), 50, (0,0,255), -1)

# Draw origin (50,300), radius (50), rotation 0, 0 degrees to 360 degrees ---④
cv2.ellipse(img, (50, 300), (50, 50), 0, 0, 360, (0,0,255))
# Origin (150, 300), draw a semicircle below ---⑤
cv2.ellipse(img, (150, 300), (50, 50), 0, 0, 180, (255,0,0))
# Origin (200, 300), Draw the upper semicircle ---⑥
cv2.ellipse(img, (200, 300), (50, 50), 0, 181, 360, (0,0,255))

# Draw a flat ellipse with origin (325, 300), radius (75, 50) ---⑦
cv2.ellipse(img, (325, 300), (75, 50), 0, 0, 360, (0,255,0))
# Origin (450,300), Radius (50,75) Draw a slender ellipse ---⑧
cv2.ellipse(img, (450, 300), (50, 75), 0, 0, 360, (255,0,255))

# origin (50, 425), radius (50, 75), rotation 15 degrees ---⑨
cv2.ellipse(img, (50, 425), (50, 75), 15, 0, 360, (0,0,0))
# origin (200,425), radius (50,75), rotation 45 degrees ---⑩
cv2.ellipse(img, (200, 425), (50, 75), 45, 0, 360, (0,0,0))

# Origin (350,425), rotate the slender ellipse 45 degrees and draw the lower semicircle ---⑪
cv2.ellipse(img, (350, 425), (50, 75), 45, 0, 180, (0,0,255))
# Origin (400,425), rotate the slender ellipse 45 degrees and draw the upper semicircle ---⑫
cv2.ellipse(img, (400, 425), (50, 75), 45, 181, 360, (255,0,0))

cv2.imshow('circle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```


### Writing

The function cv2.putText(img, text, org, font, fontScale, color, thickness, lineType) displays a string in the picture.

Text is the string to display, org is the location to display the string (based on the bottom left) (x, y), and font is the font (cv2. FONT XXXX format), fontScale is the font size.


The code below generates the writing in a variety of fonts, sizes, and placements. The code at the bottom demonstrates how to use typefaces and italics simultaneously.


```
# Write text (draw_text.py)

import cv2

img = cv2.imread('../img/blank_500.jpg')

# sans-serif small
cv2.putText(img, "Plain", (50, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0,0))
# sans-serif normal
cv2.putText(img, "Simplex", (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0,0))
# sans-serif bold
cv2.putText(img, "Duplex", (50, 110), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0,0))
# sans-serif normall X2 ---①
cv2.putText(img, "Simplex", (200, 110), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,250))

# serif small
cv2.putText(img, "Complex Small", (50, 180), cv2.FONT_HERSHEY_COMPLEX_SMALL, \
            1, (0, 0,0))
# serif normal
cv2.putText(img, "Complex", (50, 220), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0,0))
# serif bold
cv2.putText(img, "Triplex", (50, 260), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0,0))
# serif normal X2 ---②
cv2.putText(img, "Complex", (200, 260), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,255))

# hand-wringing sans-serif
cv2.putText(img, "Script Simplex", (50, 330), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, \
            1, (0, 0,0))
# hand-wringing serif
cv2.putText(img, "Script Complex", (50, 370), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, \
            1, (0, 0,0))

# sans-serif + italic ---③
cv2.putText(img, "Plain Italic", (50, 430), \
            cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC, 1, (0, 0, 0))
# sarif + italic
cv2.putText(img, "Complex Italic", (50, 470), \
            cv2.FONT_HERSHEY_COMPLEX | cv2.FONT_ITALIC, 1, (0, 0, 0))

cv2.imshow('draw text', img)
cv2.waitKey()
cv2.destroyAllWindows()
```