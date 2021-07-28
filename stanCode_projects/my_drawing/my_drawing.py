"""
File:my-drawing
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    window = GWindow(width=1000, height=500, title='robot')
    face = GRect(200, 125, x=400, y=125)
    face.filled = True
    face.fill_color = 'limegreen'
    window.add(face)

    l_eye = GOval(50, 50, x=430, y=140)
    l_eye.filled = True
    l_eye.fill_color = 'yellow'
    window.add(l_eye)

    r_eye = GOval(50, 50, x=520, y=140)
    r_eye.filled = True
    r_eye.fill_color = 'yellow'
    window.add(r_eye)

    mouth = GLine(450, 230, 550, 230)
    mouth.filled = True
    mouth.fill_color = 'red'
    window.add(mouth)

    head = GLine(500, 60, 500, 125)
    window.add(head)

    head_circle = GOval(30, 30, x=485, y=50)
    head_circle.filled = True
    head_circle.fill_color = 'red'
    window.add(head_circle)

    triangle = GPolygon()
    triangle.add_vertex((400, 160))
    triangle.add_vertex((400, 220))
    triangle.add_vertex((350, 190))
    triangle.filled = True
    triangle.fill_color = 'green'
    window.add(triangle)

    triangle = GPolygon()
    triangle.add_vertex((600, 160))
    triangle.add_vertex((600, 220))
    triangle.add_vertex((650, 190))
    triangle.filled = True
    triangle.fill_color = 'green'
    window.add(triangle)

    body = GRect(125, 125, x=440, y=250)
    body.filled = True
    body.fill_color = 'limegreen'
    window.add(body)

    word = GLabel('SC101', x=460, y=330)
    word.font = '-30'
    window.add(word)

    l_hand = GLine(440, 300, 390, 330)
    window.add(l_hand)

    l_circle = GOval(30, 30, x=370, y=320)
    l_circle.filled = True
    l_circle.fill_color = 'red'
    window.add(l_circle)

    r_hand = GLine(565, 300, 615, 330)
    window.add(r_hand)

    r_circle = GOval(30, 30, x=595, y=320)
    r_circle.filled = True
    r_circle.fill_color = 'red'
    window.add(r_circle)

    l_leg = GLine(480, 375, 440, 450)
    window.add(l_leg)

    l_leg_circle = GOval(30, 30, x=420, y=445)
    l_leg_circle.filled = True
    l_leg_circle.fill_color = 'red'
    window.add(l_leg_circle)

    r_leg = GLine(525, 375, 570, 450)
    window.add(r_leg)

    r_leg_circle = GOval(30, 30, x=560, y=445)
    r_leg_circle.filled = True
    r_leg_circle.fill_color = 'red'
    window.add(r_leg_circle)


if __name__ == '__main__':
    main()




