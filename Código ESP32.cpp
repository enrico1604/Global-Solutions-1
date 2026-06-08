#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include "DHT.h"

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET    -1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);


#define DHTPIN 15      
#define DHTTYPE DHT22  
DHT dht(DHTPIN, DHTTYPE);

#define LDRPIN 34      

Adafruit_MPU6050 mpu;

#define LED_VERDE     4
#define LED_AMARELO   5
#define LED_VERMELHO  18

void setup() {
  Serial.begin(115200);

  pinMode(LED_VERDE, OUTPUT);
  pinMode(LED_AMARELO, OUTPUT);
  pinMode(LED_VERMELHO, OUTPUT);

  dht.begin();

  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("Falha ao iniciar o SSD1306"));
    for(;;); 
  }
  display.clearDisplay();
  display.setTextColor(WHITE);

  if (!mpu.begin()) {
    Serial.println("Falha ao encontrar o chip MPU6050");
    for(;;);
  }
  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
}

void loop() {
  float temp = dht.readTemperature();

  int ldrRaw = analogRead(LDRPIN);
  int lux = map(ldrRaw, 4095, 0, 0, 12000); 

  sensors_event_t a, g, temp_mpu;
  mpu.getEvent(&a, &g, &temp_mpu);
  float accel_mag = sqrt(pow(a.acceleration.x, 2) + pow(a.acceleration.y, 2) + pow(a.acceleration.z, 2));
  float vibracao = abs(accel_mag - 9.8); // Subtrai a gravidade da Terra

  int status_temp = 0;
  int status_lux = 0;
  int status_vib = 0;

  if (temp >= 15.0 && temp <= 25.0) {
    status_temp = 0;
  } else if ((temp > 5.0 && temp < 15.0) || (temp > 30.0 && temp < 40.0)) {
    status_temp = 1;
  } else {
    status_temp = 2;
  }

if (lux >= 0 && lux <= 2000) {
    status_lux = 0;
  } else if (lux > 2000 && lux < 10000) {
    status_lux = 1;
  } else {
    status_lux = 2; 
  }

  if (vibracao >= 0.0 && vibracao <= 2.0) {
    status_vib = 0;
  } else if (vibracao > 2.0 && vibracao <= 8.0) {
    status_vib = 1;
  } else {
    status_vib = 2;
  }

  int count_perigosa = 0;
  int count_alto_risco = 0;

  if (status_temp == 1) count_perigosa++;
  if (status_temp == 2) count_alto_risco++;

  if (status_lux == 1) count_perigosa++;
  if (status_lux == 2) count_alto_risco++;

  if (status_vib == 1) count_perigosa++;
  if (status_vib == 2) count_alto_risco++;

  String msg_status = "";

  if (count_alto_risco >= 1 || count_perigosa >= 2) {
    digitalWrite(LED_VERMELHO, HIGH);
    digitalWrite(LED_AMARELO, LOW);
    digitalWrite(LED_VERDE, LOW);
    msg_status = "ALTO RISCO";
  } 
  else if (count_perigosa == 1) {
    digitalWrite(LED_VERMELHO, LOW);
    digitalWrite(LED_AMARELO, HIGH);
    digitalWrite(LED_VERDE, LOW);
    msg_status = "SITUACAO PERIGOSA";
  } 
  else {
    digitalWrite(LED_VERMELHO, LOW);
    digitalWrite(LED_AMARELO, LOW);
    digitalWrite(LED_VERDE, HIGH);
    msg_status = "TUDO CERTO";
  }

  display.clearDisplay();
  
  display.setTextSize(1);
  display.setCursor(0, 0);
  display.println(F("  SISTEMA DE CAPSULA "));
  display.drawLine(0, 9, 128, 9, WHITE);

  display.setCursor(0, 14);
  display.print(F("Temp: "));
  display.print(temp, 1);
  display.print(F(" C"));

  display.setCursor(0, 26);
  display.print(F("Luz : "));
  display.print(lux);
  display.print(F(" lux"));

  display.setCursor(0, 38);
  display.print(F("Vibr: "));
  display.print(vibracao, 1);
  display.print(F(" m/s2"));

  display.drawLine(0, 49, 128, 49, WHITE);
  display.setCursor(0, 54);
  display.print(msg_status);

  display.display();
  delay(500);
}
