# Python DogeApi

A simple python module for dogeapi.com service.

See the documentation here: https://dogeapi.com/api_documentation

## Installation

    pip install py-dogeapi

## Settings

Create api.yaml file if it doesn't exists.

    api_url: https://www.dogeapi.com/wow/
    api_key: your_api_key_here

## Usage

Before you start, you must set the api key in api.yaml file.

    from py-dogeapi import *
    
    stream = open("api.yaml", "r")
    config = yaml.load(stream)
    doge = DogeApi(config["api_url"], config["api_key"])
    print doge.get_balance()
