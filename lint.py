import sys
from pylint import lint

THRESHOLD = 5

score = lint.Run(['factorial.py'], exit=False).linter.stats.global_note

if score < THRESHOLD:
    print("Linter failed: Score < threshold value")
    print(sys.exit())
    sys.exit()
