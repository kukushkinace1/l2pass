from settings import RANDOM_WALLETS
from modules.refuel import refuel, mint_bridge
import random


def user_action_selection():
    print("Выберите действие:")
    print("1. Набить транзакции Refuel")
    print("2. Mint and bridge")

    # Получаем ввод от пользователя
    choice = input("Введите номер действия: ")

    # Проверяем, что ввод корректен
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            refuel(accounts)
        elif choice == 2:
            mint_bridge(accounts)
        else:
            return "Неверный выбор"
    else:
        return "Пожалуйста, введите цифру"


if __name__ == '__main__':
    with open("keys.txt", "r") as file:
        accounts = [line.strip() for line in file.readlines()]

    if RANDOM_WALLETS:
        random.shuffle(accounts)

    while True:
        user_action_selection()
