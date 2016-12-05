void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() 
{
  while (1) 
  {
    float sensorValueX = analogRead(A0);
    float sensorValueY = analogRead(A1);
    float sensorValueZ = analogRead(A2);

    Serial.print("$T:");
    Serial.print( millis() );
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
