kramer-python-control
=====================

Simple python-based [Kramer 8x8](http://www.kramerelectronics.com/products/model.asp?pid=387) (and alike) Computer Graphics Video Matrix Switcher (the protocol is called "Protocol 2000"); more of a PoC as of now with autoswitch capability, but simple enough to get started.

### Basic protocol syntax
Messages use 4 bytes: [INSTRUCTION][INPUT][OUTPUT][MACHINE_NUMBER]  
For instance, msg = 0x01818081, (\x01\x81\x80\x81) will switch all outputs to input #1.

Full protocol documentation can be found [here](http://www.kramerelectronics.com/downloads/protocols/protocol_2000_rev0_51.pdf)  

Default ip address is 192.168.1.39, and port is 5000

### Kramer tools
For quicker message determination, you can use kramer's [Protocol 2000 Calculator](http://www.kramerelectronics.com/support/download.asp?f=35567) (windows only)   
