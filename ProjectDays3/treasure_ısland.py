print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************  
''')

print("Hazine adasına hoşgeldiniz.\nHazine adasında doğru yolları tercih ederek ödülünüzü alabilirsiniz")
ilk_secim= input("Bi yol ayrımına geldiniz sağdan mı gitmek istersiniz soldan mı? Sağ -> Sağ/Sol : ").lower()
if ilk_secim == "sağ":
    print("Kaybettiniz! haydutlarla dolu bir yola girdiniz.")
else:
    print("Doğru yolu tercih ettiniz. Şimdi biraz ilerleyin ve nehrin kenarına gidin.")
    ikinci_secim = input("Şimdi karşıya geçmeniz gerekiyor bir tekne mi beklemek istersiniz yoksa yüzerek geçmek mi? Bekle/Yüz : ").lower()
    if ikinci_secim == "yüz":
        print("Kaybettiniz! Timsahlarla dolu bir suya girdiniz.")
    else:
        ucunuc_secim = input("Çok şanslısın tekne hemen geldi! şimdi karşıya geçtin ve karşına 3 adet kapı çıktı hazine bu kapılardan birisinin arkasında tercihin hangisi? Mavi/Kırmızı/Sarı : ").lower()
        if ucunuc_secim != "sarı":
            print("Kaybettini!")
        else:
            print("Tebrikler doğru kapıyı seçtiniz. Hazine envanterinize girdi.")