#include <SPI.h>
#include <LoRa.h>

int counter = 0;
int status = 7;

void setup() {
  Serial.begin(9600);
  //while (!Serial);  // Wartet aus Serielle schnitstelle ( beim Uno sinn los )
  
  pinMode(status, OUTPUT);
  digitalWrite(status, LOW);
  Serial.println("LoRa Sender");

  int maxRetries = 5;
  int attempt = 0;

  while (!LoRa.begin(868E6) && attempt < maxRetries) {  // Gibt wennn ein Fehler aus trit false 
    Serial.print("Starting LoRa failed!");
    Serial.println(attempt + 1);
    attempt++;
    delay(2000);
  }

  if (attempt == maxRetries) {
    Serial.println("LoRa konnte nicht gestartet werden, Modul neustraten");
    stop_ard();
    while (1);  // Das programm bleit stehen es ist eine endlos schleife
  }
  Serial.println("LoRa Erfolgreich gestartet");
  start_ard();
}

void loop() {
  while (Serial.available() == 0){digitalWrite(status, LOW);}  // wait for data available
  String msg = Serial.readString();  // read until timeout
  msg.trim();                        // remove any \r \n whitespace at the end of the String
  Serial.println("Massage sent");
  digitalWrite(status, HIGH);
  // send packet
  LoRa.beginPacket();
  LoRa.print(msg);
  LoRa.endPacket();
  
}

void stop_ard() {
  digitalWrite(status, HIGH);
  delay(5000);
  digitalWrite(status, LOW);
}

void start_ard() {
  digitalWrite(status, HIGH);
  delay(1500);
  digitalWrite(status, LOW);
}
