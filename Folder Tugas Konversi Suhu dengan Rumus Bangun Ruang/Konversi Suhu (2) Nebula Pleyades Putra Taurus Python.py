print("\n====Selamat Datang di Konversi Fahrenheit====")

fahrenheit = float(input("Silahkan masukkan nilai Fahrenheit : "))
celcius = (5 / 9) * (fahrenheit - 32)
reamur = (4 / 9) * (fahrenheit - 32)
kelvin = (5 / 9) * (fahrenheit - 32) + 273

print("Nilai dalam Fahrenheit : ", fahrenheit, "F")
print("Nilai dalam Celcius :", celcius, "C")
print("Nilai dalam reamur :", reamur, "R")
print("Nilai dalam Kelvin :", kelvin, "K")