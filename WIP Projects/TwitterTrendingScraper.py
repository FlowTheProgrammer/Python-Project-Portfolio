import requests
import bs4

res = requests.get("https://twitter.com/explore/tabs/trending")
soup = bs4.BeautifulSoup(res.text,"lxml")



print("Welcome to the Twitter Scrapper!")
print("-------------------------------")

while True:
        try: 
            trend_number = int(input("How many trending items would you like to grab?: \n"))
            while trend_number < 1 or trend_number > 30:
                while True:
                    try: 
                        print()
                        print("Please enter a number from 1-30")
                        print()
                        trend_number = int(input("How many trending items would you like to grab?: \n"))
                        break
                    except ValueError:
                        print("Invalid Input: Please input a number")
                        print()
            break
        except ValueError:
            print("Invalid Input: Please input a number")

