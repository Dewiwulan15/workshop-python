# Pertemuan 12: JUPYTER
---

## Dokumentasi Proyek Jupyter

__Selamat datang di dokumentasi Proyek Jupyter__ . Situs web ini bertindak sebagai dokumentasi "meta" untuk ekosistem Jupyter. Ini memiliki koleksi sumber daya untuk menavigasi alat dan komunitas di ekosistem.

## Jupyter

Jupyter merupakan Perangkat lunak gratis, standar terbuka, dan layanan web untuk komputasi interaktif di semua bahasa pemrograman.

`JupyterLab: Antarmuka Notebook Generasi Berikutnya`

`JupyterLab` adalah lingkungan pengembangan interaktif berbasis web terbaru untuk buku catatan, kode, dan data. Antarmukanya yang fleksibel memungkinkan pengguna untuk mengonfigurasi dan mengatur alur kerja dalam ilmu data, komputasi ilmiah, jurnalisme komputasi, dan pembelajaran mesin. Desain modular mengundang ekstensi untuk memperluas dan memperkaya fungsionalitas.

`Notebook Jupyter: Antarmuka Notebook Klasik`

`Notebook Jupyter` adalah aplikasi web asli untuk membuat dan berbagi dokumen komputasi. Ini menawarkan pengalaman yang sederhana, efisien, dan berpusat pada dokumen.

  * Bahasa pilihan : Jupyter mendukung lebih dari 40 bahasa pemrograman, termasuk Python, R, Julia, dan Scala.
  * Bagikan buku catatan : Buku catatan dapat dibagikan dengan orang lain menggunakan email, Dropbox, GitHub, dan Jupyter Notebook Viewer .
  * Keluaran interaktif : Kode Kita dapat menghasilkan keluaran yang kaya dan interaktif: HTML, gambar, video, LaTeX, dan jenis MIME khusus.
  * Integrasi data besar : Manfaatkan alat data besar, seperti Apache Spark, dari Python, R, dan Scala. Jelajahi data yang sama dengan pandas, scikit-learn, ggplot2, dan TensorFlow

`Voilà: Bagikan hasil Anda`

`Voilà` membantu mengomunikasikan wawasan dengan mengubah buku catatan menjadi aplikasi web mandiri yang aman yang dapat Anda sesuaikan dan bagikan.

### Jupyterhub

`JupyterHub` menghadirkan kekuatan notebook ke grup pengguna. Ini memberi pengguna akses ke lingkungan dan sumber daya komputasi tanpa membebani pengguna dengan tugas instalasi dan pemeliharaan. Pengguna - termasuk mahasiswa, peneliti, dan ilmuwan data - dapat menyelesaikan pekerjaan mereka di ruang kerja mereka sendiri pada sumber daya bersama yang dapat dikelola secara efisien oleh administrator sistem.

`JupyterHub` berjalan di cloud atau di perangkat keras Anda sendiri, dan memungkinkan untuk menyajikan lingkungan ilmu data yang telah dikonfigurasi sebelumnya kepada pengguna mana pun di dunia. Ini dapat disesuaikan dan terukur, dan cocok untuk tim kecil dan besar, kursus akademik, dan infrastruktur skala besar.

#### Fitur utama JupyterHub

* __Dapat disesuaikan__ - JupyterHub dapat digunakan untuk melayani berbagai lingkungan. Ini mendukung lusinan kernel dengan server Jupyter, dan dapat digunakan untuk melayani berbagai antarmuka pengguna termasuk Notebook Jupyter, Jupyter Lab, RStudio, nteract, dan banyak lagi.
* __Fleksibel__ - JupyterHub dapat dikonfigurasi dengan otentikasi untuk memberikan akses ke sebagian pengguna. Otentikasi dapat dipasang, mendukung sejumlah protokol otentikasi (seperti OAuth dan GitHub).
* __Scalable__ - JupyterHub ramah terhadap container, dan dapat digunakan dengan teknologi container modern. Itu juga berjalan di Kubernetes, dan dapat berjalan dengan hingga puluhan ribu pengguna.
* __Portable__ - JupyterHub sepenuhnya open-source dan dirancang untuk dijalankan di berbagai infrastruktur. Ini termasuk penyedia cloud komersial, mesin virtual, atau bahkan perangkat keras.

## Installing Jupyter

Alat Project Jupyter tersedia untuk instalasi melalui `Python Package Index` , repositori perangkat lunak terkemuka yang dibuat untuk bahasa pemrograman Python.

Halaman ini menggunakan instruksi dengan `pip , alat instalasi yang direkomendasikan untuk Python` . Jika Anda memerlukan manajemen lingkungan bukan hanya instalasi, lihat `conda` , `mamba` , dan `pipenv` .

### JupyterLab

Instal JupyterLab dengan `pip`:

```python
pip install jupyterlab
```

__Catatan__: Jika Anda menginstal JupyterLab dengan conda atau mamba, sebaiknya gunakan saluran conda-forge .

Setelah terinstal, luncurkan JupyterLab dengan:

```python
jupyter-lab
```

#### Jupyter Notebook

Instal Notebook Jupyter klasik dengan:

```python
pip install notebook
```

Untuk menjalankan buku catatan:

```python
jupyter notebook
```

`Voila` Instal Voilà dengan:

```python
pip install voila
```

## STRUKTUR DATA
---

Pada BAB ini menjelaskan beberapa hal mengenai struktur data pada python.

### 5.1. Lebih Lanjut tentang Daftar Lists

Tipe data daftar list memiliki beberapa metode lagi. Berikut ini semua metode dari objek daftar list:

list.__append__(x)
Tambahkan item ke akhir daftar list. Setara dengan `a[len(a):] = [x]`.

list.__extend__(iterable)
Perpanjang daftar list dengan menambahkan semua item dari iterable. Setara dengan `a[len(a):] = iterable`.

list.__insert__(i, x)
Masukkan item pada posisi tertentu. Argumen pertama adalah indeks elemen sebelum memasukkan, jadi `a.insert(0, x)` memasukkan di bagian depan daftar list, dan `a.insert(len(a), x)` sama dengan `a.append(x)`.

list.__remove__(x)
Hapus item pertama dari daftar _list_ yang nilainya sama dengan x. Ini memunculkan `ValueError` jika tidak ada item seperti itu.

list.__pop__([i])
Hapus item pada posisi yang diberikan dalam daftar, dan kembalikan. Jika tidak ada indeks yang ditentukan, `a.pop()` menghapus dan mengembalikan item terakhir dalam daftar.

list.__clear__()
Hapus semua item dari daftar list. Setara dengan del `a[:]`.

list.__index__(_x_[, _start_[, _end_]])
Kembalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan _x_. Menimbulkan `ValueError` jika tidak ada item seperti itu.

Argumen opsional start dan end ditafsirkan seperti dalam notasi _slice_ dan digunakan untuk membatasi pencarian ke urutan tertentu dari daftar. Indeks yang dikembalikan dihitung relatif terhadap awal urutan penuh daripada argumen _start_.

list.__count__(x)
Kembalikan berapa kali _x_ muncul dalam daftar.

list.__sort__(_*, key=None, reverse=False_)
Urutkan item daftar di tempat (argumen dapat digunakan untuk mengurutkan ubahsuaian customization, lihat `sorted() `untuk penjelasannya).

list.__reverse__()
Balikkan elemen daftar _list_ di tempatnya.

list.__copy__()
Kembalikan salinan daftar list yang dangkal. Setara dengan `a[:]`.

Contoh yang menggunakan sebagian besar metode daftar list:

```python
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
```

metode seperti `insert`, `remove` atau `sort` yang hanya mengubah daftar list tidak memiliki nilai pengembalian yang dicetak -- mereka mengembalikan standar None. 

### 5.1.1. Menggunakan Daftar Lists sebagai Tumpukan Stacks

_Stack_, di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil ("last-in, first-out"). Untuk menambahkan item ke atas tumpukan, gunakan append(). Untuk mengambil item dari atas tumpukan, gunakan pop() tanpa indeks eksplisit. Sebagai contoh:

```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```

### 5.1.2. Menggunakan Daftar Lists sebagai Antrian Queues

`Antrian` di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil ("first-in, first-out"); namun, daftar tidak efisien untuk tujuan ini. Sementara menambahkan dan muncul dari akhir daftar cepat, melakukan memasukkan atau muncul dari awal daftar lambat (karena semua elemen lain harus digeser satu).

Untuk mengimplementasikan antrian, gunakan `collections.deque` yang dirancang untuk menambahkan dan muncul dengan cepat dari kedua ujungnya. Sebagai contoh:

```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

### 5.1.3. Daftar List Comprehensions

`List comprehensions` menyediakan cara singkat untuk membuat daftar. Aplikasi umum adalah membuat daftar baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan pada setiap anggota dari urutan lain atau _iterable_, atau untuk membuat urutan elemen-elemen yang memenuhi kondisi tertentu.

Misalnya, anggap kita ingin membuat daftar kotak, seperti:

```python
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Perhatikan bahwa ini membuat (atau menimpa) variabel bernama x yang masih ada setelah loop selesai. Kami dapat menghitung daftar kotak tanpa efek samping menggunakan:

```python
squares = list(map(lambda x: x**2, range(10)))
```

atau, dengan kata lain:

```python
squares = [x**2 for x in range(10)]
```

Pemahaman daftar _list comprehension_ terdiri dari tanda kurung yang berisi ekspresi diikuti oleh klausa for, lalu nol atau lebih klausa for atau if. Hasilnya akan menjadi daftar baru yang dihasilkan dari mengevaluasi ekspresi dalam konteks dari klausa for dan if yang mengikutinya. Sebagai contoh, _listcomp_ ini menggabungkan elemen dari dua daftar jika tidak sama:

```python
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

dan itu setara dengan:

```python
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

Perhatikan bagaimana urutan pernyataan `for` dan `if` adalah sama di kedua cuplikan ini.

Jika ekspresi adalah tuple (mis. `(x, y)` dalam contoh sebelumnya), ekspresi tersebut harus diberi kurung.

```python
>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x**2 for x in range(6)]
  File "<stdin>", line 1, in <module>
    [x, x**2 for x in range(6)]
               ^
SyntaxError: invalid syntax
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Pemahaman daftar _list comprehensions_ dapat berisi ekspresi kompleks dan fungsi bersarang:

```python
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

### 5.1.4. Pemahaman Daftar List Comprehensions Bersarang

Ekspresi awal dalam pemahaman daftar _list comprehension_ dapat berupa ekspresi acak _arbitrary_, termasuk pemahaman daftar _list comprehension_ lainnya.

Perhatikan contoh matriks 3x4 berikut yang diimplementasikan sebagai daftar _list_ 3 dari daftar _list_ panjang 4

```python
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
```

Pemahaman daftar _list comprehension_ berikut akan mengubah baris dan kolom:

```python
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

Seperti yang kita lihat di bagian sebelumnya, listcomp bersarang dievaluasi dalam konteks for yang mengikutinya, jadi contoh ini setara dengan:

```python
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

yang, pada gilirannya, sama dengan:

```python
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

memilih fungsi bawaan untuk pernyataan aliran _flow_ yang kompleks. Fungsi `zip()` akan melakukan pekerjaan yang baik untuk kasus penggunaan ini:

```python
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

### 5.2. Pernyataan del

Pernyataan `del` dapat digunakan untuk menghapus irisan dari daftar list atau menghapus seluruh daftar list (yang kita lakukan sebelumnya dengan menetapkan daftar kosong pada slice). Sebagai contoh:

```python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```

del juga dapat digunakan untuk menghapus seluruh variabel:

```python
>>> del a
```

### 5.3. Tuples and Urutan Sequences

ebuah tuple adalah urutan objek Python yang tidak berubah. Perbedaan utama antara tupel dan daftarnya adalah bahwa tupel tidak dapat diubah tidak seperti List Python. Indexing dan slicing operation merupakan contoh tipe data dari sequence. Sebuah tuple terdiri dari sejumlah nilai yang dipisahkan oleh koma, misalnya:

```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```

Seperti yang dilihat, , pada tuple keluaran selalu tertutup dalam tanda kurung, sehingga tuple bersarang nester ditafsirkan dengan benar; mereka mungkin dimasukkan dengan atau tanpa tanda kurung di sekitarnya, meskipun seringkali tanda kurung diperlukan pula (jika tuple adalah bagian dari ekspresi yang lebih besar). Tidak mungkin untuk memberikan nilai ke masing-masing item tuple, namun dimungkinkan untuk membuat tuple yang berisi objek yang bisa berubah mutable, seperti daftar.

Meskipun tuple mungkin mirip dengan daftar, tuple sering digunakan dalam situasi yang berbeda dan untuk tujuan yang berbeda. Tuples adalah immutable, dan biasanya berisi urutan elemen yang heterogen yang diakses melalui unpacking (lihat nanti di bagian ini) atau pengindeksan (atau bahkan berdasarkan atribut dalam kasus namedtuples <collections.namedtuple> `). Daftar adalah :term:`mutable(), dan elemen-elemennya biasanya homogen dan diakses dengan menyusuri iterating daftar list.

Masalah khusus adalah pembangunan tuple yang mengandung 0 atau 1 item: sintaksis memiliki beberapa kebiasaan quirks tambahan untuk mengakomodasi ini. Tuple kosong dibangun oleh sepasang kurung kosong; tupel dengan satu item dikonstruksi dengan mengikuti nilai dengan koma (tidak cukup untuk menyertakan nilai tunggal dalam tanda kurung). Jelek, tapi efektif. Sebagai contoh:

```python
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
```

Pernyataan t = 12345, 54321, 'hello!' Adalah contoh dari tuple packing: nilainya 12345, 54321 dan 'hello!' Dikemas bersama-sama dalam tuple. Operasi terbalik juga dimungkinkan

```python
>>> x, y, z = t
```

### 5.4. Himpunan Set

Python juga menyertakan tipe data untuk sets. Himpunan atau Set adalah koleksi yang tidak terurut tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat.

sama seperti Kurung kurawal, fungsi set() dapat digunakan untuk membuat himpunan. Catatan: untuk membuat himpunan kosong Anda harus menggunakan set(), bukan {}.

Berikut ini adalah demonstrasi singkat:

```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

Seperti halnya untuk list comprehensions, set comprehensions juga didukung:

```python
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```

### 5.5. Kamus Dictionaries

Tipe data lain yang berguna yang dibangun ke dalam Python adalah dictionary. Kamus dictionary kadang-kadang ditemukan dalam bahasa lain sebagai "assosiative memories" atau "assosiative array". Tidak seperti urutan sequences, yang diindeks oleh sejumlah angka, kamus dictionary diindeks oleh keys, yang dapat berupa jenis apa pun yang tidak dapat diubah immutable type. string dan angka selalu bisa menjadi kunci key.

Operasi utama pada kamus dictionary adalah menyimpan nilai dengan beberapa kunci key dan mengekstraksi nilai yang diberikan kunci key. Dimungkinkan juga untuk menghapus pasangan kunci:nilai dengan del. Jika Anda menyimpan menggunakan kunci yang sudah digunakan, nilai lama yang terkait dengan kunci itu dilupakan. Merupakan kesalahan untuk mengekstraksi nilai menggunakan kunci yang tidak ada.

Ini adalah contoh kecil menggunakan kamus dictionary:

```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```

Pembangun constructor dict() membangun kamus langsung dari urutan pasangan kunci-nilai:

```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

Selain itu, pemahaman kamus dict _comprehensions_ dapat digunakan untuk membuat kamus _dictionary_ dari ekspresi kunci dan nilai acak _arbitrary_:

```python
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

Ketika kunci adalah string sederhana, kadang-kadang lebih mudah untuk menentukan pasangan menggunakan argumen kata kunci _keyword arguments_:

```python
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

### 5.6. Teknik Perulangan

Saat mengulang kamus _dictionaries_, kunci _key_ dan _nilai_ value terkait dapat diambil pada saat yang sama menggunakan metode _items()_.

```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```

Saat mengulang melalui urutan, indeks posisi dan nilai terkait dapat diambil pada saat yang sama menggunakan fungsi `enumerate()`.

```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
```

Untuk mengulang dua urutan atau lebih secara bersamaan, entri dapat dipasangkan dengan fungsi `zip()`.

```python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

Untuk mengulang urutan secara terbalik, pertama tentukan urutan dalam arah maju dan kemudian panggil fungsi `reversed()`.

```python
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
```

Untuk mengulangi sebuah urutan sequence dalam susunan yang diurutkan, gunakan fungsi _sort()_ yang mengembalikan daftar terurut baru dengan membiarkan sumber tidak diubah.

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
apple
apple
banana
orange
orange
pear
```

Menggunakan `set()` pada sebuah urutan dapat menghilangkan elemen-elemen yang duplikat. Penggunaan `sorted()` yang dikombinasikan dengan `set()` terhadap sebuah urutan merupakan cara idiomatik untuk _loop_ dari elemen-elemen unik dari urutan yang diurutkan.

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
```

Mengubah daftar list saat Kita mengulanginya; namun, seringkali lebih mudah dan aman untuk membuat daftar _list_ baru.

```python
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```

### 5.7. Lebih lanjut tentang Kondisi

Kondisi yang digunakan dalam pernyataan while dan if dapat berisi operator apa pun, bukan hanya perbandingan.

Perbandingan bisa dibuat berantai. Sebagai contoh, a < b == c menguji apakah a kurang dari b dan apa b sama dengan c.

Perbandingan dapat digabungkan menggunakan operator Boolean and dan or, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat dinegasikan dengan not. Ini memiliki prioritas lebih rendah daripada operator pembanding; di antara mereka, not memiliki prioritas tertinggi dan or terendah, sehingga A and not B or C setara dengan (A and (not B)) or C . Seperti biasa, tanda kurung dapat digunakan untuk mengekspresikan komposisi yang diinginkan.

Operator Boolean and dan or disebut operator short-circuit: argumen mereka dievaluasi dari kiri ke kanan, dan evaluasi berhenti segera setelah hasilnya ditentukan. Misalnya, jika A dan C bernilai benar tetapi B salah, A and B and C tidak mengevaluasi ekspresi C. Ketika digunakan sebagai nilai umum dan bukan sebagai Boolean, nilai kembalian dari operator hubung singkat short-circuit adalah argumen terakhir yang dievaluasi.

Dimungkinkan untuk menetapkan hasil perbandingan atau ekspresi Boolean lainnya ke variabel. Sebagai contoh,

```python
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
```

### 5.8. Membandingkan Urutan Sequences dan Jenis Lainnya

Objek urutan sequence biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. Perbandingan menggunakan pengurutan `lexicographical`:

pertama, dua item pertama dibandingkan, dan jika mereka berbeda ini menentukan hasil perbandingan; jika mereka sama, dua item berikutnya dibandingkan, dan seterusnya, sampai urutan mana pun habis.

Pengurutan leksikografis untuk string menggunakan nomor titik kode Unicode untuk mengurutkan masing-masing karakter. Beberapa contoh perbandingan antara urutan dengan tipe yang sama:

```python
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```