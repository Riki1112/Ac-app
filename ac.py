def get_boolean_input(prompt):
    while True:
        user_input = input(f"{prompt} (y/t): ").lower()
        if user_input == 'y':
            return True
        elif user_input == 't':
            return False
        else:
            print("Masukkan hanya 'y' untuk ya atau 't' untuk tidak.")

def get_temperature_input():
    while True:
        try:
            suhu = float(input("Masukkan suhu ruangan saat ini (°C): "))
            return suhu
        except ValueError:
            print("Masukkan angka suhu yang valid, contoh: 30.5")

def should_turn_on_ac(sensors):
    return sensors["is_hot"] and sensors["window_closed"] and sensors["someone_home"]

def main():
    print("== SISTEM PENDINGIN UDARA ==")

    temperature = get_temperature_input()
    is_hot = temperature >= 30
    if temperature > 23:
        print(f"\n⚠️  Suhu terlalu panas! ({temperature}°C)")
        print("🔄 Sistem otomatis: Mendinginkan ruangan ke suhu ideal (23°C)...")
        temperature = 23.0 
    sensors = {
        "is_hot": is_hot,  
        "window_closed": get_boolean_input("Apakah jendela tertutup?"),
        "someone_home": get_boolean_input("Apakah ada orang di rumah?")
    }

    print("\n[ STATUS SENSOR ]")
    print(f"Suhu akhir ruangan: {temperature}°C → {'Panas' if is_hot else 'Sejuk'}")

    label_sensor = {
        "window_closed": "Jendela Tertutup",
        "someone_home": "Ada Orang di Rumah"
    }

    for sensor, value in sensors.items():
        if sensor != "is_hot":
            print(f"{label_sensor[sensor]}: {'✓' if value else '✗'}")

    print("\n[ KEPUTUSAN ]")
    if should_turn_on_ac(sensors):
        print(">>> ✅ Air Conditioner MENYALA")
    else:
        print(">>> ❌ Air Conditioner MATI")

main()
