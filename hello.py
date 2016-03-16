def application(env, start_response):
	url = env['QUERY_STRING']
	url = url.replace("&","\n")
	start_response('200 OK', [('Content-Type', 'text/plain')])
	return url
