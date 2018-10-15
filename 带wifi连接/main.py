import machine
import time##导入machine库与time库
import wifi

ssid="Ap"
password="12345678"



LED_wifi=machine.Pin(16,machine.Pin.OUT)

if(wifi.do_connect(ssid,password)):
    LED_wifi.value(0)##连接到wifi，常亮
else:
    print('wifi连接失败，检查ssid和password')
    print("ssid:%s"%ssid)
    print("password:%s"%password)
    while(1):##无法连接到wifi，快速闪动
        LED_wifi.value(1)
        time.sleep_ms(100)
        LED_wifi.value(0)
        time.sleep_ms(100)

LED=machine.Pin(2,machine.Pin.OUT)##配置GPIO2为输出状态

while(1):
    LED.value(1)##GPIO输出高电平，对于电路来说，LED是灭的。
    time.sleep_ms(1000)##延时1S
    LED.value(0)
    time.sleep_ms(1000)
