import random

SIZE = 96
WIDTH = SIZE * 3
HEIGHT = SIZE * 3
finished = False # 是否完成拼图

# 图片列表
pics = []
for i in range(8):
    pic = Actor("puzzle_pic" + str(i))
    pic.index = i
    pics.append(pic)

random.shuffle(pics)
for i in range(8):
    pics[i].left = i % 3 * SIZE
    pics[i].top = i // 3 * SIZE

# 最后一块图
lastpic = Actor("puzzle_pic8", (2*SIZE+48,2*SIZE+48))

def draw():
    screen.fill((255, 255, 255))
    for pic in pics:
        pic.draw()
    if finished:
        lastpic.draw()
        screen.draw.text("FINISH!!!", center=(WIDTH//2, HEIGHT//2), fontsize=50, color="red")

def update():
    global finished
    if finished:
        return
    for i in range(8):
        pic = get_pic(i % 3, i // 3)
        if pic is None or pic.index != i:
            return
    finished = True
    sounds.win.play()

def on_mouse_down(pos):
    if finished:
        return
    grid_x = pos[0] // SIZE
    grid_y = pos[1] // SIZE
    if get_pic(grid_x, grid_y) is None:
        return
    thisPic = get_pic(grid_x, grid_y)
    # 判断图片是否可以向上移动
    if grid_y > 0 and get_pic(grid_x, grid_y - 1) is None:
        thisPic.y -= SIZE
        return
    # 判断图片是否可以向下移动
    if grid_y < 2 and get_pic(grid_x, grid_y + 1) is None:
        thisPic.y += SIZE
        return
    # 判断图片是否可以向左移动
    if grid_x > 0 and get_pic(grid_x - 1, grid_y) is None:
        thisPic.x -= SIZE
        return
    # 判断图片是否可以向右移动
    if grid_x < 2 and get_pic(grid_x + 1, grid_y) is None:
        thisPic.x += SIZE
        return
    
# 获取图片，参数为水平和垂直索引值
def get_pic(grid_x, grid_y):
    for pic in pics:
        if pic.x // SIZE == grid_x and pic.y // SIZE == grid_y:
            return pic
    return None