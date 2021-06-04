# MMXLC1-Rom-Extractor
Python based ROM extractor for Mega Man X Legacy Collection. Extracts Rockman X-X3 and Mega Man X-X3.

Place RXC1.exe from game files in the same folder and run.

This was tested against 2 versions of RXC1.exe. The international version with a hash of: 905e1d515a77193a23a79d6d92b7e414dca04bb629adc43ca02138a5e26c780baec79b82ec111bb61db4b6f8a07be522ecb90592e864568455c4d12f8cbbfbae

...and the Japanese version with a hash of:
07d069b4cc9f20b385cd4500d956c8b8fdeb62d4c4668fc5a302446e718d2338308913e360d887fa25e4766dcd4304025f73360d0e49126f71a0fe865cd3e293

This now also has sanity checking in the form of SHA512 checksums. If a known checksum is found, the files are extracted, otherwise it bails out.

Thanks to avaiski on GitHub for updating the offsets for the latest international release executable.

Thanks to Random_Rhinoceros on Reddit for letting me know about the Japanese release and helping me test the script against it.
