def eng_uzungatrni_top(fayl_ismi):
    eng_uzungatr = ""
    max_uzunluk = 0
    with open(fayl_ismi, "r") as f:
        for satr in f:
            satr = satr.strip()
            if len(satr) > max_uzunluk:
                max_uzunluk = len(satr)
                eng_uzungatr = satr
    return eng_uzungatr, max_uzunluk

fayl_ismi = "matn.txt"
eng_uzungatr, max_uzunluk = eng_uzungatrni_top(fayl_ismi)
print(f"Eng uzun satr: {eng_uzungatr}")
print(f"Uzunligi: {max_uzunluk}")
