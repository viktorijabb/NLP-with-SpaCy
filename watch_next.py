# program compares a model movie with a list of other movies based on description 
# and outputs the movie with the highest similarity
import spacy
nlp = spacy.load('en_core_web_md')

movie_to_compare= "Planet Hulk :Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
model_movie = nlp(movie_to_compare)

similarities_l = [] # empty list used to compare similarities 

print("A similar movie to Planet Hulk is...")

with open("movies.txt", "r", encoding='utf-8') as movies_file: 
    movies = movies_file.read()
    lines = movies.split("\n")

    for index, movie in enumerate(lines, start = 1):
        name, description = movie.split(" :")
        similarity = nlp(description).similarity(model_movie)
        similarities_l.append(similarity) # add similarity coefficient to list
    best_match_sim = max(similarities_l)
    for nr, item in enumerate(similarities_l, start = 1):
        if best_match_sim == item: 
            for index, movie in enumerate(lines, start = 1):
                name, description = movie.split(" :")
                similarity = nlp(description).similarity(model_movie)
                if similarity == best_match_sim: 
                    print(f"{name} :{description}")