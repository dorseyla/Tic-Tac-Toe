from django.db import models
from django.db.models.fields import *
from django.core.exceptions import ObjectDoesNotExist
from django.utils.html import strip_tags

from tic_tac_toe.settings import *

class Game(models.Model):
    block1 = models.CharField(maxlength=1, blank=True, null=True)
    block2 = models.CharField(maxlength=1, blank=True, null=True)
    block3 = models.CharField(maxlength=1, blank=True, null=True)
    block4 = models.CharField(maxlength=1, blank=True, null=True)
    block5 = models.CharField(maxlength=1, blank=True, null=True)
    block6 = models.CharField(maxlength=1, blank=True, null=True)
    block7 = models.CharField(maxlength=1, blank=True, null=True)
    block8 = models.CharField(maxlength=1, blank=True, null=True)
    block9 = models.CharField(maxlength=1, blank=True, null=True)
    
    def populate_game(self, g):
        self.block1  = strip_tags(g.clean_data['block1'])
        self.block2  = strip_tags(g.clean_data['block2'])
        self.block3  = strip_tags(g.clean_data['block3'])
        self.block4  = strip_tags(g.clean_data['block4'])
        self.block5  = strip_tags(g.clean_data['block5'])
        self.block6  = strip_tags(g.clean_data['block6'])
        self.block7  = strip_tags(g.clean_data['block7'])
        self.block8  = strip_tags(g.clean_data['block8'])
        self.block9  = strip_tags(g.clean_data['block9'])
    
    def get_absolute_url(self):
        return "/" + str(self.id)
        
    def __str__(self):
        return str(self.id)
    
    class Admin:
        list_display = ('block1', 'block2', 'block3', 'block4', 'block5', 'block6', 'block7', 'block8', 'block9')
        save_on_top=True