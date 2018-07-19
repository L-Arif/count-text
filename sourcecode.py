print("Count Substance of Text")
print(" ")

x = input("Masukkan teks disini : ")
print(" ")

jumlah_karakter = len(x)
print("Jumlah karakter adalah", jumlah_karakter)

y = x.split()
jumlah_kata = len(y)
print("Jumlah kata adalah", jumlah_kata)

z = x.split(". ")
jumlah_kalimat = len(z)
print("Jumlah kalimat adalah", jumlah_kalimat)

print(" ")


q1 = input("Apakah Anda ingin mengetahui karakter berurut? (Y/N)")

if q1=="Y" or q1=="y":
    letter = int(input("Masukkan berapa huruf yang ingin Anda ketahui: "))
    if letter <= jumlah_karakter:
        for i in range(letter):
            print("Huruf ke-%i adalah %s" %(i+1,x[i]))
    else:
        print("Maaf hanya tersedia %i karakter" % jumlah_karakter)
        for i in range(jumlah_karakter):
            print("Huruf ke-%i adalah %s" %(i+1, x[i]))
else:
    print("Baik, tidak apa :-)")

print(" ")

q2 = input("Apakah Anda ingin mengetahui kata berurut? (Y/N)")

if q2=="Y" or q2=="y":
    word = int(input("Masukkan berapa kata yang ingin Anda ketahui: "))
    if word <= jumlah_kata:
        for i in range(word):
            print("Kata ke-%i adalah %s" %(i+1,y[i]))
    else:
        print("Maaf hanya tersedia %i kata" % jumlah_kata)
        for i in range(jumlah_karakter):
            print("Kata ke-%i adalah %s" %(i+1, y[i]))
else:
    print("Baik, tidak apa :-)")

print(" ")

q3 = input("Apakah Anda ingin mengetahui kalimat berurut? (Y/N)")

if q3 == "Y" or q3 == "y":
    sentence = int(input("Masukkan berapa kalimat yang ingin Anda ketahui: "))
    if sentence <= jumlah_kalimat:
        for i in range(sentence):
            print("Kalimat ke-%i adalah %s" %(i+1, z[i]))
    else:
        print("Maaf hanya tersedia %i kalimat" % jumlah_kalimat)
        for i in range(jumlah_kalimat):
            print("Kalimat ke-%i adalah %s" %(i+1, z[i]))
else:
    print("Baik, tidak apa :-)")

print(" ")
