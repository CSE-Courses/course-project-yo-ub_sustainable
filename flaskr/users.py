Users = {
    'friends': [],
    'notFriends': 
    [
        {
            'username': 'jjohnson',
            'name': 'John Johnson',
            'profilePic': "https://via.placeholder.com/50"
        }, 
        {
            'username': 'bjackson',
            'name': 'Blake Jackson',
            'profilePic': "https://via.placeholder.com/50"
        }, 
        {
            'username': 'jkeller',
            'name': 'Jack Keller',
            'profilePic': "https://via.placeholder.com/50"
        },
        {
            'username': 'dcarlson',
            'name': 'Dave Carlson',
            'profilePic': "https://via.placeholder.com/50"
        }, 
        {
            'username': 'jdanz',
            'name': 'Jason Danz',
            'profilePic': "https://via.placeholder.com/50"
        }, 
        {
            'username': 'bpacuk',
            'name':'Ben Pacuk',
            'profilePic': "https://via.placeholder.com/50"
        }, 
        {
            'username': 'jdorr',
            'name': 'Julia Dorr',
            'profilePic': "https://via.placeholder.com/50"
        }, 
        {
            'username': 'jmogul',
            'name': 'Jordan Mogul',
            'profilePic': "https://via.placeholder.com/50"
        }
    ]
}

def getUserName(name):
    for uType in Users:
        for user in Users[uType]:
            if user['name'] == name:
                return user['username']
    return None

def getProfilePic(name):
    for uType in Users:
        for user in Users[uType]:
            if user['name'] == name:
                return user['profilePic']
    return None

def addFriend(name):
    newFriend = {'username': getUserName(name), 'name': name, 'profilePic': getProfilePic(name)}
    Users['friends'].append(newFriend)
    Users['notFriends'].remove(newFriend)

def remFriend(name):
    unFriend = {'username': getUserName(name), 'name': name, 'profilePic': getProfilePic(name)}
    Users['notFriends'].append(unFriend)
    Users['friends'].remove(unFriend)

#Sprint 4
#def searchUsers():
