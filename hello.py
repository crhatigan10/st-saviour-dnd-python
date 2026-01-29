from flower import Flower

if __name__ == '__main__':
    tulip = Flower('Tulip', 6, True)
    print(tulip.bloom())

    daisy = Flower('Daisy', 8, False)
    print(daisy.bloom())