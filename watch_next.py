import spacy
nlp = spacy.load('en_core_web_md')

print("A similar movie to Planet Hulk is...")

with open("movies.txt", "r") as movies_file: 
    movies = movies_file.read()
    name, description = movies.split(" :")
    print(movie)
