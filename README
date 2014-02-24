# Python DogeApi

A simple python module for dogeapi.com service.

See the documentation here: https://dogeapi.com/api_documentation

## Installation

Use the command below to install the py-dogeapi module.

    pip install py-dogeapi

Create config.yaml file if it doesn't exists.

config.yaml

    api_url: https://www.dogeapi.com/wow/
    api_key: your_api_key_here

## Usage

Before you start, you must set the api key in config.yaml file or if you don't want to use an additional file you can set api url/key directly in your main file.

example.py

    from py-dogeapi import *
    
    stream = open("config.yaml", "r")
    config = yaml.load(stream)
    doge = DogeApi(config["api_url"], config["api_key"])
    
    # get all addresses
    addresses = doge.get_my_adresses()

    for address in addresses:
    	print address
