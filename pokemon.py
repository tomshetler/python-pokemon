class Pokemon:
    def __init__(self, name, type, health, attacks, trainer):
        self.name = name
        self.type = type
        self.health = health
        self.attacks = attacks
        self.trainer = trainer

    def attack(self, attack_method):
        if attack_method in self.attacks:
            damage = self.attacks[attack_method]
        return damage

    def display_stats(self):
        print("Name: {}".format(self.name))
        print("Type: {}".format(self.type))
        print("Health: {}".format(self.health))
        print("Trainer: {}".format(self.trainer.name))
        for attack_num in self.attacks:
            for attack, damage in self.attacks[attack_num].items():
                print("{}: {}".format(attack, damage))