import requests


url = 'http://localhost:9696/predict'

customer_id = 'xyz-123'

customer = {'age': 60,
            'cholesterol':208,
            'heart_rate':159,
            'exercise_hours_per_week':4.168189,
            'sedentary_hours_per_day':4.963459,
            'income':235282	,
             'bmi' : 31.251233,
             'triglycerides' : 235	,
             'physical_activity_days_per_week' : 1,
             'sleep_hours_per_day' :6,
            'blood_pressure' : 158/88,
            }


response = requests.post(url, json=customer).json()
print(response)

if response['heart_attack_risk'] == True:
    print('suggesting to go to clicinic to  %s' % customer_id)
else:
    print('not suggesting to go to clicinic to %s' % customer_id)
