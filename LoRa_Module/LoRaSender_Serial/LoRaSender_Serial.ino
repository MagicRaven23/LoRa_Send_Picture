#include <SPI.h>
#include <LoRa.h>

void setup() {
  Serial.begin(9600);
  while (!Serial);

  Serial.println("LoRa Sender");

  if (!LoRa.begin(915E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
}

void loop() {
  if (Serial.available()) {
    String msg = Serial.readString(); // bis Newline lesen
    Serial.print("Empfangen: ");
    Serial.println(msg);

    // send packet
    LoRa.beginPacket();
    LoRa.print(msg);
    LoRa.endPacket();
  }

  
}
