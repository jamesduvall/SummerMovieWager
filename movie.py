class Movie:
    def __init__(self, rank, movie_title, amount):
        self.rank = rank
        self.movie_title = movie_title
        self.amount = amount
        
    def print_me(self):
        print 'Rank: ', self.rank, '\nMovie Title: ', self.movie_title, '\nAmount: ', self.amount