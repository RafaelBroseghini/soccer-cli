from random import shuffle

def get_team_color(team_colors, click_colors):
    team_colors = list(map(lambda x: x.upper(), team_colors.split(" / ")))
    shuffle(team_colors)
    for c in team_colors:
        if c in click_colors:
            return c.lower()
    return False
