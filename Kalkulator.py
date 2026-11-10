import tkinter as tk

# Fungsi untuk memasukkan angka/simbol ke layar
def klik(tombol):
    layar.insert(tk.END, tombol)

# Fungsi untuk menghitung hasil matematika
def hitung():
    try:
        hasil = eval(layar.get())
        layar.delete(0, tk.END)
        layar.insert(tk.END, str(hasil))
    except:
        layar.delete(0, tk.END)
        layar.insert(tk.END, "Error")

# Fungsi untuk membersihkan layar
def hapus():
    layar.delete(0, tk.END)

# Membuat jendela utama aplikasi
app = tk.Tk()
app.title("Kalkulator Python GUI")
app.geometry("300x420")
app.configure(bg="#222")

# Membuat kotak layar di bagian atas
layar = tk.Entry(app, font=("Arial", 24), justify="right", bd=10, bg="#eee")
layar.bind("<Key>", lambda e: "break")
layar.pack(fill="x", padx=10, pady=20)


# Membuat wadah (frame) untuk menyusun tombol
frame_tombol = tk.Frame(app, bg="#222")
frame_tombol.pack()

# Data posisi tombol (Teks, Baris, Kolom)
tombol_data = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3)
]

# Perulangan untuk memunculkan tombol-tombol di layar
for (teks, baris, kolom) in tombol_data:
    if teks == '=':
        btn = tk.Button(frame_tombol, text=teks, width=5, height=2, font=("Arial", 14, "bold"), bg="#4caf50", fg="white", command=hitung)
    elif teks == 'C':
        btn = tk.Button(frame_tombol, text=teks, width=5, height=2, font=("Arial", 14, "bold"), bg="#f44336", fg="white", command=hapus)
    else:
        btn = tk.Button(frame_tombol, text=teks, width=5, height=2, font=("Arial", 14, "bold"), bg="#555", fg="white", command=lambda t=teks: klik(t))
    
    btn.grid(row=baris, column=kolom, padx=5, pady=5)

# Menahan layar aplikasi agar tidak langsung tertutup
app.mainloop()