def draw_stick_figure(strikes):
    
    stages = [
        # Default hang pole
        """
        ________
        |      |
        |      
        |      
        |      
        |      
        |
        |________
        """,
        # Head stage (1 strike)
        """
        ________
        |      |
        |      O
        |      
        |      
        |      
        |
        |________
        """,
        # Body stage (2 strikes)
        """
        ________
        |      |
        |      O
        |      |
        |      |
        |      
        |
        |________
        """,
        # One arm stage (3 strikes)
        """
        ________
        |      |
        |      O
        |     /|
        |      |
        |      
        |
        |________
        """,
        # Both arms stage (4 strikes)
        """
        ________
        |      |
        |      O
        |     /|\\
        |      |
        |      
        |
        |________
        """,
        # One leg stage (5 strikes)
        """
        ________
        |      |
        |      O
        |     /|\\
        |      |
        |     /
        |
        |________
        """,
        # Both legs stage (6 strikes)
        """
        ________
        |      |
        |      O
        |     /|\\
        |      |
        |     / \\
        |
        |________
        """
    ]
    print(stages[strikes])

QWERTY = """
    Q W E R T Y U I O P
    A S D F G H J K L
    Z X C V B N M
    """


color_str=[
            '\033[92m',
            '\033[91m',
            '\033[0m'
        ]