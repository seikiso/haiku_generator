import glob
import random
from janome.tokenizer import Tokenizer

t = Tokenizer()
# file = open("static/haruto_shura.txt", 'r', encoding='shift_jis')
# data = file.read()


# ignore_tokens = ["一", "二", "三", "四", "五", "』", "「", "」", "を", "は", "！", "と", "の", "て", "に", "っ", "し", "で",
#                  "》", "が", "な", "う", "《", "だ", "た", "：", "−", "・", "や", "］", "も", "へ", "　", "｜", "…", "ん",
#                  "［", "れ", "り", "ぬ", "ゅ"]

def get_merged_str():
    txt_list = glob.glob('static/*.txt')
    str = ""

    for txt in txt_list:
        file = open(txt, 'r', encoding='shift_jis')
        str += file.read()

    return str


def generate_character_list(ms: str):
    five_character_length = 0
    five_character = ""
    five_character_list = []

    seven_character_length = 0
    seven_character = ""
    seven_character_list = []

    for token in t.tokenize(ms):
        if not token.reading == "*":
            # if not any(x in token.surface for x in ignore_tokens) and not len(token.reading) == 1:
            if not len(token.reading) == 1:
                five_character_length += len(token.reading)
                five_character += token.surface

                seven_character_length += len(token.reading)
                seven_character += token.surface

        if five_character_length == 5:
            five_character_list.append(five_character)

        if five_character_length >= 5:
            five_character = ""
            five_character_length = 0

        if seven_character_length == 7:
            seven_character_list.append(seven_character)

        if seven_character_length >= 7:
            seven_character = ""
            seven_character_length = 0

    five_character_list = list(set(five_character_list))
    seven_character_list = list(set(seven_character_list))

    return [five_character_list, seven_character_list]


def generate_haiku(cl: list):
    print(random.choice(cl[0]))
    print(random.choice(cl[1]))
    print(random.choice(cl[0]))


if __name__ == '__main__':
    merged_str = get_merged_str()
    character_list = generate_character_list(merged_str)
    generate_haiku(character_list)
