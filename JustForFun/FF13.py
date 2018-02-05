#! python3

import random

pulse = ['パルス', 'ファルシ', 'ルシ', 'パージ', 'コクーン']

shuffle = random.sample(pulse, 5)

print('{0}の{1}の{2}が{3}で{4}'.format(*shuffle))
