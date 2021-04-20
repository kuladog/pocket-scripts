#!/usr/bin/env python

import random

# generates a valid unicast UAA hardware address
def random_mac():
    return "%02x:%02x:%02x:%02x:%02x:%02x" % (
        (random.randint(0, 255) & 0xfc & ~2),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255))

print(random_mac())
