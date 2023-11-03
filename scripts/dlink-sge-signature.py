#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
#
# Copyright (C) 2021 Sebastian Schaper <openwrt@sebastianschaper.net>
# Copyright (C) 2023 Daniel Linjama <daniel@dev.linjama.com>
#
# append model string and checksums used by
# certain D-Link devices manufactured by SGE / T&W.
#
# e.g. COVR-P2500 requires this to be appended to the
# encrypted factory image, while for COVR-C1200 the
# signature needs to be appended to the unencrypted payload
#

import binascii, hashlib, sys

if len(sys.argv) != 3:
    exit(f"usage: {sys.argv[0]} input.bin model_name")

input_file = sys.argv[1]
model_name = sys.argv[2]

with open(input_file, "rb+") as fd:
    input_bytes = fd.read()

    crc32 = binascii.crc32(input_bytes)
    m = hashlib.md5(input_bytes)

    fd.write(m.hexdigest().encode())
    fd.write(f"\n{model_name}\n".encode())
    fd.write("{:08x}".format(crc32).encode())

    exit()

exit(1)
