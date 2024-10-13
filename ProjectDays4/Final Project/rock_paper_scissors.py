import random

# Taş
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Kağıt
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Makas
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


choise_list = [rock, paper, scissors]
computer_choise = random.choice(choise_list)


print("Taş, kağıt, makas oyununa hoşgeldin!\nŞimdi bir seçim yapman gerekiyor:")
my_choice = int(input("1 -> Taş\n2 -> Kağıt\n3 -> Makas\nSeçiminizi Giriniz: "))


if my_choice == 1:
    my_choice_ascii = rock
    my_choice_text = "Taş"
elif my_choice == 2:
    my_choice_ascii = paper
    my_choice_text = "Kağıt"
else:
    my_choice_ascii = scissors
    my_choice_text = "Makas"


print("\nSizin seçiminiz:\n---------------------------")
print(my_choice_ascii)

print("Bilgisayarın seçimi:\n---------------------------")
print(computer_choise)


if my_choice_ascii == computer_choise:
    print(f"Berabere kaldınız! İkiniz de {my_choice_text} seçtiniz.")
elif (my_choice_text == "Taş" and computer_choise == scissors) or \
     (my_choice_text == "Kağıt" and computer_choise == rock) or \
     (my_choice_text == "Makas" and computer_choise == paper):
    print(f"Kazandınız! Sizin seçiminiz: {my_choice_text}\nBilgisayarın seçimi: {computer_choise}")
else:
    print(f"Kaybettiniz! Sizin seçiminiz: {my_choice_text}\nBilgisayarın seçimi: {computer_choise}")
