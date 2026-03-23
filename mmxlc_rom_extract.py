#!/usr/bin/env python
import hashlib
int_sha512 = "7b9463e05e55a4967a7e0d53188359b9d254e49e3bd4f180b4166d6c065387e85106ca1e9ffa16182b58d3c9151e36eee3675111957082776cd4cf22f641ca8f"
jp_sha512 = "75785438024ca7bf4f819c7791060847dfc07ccb71ebb3d30661f985f67a829e915c735fbbf8da0d71fed8d0e46a90f68956b3de4797eabd142a88e81288dc81"
with open('RXC1.exe', "rb") as file_to_check:
    data = file_to_check.read()
    sha512sum = hashlib.sha512(data).hexdigest()
if int_sha512 == sha512sum:
    print("Checksum matches latest known international release, using those offsets for extraction...")
    with open("RXC1.exe", "rb") as exe:
        exe.seek(0xB8DF20,0)
        rx1 = exe.read(0x180000)
        exe.seek(0xD8DF20,0)
        mx1 = exe.read(0x180000)
        exe.seek(0xF8DF20,0)
        rx2 = exe.read(0x180000)
        exe.seek(0x110DF20,0)
        mx2 = exe.read(0x180000)
        exe.seek(0x128DF20,0)
        rx3 = exe.read(0x200000)
        exe.seek(0x148DF20,0)
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
