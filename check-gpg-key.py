#!/usr/bin/python3

from pysequoia import Cert

import datetime
import sys

if len(sys.argv) != 2:
    print("Usage: check-gpg-key.py filename")
    sys.exit(1)

filename = sys.argv[1]
today_date = datetime.date.today()
cert = Cert.from_file(filename)

try:
    if cert.expiration is None:
        # cert has no expiration
        sys.exit(0)

    if cert.expiration.date() < today_date:
        sys.stderr.write("Error: the key {} expired at {}\n".format(filename, cert.expiration))
        sys.exit(2)
except RuntimeError as e:
    sys.stderr.write("{} - {}\n".format(filename, e))
    sys.exit(3)
