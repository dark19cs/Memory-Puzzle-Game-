import os
import sys
import subprocess
import threading
import shutil
import sound_control as sc
import constants


def _async_play_cmd(cmd):
    try:
        # Start subprocess without waiting (async)
        subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass


def _system_beep():
    try:
        # Terminal bell (may or may not be audible)
        sys.stdout.write('\a')
        sys.stdout.flush()
    except Exception:
        pass


def _play_file(filename, _fallback=None):
    if sc.muted:
        return
    path = os.path.join(constants.SOUND_DIR, filename)
    if not os.path.exists(path):
        _system_beep()
        return

    # Try platform-specific players
    if sys.platform.startswith('win'):
        try:
            import winsound

            # Play asynchronously on Windows
            winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC)
            return
        except Exception:
            pass

    # macOS: afplay is commonly available
    player = shutil.which('afplay') or shutil.which('paplay') or shutil.which('aplay') or shutil.which('play')
    if player:
        _async_play_cmd([player, path])
        return

    # Last resort: try Python playsound if installed (blocking)
    try:
        from playsound import playsound

        # run blocking playsound in a thread so UI stays responsive
        threading.Thread(target=lambda: playsound(path), daemon=True).start()
        return
    except Exception:
        pass

    # Fallback to simple system beep
    _system_beep()


def toggle_mute():
    return sc.toggle()


def play_flip():
    _play_file("flip.wav")


def play_match():
    _play_file("match.wav")


def play_wrong():
    _play_file("wrong.wav")
