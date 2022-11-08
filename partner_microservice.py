import random
import time

if __name__ == '__main__':
    jokes = ["What's yellow and kills you if it gets in your eye? A bulldozer.",
             "What does Harry Potter use to get rid of a rash? Quit itch.",
             "What did the evil chicken lay? Deviled eggs.",
             "Why did Adele cross the road? To say, 'Hello!' from the other side.",
             "I sent 10 jokes to the newspaper hoping at least one would get published. No pun in ten did.",
             "Parallel lines have so much in common. It's a shame they'll never meet.",
             "I just invented an awesome new word: plagiarism.",
             "What does an annoying pepper do? It gets jalapeno face.",
             "I was playing with a boomerang and couldn't remember how to use it. Then it cam back to me.",
             "What do you call a snobby criminal going down the stairs? A condescending con descending.",
             "What word is always spelled wrong? Wrong.",
             "What did the notebook say when it graduate? College ruled.",
             "What do you get when you cross a joke with a rhetorical question?",
             "How much space do fungi need to grow? As mushroom as possible.",
             "How did the kleptomaniac treat his condition? He took something for it.",
             "Lately people have been making apocalypse jokes like there is no tomorrow.",
             "Milk is the fastest liquid on earth. It's pasteurized before you even see it!",
             "I used to be addicted to the hokey-pokey, but then I turned myself around.",
             "What blue and smells like red paint? Blue paint.",
             "What did the hat say to the scarf? You hang around. I'll go on ahead."]

    while True:
        time.sleep(2)

        joke = open("dad-joke.txt", "r")
        line = joke.readline()
        joke.close()

        if line == "dad":
            print("Message received. Getting dad joke.\n")
            time.sleep(1)
            joke_num = random.randint(0, 19)
            joke = open("dad-joke.txt", "w")
            joke.write(jokes[joke_num])
            print("Dad joke sent.\n")
            joke.close()
