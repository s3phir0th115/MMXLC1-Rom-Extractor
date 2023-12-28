#!/usr/bin/env python
import hashlib
int_sha512 = "58101af83d473667537b9e27f2d5154831917ad63193644d4c6b6c69ac5341923801ac641ba023a7ecb4e7be026a7ea3c5059826d8d9020e845f60f075530728"
jp_sha512 = "07d069b4cc9f20b385cd4500d956c8b8fdeb62d4c4668fc5a302446e718d2338308913e360d887fa25e4766dcd4304025f73360d0e49126f71a0fe865cd3e293"
with open('RXC1.exe', "rb") as file_to_check:
    data = file_to_check.read()
    sha512sum = hashlib.sha512(data).hexdigest()
if int_sha512 == sha512sum:
    print("Checksum matches latest known international release, using those offsets for extraction...")
    with open("RXC1.exe", "rb") as exe:
        exe.seek(0xB8C4E0,0)
        rx1 = exe.read(0x180000)
        exe.seek(0xD8C4E0,0)
        mx1 = exe.read(0x180000)
        exe.seek(0xF8C4E0,0)
        rx2 = exe.read(0x180000)
        exe.seek(0x110C4E0,0)
        mx2 = exe.read(0x180000)
        exe.seek(0x128C4E0,0)
        rx3 = exe.read(0x200000)
        exe.seek(0x148C4E0,0)
        mx3 = exe.read(0x200000)
elif jp_sha512 == sha512sum:
    print("Checksum matches latest known Japanese release, using those offsets for extraction...")
    with open("RXC1.exe", "rb") as exe:
        exe.seek(0xB8C750,0)
        rx1 = exe.read(0x180000)
        exe.seek(0xD8C750,0)
        mx1 = exe.read(0x180000)
        exe.seek(0xF8C750,0)
        rx2 = exe.read(0x180000)
        exe.seek(0x110C750,0)
        mx2 = exe.read(0x180000)
        exe.seek(0x128C750,0)
        rx3 = exe.read(0x200000)
        exe.seek(0x148C750,0)
        mx3 = exe.read(0x200000)
else:
    print("Checksum doesn't match any known values, exiting.")
    exit()
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
