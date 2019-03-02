from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, Bot
)
import random

doc = """
This is a one-period public goods game with 3 players.
"""

# generate random participants
#bot_contribution = random.randint(0, 200)

class Constants(BaseConstants):
    name_in_url = 'public_goods'
    players_per_group = None
    num_rounds = 1

    instructions_template = 'public_goods/Instructions.html'

    # """Amount allocated to each player"""
    possible_allocations = [50, 75, 100]
    endowment = c(possible_allocations[random.randint(0, 2)])
    multiplier = 2


class Subsession(BaseSubsession):
    def vars_for_admin_report(self):
        contributions = [p.contribution for p in self.get_players() if p.contribution != None]
        if contributions:
            return {
                'avg_contribution': sum(contributions)/len(contributions),
                'min_contribution': min(contributions),
                'max_contribution': max(contributions),
            }
        else:
            return {
                'avg_contribution': '(no data)',
                'min_contribution': '(no data)',
                'max_contribution': '(no data)',
            }


class Group(BaseGroup):
    total_contribution = models.CurrencyField()

    individual_share = models.CurrencyField()

    def set_payoffs(self):
        self.total_contribution = sum([p.contribution for p in self.get_players() if p.contribution != None]) + random.randint(0, 200)
        #self.individual_share = self.total_contribution * Constants.multiplier / Constants.players_per_group
        self.individual_share = self.total_contribution * Constants.multiplier / 3
        for p in self.get_players():
            p.payoff = (Constants.endowment - p.contribution) + self.individual_share

class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, max=Constants.endowment,
        doc="""The amount contributed by the player""",
    )
