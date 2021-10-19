#!/usr/bin/env python3

import re

str = 'a' + 'b' * 100

re.match("a(bb|b.)*a", str)
