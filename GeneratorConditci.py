import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  # Для копирования текста в буфер обмена


# Функция генерации пароля
def generate_password():
    characters = ""
    if lowercase_var.get():
        characters += string.ascii_lowercase
    if digits_var.get():
        characters += string.digits
    if special_var.get():
        characters += "!@#$%"

    # Проверка на случай, если не выбрано ни одного параметра
    if not characters:
        messagebox.showwarning("Ошибка", "Выберите хотя бы один параметр!")
        return

    # Получение длины пароля из ползунка
    password_length = length_slider.get()
    password = "".join(random.choice(characters) for _ in range(password_length))

    # Вывод пароля на экран
    output_label.config(text=password)


# Функция копирования пароля
def copy_password():
    password = output_label.cget("text")
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Копирование", "Пароль скопирован в буфер обмена!")


# Интерфейс
root = tk.Tk()
root.title("Генератор паролей")
root.geometry("300x350")

#черная темка
root.configure(background="black")



# Параметры генерации
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

tk.Label(root, text="Выберите параметры:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
tk.Checkbutton(root, text="Включить алфавит [a-z]", variable=lowercase_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Включить цифры [0-9]", variable=digits_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Включить спецсимволы [! @ # $ %]", variable=special_var).pack(anchor="w", padx=20)

# Ползунок для выбора длины пароля
tk.Label(root, text="Выберите длину пароля:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
length_slider = tk.Scale(root, from_=8, to=16, orient="horizontal")
length_slider.set(10)  # Значение по умолчанию
length_slider.pack(padx=10, pady=5)

# Кнопка генерации пароля
generate_button = tk.Button(root, text="Сгенерировать", command=generate_password, font=("Arial", 12))
generate_button.pack(pady=10)

# Поле для вывода пароля
output_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
output_label.pack(pady=10)

# Кнопка для копирования пароля
copy_button = tk.Button(root, text="Копировать пароль", command=copy_password, font=("Arial", 12))
copy_button.pack(pady=10)

root.mainloop()
