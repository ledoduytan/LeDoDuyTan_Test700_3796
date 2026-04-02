import tkinter as tk
from tkinter import messagebox

# --- PHẦN LOGIC THUẬT TOÁN PLAYFAIR ---
def prepare_key(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    for char in key + alphabet:
        if char not in matrix and char in alphabet:
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)
    return None

def playfair_process(text, key, mode="encrypt"):
    matrix = prepare_key(key)
    text = text.upper().replace("J", "I").replace(" ", "")
    
    # Xử lý cặp chữ trùng nhau (VD: HELLO -> HELXLO)
    prepared_text = ""
    i = 0
    while i < len(text):
        prepared_text += text[i]
        if i + 1 < len(text) and text[i] == text[i+1]:
            prepared_text += "X"
            i += 1
        elif i + 1 < len(text):
            prepared_text += text[i+1]
            i += 2
        else:
            prepared_text += "X"
            i += 1

    result = ""
    shift = 1 if mode == "encrypt" else -1
    
    for i in range(0, len(prepared_text), 2):
        r1, c1 = find_position(matrix, prepared_text[i])
        r2, c2 = find_position(matrix, prepared_text[i+1])
        
        if r1 == r2: # Cùng hàng
            result += matrix[r1][(c1 + shift) % 5] + matrix[r2][(c2 + shift) % 5]
        elif c1 == c2: # Cùng cột
            result += matrix[(r1 + shift) % 5][c1] + matrix[(r2 + shift) % 5][c2]
        else: # Hình chữ nhật
            result += matrix[r1][c2] + matrix[r2][c1]
            
    return result

# --- PHẦN GIAO DIỆN UI ---
def handle_encrypt():
    key = entry_key.get()
    text = entry_input.get()
    if not key or not text:
        messagebox.showwarning("Lỗi", "Vui lòng nhập Key và Văn bản!")
        return
    res = playfair_process(text, key, "encrypt")
    label_result.config(text=f"Mã hóa: {res}", fg="blue")

def handle_decrypt():
    key = entry_key.get()
    text = entry_input.get()
    if not key or not text:
        messagebox.showwarning("Lỗi", "Vui lòng nhập Key và Văn bản!")
        return
    res = playfair_process(text, key, "decrypt")
    label_result.config(text=f"Giải mã: {res}", fg="green")

root = tk.Tk()
root.title("Playfair Cipher - Lê Đỗ Duy Tân")
root.geometry("450x400")

tk.Label(root, text="THUẬT TOÁN PLAYFAIR", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(root, text="Key (Khóa):").pack()
entry_key = tk.Entry(root, width=35)
entry_key.pack(pady=5)

tk.Label(root, text="Văn bản cần xử lý:").pack()
entry_input = tk.Entry(root, width=35)
entry_input.pack(pady=5)

tk.Button(root, text="MÃ HÓA", command=handle_encrypt, bg="lightblue", width=20).pack(pady=5)
tk.Button(root, text="GIẢI MÃ", command=handle_decrypt, bg="lightgreen", width=20).pack(pady=5)

tk.Label(root, text="KẾT QUẢ:", font=("Arial", 10, "bold")).pack(pady=10)
label_result = tk.Label(root, text="...", font=("Courier", 12), wraplength=400)
label_result.pack()

root.mainloop()