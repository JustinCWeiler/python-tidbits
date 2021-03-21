import sys

from googletrans import Translator
from googletrans import LANGUAGES

print(sys.argv[1])

if len(sys.argv) < 2:
    sys.exit(1)

trans = Translator()

LANGS = []
for key in LANGUAGES:
    LANGS.append(key)

text = ''
if sys.argv[1] == '-f':
    if len(sys.argv) < 3:
        sys.exit(1)
    with open(sys.argv[2]) as f:
        text = f.read()
else:
    text = sys.argv[1]

for i in range(len(LANGS)):
    sys.stdout.write(f"---Translating {LANGUAGES[LANGS[i]]} - ")
    srce = LANGS[i-1] if i != 0 else 'auto'
    t = trans.translate(text, dest=LANGS[i], src=srce)
    print(t.text)
    text = t.text
print()
print(trans.translate(text, dest='en').text)

input()