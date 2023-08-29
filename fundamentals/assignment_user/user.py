class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(
            "user info:\n",
            "first name:", self.first_name,'\n',
            "last name:", self.last_name,'\n',
            "email:", self.email,'\n',
            "age:", str(self.age),'\n',
            "rewards member:", self.is_rewards_member,'\n',
            "gold card points:", self.gold_card_points)
    def enroll(self):
        if not (self.is_rewards_member == True):
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print("user is already a member")
            pass
    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            self.gold_card_points = self.gold_card_points - amount
        else:
            print("error: spend amount exceeds user's current points. try again.")


user_benji = User('benji', 'hix', 'benji.hix@outlook.com', 26)
user_liz = User('liz', 'hix', 'liz.hix@outlook.com', 29)
user_jd = User('jd', 'hix', 'jd.hix@outlook.com', 20)

user_benji.enroll()
user_benji.spend_points(50)
user_liz.enroll()
user_liz.spend_points(80)

user_benji.display_info()
user_liz.display_info()
user_jd.display_info()

user_jd.spend_points(40)