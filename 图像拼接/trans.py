from PIL import Image
from tqdm import *


def transfer(infile, outfile):
    im = Image.open(infile)
    reim = im.resize((128, 128))  # 宽*高
    reim.save(outfile, dpi=(128.0, 128.0))  ##200.0,200.0分别为想要设定的dpi值


if __name__ == '__main__':
    for i in trange(1, 37):
        name = 'tyrol-e' + str(i) + '.jpg'
        infil = 'AerialImageDataset/test/jpg/' + name
        outfile = "AerialImageDataset/test/trans_jpg/" + name
        transfer(infil, outfile)

# city = ['bloomington', 'innsbruck', 'sfo', 'tyrol-e']