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
template = env.get_template("all.txt")

for cadet in cadets:
    name = cadet["name"]
    filename = f"output/message_{name.lower()}.txt"
    content = template.render(
        cadet,
        max_score = MAX_SCORE,
        test_name = TEST_NAME
    )

    with open(filename, mode="w", encoding = "utf-8") as output:
        output.write(content)
        print("... wrote", filename)
