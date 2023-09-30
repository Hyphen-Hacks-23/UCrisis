import twint

try:
    # Configure
    c = twint.Config()
    c.Search = "Drake Album"
    c.Format = "Tweet id: {id} | Tweet: {tweet}"
    c.Limit = 100

    print("here1")
    # Run
    twint.run.Search(c)
    print("here2")

except Exception as e:
    print(f"An error occurred: {str(e)}")
