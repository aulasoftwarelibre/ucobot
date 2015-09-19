#!/usr/bin/env python3
import os
import sys

if sys.version_info.major < 3:
    raise Exception("Must be using Python 3")

# Add vendor directory to module search path
parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, 'dist')

sys.path.append(vendor_dir)

from ucobot import bot
bot.polling()
