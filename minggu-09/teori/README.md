# BAB 12 Virtual Environments and Packages
---
## 12.1. Pengantar (Introduction)

Aplikasi Python sering menggunakan paket dan modul yang tidak datang sebagai bagian dari pustaka standar. Aplikasi kadang-kadang membutuhkan versi pustaka tertentu, karena aplikasi mungkin mensyaratkan bug tertentu telah diperbaiki atau aplikasi dapat ditulis menggunakan versi usang dari antarmuka pustaka.

Ini berarti tidak mungkin bagi satu instalasi Python untuk memenuhi persyaratan setiap aplikasi. Jika aplikasi A membutuhkan versi 1.0 dari modul tertentu tetapi aplikasi B membutuhkan versi 2.0, maka persyaratannya bertentangan dan menginstal versi 1.0 atau 2.0 akan membuat satu aplikasi tidak dapat berjalan.

Solusi untuk masalah ini adalah membuat virtual environment, sebuah struktur direktori mandiri yang berisi instalasi Python untuk versi tertentu dari Python, serta sejumlah paket tambahan.

Aplikasi yang berbeda dapat menggunakan lingkungan virtual yang berbeda. Untuk menyelesaikan contoh sebelumnya dari persyaratan yang saling bertentangan, aplikasi A dapat memiliki lingkungan virtual sendiri dengan versi 1.0 yang diinstal sementara aplikasi B memiliki lingkungan virtual lain dengan versi 2.0. Jika aplikasi B membutuhkan pustaka ditingkatkan ke versi 3.0, ini tidak akan mempengaruhi lingkungan aplikasi A.

## 12.2. Menciptakan Lingkungan Virtual (Creating Virtual Environments)

Modul yang digunakan untuk membuat dan mengelola lingkungan virtual disebut `__venv. venv__` biasanya akan menginstal versi Python terbaru yang dimiliki. Jika kita memiliki beberapa versi Python di sistem, kita dapat memilih versi Python tertentu dengan menjalankan `python3` atau versi mana pun yang diinginkan.

Untuk membuat lingkungan virtual, tentukan direktori tempat dimana meletakkannya, dan jalankan modul __venv__ sebagai skrip dengan jalur direktori:

```python
python3 -m venv tutorial-env
```

Lokasi direktori yang umum dipakai untuk lingkungan virtual adalah `.venv.` Nama ini membuat direktori biasanya tersembunyi di shell dan dengan demikian terpencil sambil memberikan nama yang menjelaskan mengapa direktori itu ada. Ini juga mencegah bentrok dengan berkas definisi variabel lingkungan .`env` yang didukung beberapa peralatan.

Setelah membuat lingkungan virtual, kita dapat mengaktifkannya.

Di Windows, operasikan:

```python
tutorial-env\Scripts\activate.bat
```

Pada Unix atau MacOS, operasikan

```python
source tutorial-env/bin/activate
```

(Skrip ini ditulis untuk bash shell. Jika kita menggunakan __csh__ atau __fish__ shells, ada pilihan skrip `activate.csh` dan `activate.fish` alternatif yang dapat digunakan.)

Mengaktifkan lingkungan virtual akan mengubah prompt shell kita untuk menunjukkan lingkungan virtual apa yang digunakan, dan memodifikasi lingkungan sehingga menjalankan python akan membuat kita mendapatkan versi dan instalasi Python tertentu. Sebagai contoh:

```python
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>
```

## 12.3. Mengelola Paket dengan pip (Managing Packages with pip)

Kita dapat menginstal, mengupgrade, dan menghapus paket menggunakan program yang disebut __pip__. Secara bawaan pip akan menginstal paket dari Python Package Index, https://pypi.org. kita dapat menelusuri Python Package Index dengan membukanya di peramban atau browser web.

pip memiliki sejumlah sub-perintah: `"install"`, `"uninstall"`, `"freeze"`, dls. 

Kita dapat menginstal versi terbaru dari suatu paket dengan menyebutkan nama suatu paket:

```python
(tutorial-env) $ python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3
```

Kita juga dapat menginstal versi spesifik suatu paket dengan memberikan nama paket diikuti dengan `==` dan nomor versi:

```python
(tutorial-env) $ python -m pip install requests==2.6.0
Collecting requests==2.6.0
  Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0
```

Jika kita menjalankan kembali perintah ini, `pip` akan melihat bahwa versi yang diminta sudah diinstal dan tidak melakukan apa-apa. Kita dapat memberikan nomor versi yang berbeda untuk mendapatkan versi itu, atau juga dapat menjalankan pip install --upgrade untuk meningkatkan paket ke versi terbaru:

```python
(tutorial-env) $ python -m pip install --upgrade requests
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0
```

`pip uninstall` diikuti oleh satu atau beberapa nama paket akan menghapus paket-paket dari lingkungan virtual.

`pip show` akan menampilkan informasi tentang paket tertentu:

```python
(tutorial-env) $ pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:
```

```python
>>> import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"
```

`pip list` akan menampilkan semua paket yang diinstal di lingkungan virtual:

```python
(tutorial-env) $ pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
```

`pip freeze` akan menghasilkan daftar yang sama dari paket yang diinstal, tetapi keluarannya menggunakan format yang diharapkan oleh `pip install`. Sebuah konvensi yang umum digunakan adalah meletakkan daftar ini dalam file `requirements.txt`:

```python
(tutorial-env) $ pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
```

`requirements.txt` kemudian dapat dikirimkan atau commit ke sistem kontrol versi dan dikirim sebagai bagian dari aplikasi. Pengguna kemudian dapat menginstal semua paket yang diperlukan dengan `install -r`:

```python
(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0
```