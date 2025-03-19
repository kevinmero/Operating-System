import signal
def handle_timer_interrupt(signum, frame):
    print("Timer interrupt occurred.")
def main():
    # Registrar el manejador de interrupciones del temporizador
    signal.signal(signal.SIGALRM, handle_timer_interrupt)
    # Programar una interrupción del temporizador durante 5 segundos
    signal.alarm(5)
    # Iniciar el bucle principal
    while True:
        pass

if __name__ == "__main__":
    main()