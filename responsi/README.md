# Menggunakan dataset Breast-Cancer

```python
https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset
```
---

## Langkah-Langkah
---

### Mengimport dan membaca file

setelah mengimport library yang diperlukan, kita akan membaca file `.csv` kemudian menampilkannya dengan menggunakan perintah `print` dengan menggunakan `df.head` untuk menampilkan 5 data teratas pada file.

```python
import pandas as pd
import numpy as np

df=pd.read_csv('breast-cancer.csv')
print(df.head(5))
```

perintah di bawah ini digunakan untuk menampilkan 5 data terbawah pada file `.csv`

```python
df.tail(5)
```

### Jumlah data

untuk melihat jumlah data dan kolom pada file kita dapat menggunakan perintah di bawah:

```python
df.shape
```

### Mengurutkan daftar nama

perintah di bawah digunakan untuk mengurutkan keunikan nilai yang berbeda dalam index

```python
df.diagnosis.unique()
```

### Mengembalikan nilai

berfungsi mengembalikan objek yang berisi jumlah nilai unik
```python
df['diagnosis'].value_counts()
```

### Kolom

Perintah ini digunakan untuk mengetahui nama colom pada file yang digunakan dalam `.cvs`
```python
df.columns
```
