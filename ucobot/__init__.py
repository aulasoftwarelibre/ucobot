# -*- coding: utf-8 -*-

import telebot
import yaml

def configure():
    # Read configuration
    file = open("config/parameters.yml", "r")
    config = yaml.load(file)
    file.close()
    return config

config=configure()
bot = telebot.TeleBot(config['telegram']['token'])

from ucobot import model
from ucobot import commands

def starts():
    bot.polling()