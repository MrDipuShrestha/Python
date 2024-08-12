
class User:
    # creating a constructor
    def __init__(self, user_id, username): # constructor initilize the attributes
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    #creating method
    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User(1, "Dipesh")
user_2 = User(2,"Sayara")

user_1.follow(user_2)

print(user_1.following)
print(user_1.follower)
print(user_2.following)
print(user_2.follower)