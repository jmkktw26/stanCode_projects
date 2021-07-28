"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked, onmousemoved

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts
count = 0

def main():
    global graphics
    graphics = BreakoutGraphics()
    onmouseclicked(bounce)


def bounce(m):
    global NUM_LIVES
    global count
    vx = graphics.set_x_velocity()
    vy = graphics.get_vy()
    brick_n = graphics.get_brick_num()
    # Add animation loop here!
    onmouseclicked(no_interfere)
    while True:
        graphics.ball.move(vx, vy)
        graphics.check_collision()
        if graphics.check_collision() is not None:
            if graphics.check_collision() is graphics.paddle:
                vx = graphics.set_x_velocity()
                graphics.window.remove(graphics.ball)
                graphics.window.add(graphics.ball, graphics.ball.x, graphics.check_collision().y - graphics.ball.height)
                vy = -vy
            else:
                graphics.window.remove(graphics.object)
                graphics.set_x_velocity()
                count += 1
                vy = -vy
        if count == brick_n:
            onmousemoved(no_interfere)
            return None
        if graphics.ball.y + graphics.ball.height > graphics.window.height:
            NUM_LIVES -= 1
            if NUM_LIVES == 2:
                graphics.window.remove(graphics.img2)
            elif NUM_LIVES == 1:
                graphics.window.remove(graphics.img1)
            else:
                graphics.window.remove(graphics.img0)
            if NUM_LIVES > 0:
                graphics.reset_ball()
                break
            else:
                graphics.remove_ball()
                onmousemoved(no_interfere)
                break
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            vx = -vx
        if graphics.ball.y <= 0:
            vy = -vy
        # pause
        pause(FRAME_RATE)
    onmouseclicked(bounce)


def no_interfere(m):
    return

if __name__ == '__main__':
    main()