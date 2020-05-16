hosts = ["Dolores", "Teddy", "Hector", "Maeve"]

def check_host_avail():
	for name in hosts:
		if name == "Dolores":
			print("Sorry, Dolores isn't working today!")
		
# pizza_toping = []

# if pizza_toping:
# 	for topping in pizza_toping:
# 		print("Adding " + topping)
# else: 
# 	print("You want a plain pizza?")				

request_for_hosts = ["Ford", "William", "Dolores", "Teddy"]

check_host_avail() #this says Dolores isn't available 
request_for_hosts.pop(2)

#also can do this if you don't know where Dolores is located: 
#request_for_hosts.remove("Dolores")
for request in request_for_hosts:
	if request in hosts:
		print("You can meet with: ", request)
	else:
		print("sorry,", request, " is not a host at the park!")
