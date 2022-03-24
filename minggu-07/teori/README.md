# BAB 9 Classes

`Classes` atau kelas-kelas menyediakan sarana untuk menggabungkan data dan fungsionalitas bersama. Membuat sebuah class baru untuk menghasilkan objek dengan type baru, yang memungkinkan dibuatnya `instance` baru dari tipe itu. Setiap `instance` dari `class` dapat memiliki atribut yang melekat padanya untuk mempertahankan kondisi. `Instance` dari sebuah `class` juga dapat memiliki metode (ditentukan oleh class) untuk memodifikasi kondisinya.

Dibandingkan dengan bahasa pemrograman lain, mekanisme kelas Python menambah kelas dengan minimum sintaksis dan semantik baru. Hal ini adalah campuran dari mekanisme kelas yang ditemukan dalam C++ dan Modula-3. Kelas Python menyediakan semua fitur standar Pemrograman Berorientasi Objek: mekanisme pewarisan kelas memungkinkan beberapa kelas dasar, kelas turunan dapat menimpa metode apa pun dari kelas dasar atau kelasnya, dan metode dapat memanggil metode kelas dasar dengan nama yang sama . Objek dapat berisi jumlah dan jenis data yang berubah-ubah. Seperti halnya untuk modul, kelas mengambil bagian dari sifat dinamis Python: mereka dibuat pada saat runtime, dan dapat dimodifikasi lebih lanjut setelah pembuatan.

Dalam terminologi C++, biasanya anggota kelas (termasuk anggota data) adalah `public` (kecuali lihat di bawah `Variabel Privat`), dan semua fungsi anggota adalah `virtual`. Seperti dalam Modula-3, tidak ada singkatan untuk merujuk anggota objek dari metodenya: fungsi metode dideklarasikan dengan argumen pertama eksplisit yang mewakili objek, yang diberikan secara implisit oleh panggilan. Seperti dalam Smalltalk, kelas itu sendiri adalah objek. Ini memberikan semantik untuk mengimpor dan mengganti nama. Tidak seperti C++ dan Modula-3, tipe bawaan dapat digunakan sebagai kelas dasar untuk ekstensi oleh pengguna. Juga, seperti di C++, sebagian besar operator bawaan dengan sintaks khusus (operator aritmatika, subscripting dll) dapat didefinisikan ulang untuk `instance` kelas.

---

## 9.1. Sepatah Kata tentang Nama dan Objek (A Word About Names and Objects)

Objek memiliki individualitas, dan banyak nama (dalam berbagai lingkup) dapat terikat ke objek yang sama. Ini dikenal sebagai `aliasing`. Hal ini dapat di abaikan ketika berhadapan dengan tipe dasar yang tidak dapat diubah (angka, string, tuple). Namun, aliasing memiliki efek yang mungkin mengejutkan pada semantik kode Python yang melibatkan objek yang bisa berubah seperti daftar list, kamus dictionary dan sebagainya. juga dapat digunakan untuk kepentingan program, karena `alias` berperilaku seperti pointers dalam beberapa hal. 

## 9.2. Lingkup Python dan Namespaces (Python Scopes and Namespaces)

Sebuah namespace adalah pemetaan dari nama ke objek. Sebagian besar ruang nama namespace saat ini diimplementasikan sebagai kamus dictionary Python, tetapi itu biasanya tidak terlihat dengan cara apa pun (kecuali untuk kinerja), dan itu mungkin berubah di masa depan. 
Contoh ruang nama namespace adalah:
   * himpunan nama bawaan (berisi fungsi seperti abs(), dan nama pengecualian bawaan)
   * nama-nama global dalam sebuah modul
   * dan nama-nama lokal dalam pemanggilan fungsi
Dalam arti himpunan atribut suatu objek juga membentuk namespace. Ruang nama namespace adalah sama sekali tidak ada hubungan antara nama dalam ruang nama namespace yang berbeda misalnya, dua modul yang berbeda dapat mendefinisikan fungsi `maximize` tanpa kebingungan, pengguna modul harus memberikan awalan dengan nama modul.

Referensi ke nama dalam modul adalah referensi atribut, dalam ekspresi `modname.funcname`, `modname` adalah objek modul dan `funcname` adalah atributnya. Dalam kasus ini akan terjadi pemetaan langsung antara atribut modul dan nama global yang didefinisikan dalam modul, mereka berbagi namespace yang sama!
pemberian nilai ke atribut dimungkinkan. Atribut modul dapat ditulis, kita dapat menulis `modname.the_answer = 42`. Atribut yang dapat ditulis juga dapat dihapus dengan pernyataan del. Sebagai contoh, `del modname`.the_answer akan menghapus atribut `the_answer` dari objek yang dinamai oleh `modname`.

Namespace dibuat pada saat yang berbeda dan memiliki masa hidup yang berbeda. Namespace yang berisi nama-nama bawaan dibuat ketika interpreter Python dimulai, dan tidak pernah dihapus. Namespace global untuk modul dibuat ketika definisi modul dibaca; biasanya, namespace modul juga bertahan hingga `interpreter` berhenti. Pernyataan yang dieksekusi oleh pemanggilan interpreter tingkat atas, baik membaca dari file skrip atau secara interaktif, dianggap sebagai bagian dari modul yang disebut __main__, sehingga mereka memiliki namespace global sendiri.

Namespace lokal untuk suatu fungsi dibuat ketika fungsi dipanggil, dan dihapus ketika fungsi kembali `returns` atau memunculkan pengecualian yang tidak ditangani dalam fungsi tersebut.

Suatu scope adalah wilayah tekstual dari program Python di mana namespace dapat diakses secara langsung. "Directly accessible" di sini berarti bahwa referensi yang tidak memenuhi syarat untuk suatu nama berusaha menemukan nama tersebut di namespace.

Meskipun cakupan scopes ditentukan secara statis, mereka digunakan secara dinamis. Setiap saat selama eksekusi, setidaknya ada 3 atau 4 cakupan bersarang yang ruang nama-nya namespaces dapat diakses secara langsung:
   
   * ruang lingkup scope terdalam, yang dicari pertama kali, berisi nama-nama lokal
   * lingkup scope dari setiap fungsi penutup, yang dicari dimulai dengan lingkup penutup terdekat, berisi nama-nama non-lokal, tetapi juga non-global
   * lingkup berikutnya next-to-last berisi nama global modul saat ini
   * ruang lingkup scope terluar (dicari terakhir) adalah namespace yang mengandung nama bawaan

Jika sebuah nama dinyatakan global, maka semua referensi dan penugasan langsung ke lingkup `scope` tengah yang berisi nama global modul. Untuk mengembalikan variabel yang ditemukan di luar cakupan terdalam, dapat menggunakan pernyataan `nonlocal`, jika kita mendeklarasikan nonlokal, variabel-variabel itu hanya baca-saja.

cakupan lokal merujuk nama lokal dari fungsi (secara tekstual) saat ini. Fungsi luar, lingkup lokal merujuk `namespace` yang sama dengan lingkup global: namespace modul. Definisi kelas menempatkan namespace lain dalam lingkup lokal.

Pernyataan `global` dapat digunakan untuk menunjukkan bahwa variabel tertentu hidup dalam lingkup global dan harus kembali ke sana; pernyataan `nonlocal` menunjukkan bahwa variabel tertentu hidup dalam cakupan terlampir dan harus dikembalikan ke sana.

**9.2.1. Contoh Lingkup Scopes dan Ruang Nama Namespaces(Scopes and Namespaces Example)**

Ini adalah contoh yang menunjukkan cara mereferensikan lingkup scopes dan ruang nama namespaces yang berbeda, dan bagaimana global dan nonlocal memengaruhi pengikatan variabel:

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

Keluaran dari contoh kode adalah:

```python
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```

## 9.3. Pandangan Pertama tentang Kelas (A First Look at Classes)

Memperkenalkan tentang sintaks baru, tiga tipe objek baru, dan beberapa semantik baru.

**9.3.1. Sintaks Definisi Kelas(Class Definition Syntax)**

Definisi kelas paling sederhana:

```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

Definisi kelas, seperti definisi fungsi (pernyataan def) harus dieksekusi sebelum mereka memiliki efek. Pernyataan di dalam definisi kelas biasanya akan menjadi definisi fungsi, tetapi pernyataan lain diizinkan. Definisi fungsi di dalam kelas biasanya memiliki bentuk khusus daftar argumen, didikte oleh konvensi pemanggilan untuk metode. Ketika definisi kelas dimasukkan, `namespace` baru dibuat, dan digunakan sebagai lingkup `scope` lokal --- dengan demikian, semua tugas untuk variabel lokal masuk ke `namespace` baru ini. Secara khusus, definisi fungsi mengikat nama fungsi baru di sini.

**9.3.2. Objek Kelas Class Objects(Class Objects)**

Objek kelas mendukung dua jenis operasi: `referensi atribut` dan `instansiasi`.

`Attribute references` menggunakan sintaks standar yang digunakan untuk semua referensi atribut dalam Python: `obj.name`. Nama atribut yang valid adalah semua nama yang ada di `namespace` kelas saat objek kelas dibuat. Jadi, jika definisi kelas tampak seperti ini:

```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```

kemudian `MyClass.i` dan `MyClass.f` adalah referensi atribut yang valid, masing-masing mengembalikan integer dan objek fungsi. Atribut kelas juga dapat ditetapkan, sehingga kita dapat mengubah nilai `MyClass.i` oleh penugasan. `__doc__` juga merupakan atribut yang valid, mengembalikan docstring milik kelas: `"A simple example class"`.

`instantiation` kelas menggunakan notasi fungsi. Hanya berpura-pura bahwa objek kelas adalah fungsi tanpa parameter yang mengembalikan instance baru dari kelas. Misalnya (dengan asumsi kelas di atas):

```python
x = MyClass()
```

membuat `instance` baru dari kelas dan menetapkan objek ini ke variabel lokal x.

Operasi instansiasi ("calling" objek kelas) membuat objek kosong. Banyak kelas suka membuat objek dengan instance yang disesuaikan dengan kondisi awal tertentu. Oleh karena itu sebuah kelas dapat mendefinisikan metode khusus bernama __init__(), seperti ini:

```python
def __init__(self):
    self.data = []
```

Ketika sebuah kelas mendefinisikan metode __init__(), instantiasi kelas secara otomatis memanggil __init__() untuk instance kelas yang baru dibuat. Jadi dalam contoh ini, contoh baru yang diinisialisasi dapat diperoleh oleh:

```python
x = MyClass()
```

Tentu saja, metode __init__() mungkin memiliki argumen untuk fleksibilitas yang lebih besar. Dalam hal itu, argumen yang diberikan kepada operator instantiasi kelas diteruskan ke __init__(). Sebagai contoh,

```python
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
```

**9.3.3. Objek Instance (Instance Objects)**

Operasi yang dipahami oleh objek instan adalah referensi atribut. Ada dua jenis nama atribut yang valid: atribut data, dan metode.

data `attributes` sesuai dengan "variabel instan" di Smalltalk, dan "data members" di C++. Atribut data tidak perlu dinyatakan; seperti variabel lokal, mereka muncul ketika mereka pertama kali ditugaskan. Misalnya, jika x adalah turunan dari `MyClass` yang dibuat di atas, bagian kode berikut akan mencetak nilai `16`, tanpa meninggalkan jejak:

```python
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```

Jenis lain dari referensi atribut instance adalah `method`. Metode adalah fungsi yang "milik" suatu objek. (Dalam Python, istilah metode tidak unik untuk instance kelas: tipe objek lain dapat memiliki metode juga. Misalnya, objek daftar memiliki metode yang disebut `append, insert, remove, sort, dan sebagainya`. Namun, dalam diskusi berikut, kita akan menggunakan istilah metode secara eksklusif untuk mengartikan metode objek `instance` kelas, kecuali dinyatakan secara eksplisit). Menurut definisi, semua atribut dari kelas yang merupakan objek fungsi menentukan metode yang sesuai dari `instance-nya`. Jadi dalam contoh kita, `x.f` adalah referensi metode yang valid, karena `MyClass.f` adalah fungsi, tetapi `x.i` tidak, karena `MyClass.i` tidak. Tetapi `x.f` bukan hal yang sama dengan `MyClass.f` --- itu adalah method object, bukan objek fungsi.

**9.3.4. Metode Objek(Method Objects)**

Biasanya, metode dipanggil tepat setelah itu terikat:

```python
x.f()
```

Dalam contoh MyClass, ini akan mengembalikan string `'hello world'`. Namun, tidak perlu memanggil metode segera: `x.f` adalah metode objek, dan dapat disimpan dan dipanggil di lain waktu. Sebagai contoh:

```python
xf = x.f
while True:
    print(xf())
```

akan terus mencetak hello world hingga akhir waktu.

Kita memperhatikan bahwa  `x.f()` dipanggil tanpa argumen di atas, meskipun definisi fungsi untuk `f()` menentukan argumen. Metode adalah objek `instance` dilewatkan sebagai argumen pertama dari fungsi. Dalam contoh kita, panggilan `x.f()` persis sama dengan `MyClass.f(x)`. Secara umum, memanggil metode dengan daftar argumen `n` setara dengan memanggil fungsi yang sesuai dengan daftar argumen yang dibuat dengan menyisipkan objek contoh metode sebelum argumen pertama.

Ketika atribut non-data dari sebuah `instance` direferensikan, kelas `instance` tersebut dicari. Jika nama menunjukkan atribut kelas yang valid yang merupakan objek fungsi, objek metode dibuat dengan mengemas `(menunjuk pointers ke)` objek instance dan objek fungsi yang baru saja ditemukan bersama dalam objek abstrak: ini adalah objek metode. Ketika objek metode dipanggil dengan daftar argumen, daftar argumen baru dibangun dari objek `instance `dan daftar argumen, dan objek fungsi dipanggil dengan daftar argumen baru ini.

**9.3.5. Variabel Kelas dan Instance (Class and Instance Variables)**

Secara umum, variabel `instance` adalah untuk data unik untuk setiap `instance` dan variabel kelas adalah untuk atribut dan metode yang dibagikan oleh semua `instance` kelas:

```python
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
```
Dengan melibatkan objek `mutable` seperti daftar `lists` dan kamus `dictionaries`. Sebagai contoh, daftar `tricks` dalam kode berikut tidak boleh digunakan sebagai variabel kelas karena hanya satu daftar yang akan dibagikan oleh semua `Dog instance`:

```python
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
```

Desain kelas yang benar harus menggunakan variabel `instance` sebagai gantinya:

```python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```

## Keterangan Acak (Random Remarks)

Jika nama atribut yang sama muncul di kedua `instance` dan di kelas, maka pencarian atribut memprioritaskan `instance`:

```python
>>> class Warehouse:
        purpose = 'storage'
        region = 'west'

>>> w1 = Warehouse()
>>> print(w1.purpose, w1.region)
storage west
>>> w2 = Warehouse()
>>> w2.region = 'east'
>>> print(w2.purpose, w2.region)
storage east
```

Atribut data dapat dirujuk oleh metode dan juga oleh pengguna biasa `("clients")` dari suatu objek. Dengan kata lain, kelas tidak dapat digunakan untuk mengimplementasikan tipe data abstrak murni. Faktanya, tidak ada dalam Python yang memungkinkan untuk menegakkan `enforce` data yang disembunyikan --- semuanya didasarkan pada konvensi.

Objek fungsi apa pun yang merupakan atribut kelas menentukan metode untuk `instance` dari kelas itu. Tidak perlu bahwa definisi fungsi `tertutup` secara teks dalam definisi kelas: menetapkan objek fungsi ke variabel lokal di kelas juga bisa. Sebagai contoh:

```python
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```

Sekarang `f`, `g` dan `h` adalah semua atribut class C yang merujuk ke objek-objek fungsi, dan akibatnya semuanya adalah metode instance dari C --- `h` sama persis dengan `g`.

Metode dapat memanggil metode lain dengan menggunakan atribut metode dari argumen `self`:

```python
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```

Metode dapat merujuk nama global dengan cara yang sama seperti fungsi biasa. Ruang lingkup scope global yang terkait dengan suatu metode adalah modul yang berisi definisinya.

Setiap nilai adalah objek, dan karenanya memiliki kelas (juga disebut sebagai type). Ini disimpan sebagai object.__class__.

## 9.5. Pewarisan(Inheritance)

fitur bahasa tidak akan layak untuk nama `"class"` tanpa mendukung `pewarisan`. Sintaks untuk definisi kelas turunan terlihat seperti ini:

```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

Nama `BaseClassName` harus didefinisikan dalam lingkup yang berisi definisi kelas turunan. Di tempat nama kelas dasar, ekspresi berubah-ubah `arbitrary` lainnya juga diperbolehkan. Ini bisa berguna, misalnya, ketika kelas dasar didefinisikan dalam modul lain:

```python
class DerivedClassName(modname.BaseClassName):
```

Eksekusi definisi kelas turunan menghasilkan sama seperti untuk kelas dasar. Ketika objek kelas dibangun, kelas dasar diingat. Ini digunakan untuk menyelesaikan referensi atribut: jika atribut yang diminta tidak ditemukan di kelas, pencarian dilanjutkan untuk mencari di kelas dasar. Aturan ini diterapkan secara rekursif jika kelas dasar itu sendiri berasal dari beberapa kelas lain.

Tidak ada yang istimewa tentang instance kelas turunan: `DerivedClassName()` membuat instance baru dari kelas. Referensi metode diselesaikan sebagai berikut: atribut kelas yang sesuai dicari, turun rantai kelas dasar jika perlu, dan referensi metode ini valid jika ini menghasilkan objek fungsi.

Kelas turunan dapat menimpa metode kelas dasar mereka. Karena metode tidak memiliki hak khusus ketika memanggil metode lain dari objek yang sama, metode kelas dasar yang memanggil metode lain yang didefinisikan dalam kelas dasar yang sama mungkin akhirnya memanggil metode kelas turunan yang menimpanya. (Untuk programmer C++: semua metode dalam Python secara efektif `virtual`.)

Menimpa metode dalam kelas turunan mungkin sebenarnya ingin memperluas daripada hanya mengganti metode kelas dasar dengan nama yang sama. Ada cara sederhana untuk memanggil metode kelas dasar secara langsung: cukup panggil `BaseClassName.methodname(self, arguments)`. Ini kadang-kadang berguna untuk klien juga. (Perhatikan bahwa ini hanya berfungsi jika kelas dasar dapat diakses sebagai `BaseClassName` dalam lingkup global.)

Python memiliki dua fungsi bawaan yang bekerja dengan warisan:

   * Gunakan `isinstance()` untuk memeriksa jenis instance: `isinstance(obj, int) ` akan menjadi `True` hanya jika `obj.__class__` adalah `int` atau beberapa kelas yang diturunkan dari `int`.
   * Gunakan `issubclass()` untuk memeriksa warisan kelas: `issubclass(bool, int)adalah True` karena `bool` adalah subkelas dari `int`. Namun, `issubclass(float, int)` adalah `False` karena `float` bukan subkelas dari `int`.

**9.5.1. Pewarisan Berganda(Multiple Inheritance)**

Python mendukung bentuk pewarisan berganda juga. Definisi kelas dengan beberapa kelas dasar terlihat seperti ini:

```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

Jika atribut tidak ditemukan di `D`erivedClassName, itu dicari di Base1, kemudian (secara rekursif) di kelas dasar dari `Base1`, dan jika tidak ditemukan di sana, itu dicari di `Base2`, dan seterusnya. urutan resolusi metode berubah secara dinamis untuk mendukung pemanggilan kooperatif ke `super()`. Pendekatan ini dikenal dalam beberapa bahasa warisan ganda sebagai metode panggilan-berikutnya `call-next-method` dan lebih berdaya daripada panggilan super yang ditemukan dalam bahasa warisan tunggal.

Urutan dinamis diperlukan karena semua kasus pewarisan berganda menunjukkan satu atau lebih hubungan intan diamond `relationships`. Contoh, semua kelas mewarisi dari object, jadi segala kasus pewarisan berganda menyediakan lebih dari satu jalur untuk mencapai :class:` object`. Untuk menjaga agar kelas dasar tidak diakses lebih dari sekali, algoritma dinamis linier mengurutkan urutan pencarian dengan cara yang mempertahankan urutan kiri-ke-kanan yang ditentukan dalam setiap kelas, yang memanggil setiap induk hanya sekali, dan itu monoton.

## 9.6. Variabel Privat(Private Variables)

Variabel instance `"Private"` yang tidak dapat diakses kecuali dari dalam suatu objek tidak ada dalam Python. Namun, ada konvensi yang diikuti oleh sebagian besar kode Python: nama diawali dengan garis bawah (mis. `_spam`) harus diperlakukan sebagai bagian non-publik dari API (apakah itu fungsi, metode atau anggota data). Ini harus dianggap sebagai detail implementasi dan dapat berubah tanpa pemberitahuan.

Setiap pengidentifikasi dari bentuk `__spam` (setidaknya dua garis bawah utama, paling banyak satu garis bawah garis bawah) secara teks diganti dengan `_classname__spam`, di mana `classname` adalah nama kelas saat ini dengan garis(-garis) bawah utama dilucuti. `Mangling` ini dilakukan tanpa memperhatikan posisi sintaksis pengidentifikasi, asalkan terjadi dalam definisi kelas.

`Name mangling` sangat membantu untuk membiarkan subclass menimpa metode tanpa memutus panggilan metode `intraclass`. Sebagai contoh:

```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```

Contoh di atas akan berfungsi bahkan jika `MappingSubclass` akan memperkenalkan sebuah pengidentifikasi `__update` karena diganti dengan `_Mapping__update` di kelas `Mapping` dan `_MappingSubclass__update` di kelas M`appingSubclas`s masing-masing.

Aturan `mangling` sebagian besar dirancang untuk menghindari kecelakaan; masih dimungkinkan untuk mengakses atau memodifikasi variabel yang dianggap pribadi. Ini bahkan dapat berguna dalam keadaan khusus, seperti di `debugger`.

Perhatikan bahwa kode yang dilewatkan ke `exec()` atau `eval()` tidak menganggap nama kelas classname dari kelas yang dipanggil sebagai kelas saat ini; ini mirip dengan efek pernyataan `global`, yang efeknya juga terbatas pada kode yang dikompilasi`-byte byte-compiled` bersama. Pembatasan yang sama berlaku untuk `getattr()`, `setattr()` dan `delattr()`, serta saat mereferensikan __dict__ secara langsung.

## 9.7. Barang Sisa Odds and Ends

Kadang-kadang berguna untuk memiliki tipe data yang mirip dengan `"record"` Pascal atau `"struct"` C, menyatukan beberapa item data bernama. Definisi kelas kosong akan menghasilkan hal tersebut dengan baik:

```python
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
```

Objek metode instance memiliki atribut, juga: m.__self__ adalah objek instan dengan metode m(), dan m.__func__ adalah objek fungsi yang sesuai dengan metode tersebut.

## 9.8. Iterators

Sekarang kita tahu bahwa sebagian besar objek penampung `container` dapat dibuat perulangan menggunakan pernyataan `for`:

```python
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```

Penggunaan `iterator` meliputi `pervades` dan menyatukan Python. Di belakang layar, pernyataan `for` memanggil `iter()` pada objek penampung container. Fungsi mengembalikan objek iterator yang mendefinisikan metode __next__() yang mengakses elemen dalam penampung `container` satu per satu. Ketika tidak ada lagi elemen, __next__() memunculkan pengecualian `StopIteration` yang memberi tahu perulangan for untuk mengakhiri. Anda dapat memanggil metode __next__() menggunakan next() fungsi bawaan; contoh ini menunjukkan cara kerjanya:

```python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_iterator object at 0x10c90e650>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
```

Setelah melihat mekanisme di balik protokol `iterator`, mudah untuk menambahkan perilaku iterator ke kelas Anda. Definisikan metode __iter__() yang mengembalikan objek dengan metode __next__(). Jika kelas mendefinisikan __next__(), maka __iter__() bisa langsung mengembalikan `self`:

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```
```python
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
m
a
p
s
```

## 9.9. Pembangkit Generator (Generators)

`Generators` adalah sebuah `tool` yang sederhana dan simpel untuk membuat sebuah `iterasi`. seperti fungsi biasa tapi menggunakan pernyataan `yield` setiap kali ingin mengembalikan sebuah data. Tiap kali `next()` itu dipanggil, generators tersebut akan melanjutkan di mana hal itu berhenti (itu akan mengingat semua nilai dan pernyataan mana yang terakhir dieksekusi). Sebuah contoh menunjukkan bahwa generator sangat mudah dibuat:

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
```
```python
>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g
```

Apa pun yang dapat dilakukan dengan pembangkit generator juga dapat dilakukan dengan `iterator` berbasis kelas seperti yang dijelaskan pada bagian sebelumnya. Apa yang membuat pembangkit `generator` sangat kompak adalah bahwa metode __iter__() dan __next__() dibuat secara otomatis.

Fitur utama lainnya adalah variabel lokal dan status eksekusi secara otomatis disimpan di antara pemanggilan. Ini membuat fungsi lebih mudah untuk ditulis dan jauh lebih jelas daripada pendekatan menggunakan variabel instan seperti `self.index`` dan `self.data`.

Selain pembuatan metode otomatis dan menyimpan status program, ketika pembangkit `generator` berhenti, mereka secara otomatis menimbulkan `StopIteration`. Secara kombinasi, fitur-fitur ini membuatnya mudah untuk membuat `iterator` tanpa lebih dari sekadar menulis fungsi biasa.

## 9.10. Ekspresi Pembangkit Generator (Generator Expressions)

Beberapa pembangkit `generators` sederhana dapat dikodekan secara ringkas sebagai ekspresi menggunakan sintaksis yang mirip dengan pemahaman daftar `list comprehensions` tetapi dengan tanda kurung bukan dengan tanda kurung siku. Ungkapan-ungkapan ini dirancang untuk situasi di mana generator digunakan segera oleh fungsi penutup. `Ekspresi generator` lebih kompak tetapi kurang `fleksibel` daripada definisi `generator` penuh dan cenderung lebih ramah memori daripada pemahaman daftar `list comprehensions` setara.
Contoh:

```python
>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> unique_words = set(word for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
```