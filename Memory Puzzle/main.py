import os
from PIL import Image, ImageTk
import ui_design as ui
from game_logic import create_cards
from sound import play_flip, play_match, play_wrong
import ui_animations as anim
import hint_logic as hl
import sound_control as sc
import timer_logic
import constants

# --------------------
# GAME STATE
# --------------------
level = 1
MAX_LEVEL = 5

cards = []
revealed = []
buttons = []
player_choice = []
can_click = True

time_left = 0
timer_id = None
paused = False
moves = 0
hint_count = 2

# --------------------
# WINDOW & UI
# --------------------
root = ui.create_window()
root.bell = lambda *args: None

title = ui.create_title(root)
status = ui.create_status(root)
timer_label = ui.create_timer(root)
frame = ui.create_board(root)

controls = ui.create_controls_bar(root)

timer = timer_logic.Timer(root, timer_label)

# --------------------
# LOAD IMAGES
# --------------------

def load_image(name):
    img = Image.open(os.path.join(constants.IMG_DIR, name))
    img = img.resize((ui.CARD_SIZE, ui.CARD_SIZE))
    return ImageTk.PhotoImage(img)

fruit_images = {
    "A": load_image("apple.png"),
    "B": load_image("banana.png"),
    "C": load_image("grape.png"),
    "D": load_image("orange.png"),
    "E": load_image("strawberry.png"),
    "F": load_image("pineapple.png"),
}

back_image = load_image("back.png")

# --------------------
# TIMER
# --------------------
LEVEL_TIME = {1:30, 2:45, 3:60, 4:75, 5:90}

def start_timer():
    timer.start(LEVEL_TIME[level], time_up)

def stop_timer():
    timer.stop()

def time_up():
    global level
    stop_timer()
    level = 1  # restart from first level
    show_summary("⏰ Time’s Up! Restarted")

# --------------------
# GAME LOGIC
# --------------------
def load_level():
    global cards, revealed, buttons, moves, paused, can_click, hint_count

    stop_timer()
    paused = False
    can_click = True
    moves = 0
    if hint_count > 0:
        hint_btn.config(text=f"💡 Hint ({hint_count})", state="normal")
    else:
        hint_btn.config(text="💡 Hint (0)", state="disabled")
    next_level_btn.config(state="disabled")

    for w in frame.winfo_children():
        w.destroy()

    title.config(text=f"🍓 Level {level}")
    status.config(text="Match all fruit pairs")

    cards = create_cards(level)
    revealed = [False]*len(cards)
    buttons.clear()
    player_choice.clear()

    for i in range(len(cards)):
        btn = ui.create_card(frame, back_image, lambda i=i: click_card(i))
        btn.grid(row=i//4, column=i%4, padx=18, pady=18)
        buttons.append(btn)

    start_timer()

def click_card(i):
    global can_click, moves
    if paused or not can_click or revealed[i]:
        return

    play_flip()
    anim.flip(root, buttons[i], fruit_images[cards[i]], ui.CARD_SIZE)
    revealed[i] = True
    player_choice.append(i)
    moves += 1

    if len(player_choice) == 2:
        can_click = False
        root.after(800, check_cards)

def check_cards():
    global can_click
    x, y = player_choice

    if cards[x] == cards[y]:
        play_match()
    else:
        play_wrong()
        buttons[x].config(image=back_image)
        buttons[y].config(image=back_image)
        revealed[x] = revealed[y] = False

    player_choice.clear()
    can_click = True

    if all(revealed):
        complete_level()

# --------------------
# CONTROLS
# --------------------
def pause_game():
    global paused
    paused = not paused
    status.config(text="⏸ Paused" if paused else "▶ Resumed")
    if not paused:
        timer.resume(time_up)

def hint():
    global hint_count
    if hint_count <= 0 or len(player_choice) > 0:
        return
    hint_count -= 1
    hint_btn.config(text=f"💡 Hint ({hint_count})")
    if hint_count == 0:
        hint_btn.config(state="disabled")
    pair = hl.use_hint(cards, revealed)
    if pair:
        i, j = pair
        # reveal and mark as matched
        anim.flip(root, buttons[i], fruit_images[cards[i]], ui.CARD_SIZE)
        anim.flip(root, buttons[j], fruit_images[cards[j]], ui.CARD_SIZE)
        revealed[i] = revealed[j] = True
        play_match()
        # clear any pending choices and allow clicks
        player_choice.clear()

        # if all cards are now revealed, finish level
        if all(revealed):
            complete_level()

def show_summary(message):
    for w in frame.winfo_children():
        w.destroy()

    summary = f"""
{message}

Level: {level}
Moves: {moves}
Time Left: {time_left}s
"""
    status.config(text=summary)
    # After showing the message, reload the current level (used for time-up)
    root.after(3000, load_level)


def next_level():
    global level
    if level < MAX_LEVEL:
        level += 1
        load_level()
    else:
        # already at max, perhaps do nothing or restart
        pass


def restart_game():
    global level, hint_count
    hint_count = 2
    level = 1
    load_level()





def complete_level():
    global level
    stop_timer()
    if level < MAX_LEVEL:
        # show completion message and enable next level button
        status.config(text=f"🎉 Level {level} Complete! Press Next Level to continue.")
        next_level_btn.config(state="normal")
        anim.win(root, title)
        hint_btn.config(state="disabled")
    else:
        # final congratulations screen
        for w in frame.winfo_children():
            w.destroy()
        title.config(text="")
        status.config(text="🎉 Congratulations! You completed all levels 🎉")
        anim.win(root, status)
        ui.create_replay_button(root, restart_game)

# --------------------
# CONTROL BUTTONS
# --------------------
ui.create_control_button(controls, "⏸ Pause", pause_game)
# Mute button: create, show normal font initially, then toggle bold on click
hint_btn = ui.create_control_button(controls, "💡 Hint (2)", hint)

mute_btn = ui.create_control_button(controls, "🔇 Mute", lambda: None)
mute_btn.config(font=("Arial", 13, "normal"))
def _handle_mute_click():
    muted = sc.toggle()
    if muted:
        mute_btn.config(font=("Arial", 13, "bold"))
    else:
        mute_btn.config(font=("Arial", 13, "normal"))
mute_btn.config(command=_handle_mute_click)

next_level_btn = ui.create_control_button(controls, "➡️ Next Level", next_level)
ui.create_control_button(controls, "🔁 Replay", lambda: load_level())

# --------------------
# START
# --------------------
load_level()
root.mainloop()
