from signupmanager.models import UserData
from .models import UserBrainMap

def getUserData(email_address):
    user_data = UserData.objects.filter(email_address = email_address)[0]
    return user_data.id, user_data.full_name

def getUserID(email_address):
    return UserData.objects.filter(email_address = email_address)[0].id

def getBrainInfo(userID):
    brainInfo = list()
    userBrainMap = UserBrainMap.objects.filter(userID = userID)
    for each in userBrainMap:
        brainInfo.append({"id": each.id, "name":each.taskName})
    return brainInfo

def createTask(userID, taskName, taskDescription):
    row = UserBrainMap(userID = userID, taskName = taskName, taskDescription = taskDescription)
    row.save()
    return row.id
