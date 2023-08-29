class Player:
    def __init__(self, dictionary):
        self.name = dictionary['name']
        self.age = dictionary['age']
        self.position = dictionary['position']
        self.team = dictionary['team']

    @classmethod
    def get_team(cls, team_list):
        new_team = []
        for member in team_list:
            new_team.append(cls(member))
        return new_team

# ---------------------------------------------------------------------------- #

players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

# ---------------------------------------------------------------------------- #

new_team = Player.get_team(players)

print(new_team)