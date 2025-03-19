import keyboard

def handle_keyboard_input(event):
    if event.name == 'a':
        print("You pressed 'a'.")
    elif event.name == 'b':
        print("You pressed 'b'.")

keyboard.on_press(handle_keyboard_input)

# Esperar hasta que se presione la tecla 'esc' para salir
keyboard.wait('esc')  # Espera a que presiones 'esc'
print("Programa terminado.")