import secrets
import string
import keyboard
alphabet = string.ascii_letters
alphabet2 = string.ascii_letters + string.digits
alphabet3 = string.ascii_letters + string.digits + string.punctuation
alphabet4 = string.ascii_letters + string.punctuation
password1 = ''.join(secrets.choice(alphabet) for i in range(12))
password2 = ''.join(secrets.choice(alphabet2) for i in range(12))
password3 = ''.join(secrets.choice(alphabet3) for i in range(12))
password4 = ''.join(secrets.choice(alphabet4) for i in range(12))
us_input1 = input(r"Вы хотите использовать цифры в пароле? Y=да N=нет: ")
us_input2 = input(r"Вы хотите использовать спецсимволы в пароле? Y=да N=нет: ")
if us_input1 == "Y" and us_input2 == "Y" or us_input1 == "y" and us_input2 == "y":
    print(password3)
if us_input1 == "N" and us_input2 == "N" or us_input1 == "n" and us_input2 == "n":
        print(password1)
if us_input1 == "Y" and us_input2 == "N" or us_input1 == "y" and us_input2 == "n":
    print(password2)
if us_input1 == "N" and us_input2 == "Y" or us_input1 == "n" and us_input2 == "y":
 print(password4)
print("Нажмите любую клавишу чтобы закончить")
keyboard.read_key()