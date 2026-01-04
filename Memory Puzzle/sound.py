import os
import winsound
import sound_control as sc
import constants

def _play_file(filename, fallback_beep):
    if sc.muted:
        return
    path = os.path.join(constants.SOUND_DIR, filename)
    if os.path.exists(path):
        try:
            winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC)
            return
        except Exception:
            pass
    # fallback to simple system beep if file missing or play failed
    winsound.MessageBeep(fallback_beep)

def toggle_mute():
    return sc.toggle()

def play_flip():
    _play_file("flip.wav", winsound.MB_OK)

def play_match():
    _play_file("match.wav", winsound.MB_ICONASTERISK)

def play_wrong():
    _play_file("wrong.wav", winsound.MB_ICONHAND)
