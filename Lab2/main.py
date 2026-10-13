import os
import subprocess
import sys

from dependencies import install_dependencies

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def run_task(num):
    """Chay task_2_<num>.py nhu mot script doc lap."""
    clear_screen()
    print(f"===== TASK 2.{num} =====\n")
    path = os.path.join(BASE_DIR, f"task_2_{num}.py")
    if not os.path.exists(path):
        print(f"[!] Khong tim thay file: task_2_{num}.py")
    else:
        try:
            subprocess.run([sys.executable, path], cwd=BASE_DIR)
        except Exception as e:
            print(f"[!] Loi khi chay task 2.{num}: {e}")
    input("\nNhan Enter de quay ve menu...")


def show_menu():
    print("===== LAB 2 - MENU =====")
    print("1. Task 2.1 - Feistel / Avalanche")
    print("2. Task 2.2 - AES modes (ECB/CBC/CFB/OFB/CTR)")
    print("3. Task 2.3 - DES Avalanche Effect")
    print("4. Task 2.4 - Error Propagation")
    print("5. Task 2.5 (No coding required. Please choose another task)")
    print("6. Task 2.6 - Mersenne Primes, GCD, Modular Exponentiation")
    print("0. Exit")
    print("========================")


def main():
    # Tu dong cai het dependency, da co thi khong in ra (xu ly trong dependencies.py)
    install_dependencies()

    while True:
        clear_screen()
        show_menu()
        choice = input("Chon task (0-6): ").strip()

        if choice == "0":
            clear_screen()
            print("Tam biet!")
            break
        elif choice in ("1", "2", "3", "4", "6"):
            run_task(choice)
        else:
            print("[!] Lua chon khong hop le!")
            input("Nhan Enter de tiep tuc...")


if __name__ == "__main__":
    main()
