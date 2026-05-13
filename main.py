def kiritilgan_son_nuri(son):
    if son > 0:
        return "Musbat"
    elif son < 0:
        return "Manfiy"
    else:
        return "Nol"

son = float(input("Istalgan sonni kiriting: "))
print(kiritilgan_son_nuri(son))
