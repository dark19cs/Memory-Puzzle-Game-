def flip(root, widget, new_img, size=140):
    def shrink(w):
        if w > 10:
            widget.config(width=w)
            root.after(15, shrink, w-10)
        else:
            widget.config(image=new_img)
            expand(10)
    def expand(w):
        if w < size:
            widget.config(width=w)
            root.after(15, expand, w+10)
    shrink(size)

def win(root, title):
    def pulse(i):
        title.config(fg="#FF6F3C" if i%2==0 else "#333")
        if i < 10:
            root.after(150, pulse, i+1)
    pulse(0)