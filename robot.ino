char command;

void setup() {
  Serial.begin(9600);
  pinMode(8, OUTPUT);  // Example motor pins
  pinMode(9, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    command = Serial.read();

    if (command == 'F') {
      // Forward
      digitalWrite(8, HIGH);
      digitalWrite(9, LOW);
    }
    else if (command == 'B') {
      // Backward
      digitalWrite(8, LOW);
      digitalWrite(9, HIGH);
    }
    else if (command == 'L') {
      // Left turn
      // Add your motor logic here
    }
    else if (command == 'R') {
      // Right turn
      // Add your motor logic here
    }
    else if (command == 'S') {
      // Stop
      digitalWrite(8, LOW);
      digitalWrite(9, LOW);
    }
  }
}
