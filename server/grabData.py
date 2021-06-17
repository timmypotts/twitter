import twint

c = twint.Config()

c.Username = "mikerainey82"
c.Store_csv = True
c.Output = "tweets.csv"

twint.run.Search(c)