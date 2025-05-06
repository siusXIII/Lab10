from dataclasses import dataclass


@dataclass
class Country:
    StateAbb: str
    CCode: int
    StateNme: str

    def __hash__(self):
        return hash(self.StateAbb)

    def __eq__(self, other):
        return self.StateAbb == other.StateAbb
