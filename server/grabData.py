import twint

c = twint.Config()

c.Username = "ben_awareness"
c.Store_csv = True
c.Output = "tweets.csv"

twint.run.Search(c)