
def online_count(statuses):
    return len([i for i in statuses.values() if i == 'online'])


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

print(online_count(statuses), online_count(statuses) == 2)
