from pydantic import BaseModel

class Page(BaseModel):
    number: int
    text: str

class Book(BaseModel):
    author: str
    title: str
    pages: list[Page]

my_books = [
		Book(
		    author="J. K. Rowling",
		    title="Harry Potter and the Philosopher's stone",
		    pages=[
		        Page(
		            number=1,
		            text="There once was a boy...",
		        ),
		        Page(
		            number=2,
		            text="He went to magic school...",
		        )
		    ]
		),
		Book(
		    author="Roger Zelazny",
		    title="Lord of Light",
		    pages=[
		        Page(
		            number=1,
		            text="It is said that fifty-three years ago...",
		        )
		    ]
		),
		Book(
            author = "Joyce Carol Oats",
            title = "Freaky Green Eyes",
            pages = [
                Page(
                    number = 1,
                    text = "When her parents seperate..."
                )
            ]
        ),
]

print(my_books[2].author)
print(my_books[2].pages[0].text)

for book in my_books:
    print(book.title)

import yaml

print(yaml.dump(my_books[0].model_dump()))

from pydantic_core import to_jsonable_python

print(yaml.dump(to_jsonable_python(my_books)))