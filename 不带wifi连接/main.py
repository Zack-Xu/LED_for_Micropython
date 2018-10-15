import machine
import time##导入machine库与time库

LED=machine.Pin(2,machine.Pin.OUT)##配置GPIO2为输出状态

while(1):
    LED.value(1)##GPIO输出高电平，对于电路来说，LED是灭的。
    time.sleep_ms(1000)##延时1S
    print('灭')
    LED.value(0)
    time.sleep_ms(1000)
    print('亮')
