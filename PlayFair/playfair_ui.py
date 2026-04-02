import tkinter as tk
from tkinter import messagebox

# Đây là khung giao diện mẫu, bạn có thể tích hợp hàm xử lý Playfair vào sau
def handle_encrypt():
    key = entry_key.get()
    text = entry_input.get()
    if not key or not text:
        messagebox.showwarning("Thông báo", "Vui lòng nhập đầy đủ Key và Nội dung!")
        return
    # Tạm thời hiển thị thông báo (Bạn sẽ thay bằng hàm Playfair của mình)
    label_result.config(text=f"Kết quả mã hóa: [Đã mã hóa với key {key}]", fg="blue")

def handle_decrypt():
    key = entry_key.get()
    text = entry_input.get()
    if not key or not text:
        messagebox.showwarning("Thông báo", "Vui lòng nhập đầy đủ Key và Nội dung!")
        return
    label_result.config(text=f"Kết quả giải mã: [Đã giải mã với key {key}]", fg="green")

# Khởi tạo giao diện
root = tk.Tk()
root.title("Playfair Cipher - Lê Đỗ Duy Tân")
root.geometry("400x350")

tk.Label(root, text="PLAYFAIR CIPHER UI", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Nhập Key:").pack()
entry_key = tk.Entry(root, width=30)
entry_key.pack(pady=5)

tk.Label(root, text="Nhập Nội dung (Plaintext/Ciphertext):").pack()
entry_input = tk.Entry(root, width=30)
entry_input.pack(pady=5)

btn_encrypt = tk.Button(root, text="Mã hóa", command=handle_encrypt, bg="lightblue", width=15)
btn_encrypt.pack(pady=5)

btn_decrypt = tk.Button(root, text="Giải mã", command=handle_decrypt, bg="lightgreen", width=15)
btn_decrypt.pack(pady=5)

tk.Label(root, text="KẾT QUẢ:").pack(pady=10)
label_result = tk.Label(root, text="...", font=("Arial", 10, "italic"))
label_result.pack()

root.mainloop()