

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial1.begin(9600);

  Serial.println("Oprima la tecla E para empezar a correr la banda...");
}

void loop() {
  while(Serial.available() > 0){
    char caracter = Serial.read();
        Serial1.write("e");
    }
  // put your main code here, to run repeatedly:
  
}

void serialEvent1(){
  while(Serial1.available() > 0){
    char message = Serial1.read();
    Serial.print(message);  
  }
  // Serial.println();
}
