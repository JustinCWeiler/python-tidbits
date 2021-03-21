#!/venv/bot/bin/python
from googletrans import Translator

trans = Translator()

inp = "Hallo, wie geht es dir?"
t = trans.translate(inp)

print(f"{inp} -> {t.text}")
