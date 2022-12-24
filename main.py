# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

first_goal_scorer = 'Ruud Gullit'
second_goal_scorer = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = first_goal_scorer + ' ' + str(goal_0) + ', ' + second_goal_scorer + ' ' + str(goal_1)

first_goal_report = f'{first_goal_scorer} scored in the {goal_0}nd minute'
second_goal_report = f'{second_goal_scorer} scored in the {goal_1}th minute'
report = first_goal_report + '\n' + second_goal_report

player = 'Jan Wouters'

find_first_name_ending = player.find(' ')
first_name = player[:find_first_name_ending]

find_last_name_beginning = player.find(' ')
last_name_with_space = player[find_last_name_beginning:]
last_name = last_name_with_space.lstrip()
last_name_len = (len(last_name))

name_short = player[0] + '. ' + last_name

first_name_exclamation = (first_name + '!')
chant_01 = (first_name_exclamation + ' ') * len(first_name)
chant = chant_01.rstrip()

good_chant = chant[-1] != ' '