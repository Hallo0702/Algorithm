import sys
input = sys.stdin.readline

N = int(input().rstrip())
users = []
for i in range(N):
    users.append(input().rstrip())


class Node(object):
    def __init__(self,key,data=None):
        self.key = key
        self.data = data
        self.count = 0
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def search_prefix(self,string):
        now = self.head
        result = ''
        for s in string:
            result += s
            if s in now.children:
                now = now.children[s]
            else:
                return result

        if now.data != None:
            result += str(now.count + 1)
        return result

    def insert_node(self,string):
        now = self.head
        for s in string:
            if s not in now.children:
                now.children[s] = Node(s)
            now = now.children[s]
        now.data = string
        now.count += 1


trie = Trie()
for user in users:
    print(trie.search_prefix(user))
    trie.insert_node(user)
