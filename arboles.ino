// Constantes

const int ledVerde = 8;
const int ledRojo = 10;
const int ledAzul = 12;
const int pb1 = 2;
const int pb2 = 4;
const int pb3 = 6;
const int potenciometro = A3;

// Variables
int valorPotenciometro;

void setup() {
  pinMode(ledVerde, OUTPUT);
  pinMode(ledRojo, OUTPUT);
  pinMode(ledAzul, OUTPUT);
  pinMode(pb1, INPUT_PULLUP);
  pinMode(pb2, INPUT_PULLUP);
  pinMode(pb3, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  static int lastState1 = HIGH;
  static int lastState2 = HIGH;
  static int lastState3 = HIGH;  // Estado anterior del botón
  int currentState1 = digitalRead(pb1);
  int currentState2 = digitalRead(pb2);
  int currentState3 = digitalRead(pb3);

  if (digitalRead(pb1) == LOW) {
    digitalWrite(ledVerde, HIGH);
    delay(200);
  } else {
    digitalWrite(ledVerde, LOW);
  }
  if (currentState1 != lastState1) {
    if (currentState1 == LOW) {
      Serial.println("green_pressed");
    } else {
      Serial.println("green_released");
    }
  }

  if (digitalRead(pb2) == LOW) {
    digitalWrite(ledRojo, HIGH);
  } else {
    digitalWrite(ledRojo, LOW);
  }

  if (currentState2 != lastState2) {
    if (currentState2 == LOW) {
      Serial.println("red_pressed");
    } else {
      Serial.println("red_released");
    }
  }

  if (digitalRead(pb3) == LOW) {
    digitalWrite(ledAzul, HIGH);
  } else {
    digitalWrite(ledAzul, LOW);
  }

  if (currentState3 != lastState3) {
    if (currentState3 == LOW) {
      Serial.println("blue_pressed");
    } else {
      Serial.println("blue_released");
    }
  }

  lastState1 = currentState1;
  lastState2 = currentState2;
  lastState3 = currentState3;
  //Lee el valor del potenciómetro y lo envía a Processing a través del puerto serie
  valorPotenciometro = analogRead(potenciometro);
  Serial.println(valorPotenciometro);
  delay(50);  //Pequeña pausa para evitar una transimisón muy rápida de datos por el puerto serie
}
