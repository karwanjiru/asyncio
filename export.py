import jinja2
env = jinja2.Environment()
template = env.from_string("Hello {{ name }}!")
print(template.render(name="Diana"))

from jinja2 import Environment, FileSystemLoader

MAX_SCORE = 100
TEST_NAME = "Operation Shadowstrike"

cadets = [
    {"name" : "Danvers", "score" : 100},
    {"name" : "Esme", "score" : 85},
    {"name" : "Kara", "score" : 95},
    {"name" : "Lex", "score" : 45},
    {"name" : "Liberty", "score" : 65}
]

env = Environment(loader = FileSystemLoader("templates/"))
template = env.get_template("export.csv")


filename = f"output/Operation_Shadowcloak.csv"
context = {
    "cadets": cadets,
    "max_score": MAX_SCORE, 
}

with open(filename, mode="w", encoding = "utf-8") as output:
    output.write(template.render(context))
