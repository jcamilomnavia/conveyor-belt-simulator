

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial1.begin(9600);
  Serial.println("Bienvenido!");
  Serial.println("Oprima la tecla B para empezar a correr la banda");
  Serial.println("Oprima la tecla S para detener la banda");
  Serial.println("Oprima la tecla 1 para ir a S1");
  Serial.println("Oprima la tecla 2 para ir a S2");
  Serial.println("Oprima la tecla 3 para ir a S3");
  Serial.println("Oprima la tecla 4 para ir a S4");
}

void loop() {
  while(Serial.available() > 0){
    char caracter = Serial.read();
        Serial1.write(caracter);
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
