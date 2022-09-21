"""Making bug """

from os import remove
from random import choice
from carbon.events import register

@register(pattern="^/q ?(.*)")

message = 'Crow Heroku no ban Deploy Successful'


print(message)
