def custom_middleware(get_response):
	# One time configuration
	
	def middleware(request):
		
		response = get_response(request)
		
		response["Access-Control-Allow-Origin"] = "*"
		response["Access-Control-Allow-Headers"] = "*"
		response["Access-Control-Allow-Methods"] = "*"
		   
		return response
		
	return middleware