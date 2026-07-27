import tkinter as tk
import encryption

BG = "#1e1e1e"
PANEL = "#2b2b2b"
GREEN = "#4CAF50"
GREEN_HOVER = "#45a049"
TEXT = "#ffffff"

FONT = ("Segoe UI", 11)
FONT_BOLD = ("Segoe UI", 11, "bold")
TITLE_FONT = ("Segoe UI", 16, "bold")

root = tk.Tk()
root.title("Encrypted Messaging System")
root.geometry("650x240")
root.configure(bg=BG)
root.resizable(False, False)

mode_to_use = "Encryption"


def change_command():
    global mode_to_use

    if mode_to_use == "Encryption":
        mode_to_use = "Decryption"
        mode_button.config(text="Decrypt")
    else:
        mode_to_use = "Encryption"
        mode_button.config(text="Encrypt")

    status.config(text=f"Mode: {mode_to_use}")


def start():
    text_input = text_field.get("1.0", "end-1c")

    if not text_input.strip():
        return

    if mode_to_use == "Encryption":
        result = encryption.encrypt(text_input)
    else:
        result = encryption.decrypt(text_input)

    text_field.delete("1.0", tk.END)
    text_field.insert("1.0", result)


def hover_on(event):
    event.widget.config(bg=GREEN_HOVER)


def hover_off(event):
    event.widget.config(bg=GREEN)


frame = tk.Frame(root, bg=BG)
frame.pack(fill="both", expand=True, padx=20, pady=20)

title = tk.Label(
    frame,
    text="Encrypted Messaging System",
    bg=BG,
    fg=TEXT,
    font=TITLE_FONT
)
title.grid(row=0, column=0, columnspan=3, pady=(0, 20))

mode_button = tk.Button(
    frame,
    text="Encrypt",
    command=change_command,
    bg=GREEN,
    fg="white",
    activebackground=GREEN_HOVER,
    activeforeground="white",
    relief="flat",
    font=FONT_BOLD,
    width=10,
    cursor="hand2"
)
mode_button.grid(row=1, column=0, padx=(0, 15))

text_field = tk.Text(
    frame,
    width=45,
    height=4,
    bg=PANEL,
    fg=TEXT,
    insertbackground="white",
    relief="flat",
    font=FONT,
    padx=8,
    pady=8
)
text_field.grid(row=1, column=1)

start_button = tk.Button(
    frame,
    text="Start",
    command=start,
    bg=GREEN,
    fg="white",
    activebackground=GREEN_HOVER,
    activeforeground="white",
    relief="flat",
    font=FONT_BOLD,
    width=10,
    cursor="hand2"
)
start_button.grid(row=1, column=2, padx=(15, 0))

status = tk.Label(
    frame,
    text="Mode: Encryption",
    bg=BG,
    fg="#bbbbbb",
    font=("Segoe UI", 10)
)
status.grid(row=2, column=0, columnspan=3, pady=(15, 0))

for button in (mode_button, start_button):
    button.bind("<Enter>", hover_on)
    button.bind("<Leave>", hover_off)

root.mainloop()