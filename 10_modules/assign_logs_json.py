#!/usr/bin/python
"""
Purpose: Logging in JSON format
pip install -U python-json-logger --user
"""
import json
import logging
from pythonjsonlogger import jsonlogger

# Step 1: Create handler
logHandler = logging.StreamHandler()


formatter = jsonlogger.JsonFormatter(
    fmt="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Step 3: Add formatting to handler
logHandler.setFormatter(formatter)

# Step 4: Create logger object
logger = logging.getLogger("myApp")

# Step 5: Add handler to the logger object
logger.addHandler(logHandler)
logger.setLevel(logging.DEBUG)

# Logging examples
logger.debug("This is a debug log") 
logger.info("This is an info log")
logger.warning("This is a warning log") 
logger.error("This is an error log")
logger.critical("This is a critical log")
