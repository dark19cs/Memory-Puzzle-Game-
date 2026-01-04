class Timer:
    def __init__(self, root, label):
        self.root = root
        self.label = label
        self.time = 0
        self.id = None
        self.paused = False

    def start(self, seconds, timeout):
        self.time = seconds
        self.paused = False
        self._tick(timeout)

    def _tick(self, timeout):
        import __main__
        if self.paused: return
        self.label.config(text=f"⏱ {self.time}s")
        __main__.time_left = self.time
        if self.time <= 0:
            timeout()
            return
        self.time -= 1
        self.id = self.root.after(1000, self._tick, timeout)

    def stop(self):
        if self.id:
            self.root.after_cancel(self.id)

    def pause(self):
        self.paused = True

    def resume(self, timeout):
        if self.paused:
            self.paused = False
            self._tick(timeout)