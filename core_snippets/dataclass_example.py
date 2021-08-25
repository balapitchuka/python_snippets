## dataclass module is introduced in Python 3.7 as a utility tool to make structured classes specially for storing data. 
## These classes hold certain properties and functions to deal specifically with the data and its representation.
## DataClasses in widely used Python3.6 
## Although the module was introduced in Python3.7, one can also use it in Python3.6 by installing dataclasses library. 

 
# Importing dataclass module
from dataclasses import dataclass
 
@dataclass
class Article():
    """A class for holding an article content"""
 
    # Attributes Declaration
    # using Type Hints
 
    title: str
    author: str
    language: str
    upvotes: int
 
# A DataClass object
article = Article("DataClasses",
                     "vibhu4agarwal",
                     "Python", 0)
print(article)
