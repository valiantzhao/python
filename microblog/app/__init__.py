from flask import Flask
from config import Config
from views import app
from config1 import Config1

Config.from_object(Config1)
