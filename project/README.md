    # New World Adventure
    #### Video Demo:  https://www.youtube.com/watch?v=CpGGPY7mZ_4
    #### Description:

    New World Adventure is an engaging text-based game where players navigate through a thrilling adventure, making critical decisions every step of the way.

    Classes
    The project begins by defining two fundamental classes:

    Character
    The Character class represents every entity encountered in the game, from menacing monsters to friendly NPCs and the player's own character. It encompasses essential attributes such as health, mana, and strength. Notably, the max_health attribute ensures that a player's health remains within reasonable bounds, preventing it from exceeding the maximum limit when using healing potions. Additionally, a class method facilitates the input of the player's character name, ensuring it is not left empty.

    Item
    In the Item class, players can find vital statistics for various in-game items. Items are categorized into two types: weapons and potions. The class provides distinct class methods for each item type. For weapons, the method tracks durability and calls the destroy() function when it reaches zero. Conversely, the potion method utilizes the potion's attack attribute as a healing percentage, subsequently invoking the destroy() method, as potions are single-use items.

    Main Functionality
    Central to the game's mechanics is the management of the player's inventory, facilitated by the inventory variable. The show_item() function displays the items available to the player. Additionally, the clear_terminal() function ensures a clutter-free terminal window, enhancing the player's experience by preventing overwhelming dialogue lines.

    The game's introduction is embellished with stylish text displays, courtesy of the figlet library. Furthermore, a 2-second delay following the player's welcome message allows players to absorb the initial atmosphere without interruptions.

    The storyline unfolds seamlessly from the story.txt file, providing an easily expandable platform for future additions. Essential variables such as list and lin_nbr streamline the storytelling process, preventing duplicate dialogue lines.

    Interactions and Combat
    The choices.csv file contains a plethora of choices for players to make throughout their adventure. Each choice corresponds to an action executed using eval(), ensuring a dynamic and immersive narrative experience.

    Combat encounters are handled within the fight() function. Players are prompted to utilize items from their inventory strategically. Should a player's health points drop to zero, the game ends with a "Game Over" message. Conversely, victory rewards players with gold and restores their health.
