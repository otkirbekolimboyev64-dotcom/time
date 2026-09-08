import time
import os
import datetime


def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')


def get_time():
    """Hozirgi vaqtni oladi"""
    now = datetime.datetime.now()
    return {
        'hour': now.hour,
        'minute': now.minute,
        'second': now.second,
        'date': now.strftime('%d-%m-%Y'),
        'weekday': now.strftime('%A'),
        'month': now.strftime('%B'),
        'year': now.year
    }


def get_weekday_uz(weekday_en):
    """Hafta kunini o'zbekchaga o'giradi"""
    weekdays = {
        'Monday': 'Dushanba',
        'Tuesday': 'Seshanba',
        'Wednesday': 'Chorshanba',
        'Thursday': 'Payshanba',
        'Friday': 'Juma',
        'Saturday': 'Shanba',
        'Sunday': 'Yakshanba'
    }
    return weekdays.get(weekday_en, weekday_en)


def get_month_uz(month_en):
    """Oy nomini o'zbekchaga o'giradi"""
    months = {
        'January': 'Yanvar',
        'February': 'Fevral',
        'March': 'Mart',
        'April': 'Aprel',
        'May': 'May',
        'June': 'Iyun',
        'July': 'Iyul',
        'August': 'Avgust',
        'September': 'Sentabr',
        'October': 'Oktabr',
        'November': 'Noyabr',
        'December': 'Dekabr'
    }
    return months.get(month_en, month_en)


def get_timezone():
    """Vaqt zonasini oladi"""
    try:
        return time.tzname[0]
    except:
        return 'Unknown'


def show_digital_clock():
    """Raqamli soatni ko'rsatadi"""
    clear_screen()

    time_data = get_time()

    # Soat formatlash
    hour = time_data['hour']
    minute = time_data['minute']
    second = time_data['second']

    # AM/PM format
    am_pm = 'AM' if hour < 12 else 'PM'
    hour_12 = hour % 12
    if hour_12 == 0:
        hour_12 = 12

    # Katta format
    time_str = f"{hour_12:02d}:{minute:02d}:{second:02d}"

    # Chiroyli ko'rinish
    print("=" * 50)
    print("🕐 DIGITAL CLOCK")
    print("=" * 50)

    # Katta soat
    print("\n" + " " * 10 + "█" * 30)
    print(" " * 10 + "█" + " " * 28 + "█")
    print(" " * 10 + f"█   {hour_12:02d} : {minute:02d} : {second:02d}   █")
    print(" " * 10 + "█" + " " * 28 + "█")
    print(" " * 10 + "█" * 30)

    print(f"\n{' ' * 15}⏰ {am_pm}")

    print("\n" + "-" * 50)

    # Sana
    weekday_uz = get_weekday_uz(time_data['weekday'])
    month_uz = get_month_uz(time_data['month'])
    date_str = f"{weekday_uz}, {time_data['date']} {month_uz} {time_data['year']}"
    print(f"📅 {date_str}")

    # Vaqt zonasi
    print(f"🌍 Vaqt zonasi: {get_timezone()}")

    print("-" * 50)


def show_analog_clock():
    """Analog soatni ko'rsatadi (matnli)"""
    time_data = get_time()
    hour = time_data['hour'] % 12
    minute = time_data['minute']

    # Soat pozitsiyasi (0-11)
    hour_pos = hour + minute / 60

    # 12 soatlik siferblat
    clock = [
        "    12    ",
        " 11    1  ",
        "10      2 ",
        "9        3",
        "8       4 ",
        " 7    5  ",
        "    6    "
    ]

    # Soat va minut strelkalari pozitsiyasi
    # Bu soddalashtirilgan versiya
    hour_hand = round(hour_pos * 5) % 60
    minute_hand = minute

    clear_screen()
    print("=" * 50)
    print("🕐 ANALOG SOAT")
    print("=" * 50)

    print("\n   12")
    print(" 11    1")
    print("10      2")
    print("9        3")
    print("8       4")
    print(" 7    5")
    print("   6")

    print("\n" + "-" * 50)
    print(f"⏰ {hour:02d}:{minute:02d}")
    print("-" * 50)


def main():
    mode = 'digital'  # digital yoki analog

    while True:
        if mode == 'digital':
            show_digital_clock()
        else:
            show_analog_clock()

        print("\n1. Rejimni o'zgartirish (Digital/Analog)")
        print("2. Chiqish")
        print("-" * 50)

        choice = input("\nTanlang (1-2): ").strip()

        if choice == '1':
            if mode == 'digital':
                mode = 'analog'
            else:
                mode = 'digital'
            continue
        elif choice == '2':
            clear_screen()
            print("=" * 50)
            print("👋 RAXMAT! DIGITAL CLOCK YAKUNLANDI!")
            print("=" * 50)
            break
        else:
            # Har bir soniyada yangilanish
            time.sleep(1)


if __name__ == "__main__":
    main()