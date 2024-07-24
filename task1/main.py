import queue
import random
import time
import threading

request_queue = queue.Queue()
stop_processing = False

def generate_request():
    request_id = random.randint(1000, 9999)
    request_queue.put(request_id)
    print(f"Заявка {request_id} додана до черги.")

def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Обробка заявки {request_id}...")
        time.sleep(random.uniform(1, 3))
        print(f"Заявка {request_id} оброблена.")
    else:
        print("Черга пуста. Очікування нових заявок...")

def stop_program():
    global stop_processing
    input("Натисніть Enter для завершення програми...")
    stop_processing = True
    print("Завершення програми...")
    
if __name__ == "__main__":
    while not stop_processing:
        threading.Thread(target=stop_program).start()
        time.sleep(0.5)
        generate_request()
        process_request()
        time.sleep(2)
