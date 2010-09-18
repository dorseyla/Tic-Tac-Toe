from django.http import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.newforms import *
from django import oldforms
from django.conf import settings
from django.template import RequestContext

from datetime import date, timedelta
import datetime

from django.db.models import Q

#from tic_tac_toe.models import *
from tic_tac_toe.settings import *
from tic_tac_toe.board.forms import *

def index(request):
    
    if request.POST:
        g=GameForm(request.POST)
        g.is_bound

        #validate the blog, save, and redirect to the blog entry
        if g.is_valid():
            new_game = Game()
            new_game.block1 = request.POST['block1']
#            new_game.block2 = request.POST['block2']
#            new_game.block3 = request.POST['block3']
#            new_game.block4 = request.POST['block4']
#            new_game.block5 = request.POST['block5']
#            new_game.block6 = request.POST['block6']
#            new_game.block7 = request.POST['block7']
#            new_game.block8 = request.POST['block8']
#            new_game.block9 = request.POST['block9']
            
            new_game.populate_game(g) 
            new_game.save()
            
            if new_game.block1 == "X":
                new_game.block3 = "O"
                
            new_game.save()    
            
            return HttpResponseRedirect("/game/")
        else:
            errors = g.errors
            return render_to_response('errors.html',
                            {
                            
                             })
    else:
        g=GameForm()
    
    
    return render_to_response('index.html',
                            {
                            
                             }) 
    
def game(request):
    
    try:
        curr_game = Game.objects.filter().order_by('-id')[:1].get()
    except ObjectDoesNotExist:
        curr_game = {}
    
    GameInstanceForm = form_for_instance(curr_game, fields=GAME_FIELDS)
    
    if request.POST:   
        g=GameInstanceForm(request.POST)
                
        if g.is_valid():      
             
            curr_game.populate_game(g)
            
            curr_game.block1 = request.POST['block1']
#            curr_game.block2 = request.POST['block2']
            curr_game.block3 = request.POST['block3']
#            curr_game.block4 = request.POST['block4']
#            curr_game.block5 = request.POST['block5']
#            curr_game.block6 = request.POST['block6']
#            curr_game.block7 = request.POST['block7']
#            curr_game.block8 = request.POST['block8']
#            curr_game.block9 = request.POST['block9']
            
            curr_game.save()
            return HttpResponseRedirect("/game/") 
    
    else:
        g = GameInstanceForm()
    
    
    return render_to_response('game.html',
                            {
                            'curr_game':curr_game,
                             })     