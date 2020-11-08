Users = {
    'friends': [],
    'notFriends': ['John Johnson','Blake Jackson','Jack Keller','Dave Carlson','Jason Danz','Ben Pacuk','Julia Dorr','Jordan Mogul']
}

def addFriend(name):
    Users['friends'].append(name)
    if name in Users['notFriends']:
        Users['notFriends'].remove(name)

def remFriend(name):
    Users['notFriends'].append(name)
    if name in Users['friends']:
        Users['friends'].remove(name)

#Sprint 4
#def searchUsers():

addFriend("John Johnson")
print(Users['friends'])
print(Users['notFriends'])
