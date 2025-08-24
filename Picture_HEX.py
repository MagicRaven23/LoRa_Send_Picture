# Bild in Hex-Code umwandeln
def image_to_hex(path, output_path="output_hex.txt"):
    with open(path, "rb") as f:  # Bild im Binärmodus öffnen
        content = f.read()       # Bilddaten einlesen
        hex_data = content.hex() # In Hex umwandeln

    # Hex in eine Textdatei schreiben
    with open(output_path, "w") as f:
        f.write(hex_data)

    print(f"Hex-Daten gespeichert in: {output_path}")


image_to_hex("bild_01.jpg")

# Hex wieder zurück in Bild-Datei umwandeln
def hex_to_image(hex_file, output_image="output.png"):
    # Hex-String aus der Textdatei laden
    with open(hex_file, "r") as f:
        hex_data = f.read().strip()
    
    # Hex zurück zu Bytes
    img_bytes = bytes.fromhex(hex_data)
    
    # Bytes als Bild speichern
    with open(output_image, "wb") as f:
        f.write(img_bytes)

    print(f"Bild wiederhergestellt: {output_image}")


# Beispielaufruf
hex_to_image("output_hex.txt", "rekonstruiertes_bild.png")

