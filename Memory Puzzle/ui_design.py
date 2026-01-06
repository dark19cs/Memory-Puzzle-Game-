import tkinter as tk

# --------------------
# COLORS & STYLES (FRUIT THEME)
# --------------------
BG_COLOR = "#E8F9F1"
CARD_BG = "#B8E1DD"
TITLE_COLOR = "#FF6F3C"
TEXT_COLOR = "#2C3333"

FONT_TITLE = ("Comic Sans MS", 34, "bold")
FONT_STATUS = ("Arial", 16)
FONT_TIMER = ("Arial", 18, "bold")

CARD_SIZE = 140

# --------------------
# WINDOW
# --------------------
def create_window():
    root = tk.Tk()
    root.title("Fruit Memory Puzzle")
    root.geometry("1100x850")
    root.configure(bg=BG_COLOR)
    return root

# --------------------
# LABELS
# --------------------
def create_title(root):
    lbl = tk.Label(
        root,
        font=FONT_TITLE,
        fg=TITLE_COLOR,
        bg=BG_COLOR
    )
    lbl.pack(pady=10)
    return lbl

def create_status(root):
    lbl = tk.Label(
        root,
        font=FONT_STATUS,
        fg=TEXT_COLOR,
        bg=BG_COLOR
    )
    lbl.pack()
    return lbl

def create_timer(root):
    lbl = tk.Label(
        root,
        font=FONT_TIMER,
        fg="#D62828",
        bg=BG_COLOR
    )
    lbl.pack(pady=5)
    return lbl

# --------------------
# BOARD
# --------------------
def create_board(root):
    frame = tk.Frame(root, bg=BG_COLOR)
    frame.pack(pady=30)
    return frame

# --------------------
# CARD
# --------------------
def create_card(frame, image, click_handler):
    lbl = tk.Label(
        frame,
        image=image,
        bg=CARD_BG,
        width=CARD_SIZE,
        height=CARD_SIZE,
        bd=0
    )
    lbl.bind("<Button-1>", lambda e: click_handler())
    return lbl

# --------------------
# REPLAY BUTTON
# --------------------
def create_replay_button(root, command):
    btn = tk.Button(
        root,
        text="🔁 Replay Game",
        font=("Arial", 14, "bold"),
        bg="#FFB703",
        fg="#000",
        bd=0,
        padx=20,
        pady=10,
        command=command
    )
    btn.pack(pady=15)
    return btn
def create_control_button(root, text, command):
    btn = tk.Button(
        root,
        text=text,
        font=("Arial", 13, "bold"),
        bg="#90DBF4",
        fg="#000",
        bd=0,
        padx=15,
        pady=8,
        command=command
    )
    btn.pack(side="left", padx=10, pady=10)
    return btn

def create_controls_bar(root):
    frame = tk.Frame(root, bg=BG_COLOR)
    frame.pack(pady=10)
    return frame
