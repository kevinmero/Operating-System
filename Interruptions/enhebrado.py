import threading
def periodic_task():
    print("This task runs periodically.")
# Programe la tarea para que se ejecute cada 5 segundos
timer_interrupt = threading.Timer(5, periodic_task)
timer_interrupt.start()



