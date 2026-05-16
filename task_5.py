class Results:
    def __init__(self, victories, draw, losses):
        self.victories = victories
        self.draw = draw
        self.losses = losses
    
class Football(Results):
    def __init__(self, victories, draw, losses):
        super().__init__(victories, draw, losses)

    def number_of_wins(self):
        return f'Футбольных побед: {self.victories}'
    
    def number_of_draws(self):
        return f'Футбольных ничьих: {self.draw}'
    
    def number_of_losses(self):
        return f'Футбольных поражений: {self.losses}'
    
    def total_points(self):
        return f'Общее количество очков: {3*self.victories+self.draw}'

class Hockey(Results):
    def __init__(self, victories, draw, losses):
        super().__init__(victories, draw, losses)

    def number_of_wins(self):
        return f'Хоккейных побед: {self.victories}'
    
    def number_of_draws(self):
        return f'Хоккейных ничьих: {self.draw}'
    
    def number_of_losses(self):
        return f'Хоккейных поражений: {self.losses}'
    
    def total_points(self):
        return f'Общее количество очков: {2*self.victories+self.draw}'

football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

for team in (football_team, hockey_team):
    print(team.number_of_wins())
    print(team.number_of_draws())
    print(team.number_of_losses())
    print(team.total_points())