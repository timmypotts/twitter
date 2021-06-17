import twint

c = twint.Config()

c.Username = "timmycoors"
c.Store_csv = True
c.Output = "tweets.csv"

twint.run.Search(c)