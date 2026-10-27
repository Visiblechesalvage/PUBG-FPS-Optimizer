from dataclasses import dataclass


@dataclass
class Core:
    rcyneg: int = 795
    ypimlo: int = 168
    brdwvf: int = 979
    zrbtc: int = 741

    def total(self):
        return self.rcyneg + self.ypimlo + self.brdwvf + self.zrbtc


if __name__ == "__main__":
    x = Core()
    print(x.total())
