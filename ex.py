from tkinter import *
from time import sleep
from PIL import ImageTk, Image

img = [0, 0, 0]

game = Tk()
game.title('Dino Jump')

canvas = Canvas(master=game, width=600, height=300, background='black')
canvas.pack()

img[0] = ImageTk.PhotoImage(Image.open("dino.png"))
img[1] = ImageTk.PhotoImage(Image.open("cloud.png"))
img[2] = ImageTk.PhotoImage(Image.open("trees.png"))

text = canvas.create_text(200, 100, text='', fill='blue', font=('Times', 20))

dino = canvas.create_image(0, 250, anchor=NW, image=img[0])
cloud = canvas.create_image(550, 80, anchor=NW, image=img[1])
tree = canvas.create_image(550, 260, anchor=NW, image=img[2])


def color():
    canvas.itemconfig(rect, fill='blue')
    canvas.update()


def config_text():
    canvas.itemconfig(text, text='Game Over')
    canvas.update()

def moveCloud():
    global cloud
    canvas.move(cloud, -5, 0)
    if canvas.coords(cloud)[0] < -20:
        canvas.delete(cloud)
        cloud = canvas.create_image(550, 80, anchor=NW, image=img[1])
    canvas.update()


check_jump = False
score = 0
text_score = canvas.create_text(550, 50, text="Score : " + str(score), fill='red', font=('Times', 15))


def jump():
    global check_jump
    if check_jump == False:
        check_jump = True
        for i in range(40):
            canvas.move(dino, 0, -5)
            moveCloud()
            moveTree()
            canvas.update()
            sleep(0.01)

        for i in range(40):
            canvas.move(dino, 0, 5)
            moveCloud()
            moveTree()
            canvas.update()
            sleep(0.01)
        check_jump = False


def moveTree():
    global tree, score, text_score
    canvas.move(tree, -3, 0)
    if canvas.coords(tree)[0] < -20:
        score += 1
        canvas.itemconfig(text_score, text="Score : " + str(score))
        canvas.delete(tree)
        tree = canvas.create_image(550, 260, anchor=NW, image=img[2])
    canvas.update()


def keyPress(event):
    if event.keysym == 'space':
        jump()


canvas.bind_all("<KeyPress>", keyPress)

gameOver = False


def check_gameOver():
    global gameOver, score, text_score
    coords_tree = canvas.coords(tree)
    coords_dino = canvas.coords(dino)

    if coords_dino[1] > 200 and coords_tree[0] < 50:
        gameOver = True
        config_text()
        score = 0
    game.after(100, check_gameOver)


while not gameOver:
    check_gameOver()
    moveCloud()
    moveTree()
    sleep(0.01)

game = mainloop()
