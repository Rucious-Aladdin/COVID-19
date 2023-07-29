import time
from stem import Signal
from stem.control import Controller
from selenium import webdriver

with Controller.from_port(port=9051) as controller:
      print("a")
controller.close()