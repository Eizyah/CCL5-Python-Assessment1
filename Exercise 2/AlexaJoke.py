import tkinter as tk
import random


#Creates a list for the jokes
AlexaJokes = [
    "Why did the chicken cross the road?To get to the other side.",
    "What happens if you boil a clown?You get a laughing stock.",
    "Why did the car get a flat tire ?Because there was a fork in the road!",
    "How did the hipster burn his mouth? He ate his pizza before it was cool.",
    "What did the janitor say when he jumped out of the closet? SUPPLIES!!!!",
    "Have you heard about the band 1023MB? It's probably because they haven't got a gig yet…",
    "Why does the golfer wear two pants? Because he's afraid he might get a 'Hole-in-one.'",
    "Why should you wear glasses to maths class? Because it helps with division.",
    "Why does it take pirates so long to learn the alphabet? Because they could spend years at C.",
    "Why did the woman go on the date with the mushroom? Because he was a fun-ghi.",
    "Why do bananas never get lonely? Because they hang out in bunches.",
    "What did the buffalo say when his kid went to college? Bison.",
    "Why shouldn't you tell secrets in a cornfield? Too many ears.",
    "What do you call someone who doesn't like carbs? Lack-Toast Intolerant.",
    "Why did the can crusher quit his job? Because it was soda pressing.",
    "Why did the birthday boy wrap himself in paper? He wanted to live in the present.",
    "What does a house wear? A dress.",
    "Why couldn't the toilet paper cross the road? Because it got stuck in a crack.",
    "Why didn't the bike want to go anywhere? Because it was two-tired!",
    "Want to hear a pizza joke? Nahhh, it's too cheesy!",
    "Why are chemists great at solving problems? Because they have all of the solutions!",
    "Why is it impossible to starve in the desert? Because of all the sand which is there!",
    "What did the cheese say when it looked in the mirror? Halloumi!",
    "Why did the developer go broke? Because he used up all his cache.",
    "Did you know that ants are the only animals that don't get sick? It's true! It's because they have little antibodies.",
    "Why did the donut go to the dentist? To get a filling.",
    "What do you call a bear with no teeth? A gummy bear!",
    "What does a vegan zombie like to eat? Graaains.",
    "What do you call a dinosaur with only one eye? A Do-you-think-he-saw-us!",
    "Why should you never fall in love with a tennis player? Because to them... love means NOTHING!",
    "What did the full glass say to the empty glass? You look drunk.",
    "What's a potato's favorite form of transportation? The gravy train",
    "What did one ocean say to the other? Nothing, they just waved.",
    "What did the right eye say to the left eye? Honestly, between you and me something smells.",
    "What do you call a dog that's been run over by a steamroller? Spot!",
    "What's the difference between a hippo and a zippo? One's pretty heavy and the other's a little lighter",
    "Why don't scientists trust Atoms? They make up everything."
]


#Separates the setup from the punchline
def get_joke():
    global setup, punchline
    joke = random.choice(AlexaJokes)
    jokeparts = joke.split("?")
    setup = jokeparts[0] + "?"
    punchline = jokeparts[1] if len(jokeparts) > 1 else ""
    joke_label.config(text=setup)
    punchline_label.config(text="")
    showjoke_button.config(state="normal")


#shows the punchline when button is clicked
def show_punchline():
    punchline_label.config(text=punchline)
    showjoke_button.config(state="disabled")



root = tk.Tk()
root.title("Alexa Tells a Joke Program")
root.geometry("500x400")


title_label = tk.Label(root, text="Alexa, tell a joke!", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

joke_label = tk.Label(root, text="", font=("Arial", 14), wraplength=450)
joke_label.pack(pady=20)

punchline_label = tk.Label(root, text="", font=("Arial", 15, "italic"), wraplength=450, fg="green")
punchline_label.pack(pady=10)

#Creates a button frame for all buttons in the root
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

#Creates a button so when clicked, takes a joke from the list
next_button = tk.Button(button_frame, text="Tell me a joke Alexa", font=("Arial", 10), command=get_joke, width=15, height=2)
next_button.grid(row=0, column=0, padx=10)

#Creates a button so when clicked, takes the punchline from the list
showjoke_button = tk.Button(button_frame, text="Show joke punchline", font=("Arial", 10), command=show_punchline, width=15, height=2, state="disabled")
showjoke_button.grid(row=0, column=1, padx=10)

#When clicked, exits program
quit_button = tk.Button(root, text="Quit", font=("Arial", 10), command=root.quit, width=10)
quit_button.pack(pady=10)

root.mainloop()


