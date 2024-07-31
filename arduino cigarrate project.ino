int red = 12;
int GasPin = A0; # Gaspin 정의

int speakerPin = 8; # speakerPin 정의

int numTones = 8; # 부저센서 핀 정의
int tones[] = {392}; # 어떤 파장으로 출력할지 정의

int day, hour, minute, second = 0; # 시간 정의

void setup(){
  pinMode(red, OUTPUT);
  pinMode(GasPin, INPUT); # Gaspin을 통해 들어오는 이산화탄소 기체 수치를 받기 위해 input으로 정의
  Serial.begin(9600);
}

void loop(){

  int i = analogRead(GasPin); # i = Gas센서를 통해 들어오는 이산화탄소 수치
  Serial.println(i);

  if (i >= 700){ # 이산화탄소 수치가 700을 넘으면
    tone(speakerPin, tones[0]); # 부저를 울려 소리를 냄

    Serial.println("day");
    Serial.println(day);
    Serial.println("hours");
    Serial.println(hour);
    Serial.println("minutes");
    Serial.println(minute);
    Serial.println("second");
    Serial.println(second); # 아두이노가 작동한 시점을 기준으로 몇일 몇시간 몇분 몇초 뒤에 이산화탄소가 검출되었는지 기록

  }
  else if (i < 500){ # 이산화탄소 수치가 500이하로 떨어지면
    noTone(speakerPin); # 부저를 끔
  }

  delay(1000); # delay 1초
  clock(); # clock 함수 호출
} 

int clock () { # 시간을 1초씩 더하는 clock 함수

  second++;

  if (second == 60) {
    minute++;
    second = 0;
  }

  else if (minute == 60) {
    hour++;
    minute = 0;
  }

  else if (hour == 24) {
    day++;
    hour = 0;
  }
  
  return 0;
}
