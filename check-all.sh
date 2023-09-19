#!/usr/bin/bash
find keys -type f |xargs -L1 ./check-gpg-key.py 2>&1|grep 'expired at'
