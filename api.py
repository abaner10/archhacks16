from __future__ import print_function
import infermedica_api 

infermedica_api.configure(app_id='eb4835a9', app_key='679dd699e25f6bee7fe14cc3dc4d2b99')

api = infermedica_api.get_api()

print('Welcome to the interactive nurse!')
age = raw_input('What is your age?\n')
sex = raw_input('What is your sex?\n')
request = infermedica_api.Diagnosis(sex=sex, age=age)
symptom='A'
while(symptom!=""):
	symptom=raw_input('What kind of symptoms are you having?\n')
	#print (symptom)
	if(symptom==""):
		#print ('lol'+symptom)
		break
	#print (symptom)
	dic = api.search(symptom)
	SID = dic[0]['id'] 
	request.add_symptom(SID, 'present')
request = api.diagnosis(request)
#print(request)
print('There is a ' + str(request.conditions[0]['probability']*100) + '% ' +'chance that you have chance that you have ' + request.conditions[0]['name'] +'.\n')
