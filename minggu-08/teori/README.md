# BAB 10 Brief Tour of the Standard Library — Part I

## 10.1. Antarmuka Sistem Operasi (Operating System Interface)

Modul os menyediakan puluhan fungsi untuk berinteraksi dengan sistem operasi:

```python
>>> import os
>>> os.getcwd()      # Return the current working directory
'C:\\Python310'
>>> os.chdir('/server/accesslogs')   # Change current working directory
>>> os.system('mkdir today')   # Run the command mkdir in the system shell
0
```

Gunakan gaya `import os` alih-alih `from os import *`. Ini akan menjaga `os.open()` dari membayangi shadowing fungsi bawaan `open()` yang beroperasi jauh berbeda.

Fungsi bawaan `dir()` dan `help()` berguna sebagai alat bantu interaktif untuk bekerja dengan modul besar seperti `os`:

```python
>>> import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>
```

Untuk tugas manajemen berkas dan direktori sehari-hari, modul `shutil` menyediakan antarmuka level yang lebih tinggi yang lebih mudah digunakan:

```python
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'
```

## 10.2. Berkas Wildcard (File Wildcards)

Modul `glob` menyediakan fungsi untuk membuat daftar berkas dari pencarian `wildcard` di direktori:

```python
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
```

## 10.3. Baris Perintah Berargumen (Command Line Arguments)

Argumen ini disimpan dalam atribut `argv` dari modul `sys` sebagai daftar. Sebagai contoh, hasil keluaran berikut dari menjalankan `python demo.py one two three` di baris perintah

```python
>>> import sys
>>> print(sys.argv)
['demo.py', 'one', 'two', 'three']
```

Modul `argparse` menyediakan mekanisme yang lebih canggih untuk memproses argumen baris perintah. Script berikut mengekstrak satu atau lebih nama file dan baris opsional untuk ditampilkan:

```python
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
```

Ketika dijalankan pada baris perintah dengan `python top.py --lines=5 alpha.txt beta.txt`, skrip mengatur `args.lines` menjadi 5 dan `args.filenames` menjadi `['alpha.txt', 'beta.txt'].`

## 10.4. Pengalihan Output Kesalahan dan Pengakhiran Program (Error Output Redirection and Program Termination)

Modul `sys` memiliki atribut untuk `stdin, stdout, dan stderr`. Yang terakhir berguna untuk mengirimkan peringatan dan pesan kesalahan untuk membuatnya terlihat bahkan ketika stdout telah dialihkan:

```python
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
```

Cara paling langsung untuk mengakhiri skrip adalah dengan menggunakan `sys.exit()`.

## 10.5. Pencocokan Pola String (String Pattern Matching)

Modul `re` menyediakan alat ekspresi reguler untuk pemrosesan `string lanjutan`. Untuk pencocokan dan manipulasi yang kompleks, ekspresi reguler menawarkan solusi yang ringkas dan dioptimalkan:

```python
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
```

Ketika hanya kemampuan sederhana yang diperlukan, metode string lebih disukai karena lebih mudah dibaca dan dilakukan debug:

```python
>>> 'tea for too'.replace('too', 'two')
'tea for two'
```

## 10.6. Matematika (Mathematics)

Modul `math` memberikan akses ke fungsi-fungsi pustaka `C` yang mendasari untuk matematika angka pecahan `floating point`:

```python
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0
```

Modul `random` menyediakan alat untuk membuat pilihan acak:

```python
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float
0.17970987693706186
>>> random.randrange(6)    # random integer chosen from range(6)
4
```

Modul `statistics` menghitung sifat statistik dasar (rata-rata, median, varian, dll.) dari data numerik:

```python
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
```

## 10.7. Akses internet (Internet Access)

Ada modul untuk mengakses internet dan memproses protokol internet. Yang paling sederhana adalah `urllib.request` untuk mengambil data dari URL dan `smtplib` untuk mengirim email:

```python
>>> from urllib.request import urlopen
>>> with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
...     for line in response:
...         line = line.decode()             # Convert bytes to a str
...         if line.startswith('datetime'):
...             print(line.rstrip())         # Remove trailing newline
...
datetime: 2022-01-01T01:36:47.689215+00:00

>>> import smtplib
>>> server = smtplib.SMTP('localhost')
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
... """To: jcaesar@example.org
... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)
>>> server.quit()
```

## 10.8. Tanggal dan Waktu (Dates and Times)

Modul `datetime` menyediakan kelas untuk memanipulasi tanggal dan waktu dengan cara yang sederhana dan kompleks. Sementara aritmatika tanggal dan waktu didukung, fokus implementasi adalah pada ekstraksi anggota yang efisien untuk pemformatan dan manipulasi keluaran. Modul ini juga mendukung objek yang sadar zona waktu.

```python
>>> # dates are easily constructed and formatted
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

>>> # dates support calendar arithmetic
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368
```

## 10.9. Kompresi Data (Data Compression)

Format pengarsipan dan kompresi data umum didukung langsung oleh modul-modul yang ada antara lain: :mod: `zlib, gzip, bz2, lzma, zipfile dan tarfile`.

```python
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
```

## 10.10. Pengukuran Kinerja (Performance Measurement)

Beberapa pengguna Python mengembangkan minat yang mendalam untuk mengetahui kinerja relatif dari berbagai pendekatan untuk masalah yang sama. Misalnya, dapat menggunakan fitur `tuple packing` dan `unpacking` daripada pendekatan tradisional untuk bertukar argumen. Modul :mod:` timeit` dengan cepat menunjukkan keunggulan kinerja secara sederhana:

```python
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791
```

Berbeda dengan granularity tingkat halus `timeit`, modul `profile` dan `pstats` menyediakan alat untuk mengidentifikasi bagian kritis waktu dalam blok kode yang lebih besar.

## 10.11. Kontrol Kualitas (Quality Control)

Salah satu pendekatan untuk mengembangkan perangkat lunak berkualitas tinggi adalah dengan menulis tes untuk setiap fungsi yang dikembangkan dan untuk sering menjalankan tes tersebut selama proses pengembangan.

Modul: mod:`doctest` menyediakan alat untuk memindai modul dan memvalidasi tes yang tertanam dalam dokumen program. Konstruksi pengujian sesederhana memotong dan menempel panggilan khas beserta hasilnya ke dalam docstring. Ini meningkatkan dokumentasi dengan memberikan contoh kepada pengguna dan memungkinkan modul `doctest` untuk memastikan kode tetap benar untuk dokumentasi:

```python
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests
```

Modul `unittest` tidak semudah modul `doctest`, tetapi memungkinkan serangkaian tes yang lebih komprehensif untuk dipertahankan dalam file terpisah:

```python
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests
```

## 10.12. Dilengkapi Baterai (Batteries Included)

Python memiliki filosofi `"dilengkapi baterai"`. Ini paling baik dilihat melalui kemampuan yang canggih dan kuat robust dengan dukungan paket-paket yang lebih besar. Sebagai contoh:

   * Modul `xmlrpc.client` dan `xmlrpc.server` membuat penerapan panggilan prosedur jarak jauh menjadi tugas yang hampir sepele. Terlepas dari nama-nama modul, tidak diperlukan pengetahuan atau penanganan XML secara langsung.
   * Paket `email` adalah pustaka untuk mengelola pesan email, termasuk `MIME` dan lainnya `RFC 2822` dokumen pesan berbasis. Tidak seperti `smtplib dan poplib` yang benar-benar mengirim dan menerima pesan, paket `email` memiliki `toolset` lengkap untuk membangun atau mendekodekan struktur pesan kompleks (termasuk lampiran) dan untuk mengimplementasikan pengkodean `internt` dan `protokol header`.
   * Paket `json` menyediakan dukungan kuat untuk mengurai format pertukaran data populer ini. Modul `csv` mendukung pembacaan dan penulisan berkas secara langsung dalam format Nilai Terpisah-Koma atau CSV, umumnya didukung oleh database dan spreadsheet. Pemrosesan XML didukung oleh paket `xml.etree.ElementTree, xml.dom dan xml.sax`. Bersama-sama, modul dan paket ini sangat menyederhanakan pertukaran data antara aplikasi Python dan alat lainnya.
   * Modul `sqlite3` adalah pembungkus untuk pustaka basis data SQLite, menyediakan basis data persisten yang dapat diperbarui dan diakses menggunakan sintaks SQL yang sedikit tidak standar.
   * Internasionalisasi didukung oleh sejumlah modul termasuk paket `gettext, locale, dan codecs`.


# BAB 11 Brief Tour of the Standard Library — Part II

Tur kedua ini mencakup modul lanjutan yang mendukung kebutuhan pemrograman profesional. Modul-modul ini jarang terjadi dalam skrip kecil.

---

## 11.1. Pemformatan Output (Output Formatting)

Modul `reprlib` menyediakan versi `repr()` yang disesuaikan untuk tampilan yang disingkat dari wadah `containers` yang besar atau sangat bersarang

```python
>>> import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"
```

Modul `pprint` menawarkan kontrol yang lebih canggih atas pencetakan objek bawaan dan yang ditentukan pengguna dengan cara yang dapat dibaca oleh `interpreter`. Ketika hasilnya lebih dari satu baris, `"pretty printer"` menambahkan jeda baris dan indentasi untuk lebih jelas mengungkapkan struktur data:

```python
>>> import pprint
>>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
...     'yellow'], 'blue']]]
...
>>> pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
```

Modul `textwrap` memformat paragraf teks agar sesuai dengan lebar layar yang diberikan:

```python
>>> import textwrap
>>> doc = """The wrap() method is just like fill() except that it returns
... a list of strings instead of one big string with newlines to separate
... the wrapped lines."""
...
>>> print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
```

Modul `locale` mengakses basis data format data kultur khusus. Atribut pengelompokan fungsi format lokal `locale` menyediakan cara langsung memformat angka dengan pemisah grup:

```python
>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
>>> conv = locale.localeconv()          # get a mapping of conventions
>>> x = 1234567.8
>>> locale.format("%d", x, grouping=True)
'1,234,567'
>>> locale.format_string("%s%.*f", (conv['currency_symbol'],
...                      conv['frac_digits'], x), grouping=True)
'$1,234,567.80'
```

## 11.2. Templating (Templating)

Modul `string` menyertakan kelas serbaguna `Template` dengan sintaks yang disederhanakan yang cocok untuk diedit oleh pengguna. Ini memungkinkan pengguna untuk menyesuaikan aplikasi mereka tanpa harus mengubah aplikasi.

Format ini menggunakan nama penampung yang dibentuk oleh `$` dengan pengidentifikasi Python yang valid (karakter alfanumerik dan garis bawah). Mengitari placeholder dengan kurung kurawal memungkinkannya diikuti oleh lebih banyak huruf alfanumerik tanpa spasi. Menulis `$$` menciptakan satu yang terpisah `$`

```python
>>> from string import Template
>>> t = Template('${village}folk send $$10 to $cause.')
>>> t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'
```

Metode `substitute()` memunculkan `KeyError` saat `placeholder` tidak disertakan dalam `dictionary` atau argumen kata kunci `keyword argument`. Untuk aplikasi gaya gabungan-surat `mail-merge`, data yang diberikan pengguna mungkin tidak lengkap dan metode `safe_substitute()` mungkin lebih tepat --- itu akan membuat `placeholder` tidak berubah jika data hilang

```python
>>> t = Template('Return the $item to $owner.')
>>> d = dict(item='unladen swallow')
>>> t.substitute(d)
Traceback (most recent call last):
  ...
KeyError: 'owner'
>>> t.safe_substitute(d)
'Return the unladen swallow to $owner.'
```

Subkelas templat dapat menentukan pembatas khusus. Misalnya, utilitas penggantian nama setumpuk _batch_ untuk _browser_ foto dapat memilih untuk menggunakan tanda persen untuk penampung seperti tanggal saat ini, nomor urut gambar, atau format berkas:

```python
>>> import time, os.path
>>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
>>> class BatchRename(Template):
...     delimiter = '%'
>>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

>>> t = BatchRename(fmt)
>>> date = time.strftime('%d%b%y')
>>> for i, filename in enumerate(photofiles):
...     base, ext = os.path.splitext(filename)
...     newname = t.substitute(d=date, n=i, f=ext)
...     print('{0} --> {1}'.format(filename, newname))

img_1074.jpg --> Ashley_0.jpg
img_1076.jpg --> Ashley_1.jpg
img_1077.jpg --> Ashley_2.jpg
```

## 11.3. Bekerja dengan Tata Letak Rekam Data Biner (Working with Binary Data Record Layouts)

Modul __struct__ menyediakan __pack()__ dan __unpack()__ berfungsi untuk bekerja dengan format rekaman biner yang memiliki panjang variabel. Contoh berikut menunjukkan bagaimana cara loop tajuk _header_ informasi dalam berkas ZIP tanpa menggunakan modul __zipfile__. Kode paket `"H"` dan `"I"` masing-masing mewakili dua dan empat byte angka yang tidak bertanda unsigned. `"<"` Menunjukkan bahwa mereka adalah ukuran standar dan dalam urutan byte _little-endian_:

```python
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header
```

## 11.4. Multi-threading (Multi-threading)

`Threading` adalah teknik untuk memisahkan tugas yang tidak tergantung secara berurutan. Utas _threads_ dapat digunakan untuk meningkatkan responsif aplikasi yang menerima masukan pengguna saat tugas lain beroperasi di latar belakang. Kasus penggunaan terkait menjalankan I/O secara paralel dengan perhitungan di utas _thread_ lainnya.

Kode berikut menunjukkan bagaimana tingkat tinggi modul:mod:`threading` dapat menjalankan tugas di latar belakang sementara program utama terus beroperasi:

```python
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')
```

## 11.5. Pencacatan (Logging)

Modul __logging__ menawarkan sistem pencatatan _logging_ yang lengkap dan fleksibel. Paling sederhana, catatan _log_ pesan dikirim ke berkas atau ke `sys.stderr`:

```python
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
```

Script di atas menghasilkan tampilan berikut:

```python
WARNING:root:Warning:config file server.conf not found
ERROR:root:Error occurred
CRITICAL:root:Critical error -- shutting down
```

Secara bawaan, pesan informasi dan _debugging_ ditutupi suppressed dan keluaran dikirim ke standar kesalahan. Opsi keluaran lainnya termasuk merutekan pesan melalui email, datagram, soket, atau ke Server HTTP. Filter baru dapat memilih rute berbeda berdasarkan prioritas pesan: `DEBUG, INFO, WARNING, ERROR, dan CRITICAL`.

## 11.6. Referensi yang Lemah (Weak References)

Python melakukan manajemen memori otomatis (penghitungan referensi untuk sebagian besar objek dan garbage _collection_ untuk menghilangkan siklus). Memori dibebaskan tidak lama setelah referensi terakhir untuk itu telah dihilangkan.

Modul __weakref__ menyediakan alat untuk melacak objek tanpa membuat referensi. Ketika objek tidak lagi diperlukan, itu secara otomatis dihapus dari tabel _weakref_ dan panggilan balik _callback_ dipicu untuk _weakref_. Aplikasi yang umum termasuk caching objek yang mahal untuk dibuat:

```python
>>> import weakref, gc
>>> class A:
...     def __init__(self, value):
...         self.value = value
...     def __repr__(self):
...         return str(self.value)
...
>>> a = A(10)                   # create a reference
>>> d = weakref.WeakValueDictionary()
>>> d['primary'] = a            # does not create a reference
>>> d['primary']                # fetch the object if it is still alive
10
>>> del a                       # remove the one reference
>>> gc.collect()                # run garbage collection right away
0
>>> d['primary']                # entry was automatically removed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary']                # entry was automatically removed
  File "C:/python310/lib/weakref.py", line 46, in __getitem__
    o = self.data[key]()
KeyError: 'primary'
```

## 11.7. Alat untuk Bekerja dengan Daftar Lists (Tools for Working with Lists)

Modul __array__ menyediakan objek __array()__ yang seperti daftar _list_ dimana hanya menyimpan data homogen dan menyimpannya dengan lebih kompak. Contoh berikut menunjukkan array angka yang disimpan sebagai dua byte angka biner yang tidak ditandai (kode tipe `"H"`) daripada 16 byte per entri biasa untuk daftar _list_ reguler objek int Python:

```python
>>> from array import array
>>> a = array('H', [4000, 10, 700, 22222])
>>> sum(a)
26932
>>> a[1:3]
array('H', [10, 700])
```

Modul __collections__ menyediakan objek __deque()__ yang seperti daftar _list_ dengan tambahan yang lebih cepat dan muncul dari sisi kiri tetapi pencarian yang lebih lambat di tengah. Objek-objek ini sangat cocok untuk mengimplementasikan antrian dan pencarian pohon pertama yang luas _breadth first tree searches:_

```python
>>> from collections import deque
>>> d = deque(["task1", "task2", "task3"])
>>> d.append("task4")
>>> print("Handling", d.popleft())
Handling task1
```

```python
unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)
```

Selain implementasi daftar _list_ alternatif, di pustaka juga menawarkan alat-alat lain seperti modul __bisect__ dengan fungsi untuk memanipulasi daftar _list_ yang diurutkan:

```python
>>> import bisect
>>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
>>> bisect.insort(scores, (300, 'ruby'))
>>> scores
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
```

Modul __heapq__ menyediakan fungsi untuk mengimplementasikan _heaps_ berdasarkan daftar _list_ reguler. Entri dengan nilai terendah selalu disimpan di posisi nol. Ini berguna untuk aplikasi yang berulang kali mengakses elemen terkecil tetapi tidak ingin mengoperasikan daftar pengurutan _list_ secara penuh:

```python
>>> from heapq import heapify, heappop, heappush
>>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
>>> heapify(data)                      # rearrange the list into heap order
>>> heappush(data, -5)                 # add a new entry
>>> [heappop(data) for i in range(3)]  # fetch the three smallest entries
[-5, 0, 1]
```

## 11.8. Aritmatika Pecahan Floating Point Desimal (Decimal Floating Point Arithmetic)

Modul __decimal__ menawarkan __Decimal__ tipe data untuk aritmatika pecahan desimal. Dibandingkan dengan implementasi bawaan __float__ dari pecahan _floating point_ biner

   * aplikasi keuangan dan penggunaan lainnya yang membutuhkan representasi desimal yang tepat,
   * kontrol atas presisi,
   * kontrol atas pembulatan untuk memenuhi persyaratan sah legal atau peraturan,
   * pelacakan tempat desimal yang signifikan, atau
   * aplikasi tempat pengguna mengharapkan hasil agar sesuai dengan perhitungan yang dilakukan dengan tangan.

Misalnya, menghitung pajak 5% pada biaya telepon 70 sen memberikan hasil berbeda dalam pecahan _floating point_ desimal dan pecahan _floating point_ biner. Perbedaannya menjadi signifikan jika hasilnya dibulatkan ke sen terdekat:

```python
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round(.70 * 1.05, 2)
0.73
```

Hasil __Decimal__ menjaga akhiran _trailing_ nol, secara otomatis menyimpulkan empat tempat signifikansi dari _multiplicands_ dengan dua tempat signifikansi. Desimal mereproduksi matematika seperti yang dilakukan dengan tangan dan menghindari masalah yang dapat muncul ketika pecahan _floating point_ biner tidak dapat secara tepat mewakili jumlah desimal.

Representasi yang tepat memungkinkan kelas __Decimal__ untuk melakukan perhitungan modulo dan tes persamaan yang tidak cocok untuk angka pecahan _floating point_ biner:

```python
>>> Decimal('1.00') % Decimal('.10')
Decimal('0.00')
>>> 1.00 % 0.10
0.09999999999999995

>>> sum([Decimal('0.1')]*10) == Decimal('1.0')
True
>>> sum([0.1]*10) == 1.0
False
```

Modul __decimal__ menyediakan aritmatika dengan ketelitian sebanyak yang dibutuhkan:

```python
>>> getcontext().prec = 36
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857')
```
