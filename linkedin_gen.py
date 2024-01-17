import requests

api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
api_key = 'zZ708nt5Izy6RAUUlMgJuQ'
header_dic = {'Authorization':'Bearer' + api_key}
params = {
	'url': 'https://www.linkedin.com/in/eden-marco/',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

response.json()