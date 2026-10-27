from dataclasses import dataclass


@dataclass
class Client:
    yybbatp: int = 29
    sagls: int = 632
    bfakg: int = 872

    def total(self):
        return self.yybbatp + self.sagls + self.bfakg


if __name__ == "__main__":
    x = Client()
    print(x.total())
