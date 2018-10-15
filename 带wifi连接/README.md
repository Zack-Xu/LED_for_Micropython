LED demo for micropython(ESP8266)

当使用ampy方式将代码上传到Micropython中，你需要修改flash.bat中COM的端口号(windows系统下)

When using ampy to upload code to Micropython, you need to modify the port number of COM in flash. bat (under Windows)


你所需要做的是利用notepad等文本编辑器打开main.py并且修改其中的ssid和password

wifi连接状态会通过repl以文本的形式反馈。
同时GPIO16上的LED也会进行wifi连接指示
A.cannot connect wifi ：快速闪动
B.connected : 常亮
而在GPIO2上的LED，在wifi连接上以后则会进行1s间隔闪动。


All you need to do is use text editors like Notepad to open main.py and modify the SSID and password in it

WiFi connection state will be fed back in text on repl.
At the same time, LED on GPIO16 also reacts to WiFi connection state.
A.cannot connect WiFi: fast flashing
B.connected: always on
The LED on GPIO2 will blink at the interval of 1s after the WiFi connection.