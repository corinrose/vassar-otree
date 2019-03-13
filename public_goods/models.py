from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, Bot
)
import random

doc = """
This is a one-period public goods game with 3 players.
"""


class Constants(BaseConstants):
    name_in_url = 'public_goods'
    players_per_group = None
    num_rounds = 1

    bot_allocation = random.choice([50, 75, 100])
    instructions_template = 'public_goods/Instructions' + str(bot_allocation)  + '.html'

    
    # """Amount allocated to each player"""
    endowment = c(100)
    multiplier = 2


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    total_contribution = models.CurrencyField()

    individual_share = models.CurrencyField()

    def set_payoffs(self):
        self.total_contribution = sum([p.contribution + random.randint(0, p.condition * 2) for p in self.get_players() if p.contribution != None]) 
        #self.individual_share = self.total_contribution * Constants.multiplier / Constants.players_per_group
        self.individual_share = self.total_contribution * Constants.multiplier / 3
        for p in self.get_players():
            p.payoff = (Constants.endowment - p.contribution) + self.individual_share

class Player(BasePlayer):
    
    condition = models.IntegerField(initial=Constants.bot_allocation)
    
    contribution = models.CurrencyField(
        min=0, max=Constants.endowment,
        doc="""The amount contributed by the player""",
    )
