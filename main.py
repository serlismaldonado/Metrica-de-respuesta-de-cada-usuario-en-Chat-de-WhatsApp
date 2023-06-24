import datetime
from utils import secondsBetween
from calculator import percentage_time_response_by_user

chat = open('chat.txt')
content = chat.read()
distanceList = []
chatList = content.split('\n')
contact1 = "Serlis Maldonado"
contact2 = "Mi Soly🎶"

for msg in chatList:
    arr = msg.rsplit(':', 1)
    if((arr[0].startswith('0')
        or arr[0].startswith('1')
        or arr[0].startswith('2')
        or arr[0].startswith('3')
        or arr[0].startswith('3')
        or arr[0].startswith('4')
        or arr[0].startswith('5')
        or arr[0].startswith('6')
        or arr[0].startswith('7')
        or arr[0].startswith('8')
        or arr[0].startswith('9')) is True and arr[0].find("/", 1, 8) != -1):
            dates = arr[0].rsplit(':', 1)
            users = arr[0].rsplit(':', 1)

            if users[0].count(':', 1, 18) > 2:
             day = users[0].split(' ')[0]
             hour = users[0].split(' ')[1].removesuffix(':')
             user = users[0].split(':')[3]
            else:
                if str(users[1]).lstrip() == contact1 or str(users[1]).lstrip() == contact2:
                    day = users[0].split(' ')[0]
                    user = users[1]
                    hour = users[0].split(' ')[1].removesuffix(':')

            distanceList.append({"date": day, "hour": hour, "user": user})


evaluate = percentage_time_response_by_user(distanceList, contact1, contact2)
print(evaluate)

