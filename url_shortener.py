import tkinter as tk
from tkinter import messagebox, ttk
import pyshorteners
import pyperclip

def shorten_url():
    long_url = url_entry.get()
    if long_url:
        try:
            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(long_url)
            result_label.config(text=short_url)
            copy_button.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to shorten URL. Error: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter a valid URL.")

def copy_to_clipboard():
    short_url = result_label.cget("text")
    pyperclip.copy(short_url)
    messagebox.showinfo("Copied", "Short URL copied to clipboard!")

root = tk.Tk()
root.title("URL Shortener")
root.geometry("500x300")
root.config(bg="#2c3e50")


style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=10)
style.configure('TLabel', font=('Helvetica', 12), background="#2c3e50", foreground="#ecf0f1")
style.configure('TEntry', font=('Helvetica', 12), padding=5)

# Header Label
header_label = ttk.Label(root, text="URL Shortener", font=('Helvetica', 20, 'bold'), background="#2c3e50", foreground="#ecf0f1")
header_label.pack(pady=20)

# URL Entry
url_label = ttk.Label(root, text="Enter the URL to shorten:")
url_label.pack(pady=5)
url_entry = ttk.Entry(root, width=50)
url_entry.pack(pady=5)

shorten_button = ttk.Button(root, text="Shorten URL", command=shorten_url)
shorten_button.pack(pady=15)

result_frame = tk.Frame(root, bg="#34495e")
result_frame.pack(pady=10, fill=tk.X, padx=50)
result_label = ttk.Label(result_frame, text="", font=('Helvetica', 12), background="#34495e", foreground="#ecf0f1")
result_label.pack(pady=5)

copy_button = ttk.Button(root, text="Copy Short URL", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack(pady=10)

footer_label = ttk.Label(root, text="Developed by IMRAN KHAN", font=('Helvetica', 10, 'italic'), background="#2c3e50", foreground="#bdc3c7")
footer_label.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
