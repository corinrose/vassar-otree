from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):

    def vars_for_template(self):
        return { 'instructions_template' : 'public_goods/Instructions' + str(self.player.condition) + '.html'}

    """Description of the game: How to play and returns expected"""
    pass


class Contribute(Page):
    """Player: Choose how much to contribute"""

    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

    body_text = "Waiting for other participants to contribute."


class Results(Page):
    """Players payoff: How much each has earned"""

    def vars_for_template(self):
        self.group.set_payoffs()
        return {
            'earnings': self.group.total_contribution * Constants.multiplier,
        }
        #self.group.total_contributions = 0


page_sequence = [
    Introduction,
    Contribute,
    #ResultsWaitPage,
    Results
]
