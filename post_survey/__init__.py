from otree.api import *
import math



doc = """
This is the post-survey app for the project "Managing the Tragedy of the Commons: A Partial Output-Sharing Approach"
This will include Demographics, Decision, and Big 5 personality traits pages.
"""


class Constants(BaseConstants):
    name_in_url = 'post-survey'
    players_per_group = None
    num_rounds = 1
    StandardChoices = [
        [1, 'Disagree strongly'],
        [2, 'Disagree moderately'],
        [3, 'Disagree a little'],
        [4, 'Neither agree nor disagree'],
        [5, 'Agree a little'],
        [6, 'Agree moderately'],
        [7, 'Agree strongly'],
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # record payoffs
    total_earning_part1 = models.IntegerField()
    total_earning_part2 = models.IntegerField()
    total_earning = models.IntegerField()
    total_cash_b4round = models.FloatField()
    total_cash = models.FloatField()
    final_cash = models.FloatField()

    # Demographics
    age = models.IntegerField(label='Q1) How old are you?', min=13, max=125)

    gender = models.StringField(
        choices=[
                 ['Male', 'Male'],
                 ['Female', 'Female'],
                 ['Other', 'Other'],
                 ['I prefer not to say.', 'I prefer not to say.'],
                 ],
        label='Q2) What is your gender?',
        widget=widgets.RadioSelect,
    )

    race = models.IntegerField(
        label="Q3) Which race or ethnicity best describes you? ",
        choices=[
            [1, 'White or Caucasian'],
            [2, 'Black or African-American'],
            [3, 'Hispanic or Latino'],
            [4, 'Asian'],
            [5, 'Native American'],
            [6, 'Mixed Race or Multi-Racial'],
            [7, 'Other'],
        ],
        widget=widgets.RadioSelect,
    )

    # academics
    study_year = models.IntegerField(
        label="Q4) What year are you?",
        choices=[
            [1, '1st-year undergraduate'],
            [2, '2nd-year undergraduate'],
            [3, '3rd-year undergraduate'],
            [4, '4th-year undergraduate'],
            [5, 'Graduate'],
            [0, 'Other'],
        ],
        widget=widgets.RadioSelect,
    )

    study_field = models.StringField(
        choices=[
            ['Arts and Humanities', 'Arts and Humanities'],
            ['Business', 'Business'],
            ['Economics', 'Economics'],
            ['Engineering', 'Engineering'],
            ['Finance', 'Finance'],
            ['Mathematics', 'Mathematics'],
            ['Medicine', 'Medicine'],
            ['Natural Science', 'Natural Science'],
            ['Psychology', 'Psychology'],
            ['Social Studies', 'Social Studies'],
            ['Other', 'Other'],
        ],
        label='Q5) What is your field of study',
        widget=widgets.RadioSelect,
    )

    gpa_avg = models.FloatField(
        label="Q6) What is your average GPA?",
        choices=[
            [0.5, 'Less than 1'],
            [1.5, 'Between 1 and 2'],
            [2.25, 'Between 2 and 2.5'],
            [2.75, 'Between 2.5 and 3'],
            [3.25, 'Between 3 and 3.5'],
            [3.75, 'More than 3.5'],
        ],
        widget=widgets.RadioSelect,
    )

    # experiences
    experience = models.IntegerField(
        label="Q7) Please indicate how many decision-making experiments you have participated in (including this experiments).",
        choices=[
            [1, 'This is the first time.'],
            [2, '2 - 4'],
            [3, '5 - 7'],
            [4, '8 -'],
            [0, 'I prefer not to say.']
        ],
        widget=widgets.RadioSelect,
    )

    # Decisions
    decisions_clear = models.IntegerField(
        label="Q1) It was clear from the instructions what decisions I had to make during the experiment.",
        choices=[
            [1, 'Strongly Disagree'],
            [2, 'Disagree'],
            [3, 'Neutral'],
            [4, 'Agree'],
            [5, 'Strongly Agree'],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    earnings_clear = models.IntegerField(
        label="Q2) It was clear from the instructions how my earnings would be determined based on my decisions.",
        choices=[
            [1, 'Strongly Disagree'],
            [2, 'Disagree'],
            [3, 'Neutral'],
            [4, 'Agree'],
            [5, 'Strongly Agree'],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    tools_clear = models.IntegerField(
        label="Q3) Have you used a guess-slider to make your decisions?",
        choices=[
            [1, 'Yes'],
            [0, 'No'],
        ],
        widget=widgets.RadioSelect,
    )

    tools_helpful = models.IntegerField(
        label="Q4) A guess-slider was helpful for me to make decisions.",
        choices=[
            [1, 'Strongly Disagree'],
            [2, 'Disagree'],
            [3, 'Neutral'],
            [4, 'Agree'],
            [5, 'Strongly Agree'],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    tools_belief = models.IntegerField(
        label="Q5) I believe that my guess was accurate when using guess-sliders",
        choices=[
            [1, 'Strongly Disagree'],
            [2, 'Disagree'],
            [3, 'Neutral'],
            [4, 'Agree'],
            [5, 'Strongly Agree'],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    sharing_clear = models.IntegerField(
        label="Q6) It was clear from the instructions how my earnings will be affected by sharing arrangements.",
        choices=[
            [1, 'Strongly Disagree'],
            [2, 'Disagree'],
            [3, 'Neutral'],
            [4, 'Agree'],
            [5, 'Strongly Agree'],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    sharing_impact = models.IntegerField(
        label="Q7) Sharing arrangements influenced my decisions.",
        choices=[
            [1, 'Strongly Disagree'],
            [2, 'Disagree'],
            [3, 'Neutral'],
            [4, 'Agree'],
            [5, 'Strongly Agree'],
        ],
        widget=widgets.RadioSelectHorizontal,
    )


    # Big 5 personality traits using Ten-Item Personality Inventory-(TIPI) Gosling et al. (2003)
    big5_extraversion = models.IntegerField(
        label='I see myself as someone who is outgoing and full of energy.',
        choices=Constants.StandardChoices,
        # widget=widgets.RadioSelectHorizontal,
    )

    big5_agreeableness_r = models.IntegerField(
        label='I see myself as someone who tends to find fault with others and can be argumentative.',
        choices=Constants.StandardChoices,
        # widget=widgets.RadioSelectHorizontal,
    )

    big5_conscientiousness = models.IntegerField(
        label='I see myself as someone who is reliable and has strong self-discipline.',
        choices=Constants.StandardChoices,
        # widget=widgets.RadioSelectHorizontal,
    )

    big5_emotional_stability_r = models.IntegerField(
        label='I see myself as someone who often feels anxious and gets upset easily.',
        choices=Constants.StandardChoices,
        # widget=widgets.RadioSelectHorizontal,
    )

    big5_openness = models.IntegerField(
        label='I see myself as someone who is open to new experiences and has a rich imagination.',
        choices=Constants.StandardChoices,
        # widget=widgets.RadioSelectHorizontal,
    )

    big5_extraversion_r = models.IntegerField(
        label='I see myself as someone who is reserved and tends to be quiet.',
        choices=Constants.StandardChoices,
        # widget=widgets.RadioSelectHorizontal,
    )

    big5_agreeableness = models.IntegerField(
        label='I see myself as someone who is compassionate and has a warm personality.',
        choices=Constants.StandardChoices,
        # widget=widgets.RadioSelectHorizontal,
    )

    big5_conscientiousness_r = models.IntegerField(
        label='I see myself as someone who tends to be disorganized and sometimes careless.',
        choices=Constants.StandardChoices,
        # widget=widgets.RadioSelectHorizontal,
    )

    big5_emotional_stability = models.IntegerField(
        label='I see myself as someone who is generally calm and handles stress well.',
        choices=Constants.StandardChoices,
        # widget=widgets.RadioSelectHorizontal,
    )

    big5_openness_r = models.IntegerField(
        label='I see myself as someone who prefers routine over new experiences and is not very imaginative.',
        choices=Constants.StandardChoices,
        # widget=widgets.RadioSelectHorizontal,
    )

# Calculate Payoffs
def final_payoffs(p: Player):
    p.total_earning_part1 = p.participant.vars['totalEarnings_a']
    p.total_earning_part2 = p.participant.vars['totalEarnings_b']
    p.total_earning = p.participant.vars['totalEarnings']
    p.total_cash_b4round = p.participant.vars['totalCash']
    p.total_cash = (math.ceil(p.total_cash_b4round * 4)) / 4
    p.final_cash = p.total_cash + 5

# PAGES

class IntroPage(Page):

    def before_next_page(player: Player, timeout_happened):
        # Calculate payoffs after the player submits their decision
        final_payoffs(player)

class Demographics(Page):
    form_model = 'player'
    form_fields = [
        'age',
        'gender',
        'race',
        'study_year',
        'study_field',
        'gpa_avg',
        'experience',
    ]

class Decisions(Page):
    form_model = 'player'
    form_fields = [
        'decisions_clear',
        'earnings_clear',
        'tools_clear',
        'tools_helpful',
        'tools_belief',
        'sharing_clear',
        'sharing_impact',
    ]



class Big5(Page):
    form_model = 'player'
    form_fields = [
        'big5_conscientiousness',
        'big5_openness_r',
        'big5_agreeableness',
        'big5_emotional_stability',
        'big5_extraversion_r',
        'big5_openness',
        'big5_conscientiousness_r',
        'big5_agreeableness_r',
        'big5_extraversion',
        'big5_emotional_stability_r',
    ]


class EndPage(Page):
    pass

page_sequence = [
    IntroPage,
    Demographics,
    Decisions,
    Big5,
    EndPage,
]
