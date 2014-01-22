# Python DogeApi

A simple python module for dogeapi.com service.

See the documentation here: https://dogeapi.com/api_documentation

## Installation

    pip install py-dogeapi

## Settings

Create config.yaml file if it doesn't exists.

config.yaml
    api_url: https://www.dogeapi.com/wow/
    api_key: your_api_key_here

## Usage

Before you start, you must set the api key in config.yaml file.

example.py
    from py-dogeapi import *
    
    stream = open("api.yaml", "r")
    config = yaml.load(stream)
    doge = DogeApi(config["api_url"], config["api_key"])
    addresses = doge.get_my_adresses()

    for address in addresses:
	print address
