paused = False

def set_paused(value: bool):
    """Enable or disable animations. When paused, scheduled animation steps will not be queued."""
    global paused
    paused = bool(value)


def _after(root, ms, func, *args):
    """Schedule `func` to run after `ms` milliseconds only if not paused."""
    if paused:
        return
    root.after(ms, func, *args)


def flip(root, widget, new_img, size=140):
    def shrink(w):
        if w > 10:
            widget.config(width=w)
            _after(root, 15, shrink, w-10)
        else:
            widget.config(image=new_img)
            expand(10)

    def expand(w):
        if w < size:
            widget.config(width=w)
            _after(root, 15, expand, w+10)

    shrink(size)


def win(root, title):
    def pulse(i):
        title.config(fg="#FF6F3C" if i % 2 == 0 else "#333")
        if i < 10:
            _after(root, 150, pulse, i+1)

    pulse(0)