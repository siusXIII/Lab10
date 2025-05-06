from dataclasses import dataclass
from model.country import Country


@dataclass
class Arco:
    state1ab: Country
    state2ab: Country