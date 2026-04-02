import tkinter as tk
from tkinter import messagebox
import rsa

# --- PHẦN LOGIC THUẬT TOÁN RSA ---
def generate_keys():
    # Tạo cặp khóa public và private
    (pubkey, privkey) = rsa.newkeys(512)
    text_pub.delete(1.0, tk.END)
    text_pub.insert(tk.END, pubkey.save_pkcs1().decode('utf-8'))
    
    text_priv.delete(1.0, tk.END)
    text_priv.insert(tk.END, privkey.save_pkcs1().decode('utf-8'))
    messagebox.showinfo("Thành công", "Đã tạo cặp khóa RSA 512-bit!")

def encrypt_message():
    try:
        pub_data = text_pub.get(1.0, tk.END).strip().encode('utf-8')
        pubkey = rsa.PublicKey.load_pkcs1(pub_data)
        message = entry_input.get().encode('utf-8')
        
        crypto = rsa.encrypt(message, pubkey)
        entry_output.delete(0, tk.END)
        entry_output.insert(tk.END, crypto.hex()) # Hiển thị dạng Hex cho dễ nhìn
    except Exception as e:
        messagebox.showerror("Lỗi", f"Mã hóa thất bại: {e}")

def decrypt_message():
    try:
        priv_data = text_priv.get(1.0, tk.END).strip().encode('utf-8')
        privkey = rsa.PrivateKey.load_pkcs1(priv_data)
        crypto = bytes.fromhex(entry_output.get().strip())
        
        message = rsa.decrypt(crypto, privkey).decode('utf-8')
        entry_input.delete(0, tk.END)
        entry_input.insert(tk.END, message)
        messagebox.showinfo("Kết quả", f"Văn bản đã giải mã: {message}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Giải mã thất bại: {e}")

# --- PHẦN GIAO DIỆN UI ---
root = tk.Tk()
root.title("RSA Encryption - Lê Đỗ Duy Tân")
root.geometry("600x650")

tk.Label(root, text="MÃ HÓA CÔNG KHAI RSA", font=("Arial", 14, "bold")).pack(pady=10)

# Phần tạo khóa
tk.Button(root, text="TẠO CẶP KHÓA (GENERATE KEYS)", command=generate_keys, bg="orange").pack(pady=5)

tk.Label(root, text="Public Key:").pack()
text_pub = tk.Text(root, height=6, width=70)
text_pub.pack(pady=5)

tk.Label(root, text="Private Key:").pack()
text_priv = tk.Text(root, height=8, width=70)
text_priv.pack(pady=5)

# Phần nhập liệu
tk.Label(root, text="Nhập văn bản (Plaintext):").pack()
entry_input = tk.Entry(root, width=70)
entry_input.pack(pady=5)

# Nút bấm
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="MÃ HÓA", command=encrypt_message, bg="lightblue", width=20).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="GIẢI MÃ", command=decrypt_message, bg="lightgreen", width=20).pack(side=tk.LEFT, padx=5)

tk.Label(root, text="Bản mã (Ciphertext - Hex):").pack()
entry_output = tk.Entry(root, width=70)
entry_output.pack(pady=5)

root.mainloop()