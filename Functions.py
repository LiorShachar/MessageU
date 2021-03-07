pendingMessagesMap = dict()  # holds an array containing all pending messages by tuples: (client id source, msg)
usersMap = dict()   # holds users and their public keys


def register_user(client_id, public_key):
    print("Registering user!")
    usersMap[client_id] = public_key


def get_public_key(client_id):
    print("fetch public key for user!")
    if usersMap.get(client_id) is not None:
        return usersMap[client_id]


def pull_messages(client_id):
    print("pulling messages!")
    if pendingMessagesMap.get(client_id) is None:
        pendingMessagesMap[client_id] = []
    return pendingMessagesMap[client_id]


def send_message(src_id, dst_id, content):
    # fetch the pending messages array
    if pendingMessagesMap.get(src_id) is None:
        pendingMessagesMap[src_id] = []
    pendingMessagesMap.get(src_id).append((src_id, content))
    print(f"stored a msg from: {src_id} to {dst_id}")
