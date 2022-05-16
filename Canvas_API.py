import requests
import json
# Import the Canvas class
# from canvasapi import Canvas

# # Canvas API URL
# API_URL = "https://canvas.instructure.com"
# # Canvas API key
# USER_ACCESS_TOKEN = "1109~sACxtaoR8tnrE9k65gDOY2VECnFa66UdQdzW1S70QsBqdOisJKyNRDMor4JvJnPB"

# account_id = 1476326
# url = 'https://uc.instructure.com/api/v1/users/self/todo'
test_url = 'https://canvas.instructure.com/api/v1/courses'
headers = {'Authorization' : 'Bearer 1109~sACxtaoR8tnrE9k65gDOY2VECnFa66UdQdzW1S70QsBqdOisJKyNRDMor4JvJnPB'}

r = requests.get(test_url, headers = headers)
outputtxt = json.loads(str(r.text))
# print(outputtxt)

for i in range(len(outputtxt)):
    # Get courses from current semester (WIP not sure if there's a way to make this dynamic)
    if outputtxt[i]['enrollment_term_id'] == 11090000000004589:
        assignment_name = outputtxt[i]['id']
        print(outputtxt[i]['name'])
        test_url = f'https://canvas.instructure.com/api/v1/courses/{assignment_name}/assignments'
        r = requests.get(test_url, headers = headers)
        outputtxt = json.loads(str(r.text))
        # print(outputtxt)
        # Get all assignments that haven't been turned in yet
        for i in range(len(outputtxt)):
            if outputtxt[i]['has_submitted_submissions'] == False:
                print(outputtxt[i]['name'])
    test_url = 'https://canvas.instructure.com/api/v1/courses'
    r = requests.get(test_url, headers = headers)
    outputtxt = json.loads(str(r.text))
