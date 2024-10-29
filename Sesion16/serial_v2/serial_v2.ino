#include <Servo.h>

Servo myservo;  // create servo object to control a servo

String inputString = "";    //variable para concatenar los bytes del puerto serie
bool completeRead = false;  //variable para indicar la lectura completa del puerto
int pos = 30;

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  myservo.write(pos);
  delay(100);
}

void loop() {
  if (completeRead) {
    digitalWrite(LED_BUILTIN, HIGH);  //Enciende un led de verificación de comunicación
    delay(200);                       // wait for a second
    Serial.print(pos);
    digitalWrite(LED_BUILTIN, LOW);  //Apaga el led de verificación de comunicación
    delay(200);
    inputString = "";
    completeRead = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char text = (char)Serial.read();  //Pregunta por un nuevo dato en el puerto serie
    inputString += text;              //Concatena los datos en una variable inputString
    if (text == '\n') {               //Si lee /n es porque la cadena fue leida por completo
      completeRead = true;
      pos = inputString.toInt();
      myservo.write(pos);
    }
    Serial.print("");
    delay(10);
  }
}