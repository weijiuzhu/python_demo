from app.UserEntity import UserEntity

if __name__ == '__main__':
    user = UserEntity("weidashi", 18)
    user.printUser()
    print(user.name)
    print(user._UserEntity__add)