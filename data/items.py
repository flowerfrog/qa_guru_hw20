import dataclasses


@dataclasses.dataclass
class Item:
    name: str
    qty: int
    price: str
    total_price: str
