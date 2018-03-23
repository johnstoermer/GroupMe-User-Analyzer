from groupy.session import Session
from groupy.api.messages import Likes
from groupy.client import Client
client = Client.from_token('57c859b00d2c01366e14698edaba82b3')
group = client.groups.get('24252629')
dudes = {}
tier_list = []
message_count = 0
for member in group.members:
    dudes[member.user_id] = {}
    tier_list.append(member.user_id)
for dude in dudes:
    for member in group.members:
        dudes[dude][member.user_id] = 0
    dudes[dude]['totallikes'] = 0
    dudes[dude]['totalmessages'] = 1
for message in group.messages.list_all():
    if message.user_id in dudes:
        for favorite in message.favorited_by:
            if favorite in dudes[message.user_id]:
                dudes[message.user_id][favorite] += 1
                dudes[message.user_id]['totallikes'] += 1
        dudes[message.user_id]['totalmessages'] += 1
    message_count += 1
    print('Message Count: ' + str(message_count))
    if message_count == 1000000:
        break
with open('groupmedata.dat', 'w') as file:
    highest_messages = 1
    for dude in dudes:
        for member in group.members:
            if member.user_id == dude:
                file.write(member.nickname + '\n')
        if  dudes[dude]['totalmessages'] > highest_messages:
            highest_messages = dudes[dude]['totalmessages']
        highest_id = dude
        for liker in dudes[dude]:
            if liker != 'totallikes' and liker != 'totalmessages' and dudes[dude][liker] > dudes[dude][highest_id]:
                highest_id = liker
            for member in group.members:
                if member.user_id == liker:
                    file.write('\tLikes from ' + member.nickname + ': ' + str(dudes[dude][liker]) + '\n')
        for member in group.members:
            if member.user_id == highest_id:
                file.write('\tBest Friend: ' + member.nickname + ' with ' + str(dudes[dude][highest_id]) + ' likes\n')
        file.write('\tTotal Likes Acquired: ' + str(dudes[dude]['totallikes']) + '\n')
        file.write('\tTotal Messages: ' + str(dudes[dude]['totalmessages']) + '\n')
        file.write('\tAverage Likes per Message: ' + str(dudes[dude]['totallikes'] / dudes[dude]['totalmessages']) + '\n')
        file.write('\n')
    changed = True
    while changed:
        changed = False
        for i in range(len(tier_list) - 1):
            if dudes[tier_list[i]]['totallikes'] / dudes[tier_list[i]]['totalmessages'] < dudes[tier_list[i + 1]]['totallikes'] / dudes[tier_list[i + 1]]['totalmessages']:
                tier_list[i], tier_list[i + 1] = tier_list[i + 1], tier_list[i]
                changed = True
    file.write('\n')
    file.write('Tier List (Average Likes per Message):\n')
    file.write('\tS:\n')
    for member in group.members:
        if member.user_id == tier_list[0]:
            file.write('\t\t' + member.nickname + ' ALPM: ' + str(dudes[tier_list[0]]['totallikes'] / dudes[tier_list[0]]['totalmessages']) + '\n')
    file.write('\tA:\n')
    for member in group.members:
        if member.user_id == tier_list[1]:
            file.write('\t\t' + member.nickname + ' ALPM: ' + str(dudes[tier_list[1]]['totallikes'] / dudes[tier_list[1]]['totalmessages']) + '\n')
    for member in group.members:
        if member.user_id == tier_list[2]:
            file.write('\t\t' + member.nickname + ' ALPM: ' + str(dudes[tier_list[2]]['totallikes'] / dudes[tier_list[2]]['totalmessages']) + '\n')
    file.write('\tB:\n')
    for member in group.members:
        if member.user_id == tier_list[3]:
            file.write('\t\t' + member.nickname + ' ALPM: ' + str(dudes[tier_list[3]]['totallikes'] / dudes[tier_list[3]]['totalmessages']) + '\n')
    for member in group.members:
        if member.user_id == tier_list[4]:
            file.write('\t\t' + member.nickname + ' ALPM: ' + str(dudes[tier_list[4]]['totallikes'] / dudes[tier_list[4]]['totalmessages']) + '\n')
    for member in group.members:
        if member.user_id == tier_list[5]:
            file.write('\t\t' + member.nickname + ' ALPM: ' + str(dudes[tier_list[5]]['totallikes'] / dudes[tier_list[5]]['totalmessages']) + '\n')
    file.write('\tC:\n')
    for member in group.members:
        if member.user_id == tier_list[6]:
            file.write('\t\t' + member.nickname + ' ALPM: ' + str(dudes[tier_list[6]]['totallikes'] / dudes[tier_list[6]]['totalmessages']) + '\n')
    for member in group.members:
        if member.user_id == tier_list[7]:
            file.write('\t\t' + member.nickname + ' ALPM: ' + str(dudes[tier_list[7]]['totallikes'] / dudes[tier_list[7]]['totalmessages']) + '\n')
    for member in group.members:
        if member.user_id == tier_list[8]:
            file.write('\t\t' + member.nickname + ' ALPM: ' + str(dudes[tier_list[8]]['totallikes'] / dudes[tier_list[8]]['totalmessages']) + '\n')
    file.write('\tD:\n')
    for member in group.members:
        if member.user_id == tier_list[9]:
            file.write('\t\t' + member.nickname + ' ALPM: ' + str(dudes[tier_list[9]]['totallikes'] / dudes[tier_list[9]]['totalmessages']) + '\n')
    for member in group.members:
        if member.user_id == tier_list[10]:
            file.write('\t\t' + member.nickname + ' ALPM: ' + str(dudes[tier_list[10]]['totallikes'] / dudes[tier_list[10]]['totalmessages']) + '\n')
    for member in group.members:
        if member.user_id == tier_list[11]:
            file.write('\t\t' + member.nickname + ' ALPM: ' + str(dudes[tier_list[11]]['totallikes'] / dudes[tier_list[11]]['totalmessages']) + '\n')
    for member in group.members:
        if member.user_id == tier_list[12]:
            file.write('\t\t' + member.nickname + ' ALPM: ' + str(dudes[tier_list[12]]['totallikes'] / dudes[tier_list[12]]['totalmessages']) + '\n')
    file.write('\tF:\n')
    if len(tier_list) - 13 > 0:
        for i in range(len(tier_list) - 13):
            for member in group.members:
                if member.user_id == tier_list[13 + i]:
                    file.write('\t\t' + member.nickname + ' ALPM: ' + str(dudes[tier_list[13 + i]]['totallikes'] / dudes[tier_list[13 + i]]['totalmessages']) + '\n')
