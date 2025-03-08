import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os, re

def xor_crypt(data, password):
    key = password.encode("utf-8")
    key_length = len(key)
    encrypted = bytearray(data)
    for i in range(len(encrypted)):
        encrypted[i] ^= key[i % key_length]
    return bytes(encrypted)

def split_file():
    file_path = filedialog.askopenfilename(title="Select the file to split")
    if not file_path:
        return
    parts_str = simpledialog.askstring("Number of parts", "Enter the desired number of parts:", parent=root)
    if not parts_str:
        return
    try:
        num_parts = int(parts_str)
        if num_parts <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Invalid number.")
        return


    secure = messagebox.askyesno("Security", "Do you want to protect the file with a password?")
    password = None
    if secure:
        password = simpledialog.askstring("Password", "Enter the password:", parent=root, show="*")
        if not password:
            messagebox.showerror("Error", "Invalid password.")
            return

    try:
        file_size = os.path.getsize(file_path)
        base_chunk_size = file_size // num_parts
        remainder = file_size % num_parts

        base, ext = os.path.splitext(file_path)
        with open(file_path, 'rb') as f:
            for part in range(1, num_parts + 1):
                current_chunk_size = base_chunk_size + (1 if part <= remainder else 0)
                chunk = f.read(current_chunk_size)
                if secure:
                    chunk = xor_crypt(chunk, password)
                    new_filename = f"{base}{ext}.xpart{part}"
                else:
                    new_filename = f"{base}{ext}.part{part}"
                with open(new_filename, 'wb') as chunk_file:
                    chunk_file.write(chunk)
        messagebox.showinfo("Success", f"File split into {num_parts} parts.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def get_part_number(filename):
    m = re.search(r'\.(?:x?part)(\d+)$', filename)
    return int(m.group(1)) if m else 0

def custom_save_dialog(default_ext):
    top = tk.Toplevel(root)
    top.title("Save the reassembled file")
    top.configure(bg="#2e2e2e")
    tk.Label(top, text="File name (without extension):", bg="#2e2e2e", fg="white").pack(padx=10, pady=10)
    entry = tk.Entry(top, width=40)
    entry.pack(padx=10, pady=5)
    result = {}
    def on_save():
        result['filename'] = entry.get()
        top.destroy()
    tk.Button(top, text="Save", command=on_save, bg="#90EE90", fg="black").pack(padx=10, pady=10)
    top.grab_set()
    root.wait_window(top)
    return result.get('filename', None)

def merge_files():
    file_paths = filedialog.askopenfilenames(title="Select the parts in order")
    if not file_paths:
        return
    file_paths = sorted(file_paths, key=lambda x: get_part_number(os.path.basename(x)))
    first_file = os.path.basename(file_paths[0])
    ext_match = re.search(r'(.*)(\.\w+)\.(?:x?part)\d+$', first_file)
    default_ext = ext_match.group(2) if ext_match else ""
    
    is_secure = ".xpart" in first_file
    password = None
    if is_secure:
        password = simpledialog.askstring("Password", "Enter the password to decrypt:", parent=root, show="*")
        if not password:
            messagebox.showerror("Error", "Invalid password.")
            return

    save_name = custom_save_dialog(default_ext)
    if not save_name:
        return
    dir_path = os.path.dirname(file_paths[0])
    output_path = os.path.join(dir_path, save_name)
    if os.path.splitext(output_path)[1] == "":
        output_path += default_ext
    try:
        with open(output_path, 'wb') as outfile:
            for part in file_paths:
                with open(part, 'rb') as infile:
                    chunk = infile.read()
                    if is_secure:
                        chunk = xor_crypt(chunk, password)
                    outfile.write(chunk)
        messagebox.showinfo("Success", "File reassembled.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("FileSplitter")
root.configure(bg="#2e2e2e")  


label_fg = "white"
button_bg = "#90EE90"
button_fg = "black"


split_frame = tk.LabelFrame(root, text="Split a file", fg=label_fg, bg="#2e2e2e", font=("Arial", 12, "bold"))
split_frame.pack(padx=10, pady=10, fill="both", expand=True)
split_button = tk.Button(split_frame, text="Select and split", command=split_file,
                         bg=button_bg, fg=button_fg, font=("Arial", 10, "bold"))
split_button.pack(padx=20, pady=20)


merge_frame = tk.LabelFrame(root, text="Merge a file", fg=label_fg, bg="#2e2e2e", font=("Arial", 12, "bold"))
merge_frame.pack(padx=10, pady=10, fill="both", expand=True)
merge_button = tk.Button(merge_frame, text="Select parts and merge", command=merge_files,
                         bg=button_bg, fg=button_fg, font=("Arial", 10, "bold"))
merge_button.pack(padx=20, pady=20)

root.mainloop()
