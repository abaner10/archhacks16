import requests
import json
def better_doctor(loc, user_loc, gen, ski, lmt):
	url = 'https://api.betterdoctor.com/2016-03-01/'
	function = 'doctors'
	params = dict (
    	location = '37.773,-122.413,100',
    	user_location = '37.773,-122.413',
    	gender = 'male',
    	skip = '0',
    	limit = '10',
    	user_key = 'd43951330ee8fdbf751b4abb864a9ed8'
	)

	url = url + function
#url = 'https://api.betterdoctor.com/2016-03-01/doctors?location=37.773%2C-122.413%2C100&user_location=37.773%2C-122.413&gender=male&skip=0&limit=10&user_key=d43951330ee8fdbf751b4abb864a9ed8'
#r = requests.get('https://api.betterdoctor.com/2016-03-01/doctors?first_name=hahahaha&limit=10&location=37.773%2C-122.413%2C100&gender=male&user_key=d43951330ee8fdbf751b4abb864a9ed8&user_location=37.773%2C-122.413&skip=0')
#r = requests.get('https://api.betterdoctor.com/2016-03-01/doctors?first_name=hahahaha&location=37.773%2C-122.413%2C100&user_location=37.773%2C-122.413&gender=male&skip=0&limit=10&user_key=d43951330ee8fdbf751b4abb864a9ed8')

#r = requests.get(url)
#print r.text
	data = json.loads(r.text)
#print data['meta']

#user_loc = input("Enter your location:")
	params['location'] = loc
	params['user_location'] = user_loc
	params['gender'] = gen
	params['skip'] = ski
	params['limit'] = lmt 

	r = requests.get(url=url, params=params)
#print(params['user_location'])

	return r
