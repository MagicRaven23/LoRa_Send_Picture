import argparse
import serial.tools.list_ports
import sys
import serial
import time

def send_to_arduino(ports, msg, baude=9600):
    arduino = serial.Serial()
    arduino.baudrate = baude
    arduino.port = ports
    arduino.open()

    
    arduino.write(msg.encode())
    arduino.close()

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
    parser.add_argument("-l", "--list", action="store_true", help="Zeigt verfügbare Ports")

    # Entweder -i ODER -t 
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-i", "--input", help="Input Datei oder Wert")
    group.add_argument("-t", "--text", type=str, help="Sende text über LoRa")

    args = parser.parse_args()

    # Wenn nur Liste gewünscht → Ports anzeigen & beenden
    if args.list:
        list_com_ports()
        sys.exit(0)

     # Zugriff auf die Argumente
    if not args.port:
        parser.error("Das Argument -p ist erforderlich (außer bei --list).")

    # Text Senden
    if args.text and args.port:
        send_to_arduino(args.port, args.text)   


    # Wenn Port und Datei da sind
    if args.port and args.input:
        output_file = "output_hex.txt"
        with open(args.input, "rb") as f:
            content = f.read()
            hex_data = content.hex()

        with open(output_file, "w") as f:
            f.write(hex_data)

        send_to_arduino(args.port, hex_data)
        
        print(hex_data.split())

    print(f"Port: {args.port}")

    if not args.input:
        print(f"Text: {args.text}")
    else:
        print(f"Input: {args.input}")

if __name__ == "__main__":
    main()
