LED demo for micropython(ESP8266)

��ʹ��ampy��ʽ�������ϴ���Micropython�У�����Ҫ�޸�flash.bat��COM�Ķ˿ں�(windowsϵͳ��)

When using ampy to upload code to Micropython, you need to modify the port number of COM in flash. bat (under Windows)


������Ҫ����������notepad���ı��༭����main.py�����޸����е�ssid��password

wifi����״̬��ͨ��repl���ı�����ʽ������
ͬʱGPIO16�ϵ�LEDҲ�����wifi����ָʾ
A.cannot connect wifi ����������
B.connected : ����
����GPIO2�ϵ�LED����wifi�������Ժ�������1s���������


All you need to do is use text editors like Notepad to open main.py and modify the SSID and password in it

WiFi connection state will be fed back in text on repl.
At the same time, LED on GPIO16 also reacts to WiFi connection state.
A.cannot connect WiFi: fast flashing
B.connected: always on
The LED on GPIO2 will blink at the interval of 1s after the WiFi connection.