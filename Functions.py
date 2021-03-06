pendingMessagesMap = dict()
usersMap = dict()


def register_user(client_id, public_key):
    print("Registering user!")
    usersMap[client_id] = public_key


def get_public_key():
    print("fetch public key for user!")
    return


def pull_messages():
    print("pulling messages!")
    pass


def send_message(src_id, dst_id):
    print("sending message!")
    pass