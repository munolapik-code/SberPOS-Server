import threading
import os

# Функция для запуска сайта/сервера (например, на Flask)
def run_server():
    os.system("python api_server.py")

# Функция для запуска бота
def run_bot():
    os.system("python bot.py")

if __name__ == "__main__":
    # Запускаем их в разных потоках, чтобы они работали одновременно
    t1 = threading.Thread(target=run_server)
    t2 = threading.Thread(target=run_bot)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
