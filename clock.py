import tkinter as tk
import time
import math

def update_clock():
    #秒針を消す
    canvas.delete("all")

    #時計の外枠
    canvas.create_oval(10, 10, 190, 190, outline="white", width=2)

    #現在の「秒」を取得する
    now = time.localtime()
    seconds = now.tm_sec

    #秒を角度に変換 1sec 360° / 60sec = 6°
    angle = math.radians(seconds * 6)

    #針のセンタの座標を計算。Cneter 100, 100 から長さ80の線を引く
    x = 100 + 80 * math.sin(angle)
    y = 100 - 80 * math.cos(angle)

    #秒針を描画
    canvas.create_line(100, 100, x, y, fill="White", width=2)

    #1000sec後に呼び出す
    root.after(1000, update_clock)

#Main_window
root = tk.Tk()
root.title("My Pthon Clock")
canvas = tk.Canvas(root, width=200, height=200, bg="#3a3a3a", highlightthickness=0)
canvas.pack()

update_clock()
root.mainloop()