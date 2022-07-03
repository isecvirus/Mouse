from pynput import mouse


def moved(x, y):
    print(x, y)
with mouse.Listener(on_move=moved) as t:
    t.join()