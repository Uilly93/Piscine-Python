from time import sleep
from tqdm import tqdm
# from Loading import ft_tqdm


packs = ["curl", "net", "ari", "ari1", "ar4"]


def install_pack(pack):
    pass
    # print("Installing pack", pack, sep=":")


    # for elem in ft_tqdm(range(333)):
    #     sleep(0.005)
    # print()
for pack in tqdm(range(333)):
    install_pack(pack)
    sleep(0.4)
# sleep(0.005)
# print()
