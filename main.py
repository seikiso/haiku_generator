import random
from janome.tokenizer import Tokenizer

t = Tokenizer()
f = open("static/haruto_shura.txt", 'r', encoding='shift_jis')
d = f.read()

five_char = ""
five_char_list = []
five_char_length = 0

seven_char = ""
seven_char_list = []
seven_char_length = 0

for token in t.tokenize(d):
    if not token.reading == "*":
        if not any(x in token.surface for x in ("。", "、", "（", "）", "『", "』", "「", "」", "を", "は", "！", "と", "の",
                                                "て", "に", "っ", "し", "で", "》", "が", "な", "う", "《", "だ", "た",
                                                "：", "−", "・", "や", "］", "も", "へ", "　", "｜", "…", "ん", "［", "れ",
                                                "り")):
            five_char_length += len(token.reading)
            five_char += token.surface

            seven_char_length += len(token.reading)
            seven_char += token.surface

    if five_char_length == 5:
        five_char_list.append(five_char)

    if seven_char_length == 7:
        seven_char_list.append(seven_char)

    if five_char_length >= 5:
        five_char = ""
        five_char_length = 0

    if seven_char_length >= 7:
        seven_char = ""
        seven_char_length = 0

print(random.choice(five_char_list))
print(random.choice(seven_char_list))
print(random.choice(five_char_list))
