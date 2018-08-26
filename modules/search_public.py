


from pgoogle import GoogleSearch
def searchPublicly(domain):
	ext = ('docs','odf','pdf','rtf','sxw','psw','ppt','pptx','pps','csv')
	print("start searching for Publicly exposed documents\n")
	for getAll in range(len(ext)):
		GoogleSearch(domain,'ext:'+ext[getAll])

