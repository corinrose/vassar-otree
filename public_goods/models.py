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


    # """Amount allocated to each player"""
    endowment = c(100)
    multiplier = 2


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    total_contribution = models.CurrencyField()

    individual_share = models.CurrencyField()

    def set_payoffs(self):
        player = self.get_players()[0]

        bot_allocation = 100

        if player.condition == 2:
            bot_allocation = 50
        elif player.condition == 3:
            bot_allocation = 75

        self.total_contribution = player.contribution + random.randint(0, bot_allocation * 2)
        self.individual_share = self.total_contribution * Constants.multiplier / 3
        player.payoff = (Constants.endowment - player.contribution) + self.individual_share

class Player(BasePlayer):

    condition = models.IntegerField(initial=random.choice([1, 2, 3, 4]))
    
    contribution = models.CurrencyField(
        min=0, max=Constants.endowment,
        doc="""The amount contributed by the player""",
    )
