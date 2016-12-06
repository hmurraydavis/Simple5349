double perviousTime = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() 
{
  while (1) 
  {
    if( (millis() - perviousTime) >= 5){
      perviousTime = millis();
      float sensorValueX = analogRead(A0);
      float sensorValueY = analogRead(A1);
      float sensorValueZ = analogRead(A2);
  
      Serial.print("$T:");
      Serial.print( perviousTime );
      Serial.print(",X:");
      Serial.print( sensorValueX );
      Serial.print(",Y:");
      Serial.print( sensorValueY );
      Serial.print( ",Z:" );
      Serial.print( sensorValueZ );
      Serial.println(); 
      //delay(1);
    }
  }
  
}
