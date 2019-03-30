from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'public_goods',
        'display_name': "Public Goods Game",
        'num_demo_participants': 1,
        'app_sequence': ['public_goods', 'survey', 'payment_info'],
        'group_by_arrival_time': True,
    },
]
# see the end of this file for the inactive session configs

ROOMS = [
    {
        'name': 'vassar_experiment',
        'display_name': 'Vassar Experiment',
    },
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


DEMO_PAGE_INTRO_HTML = """
Welcome to the oTree Demo. Please begin with the Dictotor game, and then play the Public Goods game.
"""

# don't share this with anybody.
SECRET_KEY = 'l^6&g8(xewub4lt+%y^$zq3q-juw4khsh^b$gks5!%xc@&kh19'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

