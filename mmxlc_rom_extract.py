#!/usr/bin/env python
with open("RXC1.exe", "rb") as exe:
    exe.seek(0xB8A850,0)
    rx1 = exe.read(0x180000)
    exe.seek(0xD8A850,0)
    mx1 = exe.read(0x180000)
    exe.seek(0xF8A850,0)
    rx2 = exe.read(0x180000)
    exe.seek(0x110A850,0)
    mx2 = exe.read(0x180000)
    exe.seek(0x128A850,0)
    rx3 = exe.read(0x200000)
    exe.seek(0x148A850,0)
    mx3 = exe.read(0x2000000)
with open("Rock Man X" + ".sfc", "wb") as rx1out:
	rx1out.write(rx1)
	rx1out.close()
with open("Mega Man X" + ".sfc", "wb") as mx1out:
	mx1out.write(mx1)
	mx1out.close()
with open("Rock Man X2" + ".sfc", "wb") as rx2out:
	rx2out.write(rx2)
	rx2out.close()
with open("Mega Man X2" + ".sfc", "wb") as mx2out:
	mx2out.write(mx2)
	mx2out.close()
with open("Rock Man X3" + ".sfc", "wb") as rx3out:
	rx3out.write(rx3)
	rx3out.close()
with open("Mega Man X3" + ".sfc", "wb") as mx3out:
	mx3out.write(mx3)
	mx3out.close()