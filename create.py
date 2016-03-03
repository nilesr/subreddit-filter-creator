import itertools, string
from iso639 import is_valid639_1
ascii = string.ascii_lowercase
table_true = "[Yes](/wiki_table_true)"
table_false =  "[No](/wiki_table_false)"
def nextid(old):
    if old[1] != "z":
        return old[0] + ascii[ascii.index(old[1])+1]
    else:
        return ascii[ascii.index(old[0]) + 1] + "a"
flairs = [
    ["No hrkgame", "div.link[data-domain='hrkgame.com']"],
    ["No dlc", ".linkflair-dlc"],
    ["No ended giveaways", ".linkflair-ended"],
    ["No gleam.io", "div.link[data-domain='gleam.io']"]
]
combinations = []
tables = []
for i in range(2, len(flairs)+1):
    for f in itertools.combinations(flairs, i):
        combinations.append(f)
current_id = "ac"
for f in combinations:
    print(", ".join(["html:lang(" + current_id + ") " + s[1] for s in f]) + " {")
    print("    display: none;")
    print("}")
    table = []
    for z in flairs:
        if z in f:
            table.append(table_true)
        else:
            table.append(table_false)
    tables.append([table, current_id])
    current_id = nextid(current_id)
    while is_valid639_1(current_id):
        current_id = nextid(current_id)

for f in range(3):
    print()
print ("Subdomain | " + " | ".join(f[0] for f in flairs))
print("-|" + "|".join([":-:" for i in range(len(flairs))]))
for table in tables:
    print("[`" + table[1] + "`](http://"+table[1]+".reddit.com/r/FreeGamesOnSteam) | " + " | ".join(table[0]))

