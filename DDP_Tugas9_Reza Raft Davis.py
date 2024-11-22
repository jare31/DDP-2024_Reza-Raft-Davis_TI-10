print()
print('## Nomor 1 ##')
def celcius_ke_farenheit(celcius):
    konversi=(celcius*9/5)+32
    return konversi

print(celcius_ke_farenheit(0))
print(celcius_ke_farenheit(100))

print()
print('## Nomor 2 ##')
def ganjil_genap(bilangan):
    penentu=bilangan % 2 == 0
    return penentu

print(ganjil_genap(4)) #True
print(ganjil_genap(7)) #True

print()
print('## Nomor 3 ##')
def nilai(keterangan):
    if keterangan >= 80:
        print('lulus')
    elif keterangan <= 60:
        print('gagal')
    else:
        print('tdak valid')            

nilai(80)
nilai(60)

print()
print('## Nomor 4 ##')
def bilangan_ganjil(asoy):
    return[i for i in range(1,asoy,2)]
print(bilangan_ganjil(20))

