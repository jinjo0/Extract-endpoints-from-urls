target = open("urls.txt","r")
urls = target.readlines()
result = open("endpoints.txt","w")


for url in urls:
	url = url.split("/")
	endpoints=""
	i=0
	endpoint=""
	for ep in url:
		i=i+1
		if (i>3):
			endpoint= endpoint+"/"+ep
	print(endpoint)
	result.write(endpoint)
print("\n\nDone Collected "+str(len(urls))+" endpoints")

