# MMXLC1-Rom-Extractor
Python based ROM extractor for Mega Man X Legacy Collection. Extracts Rockman X-X3 and Mega Man X-X3.

Place RXC1.exe from game files in the same folder and run.

This was tested against 2 versions of RXC1.exe. The international version with a hash of: 58101af83d473667537b9e27f2d5154831917ad63193644d4c6b6c69ac5341923801ac641ba023a7ecb4e7be026a7ea3c5059826d8d9020e845f60f075530728

...and the Japanese version with a hash of:
75785438024ca7bf4f819c7791060847dfc07ccb71ebb3d30661f985f67a829e915c735fbbf8da0d71fed8d0e46a90f68956b3de4797eabd142a88e81288dc81

This now also has sanity checking in the form of SHA512 checksums. If a known checksum is found, the files are extracted, otherwise it bails out.

Thanks to avaiski on GitHub for updating the offsets for the latest international release executable.

Thanks to Random_Rhinoceros on Reddit for letting me know about the Japanese release and helping me test the script against it.

Thanks to Leatherhide and RealRelativeEase for notifying me of new updates to the executables and providing updated hashes.
