pop_dict = {"The Matrix":["Keanu Reeves", "Carrie-Anne Moss", "Hugo Weaving"],
            "Harry Potter":["Danie Ratcliffe", "Emma Watson", "Rupert Grint"],
            "Friends": ["Jenifer Ariston", "Courtney Cox", "Lisa Kudrow"],
            "The Office": ["Steve Carell", "Rain Wilson", "John Krasinski"]}



def get_cast(title):
    if title in pop_dict:
        return pop_dict[title]
    else:
        print(f"{title} is not part of the database")
        return []


def add_title(title, cast):
    pop_dict[title] = cast


def count_actors():
    actors = dict()
    for cast_list in pop.dict.values():
        for actor in cast_list:
            if actor in actors:
                a

add_title("The Boys", ["Antony Starr", "William Butcher", "Hughie"])

#t = input ("What is the title of a movie you want to check "):