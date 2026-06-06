import tkinter as tk
def key_pressed(event):
    key = event.keysym
    log_box.insert(tk.END, f"Key pressed: {key}\n")
    log_box.see(tk.END)
root = tk.Tk()
root.title("Keyboard Event Monitor")
root.geometry("500x300")
label = tk.Label(
    root,
    text="Click inside this window and press keys.\nOnly keys entered here are displayed."
)
label.pack(pady=10)
log_box = tk.Text(root, height=12, width=60)
log_box.pack(pady=10)
root.bind("<Key>", key_pressed)
root.mainloop()