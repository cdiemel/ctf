green = u'\u001b[32m'
yellow = u'\u001b[33m'
red = u'\u001b[31m'
reset = u'\u001b[0m'

percent = 85.25
graph_char_count = round(percent/5)
graph_chars = "#"*graph_char_count
r = graph_chars[0:6]
y = graph_chars[6:12]
g = graph_chars[12:20]

print("[{}{:6s}{}{:6s}{}{:8s}{}]{}%".format(red,r,yellow,y,green,g,reset,percent))