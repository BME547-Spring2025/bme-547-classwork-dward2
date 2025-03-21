import tkinter as tk
from tkinter import ttk
from tkinter import font


def main_window():
    root = tk.Tk()
    root.title("Health DB Gui")

    my_font = font.Font(size=18)

    title_label = tk.Label(root, text="Blood Donor Database", font=my_font)
    title_label.grid(column=0, row=0, columnspan=2, sticky=tk.W)
    name_label = tk.Label(root, text="Name:", font=my_font)
    name_label.grid(column=0, row=1, sticky=tk.E)

    entry_box = tk.Entry(root, font=my_font, width=50)
    entry_box.grid(column=1, row=1, pady=5)

    id_label = tk.Label(root, text="Id:", font=my_font)
    id_label.grid(column=0, row=2, sticky=tk.E)
    id_box = tk.Entry(root, font=my_font)
    id_box.grid(column=1, row=2, pady=5)

    radio_a = tk.Radiobutton(root, text="A", font=my_font)
    radio_a.grid(column=0, row=3, sticky=tk.W)
    radio_b = tk.Radiobutton(root, text="B", font=my_font)
    radio_b.grid(column=0, row=4, sticky=tk.W)
    radio_ab = tk.Radiobutton(root, text="AB", font=my_font)
    radio_ab.grid(column=0, row=5, sticky=tk.W)
    radio_o = tk.Radiobutton(root, text="O", font=my_font)
    radio_o.grid(column=0, row=6, sticky=tk.W)

    rh_checkbox = tk.Checkbutton(root, text="rH Positive", font=my_font)
    rh_checkbox.grid(column=1, row=4)

    center_label = tk.Label(root, text="Donation Center", font=my_font)
    center_label.grid(column=2, row=0)
    center_box = ttk.Combobox(root)
    center_box.grid(column=2, row=1)

    ok_button = tk.Button(root, text="Ok", font=("TimesNewRoman", 24, "italic"))
    ok_button.grid(column=1, row=6)
    cancel_button = tk.Button(root, text="Cancel", font=my_font, fg="red", bg="yellow")
    cancel_button.grid(column=2, row=6)

    root.mainloop()
    print("Done")


if __name__ == "__main__":
    main_window()
