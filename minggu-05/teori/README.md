# BAB 7 Input(Masukan) dan Output(keluaran) (I/O)

Ada beberapa cara dalam mempresentasikan keluaran suatu program. Di mana data akan dicetak dalam bentuk dan dapat dibaca oleh manusia, atau ditulis ke berkas untuk digunakan di masa mendatang.

---

## 7.1. Pemformatan Keluaran yang Lebih menarik

Dalam python terdapat dua cara penulisan nilai yaitu `expression statements` dan fungsi `print()`. lalu cara ketiga menggunakan write() berkas keluaran standar dapat dirujuk sebagai `sys.stdout`.

Ada beberapa cara untuk memformat keluaran yaitu:
  * Untuk menggunakan `formatted string literals`, mulailah string dengan `f` atau `F` sebelum tanda kutip pembuka atau tanda kutip tiga. Dalam string ini, kita bisa menulis ekspresi Python antara karakter `{` dan `}` yang dapat merujuk ke variabel atau nilai literal.

```python
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
```

  * Metode `str.format()` dari string membutuhkan lebih banyak upaya manual. Kita biasanya menggunakan `{` dan `}` untuk menandai di mana variabel akan diganti dan dapat memberikan arahan pemformatan terperinci.

```python
>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
```

  * Lalu yang terakhir, melakukan semua string yang menanganinya menggunakan operasi `slicing string` dan `concatenation` untuk membuat tata letak.

Ketika kita tidak membutuhkan keluaran yang menarik tetapi hanya ingin tampilan cepat dari beberapa variabel untuk keperluan `debugging`, kita dapat mengonversi nilai apapun menjadi string dengan fungsi `repr()` atau `str()`.

Fungsi `str()` dimaksudkan untuk mengembalikan representasi nilai-nilai yang terbaca oleh manusia, sementara `repr()` dimaksudkan untuk menghasilkan representasi yang dapat dibaca oleh penerjemah (interpreter atau akan memaksa `SyntaxError` jika tidak ada sintaks yang setara). jika objek yang tidak memiliki representasi yang sama,  `str()` akan mengembalikan nilai yang sama dengan `repr()` . Beberapa contoh Fungsi tersebut ialah:

```python
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
... hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
... repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```

Modul `string` berisi kelas `Template` yang menawarkan cara lain untuk menggantikan nilai menjadi string.

**7.1.1. Literal String Terformat**

`Formatted string literals`  (juga disebut f-string) memungkinkan kita dalam menyertakan nilai ekspresi Python di dalam string dengan mengawali string dengan `f` atau `F` dan menulis ekspresi sebagai `{expression}`.

Contoh berikut ini pembulatan pi ke tiga tempat setelah desimal:

```python
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
```

Melewatkan bilangan bulat setelah `:` akan menyebabkan `field` lalu hal itu menjadi jumlah minimum lebar karakter. Ini berguna untuk membuat kolom berbaris.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```

Pengubah lain yang dapat digunakan untuk mengonversi nilai sebelum diformat. `!a` berlaku untuk `ascii()`, `!s` berlaku untuk `str()`, dan `!r` berlaku untuk `repr()`:

```python
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```

**7.1.2. Metode String format()**

Penggunaan dasar metode `str.format()` terlihat seperti dibawah ini:

```python
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```

Tanda kurung dan karakter di dalamnya (disebut juga dengan fields format) diganti dengan objek yang diteruskan ke metode `str.format()`. Angka dalam tanda kurung dapat digunakan untuk merujuk ke posisi objek yang dilewatkan ke dalam metode `str.format()`.

```python
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```

ketika argumen kata kunci `keyword argument` digunakan dalam metode `str.format()`, nilainya dirujuk dengan menggunakan nama argumen.

```python
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```

Argumen posisi dan kata kunci dapat dikombinasikan secara bergantian yaitu:

```python
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
The story of Bill, Manfred, and Georg.
```

Ketika memiliki string format yang sangat panjang yang tidak ingin kita pisahkan, dan jika kita bisa mereferensikan variabel yang akan diformat berdasarkan nama daripada berdasarkan posisi. Hal tersebut dapat dilakukan hanya dengan melewatkan `dict` dan menggunakan tanda kurung siku `[]` untuk mengakses kunci dari `dict`.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

Hal ini juga dapat dilakukan dengan memberikan tabel sebagai argumen kata kunci `keyword argument` dengan notasi `**`.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

Hal ini sangat berguna dalam kombinasi dengan fungsi bawaan `vars()`, yang mengembalikan dictionary yang berisi semua variabel lokal.

Sebagai contoh, baris-baris berikut menghasilkan kumpulan kolom yang disejajarkan rapi memberikan bilangan bulat, kotak, dan kubusnya:

```python
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

**7.1.3. Pemformatan String Manual**

Berikut tabel kotak dan kubus yang sama, yang diformat secara manual:

```python
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # Note use of 'end' on previous line
...     print(repr(x*x*x).rjust(4))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

Metode `str.rjust()` dari objek string merata-kanan-kan sebuah string dalam bidang dengan lebar tertentu dengan menambahkannya dengan spasi di sebelah kiri. Ada metode serupa `str.ljust()` dan `str.center()`.(Jika kita benar-benar menginginkan pemotongan, kita selalu dapat menambahkan operasi `slice`, seperti pada `x.ljust(n)[:n]`.)

Ada metode lain, `str.zfill()`, yang melapisi string numerik di sebelah kiri dengan nol. Metode tersebut mengerti tentang tanda plus dan minus:

```python
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
```

**7.1.4. Pemformatan string lama**

Operator `%` (modulo) dapat digunakan untuk pemformatan string. Akan diberikan `string % values`, instansiasi dari `%` di `string` diganti dengan nol atau elemen yang lebih dari `values`. Contohnya sebagai berikut:

```python
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```

## 7.2. Membaca dan Menulis Berkas

Fungsi `open()` mengembalikan sebuah `file object`, dan paling umum digunakan dengan dua argumen: `open(filename, mode)`.

```python
>>> f = open('workfile', 'w')
```

Pada Argumen pertama adalah string yang berisi nama file. Argumen kedua adalah string lain yang berisi beberapa karakter. Mode menggunakan `r` ketika file hanya akan dibaca, lalu `w` digunakan untuk menulis (berkas yang ada dengan nama yang sama akan dihapus), dan mode `a` digunakan untuk membuka berkas untuk ditambahkan. Setiap data yang ditulis ke file secara otomatis ditambahkan ke bagian akhir. setelah itu, mode `r+` membuka berkas untuk membaca dan menulis. Argumen mode adalah opsional, `r` akan diasumsikan jika dihilangkan.

Berikut adalah praktik yang baik untuk menggunakan kata kunci `with` saat berurusan dengan objek file. Keuntungannya adalah bahwa file ditutup dengan benar setelah rangkaiannya selesai, bahkan jika suatu pengecualian muncul di beberapa titik. Menggunakan `with` juga jauh lebih pendek daripada penulisan yang setara `try-blok finally`:

```python
>>> with open('workfile') as f:
...     read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True
```

Setelah objek file ditutup, baik dengan pernyataan `with` atau dengan memanggil `f.close()`, upaya untuk menggunakan objek file akan otomatis gagal.

```python
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

**7.2.1. Metode Objek Berkas**

Ketika membaca konten file bisa dengan memanggil `f.read(size)`, yang membaca sejumlah kuantitas data dan mengembalikannya sebagai string (dalam mode teks) atau objek byte (dalam mode biner). size adalah argumen numerik opsional. Ketika size dihilangkan atau negatif, seluruh isi file akan dibaca dan dikembalikan; itu masalah kita jika file tersebut dua kali lebih besar dari memori mesin kita. Kalau tidak, paling banyak size karakter (dalam mode teks) atau size byte (dalam mode biner) dibaca dan dikembalikan. Jika akhir file telah tercapai, `f.read()` akan mengembalikan string kosong `('')`.

```python
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
```

`f.readline()` membaca satu baris dari file, karakter baris baru `(\n)` dibiarkan di akhir string, dan hanya dihapus pada baris terakhir file ketika file tidak berakhir pada baris baru. hal tersebut akan membuat nilai pengembalian tidak ambigu. lalu `f.readline()` mengembalikan string kosong, akhir file telah tercapai, sementara baris kosong diwakili oleh `\n`, string yang hanya berisi satu baris baru.

```python
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
```

Untuk membaca baris dari file, kita dapat mengulangi objek berkas. Hal ini dapat menghemat memori, cepat, dan mengarah ke kode sederhana sebagai contoh berikut:

```python
>>> for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the file
```

Jika ingin membaca semua baris file dalam daftar `list`, dapat menggunakan `list(f)` atau `f.readlines()`.

Fungsi `f.write(string)` dapat menulis konten string ke berkas, mengembalikan jumlah karakter yang ditulis.

```python
>>> f.write('This is a test\n')
15
```

Jenis objek lain perlu dikonversi baik menjadi string (dalam mode teks) atau objek byte (dalam mode biner) sebelum menulisnya:

```python
>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18
```

`f.tell()` mengembalikan integer yang memberikan posisi objek file saat ini dalam berkas yang direpresentasikan sebagai jumlah byte dari awal berkas ketika dalam mode biner dan angka buram `opaque` ketika dalam mode teks.

Ketika ingin mengubah posisi objek file, gunakan `f.seek(offset, whence)`. Posisi dihitung dari menambahkan offset ke titik referensi. Titik referensi dipilih oleh argumen `whence`. Nilai A whence dari 0 mengukur dari awal berkas, 1 menggunakan posisi file saat ini, dan 2 menggunakan akhir file sebagai titik referensi. `whence` dapat dihilangkan dan default ke 0, menggunakan awal file sebagai titik referensi.

```python
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
```

**7.2.2. Menyimpan data terstruktur dengan json**

String dapat dengan mudah ditulis dan dibaca dari file. Angka membutuhkan sedikit usaha, karena metode `read()` hanya mengembalikan string, yang harus diteruskan ke fungsi seperti `int()`, yang mengambil string seperti `123` dan mengembalikan nilai numerik 123. Ketika kita ingin menyimpan tipe data yang lebih kompleks seperti daftar list dan dictionary bersarang, penguraian dan pembuatan serialisasi dengan tangan menjadi rumit.

Python memungkinkan kita untuk menggunakan format pertukaran data populer yang disebut dengan `JSON` (JavaScript Object Notation). Modul standar bernama `json` dapat mengambil hierarki data Python, dan mengubahnya menjadi representasi string. Proses ini disebut serializing. Kemudian Merekonstruksi data dari representasi string disebut deserializing. Antara serializing dan deserializing, string yang mewakili objek mungkin telah disimpan dalam berkas atau data, atau dikirim melalui koneksi jaringan ke beberapa mesin yang jauh.

jika kita memiliki objek `x`, kita dapat melihat representasi string `JSON` dengan baris kode sederhana:

```python
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'
```

Varian lain dari fungsi `dumps()`. Kenapa disebut `dump()`, karena dengan mudah membuat serialisasi objek menjadi `:term:` text file. Jadi jika `f` adalah objek text file dibuka untuk menulis, kita dapat melakukan ini:

```python
json.dump(x, f)
```

Untuk menerjemahkan `decode` objek lagi, jika `f` adalah objek text file yang telah dibuka untuk membaca:

```python
x = json.load(f)
```

Teknik serialisasi sederhana ini dapat menangani daftar list dan dictionary.