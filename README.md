# MMXLC1-Rom-Extractor
Python based ROM extractor for Mega Man X Legacy Collection. Extracts Rockman X-X3 and Mega Man X-X3.

Place RXC1.exe from game files in the same folder and run.

This was tested against 2 versions of RXC1.exe. The international version with a hash of: `7b9463e05e55a4967a7e0d53188359b9d254e49e3bd4f180b4166d6c065387e85106ca1e9ffa16182b58d3c9151e36eee3675111957082776cd4cf22f641ca8f`

...and the Japanese version with a hash of:
`75785438024ca7bf4f819c7791060847dfc07ccb71ebb3d30661f985f67a829e915c735fbbf8da0d71fed8d0e46a90f68956b3de4797eabd142a88e81288dc81`

Unfortunately the Japanese hash is out of date. If anyone has access to that and can contribute the hash and/or offsets, that'd be greatly appreciated!

This now also has sanity checking in the form of SHA512 checksums. If a known checksum is found, the files are extracted, otherwise it bails out.

Thanks to avaiski on GitHub for updating the offsets for the latest international release executable.

Thanks to Random_Rhinoceros on Reddit for letting me know about the Japanese release and helping me test the script against it.

Thanks to Leatherhide, RealRelativeEase and IcyWind14 for notifying me of new updates to the executables and providing updated hashes.
