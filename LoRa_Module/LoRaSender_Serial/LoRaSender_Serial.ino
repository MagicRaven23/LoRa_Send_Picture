#include <SPI.h>
#include <LoRa.h>

void setup() {
  Serial.begin(9600);
  while (!Serial);  // Wartet aus Serielle schnitstelle ( beim Uno sinn los )

  Serial.println("LoRa Sender");

  if (!LoRa.begin(868E6)) {  // Gibt wennn ein Fehler aus trit false 
    Serial.println("Starting LoRa failed!");
    while (1);  // Das programm bleit stehen es ist eine endlos schleife
  }
}

void loop() {
  while (Serial.available() == 0){}  // wait for data available
  String msg = Serial.readString();  // read until timeout
  msg.trim();                        // remove any \r \n whitespace at the end of the String
  Serial.println("Massage sent");

  // send packet
    LoRa.beginPacket();
    LoRa.print(msg);
    LoRa.endPacket();
  
}
