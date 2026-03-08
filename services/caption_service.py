import random

# -------- CAPTION DATABASE --------

captions = {

    "happy and energetic": [
        "Smiles, sunshine, and unstoppable energy today!",
        "Good vibes only today!",
        "Happiness is in the air!",
        "Energy high and mood higher!",
        "Smiling through every moment!",
        "Living today with pure joy!",
        "Sunshine mixed with a little happiness.",
        "Today's mood: bright and energetic!",
        "Feeling amazing and unstoppable!",
        "Just enjoying the happy moments!",
        "Positivity everywhere today!",
        "Smiles that never fade.",
        "A day full of good energy.",
        "Let the happiness flow!",
        "Today feels amazing!",
        "Energy and positivity all around!",
        "Joy in every step today!",
        "Bright day, brighter mood!",
        "Feeling the good vibes!",
        "Just loving life today!"
    ],

    "calm and neutral": [
        "Peaceful moments make the best memories.",
        "Just breathing and enjoying the silence.",
        "Calm mind, calm life.",
        "Taking life slow and steady.",
        "Peace is the real luxury.",
        "A quiet moment of clarity.",
        "Finding beauty in simplicity.",
        "Relaxing and recharging today.",
        "Calm vibes only.",
        "Let the mind rest today.",
        "Serenity in every moment.",
        "Stillness is powerful.",
        "Slow days are the best days.",
        "Balanced and peaceful today.",
        "Just enjoying the quiet moments.",
        "Simple moments matter most.",
        "Peaceful thoughts today.",
        "Finding calm in chaos.",
        "A gentle and peaceful day.",
        "Tranquility feels good."
    ],

    "sad and reflective": [
        "Some days are meant for reflection.",
        "Quiet thoughts and deeper feelings.",
        "Every emotion has its story.",
        "Learning through every feeling.",
        "Taking time to understand life.",
        "Sometimes silence says everything.",
        "Growth comes from reflection.",
        "A thoughtful moment today.",
        "Emotions shape who we become.",
        "Even sad moments teach us.",
        "Looking inward today.",
        "Understanding life one thought at a time.",
        "Deep thoughts and calm reflections.",
        "Life lessons everywhere.",
        "Every feeling has meaning.",
        "Listening to my thoughts today.",
        "Moments of reflection.",
        "Thinking about life's journey.",
        "Sometimes slow days help us grow.",
        "Every day teaches something new."
    ],

    "excited and adventurous": [
        "Adventure mode activated!",
        "Exploring new possibilities today!",
        "Life begins outside the comfort zone.",
        "Every day is a new adventure.",
        "Ready for the next journey!",
        "Excitement in every step.",
        "Let the adventure begin!",
        "Chasing dreams and experiences.",
        "Energy for the next big adventure!",
        "Life is meant to be explored.",
        "Thrill in every moment!",
        "Adventure never stops.",
        "New roads, new memories.",
        "Exploring life with excitement.",
        "Every moment is an adventure.",
        "Time to discover something new.",
        "Excited for what comes next!",
        "Adventure fuels the soul.",
        "Stepping into something amazing.",
        "Life is a journey worth exploring."
    ]

}


# -------- MAIN FUNCTION --------

def generate_caption(mood):

    if mood in captions:
        return random.choice(captions[mood])

    return "Living the moment."