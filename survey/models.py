from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    econ_train = models.StringField(
        choices=['None', 'Some classes in high school', 'Some classes in college', 'Minor in college', 'Major in college', 'Advanced degree in economics'],
        label=''' Have you had any formal economics training? ''',
        widget=widgets.RadioSelect,)

    prol_id = models.StringField(
        label=''' Please enter your Prolific ID''')
    
    sugg = models.StringField(blank=True,
        label=''' Were there any technical problems with this experiment? Did you find the instructions to be
        clear? Do you have any other comments? ''')
