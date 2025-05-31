import tkinter as tk
from tkinter import Toplevel
import threading
import time
import itertools

шутки = [
    "Читаю мысли...",
    "Лезу в чертоги разума...",
    "Сканирую нейроны...",
    "Взламываю подсознание...",
    "Уточняю с потусторонними силами...",
    "Обращаюсь к звёздам...",
    "Вызываю Джина..."
]

индикаторы = ["●○○", "○●○", "○○●", "○●●", "●●○", "●○●"]

def начать_загрузку():
    def загрузка():
        кнопка_угадать.config(state="disabled")
        старт = time.time()
        i = 0
        j = 0
        while time.time() - старт < 7:
            метка_статуса.config(text=шутки[i % len(шутки)])
            метка_индикатор.config(text=индикаторы[j % len(индикаторы)])
            i += 1
            j += 1
            time.sleep(0.6)
        показать_результат()

    threading.Thread(target=загрузка).start()

def показать_результат():
    число = поле_ввода.get()
    окно_результата = Toplevel(окно)
    окно_результата.title("Результат")
    окно_результата.geometry("300x100")
    tk.Label(окно_результата, text=f"Вы загадали число: {число}", font=("Arial", 12)).pack(pady=20)
    метка_статуса.config(text="")
    метка_индикатор.config(text="")
    кнопка_угадать.config(state="normal")

# Главное окно
окно = tk.Tk()
окно.title("Супер Джин")
окно.geometry("320x220")

tk.Label(окно, text="Ввести отгадываемое число:", font=("Arial", 12)).pack(pady=10)

поле_ввода = tk.Entry(окно, font=("Arial", 12))
поле_ввода.pack(pady=5)

кнопка_угадать = tk.Button(окно, text="Угадать", font=("Arial", 12), command=начать_загрузку)
кнопка_угадать.pack(pady=10)

метка_статуса = tk.Label(окно, text="", font=("Arial", 10), fg="gray")
метка_статуса.pack()

метка_индикатор = tk.Label(окно, text="", font=("Arial", 14))
метка_индикатор.pack()

окно.mainloop()