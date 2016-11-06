from __future__ import print_function
import infermedica_api 

infermedica_api.configure(app_id='eb4835a9', app_key='679dd699e25f6bee7fe14cc3dc4d2b99')

api = infermedica_api.get_api()

print('Welcome to the interactive nurse!')
age = raw_input('What is your age?\n')
sex = raw_input('What is your sex?\n')
request = infermedica_api.Diagnosis(sex=sex, age=age)

#request.add_symptom('s_21', 'present')
#request.add_symptom('s_98', 'present'#request.add_symptom('s_107', 'absent')

#request.set_pursued_conditions(['c_33', 'c_49'])  # Optional

# call diagnosis
#request = api.diagnosis(request)
# Access question asked by API
#print(request.question)
#print(request.question.text)  # actual text of the question
#print(request.question.items)  # list of related evidences with possible answers
#print(request.question.items[0]['id'])
#print(request.question.items[0]['name'])
#print(request.question.items[0]['choices'])  # list of possible answers
#print(request.question.items[0]['choices'][0]['id'])  # answer id
#print(request.question.items[0]['choices'][0]['label'])  # answer label

# Access list of conditions with probabilities
#print(request.conditions)
#print(request.conditions[0]['id'])
#print(request.conditions[0]['name'])
#print(request.conditions[0]['probability'])

# Next update the request and get next question:
# Just example, the id and answer shall be taken from the real user answer
#request.add_symptom(request.question.items[0]['id'], request.question.items[0]['choices'][1]['id'])

# call diagnosis method again
#request = api.diagnosis(request)
symptom=raw_input('What kind of symptoms are you having?')
dic = api.search(symptom)
SID = dic[0]['id'] 
request.add_symptom(SID, 'present')
request = api.diagnosis(request)
#print(request)
print('There is a ' + str(request.conditions[0]['probability']*100) + '% ' +'chance that you have chance that you have ' + request.conditions[0]['name'] +'.\n')

#print(dic)
# ... and so on, until you decide to stop the diagnostic interview.
