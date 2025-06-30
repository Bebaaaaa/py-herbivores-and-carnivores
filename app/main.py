class Animal:
    alive = []  # type: list

    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @classmethod
    def __str__(cls) -> str:
        return str([repr(animal) for animal in cls.alive])


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target) -> None:
        if not isinstance(target, Herbivore):
            return
        if target.hidden:
            return

        target.health -= 50
        if target.health <= 0:
            target.health = 0
            if target in Animal.alive:
                Animal.alive.remove(target)
