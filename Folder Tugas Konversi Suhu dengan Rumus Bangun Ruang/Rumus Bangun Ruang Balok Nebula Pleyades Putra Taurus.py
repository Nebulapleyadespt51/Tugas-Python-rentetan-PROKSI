print('Rumus Balok\n1. luas,\n2. volume\n3. keliling balok')
pilihan = int(input('Silahkan masukan pilihan: '))
 
def luas_permukaan(p,l,t):
    L = 2 * ( (p*l) + (p*t) + (l*t) )
    return L
 
def volume(p,l,t):
    V = p * l * t
    return V
 
def keliling(p,l,t):
    k = 4 * (p + l + t)
    return k
 
if pilihan == 1:
    p = int(input('silahkan masukan panjang balok: '))
    l = int(input('silahkan masukan lebar balok: '))
    t = int(input('silahkan masukan tinggi balok: '))
    luas_permukaan(p,l,t)
    print('Jadi balok dengan ukuran panjang:{}, lebar:{}, tinggi:{}\nMempunyai luas:{}'.format(p,l,t, luas_permukaan(p,l,t)))
 
elif pilihan == 2:
    p = int(input('silahkan masukan panjang balok: '))
    l = int(input('silahkan masukan lebar balok: '))
    t = int(input('silahkan masukan tinggi balok: '))
    volume(p,l,t)
    print('Jadi balok dengan ukuran panjang:{}, lebar:{}, tinggi:{}\nMempunyai volume:{}'.format(p,l,t, volume(p,l,t)))
 
elif pilihan == 3:
    p = int(input('silahkan masukan panjang balok: '))
    l = int(input('silahkan masukan lebar balok: '))
    t = int(input('silahkan masukan tinggi balok: '))
    keliling(p,l,t)
    print('Jadi balok dengan ukuran panjang:{}, lebar:{}, tinggi:{}\nMempunyai keliling:{}'.format(p,l,t, keliling(p,l,t)))
 
else:
    print('Yah Sayang Sekali Pilihan tidak tersedia, coba lagi')