import keyboard

var = "none"

def def1():
    var = "up"
    print(var)

def def2():
    var = "down"
    print(var)

while True:
    # Wait for the next event.
    event = keyboard.read_event()

    if event.event_type == keyboard.KEY_DOWN and event.name == 'w':
        def2()

    if event.event_type == keyboard.KEY_DOWN and event.name == 's':
        def1()