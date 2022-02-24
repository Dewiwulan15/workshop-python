#Struktur Data

Pada bab Struktur Data ini akan menjelaskan beberapa materi yang telah dipelajari sebelumnya dengan lebih rinci, serta menambahkan beberapa materi atau hal yang baru.

**Materi lebih lanjut tentang Daftar Lists**

Beberapa metode yang dimiliki oleh Daftar list. yaitu:

list.append(x) 
 Menambahkan item ke akhir daftar. Setara dengan a[len(a):] = [x].

list.extend(iterable)
 Memperpanjang daftar list semua item dengan menambahkannya dari iterable. yang setara dengan a[len(a):] = iterable.

list.insert(i, x)
 Memasukkan item di posisi tertentu. Dimana Argumen pertama merupakan indeks elemen sebelum dimasukkan jadi a.insert(0, x), lalu memasukkan bagian depan daftar list yang mana a.insert(len(a), x) sama dengan a.append(x).

list.remove(x)
 Menghapus item pada daftar pertama di list yang mana nilainya sama dengan X. Hal ini menimbulkan ValueError jika tidak ada item tersebut.

list.pop ([i]) 
 Menghapus item pada posisi tertentu dalam daftar dan mengembalikannya. Jika tidak ada indeks yang akan dilakukan atau tentukan. a.pop() akan menghapus dan mengembalikan item terakhir dalam daftar list. 

list.clear()
 Menghapus semua item dari daftar list Yang setara dengan del a[:].

list.index(x[, start[, end]])
 Mengembalikan indeks yang berbasis nol pada daftar item pertama yang mana nilainya sama dengan x. dan memunculkan ValueError jika tidak ada item tersebut.
 Argumen opsional yang ditemukan di awal dan akhir akan ditafsirkan sebagai notasi irisan yang digunakan untuk membatasi pencarian ke urutan tertentu. serta Indeks Pengembalian akan dihitung relatif terhadap awal string lengkap yang terdapat dalam argumen awal.

list.count(x)
 Mengembalikan beberapa kali x yang muncul dalam daftar.

list.sort(*, key=None, reverse=False)
 Mengurutkan item daftar yang terdapat ditempat atau argumen yang dapat digunakan untuk mengurutkan dan mengubah sehingga sesuai dengan kustomisasi, dan melihat pengurutan sebagai penjelasannya

list.reverse()
 Membalikkan elemen list dari daftar di tempatnya.

list.copy()
 Mengembalikan salinan daftar yang mendasar atau dangkal. dan setara dengan a[:].

kami melihat bahwa metode seperti menyisipkan, menghapus, atau mengurutkan hanya  mengubah daftar. daftar tanpa nilai pengembalian  dicetak dan mereka akan mengembalikan nilai default Tidak ada. 1 Ini adalah  prinsip desain untuk semua struktur data yang dapat diubah dengan Python.
Hal lain yang perlu diingat adalah  tidak semua data dapat diurutkan atau dibandingkan. Misalnya: [None, 'hello', 10] tidak diurutkan sebagai bilangan normal atau string normal, karena bilangan bulat ini tidak dapat dibandingkan dengan apapun yang memiliki string atau none sehingga variabel yang lainnya juga tidak dapat dibandingkan dengan jenis lain. dan ada beberapa tipe yang tidak memiliki hubungan urutan yang telah ditentukan sebelumnya. Misalnya, 3 
j dan lt; 5 7h bukan perbandingan yang valid.

***Menggunakan Daftar List sebagai Tumpukan Stacks***

Menggunakan metode daftar memudahkan untuk menghitung keinginan sebagai tumpukan di tumpukan, di mana item terakhir yang  ditambahkan adalah item pertama yang diambil ("lastin, firstout"). Dan untuk menambahkan item ke bagian atas tumpukan, gunakan fungsi append(). serta untuk mendapatkan item dari atas tumpukan, menggunakan fungsi pop() tanpa indeks eksplisit.

***Menggunakan Daftar List Sebagai Antrian Queues***

Dapat dimungkinkan untuk menggunakan daftar sebagai antrian yang mana elemen pertama yang akan ditambahkan adalah elemen pertama yang akan di ambil atau biasa disebut dengan ("first-in, first-out"). tetapi daftar tidak akan efisien dengan tujuan ini karena semua elemen akan digeser satu persatu.

***Daftar List Comprehensions***

Pemahaman pada daftar list comprehensions akan menyediakan cara singkat untuk membuat daftar. Dimana Aplikasi umum adalah pembuat daftar baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan pada anggota dari urutan lain, ataupun untuk membuat urutan elemen yang memenuhi kondisi tertentu.

Comprehension terdiri dari tanda kurung yang berisi ekspresi dan diikuti oleh klausa for, lalu nol dan juga lebih klausa for atau if. Hasilnya akan menjadi daftar baru yang akan dihasilkan dari evaluasi ekspresi pada konteks dari klausa for serta if yang mengikutinya.

***Pemahaman Daftar List Comprehensions Bersarang***

Ekspresi awal yang digunakan dalam pemahaman daftar list comprehension dapat berupa ekspresi yang acak atau arbitrary, termasuk juga pemahaman daftar list comprehension lainnya. Pemahaman daftar list comprehension tersebut akan mengubah baris dan kolom. Serta listcomp yang bersarang akan dievaluasi dalam konteks for yang mengikutinya, kita juga memilih fungsi bawaan untuk pernyataan aliran flow yang kompleks.

**Pernyataan del**

Ada cara untuk menghapus elemen dari daftar  pada indeksnya, bukan nilainya: pernyataan del. hal ini berbeda dari metode pop() yang akan mengembalikan nilai. Pernyataan del dapat digunakan untuk menghapus irisan dari daftar  atau untuk menghapus seluruh daftar dari daftar.

**Tuples dan Urutan Sequences**

Kita tahu bahwa daftar list dan string memiliki banyak properti yang sama, seperti dalam operasi pengindeksan dan pemotongan. Mereka merupakan dua contoh tipe data sequence. Karena Python merupakan bahasa yang berkembang, tipe data urutan lain akan dapat ditambahkan. serta terdapat tipe data urutan standar lainseperti tuple.   Sebuah tuple terdiri dari sejumlah nilai yang dipisahkan oleh koma.  Seperti yang kita dapat lihat, tupel keluaran selalu diapit tanda kurung, menjadi tupel bersarang ketika diinterpretasikan dengan benar; mereka dapat dimasukkan dengan atau tanpa tanda kurung siku, meskipun  tanda kurung juga dapat diperlukan. Nilai tidak dapat ditetapkan ke elemen tupel individual, tetapi tupel yang berisi objek yang dapat diedit, seperti daftar, dapat dibuat.   Meskipun tupel dapat mirip dengan daftar, tupel sering digunakan dalam situasi yang berbeda dan untuk tujuan yang berbeda. Tuple tidak dapat diubah dan biasanya berisi urutan elemen yang heterogen yang dapat diakses melalui pembongkaran atau pengindeksan. Daftar merupakan istilah dari `mutable(), dan elemennya umumnya identik dan dapat diakses dengan mengulangi daftar.   Masalah yang khusus merupakan pembangunan tuple yang mengandung 0 atau 1 item: sintaksis memiliki  kebiasaan quirks tambahan untuk mengakomodasi hal tersebut. Tuple kosong tersebut dibangun oleh sepasang kurung yang kosong, tupel dengan 1 item konstruksi yang mengikuti nilai dengan koma (tidak akan cukup untuk menyertakan nilai tunggal dalam kurung). Jelek, tapi efektif  Ini disebut, cukup tepat, urutan membongkar sequence unpacking dan berfungsi untuk setiap urutan di sisi kanan. Urutan membongkar tersebut dapat mensyaratkan bahwa ada banyak variabel di sisi kiri tanda sama dengan dan ada elemen dalam urutan tersebut. Perhatikan bahwa banyak tugas benarbenar hanya kombinasi dari tuple packing dan urutan pembongkaran sequence unpacking.

**Himpunan Set**

Python menyertakan tipe data untuk data set. Himpunan atau himpunan adalah himpunan tak beraturan tanpa elemen duplikat. Penggunaan dasar termasuk pengujian untuk adhesi dan menghapus entri duplikat. Objek Set juga mendukung operasi  seperti penyatuan, persimpangan, perbedaan perbedaan, dan perbedaan simetri. Fungsi set() berfungsi untuk membuat set. Catatan: untuk membuat set kosong Anda harus menggunakan set() sebagai ganti {}; Bagian berikut membuat kamus  kosong.

**Kamus Dictionaries**

Tipe data  berguna lainnya yang dibangun ke dalam Python adalah kamus (lihat dict Jenis Pemetaan). Kamus biasanya ditemukan dalam bahasa lain sebagai "ingatan asosiatif" ataupun "array terkait". Tidak seperti string, yang diindeks oleh sejumlah digit, kamus ini diindeks oleh kunci, yang dapat berupa jenis apa pun yang tidak dapat diubah; string dan angka masih bisa menjadi kunci. Tupel dapat digunakan sebagai kunci jika hanya berisi string, angka, atau tupel; jika  tuple berisi objek yang bisa berubah  secara langsung atau tidak langsung, hal tersebut tidak akan dapat digunakan sebagai kuncinya. Anda tidak dapat menggunakan daftar sebagai kunci karena daftar dapat dimodifikasi di tempat menggunakan penetapan indeks, penetapan irisan, atau metode seperti append() dan juga fungsi expand().  biasanya kamus dictionary sebagai satu set key merupakan value berpasangan, dengan persyaratan bahwa kunci tersebut unik (dalam satu kamus dictionary). kemudian kurung kurawal membuat kamus dictionary kosong: {}. Menempatkan daftar pasangan kunci yang berupa nilai yang dipisah koma dalam kurung menambahkan pasangan kunci ini kedalam nilai ke kamus dictionary, hal ini juga cara kamus dictionary ditulis pada keluaran tersebut.   Operasi utama dalam kamus dictionary yaitu menyimpan nilai dengan beberapa kunci key dan mengekstraksi nilai yang diberikan oleh kunci key. dapat dimungkinkan untuk menghapus pasangan kunci ini dengan nilai del. Jika kita menyimpan dan menggunakan kunci yang telah digunakan, nilai lama yang terkait dengan kunci tersebut akan dilupakan. juga masuk dalam kesalahan untuk mengekstraksi nilai menggunakan kunci yang tidak ada.   Melakukan list(d) dalam kamus untuk mengembalikan daftar list kesemua kunci yang digunakan, pada urutan penyisipan (jika kita ingin diurutkan, cukup menggunakan sorted(d)). serta untuk memeriksa apakah ada satu kunci pada kamus, kita bisa menggunakan kaca kunci in.

**Teknik Perulangan**

Ketika mengulang dalam kamus dictionaries, kunci key dan nilai value yang terkait akan dapat diambil pada saat yang sama menggunakan metode items(). Dan pada saat mengulang melalui urutannya, indeks posisi dan nilai terkait akan dapat diambil pada saat yang sama menggunakan fungsi enumerate(). Dan untuk mengulang dua urutan atau lebih secara bersama, entri dapat dipasangkan melalui/dengan fungsi zip(). Lalu ketika mengulang secara terbalik, awalnya kita akan menentukan urutan dalam arah maju dan kemudian memanggil fungsi reversed(). Kemudian untuk mengulangi urutan sequence yang ada dalam susunan yang diurutkan, gunakan fungsi sort() yang berfungsi untuk mengembalikan daftar terurut baru dengan membiarkan sumber tidak diubah.

Menggunakan set() pada urutan akan dapat menghilangkan elemen yang duplikat. dan penggunaan sorted() yang dikombinasikan dengan set() terhadap urutan merupakan cara idiomatik untuk loop dari elemen-elemen unik yang terdapat dari urutan yang diurutkan.

**Lanjutan tentang Kondisi**

Kondisi yang digunakan pada pernyataan while dan if dapat berisi operator apa pun, bukan hanya perbandingan.   Operator perbandingan in dan not di adalah tes keanggotaan yang menentukan apakah suatu nilai ada di (atau tidak) dalam wadah. Operator adalah dan tidak membandingkan apakah dua objek merupakan objek yang sama. Semua operator pembanding akan memiliki prioritas yang sama, yaitu lebih rendah dari semua operator numerik.   Perbandingan bisa dibuat berantai. Misalnya, sebuah andlt; b == c memeriksa apakah a lebih kecil dari b dan apakah b sama dengan c.   Perbandingan dapat digabungkan menggunakan operator Boolean  dan dan atau, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat dinegasikan dengan komentar. Ini memiliki prioritas lebih rendah daripada operator perbandingan; di antara mereka, nada memiliki prioritas tertinggi dan/atau terendah, jadi A tetapi bukan B atau C setara dengan (A dan (bukan B)) atau C. Seperti biasa, tanda kurung dapat digunakan untuk mewakili komposisi yang diinginkan.    Boolean  dan atau yang disebut operator hubung singkat: argumen mereka dievaluasi dari kiri ke kanan, dan evaluasi berhenti segera setelah hasilnya ditentukan. Misalnya, jika A dan C bernilai benar tetapi B salah atau tidak benar, A dan B dan C tidak akan mengevaluasi ekspresi C. Ketika digunakan sebagai nilai umum dan bukan sebagai Boolean, nilai kembalian dari operator adalah argumen terakhir yang dievaluasi.

**Membandingkan Urutan Sequence dan Jenis Lainnya**

Objek urutan umumnya dapat dibandingkan dengan objek lain dari jenis urutan yang sama. Perbandingan menggunakan urutan leksikal: pertama dua elemen pertama dibandingkan dan jika berbeda, ini menentukan hasil perbandingan; jika mereka sama, dua item berikutnya dibandingkan, dan seterusnya, sampai salah satu string berkurang dan sampai habis. Jika dua item yang akan dibandingkan menurut urutannya berjenis sama, maka perbandingan leksikografis dilakukan secara rekursif. Jika semua elemen dari dua barisan yang bersesuaian adalah sama, maka ordo tersebut dianggap sama. Jika satu barisan merupakan barisan awal dari barisan yang lain, barisan yang lebih pendek adalah barisan yang lebih kecil (lebih pendek). Pengurutan leksikografis untuk string menggunakan nomor titik kode Unicode untuk mengurutkan masingmasing karakter.   Perhatikan ketika membandingkan objek dari berbagai jenis dengan < atau> adalah sah asalkan objek memiliki metode perbandingan yang sesuai. contohnya, tipe numerik campuran akan dibandingkan berdasarkan nilai numeriknya, sehingga 0 sama dengan 0.0, dll. Jika tidak, selain memberikan penyusunan acak, interpreter akan memunculkan pengecualian TypeError.
