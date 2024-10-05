# 1
jumla = input("Jumla kiriting: ")

def uzunlik(matn):
    
    uzunligi = 0
    
    for i in matn:
        uzunligi += 1
    return uzunligi

print(f"jumla uzunligi {uzunlik(jumla)}")



# 2
faktlar = {
    1984: "Yer sharining eng katta vulqoni otilgan",
    1876: "Telefonning ixtiro qilingan",
    868: "Eng qadimgi kitob chop etilgan"   
}

def vaqt_mashinasi(yil):
    if yil in faktlar:
        return faktlar[yil]
    else:
        return "bunday malumot yoq"

kiritilgan_yil = int(input("yil kiriyng: "))

print(vaqt_mashinasi(kiritilgan_yil))


