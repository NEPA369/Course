# 3. Show the basic implementation of Hashing

def hash(data):
    counter = 1
    sum = 0
    for d in data:
        sum += counter * ord(d)
    return sum % 256

if __name__ == "__main__":
    items = ['tool', 'is', 'a', 'progressive', 'rock', 'band', 'formed']
    for item in items:
        print("{}: {}".format(item, hash(item)))
