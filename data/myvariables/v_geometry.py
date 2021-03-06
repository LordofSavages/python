# creating geometry values

# imports
from data.myvariables.userconfig import width as config_width
from data.myvariables.userconfig import height as config_height

# main geometry
main_width = config_width
main_height = config_height
main_width = int(main_width)
main_height = int(main_height)
main_geometry = str(main_width) + "x" + str(main_height)

# game geometry (set to the same as main)
game_width = main_width
game_height = main_height
game_width = int(game_width)
game_height = int(game_height)
game_geometry = str(game_width) + "x" + str(game_height)

# cheatsheet geometry
# image resolution
cheatsheet_width = 2000
cheatsheet_height = 1750

cheatsheet_aspect = float(cheatsheet_width) / float(cheatsheet_height)
cheatsheet_resize_factor = float(main_height) / float(cheatsheet_height)
cheatsheet_height = cheatsheet_height * cheatsheet_resize_factor
cheatsheet_width = cheatsheet_height * cheatsheet_aspect

cheatsheet_width = int(cheatsheet_width)
cheatsheet_height = int(cheatsheet_height)
cheatsheet_geometry = str(cheatsheet_width) + "x" + str(cheatsheet_height)

# documentation geometry (coincidentally similar to cheatsheet)
# image resolution
documentation_width = 2000
documentation_height = 1750

documentation_aspect = float(documentation_width) / float(documentation_height)
documentation_resize_factor = float(main_height) / float(documentation_height)
documentation_height = documentation_height * documentation_resize_factor
documentation_width = documentation_height * documentation_aspect

documentation_width = int(documentation_width)
documentation_height = int(documentation_height)
documentation_geometry = str(documentation_width) + "x" + str(documentation_height)

# start geometry
start_height = main_height
start_width = start_height / 2
start_width = int(start_width)
start_height = int(start_height)
start_geometry = str(start_width) + "x" + str(start_height)
