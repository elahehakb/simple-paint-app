from graphics import *
import random
import time

def main():
    win = GraphWin("🎨 Paint - working version", 800, 500)
    win.setBackground("white")

    colors = ["black", "red", "blue", "green", "purple", "orange"]
    current_color = "black"
    pen_size = 3

    info = Text(Point(400, 20),
        "Click & drag to draw • C=color • +/-=size • X=clear • Q=quit")
    info.setSize(10)
    info.draw(win)

    last_point = None
    win.flush()  # make sure window updates correctly

    while True:
        key = win.checkKey()
        point = win.checkMouse()

        # if user clicked somewhere
        if point:
            # user pressed mouse down → start drawing
            last_point = point

            # keep drawing while mouse button held down
            while True:
                new_point = win.checkMouse()
                key_inner = win.checkKey()

                if key_inner == "q":
                    win.close()
                    return
                elif key_inner == "c":
                    current_color = random.choice(colors)
                    info.setText(f"Color: {current_color} • Size: {pen_size}")
                elif key_inner in ["equal", "plus"]:
                    pen_size = min(20, pen_size + 1)
                    info.setText(f"Color: {current_color} • Size: {pen_size}")
                elif key_inner == "minus":
                    pen_size = max(1, pen_size - 1)
                    info.setText(f"Color: {current_color} • Size: {pen_size}")
                elif key_inner == "x":
                    for item in win.items[:]:
                        if isinstance(item, Line):
                            item.undraw()

                if not new_point:
                    time.sleep(0.01)
                    continue

                line = Line(last_point, new_point)
                line.setWidth(pen_size)
                line.setOutline(current_color)
                line.draw(win)
                last_point = new_point

                # stop drawing if mouse released (no new clicks)
                if not win.checkMouse():
                    break

        # exit if pressed q outside loop
        if key == "q":
            break

    win.close()

if __name__ == "__main__":
    main()
