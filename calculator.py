import datetime
import math

from utils import secondsBetween


def percentage_time_response_by_user(collection, contact1,contact2):
    ptr_1 = 0
    total_seconds_contact1 = 0
    quantity_msg_contact1 = 0
    ptr_2 = 0
    quantity_msg_contact2 = 0
    total_seconds_contact2 = 0

    for (i, item) in enumerate(collection):
        if i != (len(collection) - 1):
                user = str(item['user']).strip()

                ''' DATOS DE USUARIO ACTUAL'''
                formatedDate = str(item['date']).replace('/', '-').split('-')
                frmt = "20{}-{}-{}"
                userDate = ''

                if len(formatedDate[0]) == 1:
                    formatedDate[0] = '0' + formatedDate[0]
                if len(formatedDate[1]) == 1:
                    formatedDate[1] = '0'+ formatedDate[1]
                if len(formatedDate[2]) == 1:
                    formatedDate[2] = '0'+ formatedDate[2]
                else:
                    userDate = datetime.datetime.fromisoformat(frmt.format(formatedDate[2], formatedDate[1], formatedDate[0]))

                hours = int(str(item['hour']).split(':')[0])
                minutes = int(str(item['hour']).split(':')[1])
                seconds = int(str(item['hour']).split(':')[2])
                d1 = datetime.datetime(year=int(userDate.year), month=int(userDate.month), day=int(userDate.day),
                                       hour=hours, minute=minutes, second=seconds)

                msgUser = {'time': d1, 'user': str(user).strip()}
                userTime = {"year": d1.year, "month": d1.month, "day": d1.day, "hours": d1.hour, "minutes": d1.minute,
                           "seconds": d1.second, 'user': user}
                ''' -----------------------------------------------------'''
                print('Historial', item)
                ''' DATOS DE USUARIO SIGUIENTE'''

                nextUser = str(collection[i + 1]['user']).strip()

                if(user != nextUser):
                    f_d = str(collection[i]['date']).replace('/', '-').split('-')
                    frmt_2 = "20{}-{}-{}"

                    if len(f_d[0]) == 1:
                        f_d[0] = '0' + f_d[0]
                    if len(f_d[1]) == 1:
                        f_d[1] = '0' + f_d[1]
                    if len(f_d[2]) == 1:
                        f_d[2] = '0' + f_d[2]
                    else:
                        user_next_date = datetime.datetime.fromisoformat(
                            frmt_2.format(f_d[2], f_d[1], f_d[0]))

                    hoursN = int(str(collection[i + 1]['hour']).split(':')[0])
                    minutesN = int(str(collection[i + 1]['hour']).split(':')[1])
                    secondsN = int(str(collection[i + 1]['hour']).split(':')[2])

                    d2 = datetime.datetime(year=int(user_next_date.year), month=int(user_next_date.month),
                                           day=int(user_next_date.day),
                                           hour=hoursN, minute=minutesN, second=secondsN)
                    msgNextUser = {'time': d2, 'NextUser': str(nextUser).strip()}

                    nextUserTime = {"year": d2.year, "month": d2.month, "day": d2.day, "hours": d2.hour, "minutes": d2.minute,
                           "seconds": d2.second, 'user': nextUser}

                    diference = secondsBetween(userTime, nextUserTime)

                    if diference != -1:
                        if nextUser == contact1:
                            total_seconds_contact1 = total_seconds_contact1 + diference
                            quantity_msg_contact1 = quantity_msg_contact1 + 1

                        if nextUser == contact2:
                            total_seconds_contact2 = total_seconds_contact2 + diference
                            quantity_msg_contact2 = quantity_msg_contact2 + 1


    ptr_1 = float(( total_seconds_contact1 / quantity_msg_contact1) / 60)
    ptr_2 = float(( total_seconds_contact2 / quantity_msg_contact2) / 60)

    return [{"contact": contact1, "ptr_in_minutes": '{0:.2f}'.format(ptr_1)}, {"contact": contact2, "ptr_in_minutes": '{0:.2f}'.format(ptr_2)}, {"quantity_messages": len(collection)}]
