import tkinter as tk
from tkinter import messagebox
import random


class GameCharacter:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 50
        self.level = 1
        self.xp = 0
        self.potions = 3

    def attack(self, enemy):
        damage = random.randint(10, 20) + self.level * 2
        enemy.health -= damage
        return f"{self.name} attacks for {damage} damage!"

    def fire_spell(self, enemy):

        if self.mana < 15:
            return "Not enough mana!"

        self.mana -= 15

        damage = random.randint(25, 45)

        enemy.health -= damage

        return f"🔥 Fire Blast deals {damage} damage!"

    def heal(self):

        if self.potions <= 0:
            return "No potions left!"

        self.potions -= 1

        amount = random.randint(30, 50)

        self.health = min(100, self.health + amount)

        return f"❤️ Healed {amount} HP!"

    def gain_xp(self):

        self.xp += 50

        if self.xp >= 100:
            self.level += 1
            self.xp = 0
            self.health = 100
            self.mana = 50

            return f"⭐ Level up! Level {self.level}"

        return ""


class Enemy:

    def __init__(self, level):

        names = [
            "Goblin",
            "Skeleton",
            "Orc",
            "Dark Knight",
            "Dragon"
        ]

        self.name = random.choice(names)

        self.health = 50 + level * 30

        self.damage = 10 + level * 5


    def attack(self, player):

        damage = random.randint(
            self.damage - 5,
            self.damage + 5
        )

        player.health -= damage

        return f"{self.name} hits you for {damage} damage!"



class RPGGame:


    def __init__(self, root):

        self.root = root

        root.title("⚔️ Endless RPG")

        root.geometry("600x500")


        self.player = GameCharacter("Hero")

        self.enemy = Enemy(
            self.player.level
        )


        # Title

        self.title = tk.Label(
            root,
            text="⚔️ ENDLESS RPG ⚔️",
            font=("Arial", 22)
        )

        self.title.pack(pady=10)


        # Player Panel

        self.player_box = tk.LabelFrame(
            root,
            text="Player",
            padx=20,
            pady=10
        )

        self.player_box.pack(
            side="left",
            padx=20
        )


        self.player_text = tk.Label(
            self.player_box,
            font=("Arial",12)
        )

        self.player_text.pack()


        # Enemy Panel

        self.enemy_box = tk.LabelFrame(
            root,
            text="Enemy",
            padx=20,
            pady=10
        )

        self.enemy_box.pack(
            side="right",
            padx=20
        )


        self.enemy_text = tk.Label(
            self.enemy_box,
            font=("Arial",12)
        )

        self.enemy_text.pack()



        # Log

        self.log = tk.Label(
            root,
            text="A battle begins!",
            wraplength=500
        )

        self.log.pack(
            pady=20
        )



        # Buttons

        self.buttons = tk.Frame(root)

        self.buttons.pack()


        tk.Button(
            self.buttons,
            text="⚔️ Attack",
            width=15,
            command=self.attack
        ).grid(row=0,column=0,padx=5)


        tk.Button(
            self.buttons,
            text="🔥 Spell",
            width=15,
            command=self.spell
        ).grid(row=0,column=1,padx=5)


        tk.Button(
            self.buttons,
            text="❤️ Heal",
            width=15,
            command=self.heal
        ).grid(row=0,column=2,padx=5)


        tk.Button(
            root,
            text="Quit",
            command=root.destroy
        ).pack(pady=20)


        self.update()



    def update(self):

        self.player_text.config(
            text=
            f"""
Name: {self.player.name}

Level: {self.player.level}

❤️ Health:
{self.player.health}/100

🔵 Mana:
{self.player.mana}/50

⭐ XP:
{self.player.xp}/100

Potions:
{self.player.potions}
"""
        )


        self.enemy_text.config(
            text=
            f"""
{self.enemy.name}

❤️ Health:
{max(self.enemy.health,0)}
"""
        )



    def enemy_turn(self):

        if self.enemy.health > 0:

            msg = self.enemy.attack(
                self.player
            )

            self.log.config(
                text=msg
            )



    def check_battle(self):

        if self.enemy.health <= 0:

            bonus = self.player.gain_xp()

            self.log.config(
                text=
                f"🏆 You defeated {self.enemy.name}\n"
                f"{bonus}"
            )

            self.enemy = Enemy(
                self.player.level
            )


        if self.player.health <= 0:

            messagebox.showinfo(
                "Game Over",
                "You died!"
            )

            self.root.destroy()


    def attack(self):

        msg = self.player.attack(
            self.enemy
        )

        self.log.config(
            text=msg
        )

        self.enemy_turn()

        self.check_battle()

        self.update()



    def spell(self):

        msg = self.player.fire_spell(
            self.enemy
        )

        self.log.config(
            text=msg
        )

        self.enemy_turn()

        self.check_battle()

        self.update()



    def heal(self):

        msg = self.player.heal()

        self.log.config(
            text=msg
        )

        self.enemy_turn()

        self.update()



# Start game

window = tk.Tk()

game = RPGGame(window)

window.mainloop()
