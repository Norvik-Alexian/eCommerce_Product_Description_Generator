import re

ENGINE = 'text-davinci-002'
MAX_TOKENS = 80
TOP_P = 1.
FREQUENCY_PENALTY = 1.
PRESENCE_PENALTY = 1.
ENDING_PUNCTUATION = [',', '!']
REMOVE_EXTRA_SPACE_PATTERN = re.compile(r'\s+')
HIGHLIGHT_PROMPT = '''
Generate Highlights from Product Description using bullet points:
Product Description: The all-seeing eye of fashion knows all. Rock its omniscience in your favorite summer outfits and wear this edgy piece with dark wash denim and chunky sneakers. Its unisex design makes it the perfect T-shirt dress too if that's the look you're going for. Don't forget your strappy heels.
Highlights:
* Material: Cotton.
* Loose and comfy.
* Light and breathable.
* Unique illustration.
* Print won't lose colors.
'''