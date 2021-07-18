# tkinterライブラリを使用 => tkで呼び出し可能
import tkinter as tk
# tkinter内のttk機能をインポート
from tkinter import ttk

# ###############################################
# メインウィンドウ生成
# ###############################################
# メインウィンドウオブジェクト作成
root = tk.Tk()
# ウィンドウサイズ指定(横:220 縦:180)
root.geometry('220x180')
# ウィンドウタイトル指定
root.title("年号換算")

# ###############################################
# フレーム生成
# ###############################################
# ウィジェット(部品)をまとめるフレームを作成
frame = ttk.Frame(root)
# フレームを画面上に配置
frame.pack()

# ###############################################
# ウィジェット生成
# > frameを親要素とする
# > justify : 文字揃え
# > state : 状態
# >> readonly : 読み込み専用 -> 書き込み不可
# ###############################################
# コンボボックス生成
cbox = ttk.Combobox(frame,
                    width=8,
                    justify='center',
                    state='readonly',
                    values=['西暦', '令和', '平成', '昭和'])
# 入力ボックス生成
ibox = ttk.Entry(frame,
                 width=10,
                 justify='right')
# ラベル生成 - 西暦
era1 = ttk.Label(frame,
                 text='西暦 : ')
nen1 = ttk.Label(frame,
                 text=2021)
# ラベル生成 - 令和
era2 = ttk.Label(frame,
                 text='令和 : ')
nen2 = ttk.Label(frame,
                 text=3)
# ラベル生成 - 平成
era3 = ttk.Label(frame,
                 text='平成元年から : ')
nen3 = ttk.Label(frame,
                 text=33)
# ラベル生成 - 昭和
era4 = ttk.Label(frame,
                 text='昭和元年から : ')
nen4 = ttk.Label(frame,
                 text=96)
# ボタン生成
btn1 = ttk.Button(frame,
                  text='換算')
# ボタン生成
# => root.destroy : ウィンドウ終了命令を設定
btn2 = ttk.Button(frame,
                  text='終了',
                  command=root.destroy)

# ###############################################
# ウィジェット配置
# > row : 行
# > column : 列
# > padx : 左右の空き具合
# > pady : 上下の空き具合
# > sticky : ラベルの文字揃え
# >> e : 右揃え
# ###############################################
# ラベル･入力ボックス･ボタンをgridで画面上に配置
cbox.grid(row=0, column=0, padx=5, pady=10)
ibox.grid(row=0, column=1, padx=2, pady=10)
era1.grid(row=1, column=0, padx=5, pady=3, sticky='e')
nen1.grid(row=1, column=1, padx=2, pady=3, sticky='e')
era2.grid(row=2, column=0, padx=5, pady=3, sticky='e')
nen2.grid(row=2, column=1, padx=2, pady=3, sticky='e')
era3.grid(row=3, column=0, padx=5, pady=3, sticky='e')
nen3.grid(row=3, column=1, padx=2, pady=3, sticky='e')
era4.grid(row=4, column=0, padx=5, pady=3, sticky='e')
nen4.grid(row=4, column=1, padx=2, pady=3, sticky='e')
btn1.grid(row=5, column=0, padx=5, pady=3)
btn2.grid(row=5, column=1, padx=2, pady=3)

# ###############################################
# 画面表示
# > 操作可能状態にする
# ###############################################
root.mainloop()
