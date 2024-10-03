print("Pizza dükkanıma hoşgeldiniz.")
size = input("Pizza boyutunuz nasıl olsun Küçük(k), Orta(o), Büyük(b) : ")
pepperoni = input("Pizzanızda pepperoni olsun mu? Evet(e), Hayır(h) : ")
extra_cheese = input("Ekstra peynir ister misiniz? Evet(e), Hayır(h) : ")
tutar = 0
if size == 'k':
    tutar += 15
    if pepperoni == 'e':
        tutar +=2
elif size == 'o':
    tutar += 20
    if pepperoni == 'e':
        tutar += 3
elif size == 'b':
    tutar += 25
    if pepperoni == 'e':
        tutar += 3
else:
    print("Hatalı giriş yaptınız.")


if extra_cheese == 'e':
    tutar +=1


print(f"Toplam ödemeniz gereken tutar : {tutar}")

