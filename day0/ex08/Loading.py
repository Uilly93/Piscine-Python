from time import sleep
import os

# def ft_tqdm() -> None:
# 	yeild


def count_up_to(max):
    count = 0
    while count <= max:
        yield count
        count += 1


# Utilisation du générateur
# def ft_tqdm(range: range):
	# pps = 
counter = count_up_to(100)
# print (os.get_terminal_size())

loading: str = ''
for number in counter:
	# print("Each one, before")
	loading += '█'
	print(f"loading {number}%: {loading}", end='\r')
	sleep(0.4)
print(f"loading {number}%: {loading} finished")
