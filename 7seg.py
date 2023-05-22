# Đính kèm thư viện RPi.GPIO
import RPi.GPIO as GPIO
# Gọi hàm time để tạo thời gian trễ 
import time


GPIO.setwarnings(False)
GPIO.setmode (GPIO.BOARD)

# Khởi tạo các chân GPIO là đầu ra

GPIO.setup(10,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

GPIO.setup(8,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)


digitclr=[1,1,1,1,1,1,1]
digit0=[0,0,0,0,0,0,1]
digit1=[1,0,0,1,1,1,1]
digit2=[0,0,1,0,0,1,0]
digit3=[0,0,0,0,1,1,0]
digit4=[1,0,0,1,1,0,0]
digit5=[0,1,0,0,1,0,0]
digit6=[0,1,0,0,0,0,0,]
digit7=[0,0,0,1,1,1,1]
digit8=[0,0,0,0,0,0,0]
digit9=[0,0,0,1,1,0,0,]

gpin=[10,3,40,38,36,11,13]

# Vòng lặp xóa và sau đó ghi để hiển thị

def digdisp(digit):
for x in range (0,7):
GPIO.output(gpin[x], digitclr[x])
for x in range (0,7):
GPIO.output(gpin[x], digit[x])

# Vòng lặp để hiển thị các số thập phân từ 0 đến 9

while True:
	digdisp(digit0)
	time.sleep(1)
	digdisp(digit1)
	time.sleep(1)
	digdisp(digit2)
	time.sleep(1)
	digdisp(digit3)
	digitalWrite(8, HIGH);
	time.sleep(3)
	digitalWrite(8, LOW);
	digdisp(digit4)
	time.sleep(1)
	digdisp(digit5)
	time.sleep(1)
	digdisp(digit6)
	digitalWrite(12, HIGH);
	time.sleep(3)
	digitalWrite(12, LOW);
	digdisp(digit7)
	time.sleep(1)
	digdisp(digit8)
	time.sleep(1)
	digdisp(digit9)
	digitalWrite(24, HIGH);
	time.sleep(3)
	digitalWrite(24, LOW);

GPIO.cleanup()