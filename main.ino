#define BUTTON_PIN 2

const int ledPin1 = 8;
const int ledPin2 = 9;

bool buttonPressed = false;

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);

  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);

  Serial.begin(9600);
}

void ledSequence() {
  digitalWrite(ledPin1, HIGH);
  delay(250);
  digitalWrite(ledPin1, LOW);

  digitalWrite(ledPin2, HIGH);
  delay(250);
  digitalWrite(ledPin2, LOW);
}

void loop() {
  if (digitalRead(BUTTON_PIN) == LOW) {
    if (!buttonPressed) {
      Serial.println("Doorbell Pressed");
      buttonPressed = true;
      
      for (int i = 0; i < 30; i++) {
        ledSequence();
      }
    }
  } else {
    buttonPressed = false;
  }

  delay(50);
}