中文说明是必须要有的

WiringPI是树莓派上的类Arduino编程库，方便对GPIO操作，可以提供快速连接和使用传感器模块的开发使用环境


WiringCB是在WiringPI2-python的基础上移植过来的

方便大家使用GPIO口控制个LED、电机、传感器什么的，有兴趣的话可以搭建个智能家居控制中心【做终端控制太浪费资源】

后续代码库中将维护一个FAQ目录，整理好大家的需求和常见问题，希望能给大家带来更加便利更加强大的工具库

================================= Python 篇


安装（cubieboard ubuntu/linaro 环境）：
	
	python 环境安装：
		python-dev 
		python-setuptools

	git clone https://github.com/gootoomoon/WiringCB-python.git   【需要联网】
	或者在电脑上下载：https://github.com/gootoomoon/WiringCB-python
	下载后扔sdcard中
	
	进入WiringCB-python目录
	执行：python setup.py install
	
使用：
	可以直接从 WiringCB-python\cb_test\py_test 中执行测试用例
	python digital.py   【闪灯程序】


API说明：
	wiringpi2.wiringPiSetupPhys() 
	初始化管脚映射，此方法比较好用，直接将cubieboard 上的可用管脚对应数字1~96
	1~48  对应 U14【sata接口附近】
	49~96 对应 U15【USB接口侧】

	wiringpi2.pinMode(pin,1)  设置pin脚 为输出模式
	wiringpi2.pinMode(pin,0)  输入模式
	wiringpi2.pinMode(pin,2)  PWM输出模式【此模式只对PB02有用，另外一个支持硬PWM的管脚未引出】

	

++++++++++++++++++++++++++++++++++++++++++++++++++++++++

================================= C 篇

++++++++++++++++++++++++++++++++++++++++++++++++++++++++
安装：
	git clone https://github.com/gootoomoon/WiringCB-python.git   【需要联网】
	或者在电脑上下载：https://github.com/gootoomoon/WiringCB-python
	下载后扔sdcard中
	
	进入WiringCB-python/WiringPi目录
	执行：./build

使用：
	可以直接从 WiringCB-python\cb_test\c_test 中编译应用程序
	cd  WiringCB-python\cb_test\c_test
	gcc -o led digital.c -lwiringPi -lpthread
	【led 负极接U14 的第2管脚，正极连接一个100欧左右的电阻后连接第1管脚】
	./led	【人品好的话就可以见到闪烁的led灯了】

说明：
	写c代码时接的包含  #include <wiringPi.h> 
	编译时需要连接 -lwiringPi -lpthread -lm 库【一些简单的API也可能只需要连接-lwiringPi就行】

API说明：
	wiringPiSetupPhys()	
	根据cubieboard上的pin脚位置映射管脚，U14的1~48 分别对应1~48，U15的1~48对应49~96
	eg：执行完 wiringPiSetupPhys() 函数后，对49 脚的操作实际上就是对U15第1个管脚的操作【某些特殊的电源、GND为无效管脚】

	digitalWrite(pin,1)；	对编号为pin 的管脚写1【高电平】
	digitalWrite(pin,0)；	拉低

	delay(1000)		延时1秒

			
	
	
 