from django.http import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.newforms import *
from django import oldforms
from django.conf import settings
from django.template import RequestContext

from datetime import date, timedelta
import datetime

from tic_tac_toe.board.models import *
from tic_tac_toe.settings import *
from tic_tac_toe.board.forms import *

def index(request):
    
    if request.POST:
        g=GameForm(request.POST)
        g.is_bound

        #validate the blog, save, and redirect to the blog entry
        if g.is_valid():
            new_game = Game()
            
            if 'block1' in request.POST:
                new_game.block1 = request.POST['block1']
                if new_game.block1 == "X":
                    new_game.block3 = "O"
            
            if 'block2' in request.POST:
                new_game.block2 = request.POST['block2']
                if new_game.block2 == "X":
                    new_game.block1 = "O"
            
            if 'block3' in request.POST:
                new_game.block3 = request.POST['block3']
                if new_game.block3 == "X":
                    new_game.block1 = "O"
            
            if 'block4' in request.POST:
                new_game.block4 = request.POST['block4']
                if new_game.block4 == "X":
                    new_game.block1 = "O"
                    
            if 'block5' in request.POST:
                new_game.block5 = request.POST['block5']
                if new_game.block5 == "X":
                    new_game.block1 = "O"
                    
            if 'block6' in request.POST:
                new_game.block6 = request.POST['block6']
                if new_game.block6 == "X":
                    new_game.block1 = "O"
                    
            if 'block7' in request.POST:
                new_game.block7 = request.POST['block7']
                if new_game.block7 == "X":
                    new_game.block1 = "O"
                    
            if 'block8' in request.POST:
                new_game.block8 = request.POST['block8']
                if new_game.block8 == "X":
                    new_game.block1 = "O"
                    
            if 'block9' in request.POST:
                new_game.block9 = request.POST['block9']
                if new_game.block9 == "X":
                    new_game.block1 = "O"                                        
                
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
            
            if 'block2' in request.POST:
                curr_game.block2 = request.POST['block2']
                if curr_game.block9 == None:
                    curr_game.block9 = "O"
            
            if 'block4' in request.POST:
                curr_game.block4 = request.POST['block4']
                
                if curr_game.block5:
                    curr_game.block6 = "O"
                
                if curr_game.block1:
                    if curr_game.block9:
                        curr_game.block6 = "O"
                    else:    
                        curr_game.block7 = "O"
            
            if 'block5' in request.POST:
                curr_game.block5 = request.POST['block5']
                
                if curr_game.block9:
                    curr_game.block8 = "O"
                elif curr_game.block4:
                    curr_game.block6 = "O"    
                
                if curr_game.block1 == "X":
                    curr_game.block9 = "O"
                
                if curr_game.block3 == "X":
                     curr_game.block7 = "O"
                    
                
            if 'block6' in request.POST:
                curr_game.block6 = request.POST['block6']
                if curr_game.block7 == None:
                    curr_game.block7 = "O"
            
            if 'block7' in request.POST:
                curr_game.block7 = request.POST['block7']
                
                if curr_game.block1 == "X":
                    curr_game.block4 = "O" 
                    
                if curr_game.block3:
                    curr_game.block5 = "O"    
            
            if 'block8' in request.POST:
                curr_game.block8 = request.POST['block8']
                
                if curr_game.block9:
                    if curr_game.block7:
                       curr_game.block8 = "O" 
                    else:    
                        curr_game.block5 = "O"
                
                if curr_game.block7 == "X":
                    if curr_game.block9 == "X":
                        curr_game.block8 = "X"
                        
            
            if 'block9' in request.POST:
                curr_game.block9 = request.POST['block9']
                
                if curr_game.block3:
                    if curr_game.block7:
                        curr_game.block8 = "O"
                
                if curr_game.block1:
                    curr_game.block5 = "O"
                
            
            curr_game.save()
            return HttpResponseRedirect("/game/") 
    
    else:
        g = GameInstanceForm()
    
    
    return render_to_response('game.html',
                            {
                            'curr_game':curr_game,
                             })     