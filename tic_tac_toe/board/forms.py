from django.newforms import form_for_model
from tic_tac_toe.board.models import Game

#GAME_FIELDS=('block1', 'block2', 'block3', 'block4', 'block5', 'block6', 'block7', 'block8', 'block9')
GAME_FIELDS=('block1', 'block3')

# Game form
GameForm = form_for_model(Game, fields=GAME_FIELDS)
