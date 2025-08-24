import argparse
import serial.tools.list_ports
import sys
import serial
import time

def send_to_arduino(ports, msg):
    arduino = serial.Serial(port=ports, baudrate=9600, timeout=1)
    time.sleep(2)

    arduino.write(msg)

def list_com_ports():
    ports = serial.tools.list_ports.comports()
    if not ports:
        print("⚠️ Keine COM-Ports gefunden.")
    else:
        print("🔌 Verfügbare Ports:")
        for port in ports:
            print(f"  {port.device} - {port.description}")

def main():
    parser = argparse.ArgumentParser(description="Beispiel für Terminal Parameter")

    # Argumente definieren
    parser.add_argument("-p", "--port", help="Serieller Port (z.B. COM3)")
    parser.add_argument("-i", "--input", help="Input Datei oder Wert")
    parser.add_argument("-l", "--list", action="store_true", help="Zeigt verfügbare Ports")

    args = parser.parse_args()

    # Wenn nur Liste gewünscht → Ports anzeigen & beenden
    if args.list:
        list_com_ports()
        sys.exit(0)

    # Zugriff auf die Argumente
    if not args.port or not args.input:
        parser.error("Die Argumente -p und -i sind erforderlich (außer bei --list).")

    # Wenn Port und Datei da sind
    if args.port and args.input:
        output_file = "output_hex.txt"
        with open(args.input, "rb") as f:
            content = f.read()
            hex_data = content.hex()

        with open(output_file, "w") as f:
            f.write(hex_data)

        send_to_arduino(args.port, hex_data)
        
        print(hex_data)

    print(f"Port: {args.port}")
    print(f"Input: {args.input}")

if __name__ == "__main__":
    main()
