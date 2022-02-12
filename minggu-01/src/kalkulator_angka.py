#interpreter bertindak sebagai kalkulator sederhana dengan operator +,-,* dan/
2 + 2
50 - 5*6
(50 - 5*6) / 4
8 / 5  # division always returns a floating point number

#Division (/) selalu mengembalikan float atau bilangan pecahan
17 / 3  # classic division returns a float
17 // 3  # floor division discards the fractional part
17 % 3  # the % operator returns the remainder of the division
5 * 3 + 2  # floored quotient * divisor + remainder

#menggunakan operator ** untuk menghitung pemangkatan
5 ** 2  # 5 squared
2 ** 7  # 2 to the power of 7

#tanda (=) digunakan untuk memberikan nilai ke variabel
width = 20
height = 5 * 9
width * height

#Jika variabel tidak "didefinisikan" (diberi nilai), maka akan muncul kesalahan
n  # try to access an undefined variable

#operator dengan operan tipe campuran akan mengubah operan integer ke floating point
4 * 3.75 - 1

#Dalam mode interaktif, ekspresi cetak terakhir diberikan ke variabel _
tax = 12.5 / 100
price = 100.50
price * tax
price + _
round(_, 2)