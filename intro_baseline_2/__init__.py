from otree.api import *


doc = """
This is the intro app for Part 2 (baseline) of 
the project "Managing the Tragedy of the Commons: A Partial Output-Sharing Approach"
This will include Instructions, Example, KnowledgeCheck Pages.
"""


class C(BaseConstants):
    NAME_IN_URL = 'intro_baseline_2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # KnowledgeCheck questions

    kc1 = models.StringField(
        choices=[['False', 'Remain the same'], ['True', 'Randomly reassigned'],],
        label='1. Will your group (Part 1) remain the same or be randomly reassigned in Part 2?',
        widget=widgets.RadioSelect,
    )

    kc2 = models.StringField(
        choices=[['False', '5'], ['True', '10'], ['False', '15'], ['False', '20'], ],
        label='2. How many rounds will you play in Part 2?',
        widget=widgets.RadioSelect,
    )

    kc3 = models.StringField(
        choices=[['True', 'The sum of your earnings from both Part 1 and Part 2.'],
                 ['False', 'The earnings from Part 2.'],
                 ['False', 'A random Part will be selected, and only the earnings from that Part.'],
                 ['False', 'A fixed amount of money, regardless of your performance.'],
                 ],
        label='3. How will your final payoff be calculated?',
        widget=widgets.RadioSelect,
    )


# PAGES
class Instructions(Page):
    pass


class Wait(Page):
    pass



class KnowledgeCheck(Page):
    form_model = 'player'
    form_fields = [
        'kc1',
        'kc2',
        'kc3',
                   ]

    @staticmethod
    def error_message(player, values):
        solution = dict(
            kc1='True',
            kc2='True',
            kc3='True',
        )

        # Define specific error messages for each question
        error_messages = dict(
            kc1="The group will be reassigned randomly at the beginning of Part 2",
            kc2="There are 10 rounds in the game.",
            kc3="Your final earnings will be the sum of the earnings from both parts."
        )

        # Prepare the final error messages for display if a wrong answer is selected
        final_errors = {}
        for field_name, correct_value in solution.items():
            if values[field_name] != correct_value:
                final_errors[field_name] = error_messages[field_name]

        return final_errors



class BeforePractice(Page):
    pass



page_sequence = [
    Instructions,
    Wait,
    KnowledgeCheck,
    BeforePractice,
]
