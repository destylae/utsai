# Jawaban UTS No. 1

import pandas as pd

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ]

df = pd.DataFrame(data)

df

# Jawaban UTS No. 2

import numpy as np

P1 = np.array([1,2])
P2 = np.array([3,4])

def euclidean_distance (point1,point2):
    return np.sqrt(np.sum((point1-point2)**2))
distance = euclidean_distance(P1,P2)

print(F"Titik 1 : {P1}")
print(F"Titik 2 : {P2}")
print(F"Jarak Euclidean : {distance}")

# Jawaban UTS No. 3

from sklearn.neighbors import KNeighborsClassifier

data = [
    [1,2,'A'],
    [4,5,'B'],
    [7,8,'A'],
]

x = [[row[0],row[1]] for row in data]
y = [row[2] for row in data]

model = KNeighborsClassifier(n_neighbors=1)
model.fit(x, y)

data_test = [
    [2,3],
    [6,7],
]

for point in data_test:
  prediction = model.predict([point])
  print(f'Data {point} diklasifikasikan sebagai kelas {prediction[0]}')
  print()

# Jawaban UTS No. 4

# a. Keamanan Data
      # Google Colab : Colab berjalan di server Google, Kode dijalankan di mesin virtual pribadi untuk akun Anda sehingga sebagian besar aman.
      # Jupyter Notebook : Semuanya berjalan secara lokal di mesin Anda sendiri sehingga pengguna dapat membatasi akses ke buku catatan pengguna.
# b. Kontrol Akses
      # Google Colab : Menggunakan Gsuite/Gmail.
      # Jupyter Notebook : Menggunakan platform kontrol seperti (GitHub, GitLab, Bitbucket) yang akan memberi Anda keduanya - kontrol akses & kontrol versi.
# c. Tempat berkomentar
      # Google Colab : Dapat mengomentari sel buku catatan tertentu untuk memulai percakapan.
      # Jupyter Notebook : Tidak dapat berkomentar karena tidak ada dukungan bawaan untuk berkomentar di Jupyter Notebook.
# d. Menginstal Paket
      # Google Colab : Sudah diinstal sebelumnya dengan banyak perpustakaan umum misalnya Plotly, Numpy, Scipy, Tensorflow, Matplotlib semuanya tersedia secara default.
      # Jupyter Notebook : Dapat membuat lingkungan (virtualenv/conda) satu kali & menggunakannya kembali kapan saja kita mengerjakan proyek yang sama.
# e. Kontrol Versi Notebook
      # Google Colab : Cukup klik File -> Riwayat revisi di Colab UI untuk melihat riwayat perubahan yang dibuat pada file buku catatan.
      # Jupyter Notebook : Menggunakan platform berbasis git (GitHub, GitLab, Bitbucket). Ada ekstensi JupyterLab ( jupyterlab-git & GitPlus ) yang memudahkan untuk melakukan push commit dan membuat permintaan pull langsung dari UI JupyterLab.

# Jawaban UTS No. 5

# 1. Buka browser web dan pergi ke Google Colab. Pastikan sudah masuk ke akun Google pribadi.
# 2. Klik tombol "File" di sudut kiri atas. Pilih "New Notebook" untuk membuat notebook Python baru.
# 3. Beri nama notebook baru Anda dengan mengklik pada area yang berisi teks "Untitled" di bagian atas dan beri nama sesuai keinginan.
# 4. Untuk membuat sel baru, klik tombol "+ Code" atau "+ Text" di toolbar.
# 5. Mulai menulis kode Python di dalam sel.
# 6. Untuk menjalankan sel kode, klik tombol "Run" yang terletak di sebelah kiri sel. Hasil eksekusi kode akan ditampilkan di bawah sel tersebut.
# 7. Notebook otomatis disimpan di Google Drive, Google Colab secara otomatis menyimpan perubahan. Jika ingin menutup browser, dapat membuka notebook yang ada di Google Drive lagi.