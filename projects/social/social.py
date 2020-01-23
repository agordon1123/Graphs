
from util import Queue

from itertools import permutations
import random


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        temp = []
        # add users to graph with name as int
        for i in range(num_users):
            self.add_user(i)
            temp.append(i+1)
        
        # generate all possible permutations
        perm = permutations(temp, 2)

        # add to list 
        possibilities = []
        for i in list(perm):
            possibilities.append(i)
        
        random.shuffle(possibilities)

        # grab n tuples
        # possibilities = possibilities[:avg_friendships * len(self.users)]

        # different method to generate
        for user_id in self.users:
            iterable = avg_friendships
            while iterable > 0:
                self.add_friendship(user_id, random.randint(user_id, len(self.users)))
                iterable -= 1


        # create friendships
        # TODO: not optimal -> 10 receives none and the rest rest receive double
        #         if possibilities[target][0] == i+1:

        #             # target user has friends
        #             if self.friendships.get(target):
        #                 # friendship does not already exist
        #                 if i+1 not in self.friendships.get(target):                            
        #                     # add as friend with whichever num bigger
        #                     if possibilities[target][0] > possibilities[target][1]:
        #                         self.add_friendship(possibilities[target][0], possibilities[target][1])
        #                         amount -= 1
        #                     else: 
        #                         self.add_friendship(possibilities[target][1], possibilities[target][0])
        #                         amount -= 1
        #                 else:
        #                     # iterate
        #                     target += 1
                    
        #             else:
        #                 # add as friend with whichever num bigger
        #                 if possibilities[target][0] > possibilities[target][1]:
        #                     self.add_friendship(possibilities[target][0], possibilities[target][1])
        #                     amount -= 1
        #                 else: 
        #                     self.add_friendship(possibilities[target][1], possibilities[target][0])
        #                     amount -= 1
                    
        #         else:
        #             # iterate
        #             target += 1


            



            # if self.friendships.get(i[0]):
            #     # friendship does not already exist
            #     if i[1] not in self.friendships.get(i[0]):
            #         if i[0] > i[1]:
            #             self.add_friendship(i[0], i[1])
            #         else: 
            #             self.add_friendship(i[1], i[0])
            # else:
            #     if i[0] > i[1]:
            #         self.add_friendship(i[0], i[1])
            #     else: 
            #         self.add_friendship(i[1], i[0])

        # -------------

        # # create friendships
        # for i in range(len(temp)):
        #     print(i)
        #     # randomly choose n amount of friendships
        #     mid = avg_friendships // 2
        #     # calculate num of friendships around average given
        #     amount = random.randint(avg_friendships - mid, avg_friendships + mid)
        #     target = int(i)
        #     print(amount)
        #     while amount > 0:
        #         if possibilities[target][0] == i+1:

        #             # target user has friends
        #             if self.friendships.get(target):
        #                 # friendship does not already exist
        #                 if i+1 not in self.friendships.get(target):                            
        #                     # add as friend with whichever num bigger
        #                     if possibilities[target][0] > possibilities[target][1]:
        #                         self.add_friendship(possibilities[target][0], possibilities[target][1])
        #                         amount -= 1
        #                     else: 
        #                         self.add_friendship(possibilities[target][1], possibilities[target][0])
        #                         amount -= 1
        #                 else:
        #                     # iterate
        #                     target += 1
                    
        #             else:
        #                 # add as friend with whichever num bigger
        #                 if possibilities[target][0] > possibilities[target][1]:
        #                     self.add_friendship(possibilities[target][0], possibilities[target][1])
        #                     amount -= 1
        #                 else: 
        #                     self.add_friendship(possibilities[target][1], possibilities[target][0])
        #                     amount -= 1
                    
        #         else:
        #             # iterate
        #             target += 1
        
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        q = Queue()
        path = []
        # initialize path with starting node
        q.enqueue([user_id])

        # perform bfs on each conected node
        while q.size() > 0:
            path = q.dequeue()
            last = path[-1]
            if last not in visited:
                visited[last] = path
                # perform bfs on all connected nodes
                for v in self.friendships[last]:
                    if v not in visited:
                        new_path = list(path)
                        new_path.append(v)
                        q.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
