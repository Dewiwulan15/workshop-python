# Tutorial Python

Python merupakan Bahasa pemograman yang mudah dipelajari. Yang memiliki struktur data tingkat tinggi dan pendekatan yang sederhana serta efektif untuk pemograman berorientasi objek. Sintaks python menjadikannya Bahasa yang ideal untuk skrip dan pengembangan aplikasi di Sebagian besar platform.
Interpreter Python mudah dikembangkan dengan fungsi dan tipe data baru, python juga cocok sebagai Bahasa tambahan untuk aplikasi yang dapat disesuaikan.
Tutorial ini memperkenalkan banyak fitur python yang penting, dan memberi gaya serta ide tentang rasa dan gaya bahasa itu. 


**Bab 1**

Jika kita merupakan seorang pengembang perangkat lunak professional, kita harus mengerti dan dan bekerja dengan beberapa Pustaka atau sumber C/C++/Java.
Python merupakan Bahasa yang sesuai, karena mudah digunakan dan merupkan Bahasa pemograman nyata, menawarkan lebih banyak struktur dan dukungan untuk program besar dari pada skrip shell. Python juga menawarkan pemeriksaan kesalahan jauh lebih banyak daripada C dan merupakan Bahasa tingkat tinggi. Python dapat diterapkan pada domain masalah yang jauh lebih besar daripada Awk atau bahkan Perl.
Python adalah bahasa yang ditafsirkan, yang dapat menghemat waktu  selama pengembangan program karena tidak diperlukan kompilasi dan penautan. Python memungkinkan program ditulis secara ringkas dan mudah dibaca. Program yang ditulis dengan Python biasanya jauh lebih pendek daripada program C, C++, atau Java yang setara.
Tutorial ini memperkenalkan fitur Bahasa dan system python, dimulai dengan ekspresi sederhana, pernyataan dan tipe data, dari fungsi dan juga modul, serta akhirnya menyentuh konsep lanjutan.


**Bab 2**

***Menggunakan Interpreter Python***

Memanggil Interpreter
Interpreter python biasanya di instal di /usr/local/bin/python3.10. Pengeditan garis interpreter merupakan pengeditan interaktif, penggantian Riwayat dan penyelesaian kode pada system yang mendukung GNU Readline. Pemeriksaan tercepat untuk melihat apakah pengeditan baris perintah di dukung, yaitu dengan mengetik Control-P ke prompt Python. Jika berbunya, maka kita memiliki baris perintah. Jika tidak ada yang terjadi dan atau muncul ^P, pengeditan baris tidak tersedia, dan hanya akan dapat menggunakan backspace untuk menghapus karakter dan baris saat ini.
Interpreter beroperasi sangan mirip dengan shell Unix, dan dipanggil dengan memasukkan bawaan yang terhubung keperangkat tty, makai a akan membaca dan mengeksekusi perintah secara interaktif. Dan jika dipanggil dengan argument nama berkas atau dengan berkas sebagai masukan bawaan, ia akan membaca dan mengeksekusi scrip dari berkas tersebut.
Cara kedua untuk memulai interpreter adalah python -c command [arg] ..., yang mengeksekusi pernyataan(-pernyataan) dalam command, dianalogikan sebagai opsi shell -c. karena pernyataan python tersebut sering mengandung spasi atau karakter lain yang khusus untuk shell.

***Melewatkan Argumen***
Jika telah diketahui oleh interpreter, nama skrip dan argument tambahan setelahnya diubah jadi daftar string dan diberikan nilai ke variable argv dalam modul sys. Kita dapat mengakses daftar dengan menjalankan import sys. Panjang daftar setidaknya satu, jadi Ketika tidak ada skrip dan tidak ada argument yang diberikan, sys.argv[0] di atur k eke ‘_’ Ketika command -c atau module -m.

***Mode Interaktif***
Jika perintah dibaca dari tty, interpreter dikatakan dalam interactive mode. Pada mode ini interpreter meminta perintah berikutnya dengan primary prompt, namun biasanya tiga tanda lebih besar dari (>>>) digunakan untuk garis lanjutan, interpreter meminta dengan menggunakan secondary prompt, secara bawaan tiga titik (…) dengan interpreter mencetak pesan selamat dating yang menyatakan nomor versinya dan pemberitahuan hak cipta.

***Interpreter dan lingkungannya***
encoding penulisan kode sumber
Berkas sumber python merupakan tulisan encoded dalam UTF-8. Dalam pengkodean karakter Bahasa dapat digunakan secara bersamaan dalam string literal, pengidentifikasian dan komentar. Sebuah konvensi yang harus di ikuti oleh setiap kode portable. Untuk menampilkan semua karakter in dengan benar, editor harus mengenali bahwa berkas tersebut adalah UTF-8 dan harus menggunakan font yang mendukung semua karakter dalam berkas.


**Bab 3**

Pengantar Informal tentang Python
Dalam contoh ini, masukan dan keluaran dibedakan dengan ada tidaknya prompt (>>> dan …). Misalnya kita harus mengetik semuanya setelah prompt, di saat prompt muncul. Ketika baris tidak dimulai dengan prompt disebut output dari output dari interpreter. Baris yang hanya berisi prompt sekunder pada contoh tersebut berarti kita harus mengetikkan baris kosong, hal tersebut digunakan untuk mengakhiri perintah multi-baris.
Ada banyak contoh manual dan bahkan dimasukkan kedalam prompt interaktif, termasuk komentar. Komentar pada python dapat dimulai dengan karakter hash, #, dan diperluas hingga akhir garis fisik. Komentar dapat muncul di awal baris atau mengikuti spasi ataupun kode tetapi tidak dalam string literal. Karakter hash pada string literal hanyalah karakter hash. Karena komentar digunakan untuk mengklarifikasi kode dan tidak ditafsirkan oleh python dan dapat dihilangkan. Menggunakan Python sebagai Kalkulator
Kita akan mencoba perintah python sederhana. Dari interpreter dan tunggu prompt utama,>>>.

***Angka***
Interpreter bertindak sebagai kalkulator sederhana, dapat mengetikkan dan kalkulator akan menulis nilai. Sintaks ekspresi yang mudah contohnya: operator +, -, * dan / yang berfungsi seperti kebanyakan Bahasa program seperti pascal atau C, tanda kurung (()) digunakan untuk pengelompokan.
Bilangan bulat (2,4,20) memiliki tipe data int, bilangan pecahan (“5.0”,”1.6”) memiliki tipe data float. Division (/) selalu mengembalikan float atau bilangan pecahan untuk melakukan floor devision dan mendapat hasil integer atau bilangan bulat untuk menghilangan hasil pecahannya. Kita dapat menggunakan operator // untuk menghitung sisanya dan dapat menggunakan %.
Dalam python ooperator ** digunakan untuk menghitung pemangkatan. Tanda sama dengan (=) digunakan untuk memberikan nilai ke variable dan tidak ada yang dihasilkan sebelum prompt interaktif berikutnya.
Ketika variable tidak “didefinisikan (diberi nilai)” dan saat menggunakannya kita akan menghasilkan kesalahan. Adapun dukungan penuh untuk floating point atau operator dengan operan tipe campuran, akan berubah mengubah operan integer ke floating point.
Pada mode interaktif, ekspresi cetak terakhir akan diberikan pada variable _. Hal ini menunjukkan bahwa Ketika menggunakan python sebagai kalkulator, agak lebih mudah untuk melanjutkan perhitungan. Variable tersebut harus diperlakukan sebagai baca saja oleh pengguna, jangan secara eksplisit menggunakan atau memberikan nilai padanya, Ketika hal itu terjadi kita akan memberikan atau membuat variable lokal independent dengan nama yang sama serta menutupi variable bawaannya.
Selain tipe data int dan float, python mendukung tipe data lainnya, seperti decimal dan fraction. Python juga memiliki dukungan bawaan untuk complex number, menggunakan akhiran j atau J untuk menunjukkan bagian imajiner (contoh: 3+5j).

***String***
Selain angka, Python juga dapat atau bisa memanipulasi string atau teks, yang diekspresikan dalam beberapa cara. Dapat disertakan dalam tanda kutip tunggal (‘…’) atau kutip ganda (“…”) dengan hasil yang sama untuk penggunaan kutipnya. Tanda \ dapat digunakan untuk keluar kutipan.
Pada interpreter interaktif, string keluarandi apait dengan tanda kutp dan karakter khusus dan dipisahkan dengan garis miring terbalik. Meskipun kadang terlihat berbeda dari input, kedua string tersebut setara. String disertakan dalam kutip ganda jika string tersebut berisi kutipan tunggal dan tidak ada kutip ganda, jika tidak, maka dilampirkan dalam kutip tunggal. Fungsi print() adalah menghasilkan keluaran yang lebih mudah dibaca, dengan menghilangkan tanda kutip terlampir dengan mencetak karakter yang dipisahkan. Ketika kita tidak ingin karakter diawali dengan \ atau ditafsirkan dengan karakter khusus, kita dapat emnggunakan raw string dengan menambhkan r sebelum kutipan pertama.
String literal dapat melebar hingga beberapa baris, salah satunya dengan cara menggunakan tiga tanda kutip. Ketika hal tersebut dilakukan akhir baris akan secara otomatis termasuk dalam string. String dapat digabungkan (direkatkan) dengan operator +, dan diulangi dengan *. 

***List***
Python mengetahui beberapa tipe data compound atau gabungan, yang digunakan untuk mengelompokkan nilainya. Dari tipe data tersebut yang paling berguna adalah list, yang dapat ditulis sebagai daftar nilai yang dipisahkan koma antara tanda kurung siku. List atau daftar dapat berisi items dari tipe yang berbeda, tetapi biasanya semua items memiliki tipe yang sama. Seperti string (dan semua bawaan lainnya tipe sequence), list atau daftar tersebut dapat diindeks dan diiris. Semua operasi iris mengembalikan list atau daftar baru yang berisi variabel yang diminta. Ini berarti bahwa irisan berikut mengembalikan shallow copy dari list. List atau daftar mendukung operasi seperti perangkaian. Tidak seperti string, yang immutable, list adalah mutable.

***Langkah Awal Menuju Pemograman***
Kita bisa menggunakan Python untuk tugas yang lebih rumit daripada menambahkan dua dan dua bersamaan. Perulangan while dieksekusi selama kondisi masih benar. Body dari pengulangan adalah indentasi, identasi merupakan cara python untuk mengelompokkan pernyataan. Semua editor teks yang baik memiliki fasilitas indentasi otomatis, dan Ketika pernyataan majemuk dimasukkan secara interaktif, hal tersebut harus diikuti dengan baris kosong untuk menunjukkan penyelesaian. Fungsi print() menulis nilai argument yang diberikan.