import vk
import time

userId = input()
access_token = input()
session = vk.Session(access_token = access_token)
vk_api = vk.API(session)
version = '5.00'


def friends():
    friends = vk_api.friends.get(user_id = userId, v = version)
    return friends

def groups():
    groups = vk_api.groups.get(user_id=id, v=version)
    time.sleep(1.0)
    return groups


def theme(pageid):
    themeOfGroup = vk_api.groups.getById(group_id=pageid, v=version, fields='activity')
    time.sleep(1.0)
    return themeOfGroup
