import os
import time


def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')


def get_float(prompt, min_val=0):
    """Foydalanuvchidan float son oladi"""
    while True:
        try:
            value = float(input(prompt))
            if value > min_val:
                return value
            print(f"❌ {min_val} dan katta son kiriting!")
        except ValueError:
            print("❌ Iltimos, son kiriting!")


def calculate_bmi(weight, height):
    """BMI ni hisoblaydi"""
    return weight / (height ** 2)


def get_bmi_category(bmi):
    """BMI kategoriyasini aniqlaydi"""
    if bmi < 16:
        return {
            'category': 'Og\'ir darajadagi vazn yetishmasligi',
            'emoji': '⚡',
            'color': '🔴'
        }
    elif bmi < 17:
        return {
            'category': 'O\'rta darajadagi vazn yetishmasligi',
            'emoji': '⚠️',
            'color': '🟠'
        }
    elif bmi < 18.5:
        return {
            'category': 'Engil darajadagi vazn yetishmasligi',
            'emoji': '📉',
            'color': '🟡'
        }
    elif bmi < 25:
        return {
            'category': 'Normal vazn',
            'emoji': '✅',
            'color': '🟢'
        }
    elif bmi < 30:
        return {
            'category': 'Ortiqcha vazn (Semirishning 1-darajasi)',
            'emoji': '📈',
            'color': '🟠'
        }
    elif bmi < 35:
        return {
            'category': 'Semirishning 2-darajasi',
            'emoji': '🔺',
            'color': '🔴'
        }
    elif bmi < 40:
        return {
            'category': 'Semirishning 3-darajasi (Og\'ir)',
            'emoji': '🚨',
            'color': '🔴'
        }
    else:
        return {
            'category': 'Semirishning 4-darajasi (Juda og\'ir)',
            'emoji': '💀',
            'color': '⚫'
        }


def show_bmi_table():
    """BMI jadvalini ko'rsatadi"""
    clear_screen()
    print("=" * 50)
    print("📊 BMI JADVALI")
    print("=" * 50)
    print("\n  BMI  | Holat")
    print("-" * 30)
    print(" < 16  | Og'ir darajadagi vazn yetishmasligi")
    print(" 16-17 | O'rta darajadagi vazn yetishmasligi")
    print(" 17-18.5| Engil darajadagi vazn yetishmasligi")
    print("18.5-25 | Normal vazn")
    print(" 25-30 | Ortiqcha vazn")
    print(" 30-35 | Semirishning 2-darajasi")
    print(" 35-40 | Semirishning 3-darajasi")
    print(" > 40  | Semirishning 4-darajasi")
    print("=" * 50)
    input("\n⏎ Davom etish uchun Enter bosing...")


def show_result(weight, height, bmi, category):
    """Natijani ko'rsatadi"""
    clear_screen()
    print("=" * 50)
    print("📊 BMI NATIJASI")
    print("=" * 50)

    print(f"\n📏 Bo'y: {height:.2f} m")
    print(f"⚖️  Vazn: {weight:.2f} kg")
    print("-" * 30)
    print(f"📊 BMI: {bmi:.2f}")
    print("-" * 30)

    print(f"\n{category['color']} {category['emoji']} {category['category']}")

    # Tavsiya
    print("\n💡 TAVSIYA:")
    if bmi < 18.5:
        print("   🍽️  Sog'lom ovqatlaning va vazn oling!")
    elif bmi < 25:
        print("   🎉  Sog'lom vazn! Davom eting!")
    elif bmi < 30:
        print("   🏃  Jismoniy faollikni oshiring!")
    else:
        print("   🏥  Shifokor bilan maslahatlashing!")

    print("=" * 50)


def get_units():
    """O'lchov birliklarini tanlash"""
    print("\n📏 O'lchov birliklarini tanlang:")
    print("1. Metrik (kg, m)")
    print("2. Imperial (lb, ft/in)")
    print("-" * 30)

    while True:
        choice = input("\nTanlang (1-2): ").strip()
        if choice == '1':
            return 'metric'
        elif choice == '2':
            return 'imperial'
        print("❌ Noto'g'ri tanlov!")


def get_imperial_height():
    """Imperial o'lchovda bo'y olish (fut va dyum)"""
    feet = get_float("👣 Fut: ", 0)
    inches = get_float("📏 Dyum: ", 0)
    return (feet * 0.3048) + (inches * 0.0254)


def main():
    while True:
        clear_screen()
        print("=" * 50)
        print("⚖️  BMI CALCULATOR")
        print("=" * 50)

        print("\n1. BMI hisoblash")
        print("2. BMI jadvali")
        print("3. Chiqish")
        print("-" * 50)

        choice = input("\nTanlang (1-3): ").strip()

        if choice == '1':
            units = get_units()

            if units == 'metric':
                print("\n📏 Metrik o'lchov:")
                weight = get_float("⚖️  Vazn (kg): ", 0)
                height = get_float("📏 Bo'y (m): ", 0)
            else:
                print("\n📏 Imperial o'lchov:")
                weight = get_float("⚖️  Vazn (lb): ", 0)
                height = get_imperial_height()
                # lb ni kg ga o'tkazish
                weight = weight * 0.453592

            bmi = calculate_bmi(weight, height)
            category = get_bmi_category(bmi)
            show_result(weight, height, bmi, category)

            input("\n⏎ Davom etish uchun Enter bosing...")

        elif choice == '2':
            show_bmi_table()

        elif choice == '3':
            clear_screen()
            print("=" * 50)
            print("👋 RAXMAT! BMI CALCULATOR YAKUNLANDI!")
            print("=" * 50)
            print("\n⚖️  Sog'lom bo'ling!")
            break

        else:
            print("❌ Noto'g'ri tanlov!")
            time.sleep(1)


if __name__ == "__main__":
    main()