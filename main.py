import tkinter as tk

def button_clicked():
    value = float(value_to_be_converted.get())
    km_value = value * 1.6
    kilometer_label.config(text=f"{km_value:.2f} km")

window = tk.Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=320, height=200)
window.config(padx=20, pady=20)

welcome_label = tk.Label(text="Welcome!", font=("Arial", 20, "italic"))
welcome_label.grid(column=0, row=0, columnspan=3, pady=5)

description_label = tk.Label(text="Let's convert, shall we?", font=("Arial", 14, "italic"))
description_label.grid(column=0, row=1, columnspan=3, pady=5)

text_label_left = tk.Label(text="I've ran ", font=("Arial", 14))
text_label_left.grid(column=0, row=2, padx=5)
value_to_be_converted = tk.Entry(width=10)
value_to_be_converted.grid(column=1, row=2, padx=5)

text_label_right = tk.Label(text=" miles!", font=("Arial", 14))
text_label_right.grid(column=2, row=2, padx=5)
kilometer_label = tk.Label(text="0.00 km", font=("Arial", 16, "bold"))
kilometer_label.grid(column=1, row=3, pady=10)

convert_button = tk.Button(text="CONVERT", command=button_clicked)
convert_button.grid(column=1, row=4, pady=5)
window.mainloop()
