import tkinter as tk
from pandas import read_csv
import requests
import pandas as pd
from threading import Thread
import csv
import random

from scipy import rand
from sympy import content

# file = pd.read_csv("quotes1_100.csv")
# file = file[["quote", "author"]]
file = "quotes1_100.csv"


quotes = []


with open(file) as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        quotes.append(row)
    
quote_number = 0

window = tk.Tk()
window.geometry("1000x500")
window.title("Happy Valentine's Day")
window.grid_columnconfigure(0, weight=1)
window.resizable(False, False)
window.configure(bg = "pink")

# data_list = csv.reader(file)
# chosen_row = random.choice(data_list)

db_length = len(quotes) #length of database
# rand_quote = random.randint(0, db_length-1) #generates random number without going beyond scope of database


def preload_quotes():
    global quotes
    global quote_label
    
    print("***Loading more quotes***")
    for x in range(10):
        rand_quote = random.randint(0, db_length-1)
        random_quote = quotes[rand_quote]
        content = random_quote[1]
        author = random_quote[2]
        quote = content + "\n\n" + "By " + author
        print(content)


        quotes.append(quote)

    print("***Finished  loading more quotes***")

preload_quotes()

def get_random_quote():
    #pass
    global quote_label
    global quotes
    global quote_number

    for x in range(10):
        rand_quote = random.randint(0, db_length-1)
        random_quote = quotes[rand_quote]
        content = random_quote[1]
        author = random_quote[2]
        quote = content + "\n\n" + "By " + author
        print(content)

    quote_label.configure(text=quote)
    quote_number = quote_number + 1
    print(quote_number)

    if quotes[quote_number] == quotes[-3]:
        thread = Thread(target=preload_quotes) 
        thread.start()


# UI
quote_label = tk.Label(window, text="Happy Valentine's Day my love. It's our third one together, and every day you teach me how to love harder. I associated love only with loss before I met you, and with you I feel in love every second of the day regardless of my emotions. I hope you enjoy this compilation of quotes by romantics and authors of the century, and maybe even get some new book suggestions out of it. \n Yours Forever, \n Sandra \n 'There I was, way off my ambitions, getting deeper in love every minute.' \n \n The Great Gatsby",
    height = 20, 
    pady=15,
    wraplength=800,
    font=("Helvetica", 15))
quote_label.grid(row = 0, column=0, stick="WE", padx=20, pady=10)

button = tk.Button(text = "Click for Quotes!", command=get_random_quote, bg="grey",
    fg = "pink",
    activebackground="grey", font=("Helvetica", 14))
button.grid(row = 1, column=0, stick="WE", padx=20, pady=10)

# Runs program
if __name__ == "__main__":
    window.mainloop()
