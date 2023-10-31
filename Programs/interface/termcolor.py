#first install termcolor by running pip install termcolor 
from termcolor import colored
text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
