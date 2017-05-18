import urllib
import json

url = "http://sandbox.api.simsimi.com/request.p"
key = "b18190b0-ba16-4ef1-ab52-3d08eff07395"
lc = "id"
ft = "1.0"

def simi(text):
	param = {
			'key':key,
			'lc':lc,
			'ft':ft,
			'text':text
			}
	query = urllib.parse.urlencode(param)
	resp = urllib.request.urlopen("%s?%s" % (url, query)).read().decode()
	try:
		response = json.loads(resp)
		if response["msg"].strip().lower() == "ok.":
			return response["response"].strip()
		else:
			return response["msg"].strip()
	except Exception as e:
		return str(e)
