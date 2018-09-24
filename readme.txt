■ ♦ · ♣ · ♥ · ♠ · ♦ · ♣ · ♥ · ♠ · ♦ · ♣ · ♥ · ♠ ■
♠ _______ _           __    _           __      ♠
· \ ♠___ \ |          \ |  (_)          \ |     ·
♥  |♥|_/ / | __ _  ___| | ___  __ _  ___| | __  ♥
·  |♣___ \ |/ _` |/ __/ |/ / |/ _` |/ __/ |/ /  · 
♣  |♦|_/ / | (_| | (__|   <| | (_| | (__|   <   ♣
· /_____/|_|\__,_\\___\_|\_\ |\__,_\\___\_|\_\  ·
♦ \______________________ _/ |_______________/  ♦      
·                        /__/                   ·
■ ♦ · ♣ · ♥ · ♠ · ♦ · ♣ · ♥ · ♠ · ♦ · ♣ · ♥ · ♠ ■
by Jonathan Fox


Prerequisites:
• Python installed


How to Run:

• With Python:
    1. Double-click jfox-terminal-blackjack.zip
    2. Double-click blackjack.py

• With Terminal:
    1. Unzip jfox-terminal-blackjack.zip.
    2. cd to jfox-terminal-blackjack 
    3. Run this command: python ./blackjack.py

• Respond to most prompts in game with yes(or y) or no(or n)
• Game can be exited at any time with exit(or e) or quit(or q)


Design decisions:
• Python:
    - I chose to use Python because it's the most simple to use in 
    console. The more straightforward, the better!

• Card and Deck Classes:
    - The Card class allows for individual Card instances with a 
    specific rank and suit.
    - A Deck instance is initialized with an array holding all 52 
    distinct Cards. Cards are drawn at random and removed from the 
    array when drawn.

• Rank and Suit:
    - Enums for Rank and Suit guarantee that a card's Rank and Suit 
    will be valid. It also makes it convenient to iterate through 
    them.
    - Dictionaries for rank value, rank string, and suit string allow 
    for O(1) lookup time.
    - Rank.LOWACE: The deck does not initialize a card with this rank. 
    LowAce is only used when counting points in the player's or 
    dealer's cards. In Blackjack, an Ace's value can be either 1 or 
    11, depending on whether or not an 11 will push the total points 
    over 21. When calculating points, if the total points are over 21, 
    an Ace(value 11) is changed to a LowAce(value 1) and the points 
    are recalculated.

• Player Responses:
    - Player responses that are interpreted as yes, no, or exit are in 
    dictionaries, which allow for O(1) lookup time. There aren't very 
    many possible responses so this isn't a huge optimization, but if 
    more responses were added it could be more significant.

• Game Loop:
    - The core of the game can be repeated an arbitrary amount of 
    times. Because of that, it's an infinite while(True) loop, which 
    pauses for player input and breaks when necessary.

• Dialogue:
    - I added some very short pauses in the game (about 0.5 seconds 
    each) after certain actions in order to give the feeling of an 
    actual game being played, which is quite different to the robotic, 
    lightning-fast responses of a normal program. It's not my program 
    lagging, I swear!! (If you'd like to see the game without it, 
    change the value of "pauseOn" in blackjack.py to False)
    - I made the dealer a character who talks to you and asks for 
    your name, just to add some color to the game. His name is George 
    and he enjoys a good book.


Hope you enjoyed it!!


Acknowledgements:
• Very cool ASCII title art mostly obtained from 
http://patorjk.com/software/taag/