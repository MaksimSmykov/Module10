import time
from time import sleep
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf8') as file:
        for word in range(word_count):
            file.write(f"Какое-то слово № {word + 1}\n")
            # print(word + 1, threading.current_thread())
            sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")


start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time.time()
print(f'Работа функций {end_time - start_time}')

start_time = time.time()
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()

end_time = time.time()
print(f'Работа потоков {end_time - start_time}')