import urllib2
import json
import yaml

class DogeApi(object):

	api_url = None

	api_key = None

	def __init__(self, api_url, api_key):
		self.api_url = api_url
		self.api_key = api_key

	def request(self, action_url, api_key = True):
		url = self.api_url + "?"

		if api_key == True:
			url += "api_key=" + self.api_key + "&"

		url += "a=" + action_url
		response = urllib2.urlopen(url)
		return json.load(response)

	def get_balance(self):
		return self.request("get_balance")

	def withdraw(self, amount, address):
		return self.request("withdraw&amount=" + amount + "&payment_address=" + address)

	def get_new_address(self, label):
		return self.request("get_new_address&address_label=" + label)

	def get_my_addresses(self):
		return self.request("get_my_addresses")

	def get_address_received(self, address):
		return self.request("get_address_received&payment_address=" + address)

	def get_address_by_label(self, label):
		return self.request("get_address_by_label&address_label=" + label)

	def get_difficulty(self):
		return self.request("get_difficulty", False)
			
	def get_current_block(self):
		return self.request("get_current_block", False)

	def get_current_price(self):
		return self.request("get_current_price", False)
		
def main():
	stream = open("api.yaml", "r")
	config = yaml.load(stream)
	doge = DogeApi(config["api_url"], config["api_key"])
	print doge.get_balance()
	#print doge.get_difficulty()
	
if __name__ == "__main__":
	main()
