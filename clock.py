import tkinter as tk
import time
import math

def update_clock():
    #秒針を消す
    canvas.delete("all")
    
    #現在の「秒」を取得する
    now = time.localtime()
    h = now.tm_hour % 12
    m = now.tm_min
    s = now.tm_sec

    #中心点
    cx, cy = 125, 125

    #ロドスぽくデザイン
    #デジタル時計を配置
    current_time_str = f"{now.tm_hour:02}:{now.tm_min:02}:{now.tm_sec:02}"
    canvas.create_text(125, 180, text=current_time_str, fill="#00ffff", font=("Lucida Console", 10, "bold"))
    # PRTS: CONNECTED を左上に配置
    canvas.create_text(55, 10, text="PRTS: CONNECTED", fill="#474b4b", font=("Lucida Console", 8))

    #右下に日付を配置
    date_str = time.strftime("%Y/%m/%d")
    canvas.create_text(210, 240, text=date_str, fill="#474b4b", font=("Lucida Console", 8))
    #ロドスアイランドの文字を配置
    canvas.create_text(125, 125, text="RHODES\nISLAND", fill="#474b4b", font=("Times New Roman", 28, "bold"), justify="center")

    #デザインPRTS風
    r_frame = 110
    big_rhombus = [cx, cy - r_frame, 
                   cx+r_frame, cy, 
                   cx, cy + r_frame, 
                   cx-r_frame, cy]
    #線だけ(outline)で描く
    canvas.create_polygon(big_rhombus, fill="", outline="#474b4b", width=10) 

    #文字盤の目盛りを描画
    for i in range(12):
        #30°毎に角度を計算
        str_angle = math.radians(i * 30)

        #目盛を打つ
        if i % 3 == 0: #3の倍数の時は数字を描画する。
            #文字の位置計算
            r_text = 110
            x = cx + r_text * math.sin(str_angle)
            y = cy -r_text * math.cos(str_angle)
            #描画
            display_num = i if i != 0 else 12
            canvas.create_text(x, y, text=str(display_num), fill="#00ffff", font=("Times New Roman", 20, "bold"))
        else:
            r_mark = 100
            x = cx + r_mark * math.sin(str_angle)
            y = cy - r_mark * math.cos(str_angle)

            size = 3
            points = [
                x, y - size,
                x + size, y,
                x, y + size,
                x - size, y
            ]
            canvas.create_polygon(points, fill="White", outline="#00ffff")

    #時針の計算
    h_angle = math.radians(h * 30 + m * 0.5)
    h_x = CENTER + 75 * math.sin(h_angle)
    h_y = CENTER - 75 * math.cos(h_angle)

    #分針の計算
    m_angle = math.radians(m * 6 + s * 0.1)
    m_x = CENTER + 100 * math.sin(m_angle)
    m_y = CENTER - 100 * math.cos(m_angle)

    #秒針の計算　針のセンターの座標を計算。Cneter 100, 100 から長さ80の線を引く
    #秒を角度に変換 1sec 360° / 60sec = 6°
    s_angle = math.radians(s * 6)
    s_x = CENTER + 100  * math.sin(s_angle)
    s_y = CENTER - 100 * math.cos(s_angle)

    #時針を描画
    canvas.create_line(CENTER, CENTER, h_x, h_y, fill="White", width=6)  
    #分針を描画
    canvas.create_line(CENTER, CENTER, m_x, m_y, fill="White", width=2)
    #秒針を描画
    canvas.create_line(CENTER, CENTER, s_x, s_y, fill="#00ffff", width=1)

    #中心点を打つ
    center_x, center_y = CENTER, CENTER
    size = 6
    rhombus_points = [
        center_x, center_y - size,
        center_x + size, center_y,
        center_x, center_y + size,
        center_x - size, center_y
    ]
    canvas.create_polygon(rhombus_points, fill="#1D1D1D", outline="White")

    #1000ミリ秒後に呼び出す
    root.after(1000, update_clock)

#Main_window
SIZE = 250
CENTER = SIZE / 2

root = tk.Tk()
root.title("My Python Clock")
root.attributes("-topmost", True) #常に最前面に表示
root.configure(bg="#1D1D1D")
canvas = tk.Canvas(root, width=SIZE, height=SIZE, bg="#1D1D1D", highlightthickness=0, bd=0)
canvas.pack()

update_clock()
root.mainloop()