# define ativar_motor '1'
# define desativar_motor '2'

char comando = 'S';
bool novo_comando = false;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(3,OUTPUT);
  Serial.write("1"); 

}

void loop() {

  if(Serial.available() > 0){

    comando = Serial.read();
    novo_comando = true;
  } 

  if(novo_comando){
    novo_comando = false;  

    if (comando == ativar_motor){
      digitalWrite(3,HIGH);
    }
    else if(comando == desativar_motor){
      digitalWrite(3,LOW);
      }
  }
  
  
}
