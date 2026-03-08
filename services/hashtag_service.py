import random

def generate_hashtags(mood):

    hashtags = {

        "happy and energetic": [
            "#happy","#goodvibes","#smile","#joy","#positive",
            "#happiness","#energy","#brightday","#fun","#livelife",
            "#cheerful","#optimism","#goodmood","#positivity",
            "#vibes","#happymoments","#sunshine","#lifestyle",
            "#feelinggood","#dailyjoy"
        ],

        "calm and neutral": [
            "#calm","#peace","#mindful","#serenity","#relax",
            "#quiet","#balanced","#stillness","#peaceful",
            "#slowmoments","#innerpeace","#tranquil","#gentle",
            "#rest","#calmvibes","#peacefullife","#meditation",
            "#simplelife","#relaxed","#serenemind"
        ],

        "sad and reflective": [
            "#reflect","#deepthoughts","#emotions","#thoughtful",
            "#lifequotes","#innerthoughts","#selfreflection",
            "#growth","#feelings","#learning","#deepmind",
            "#soulsearching","#wisdom","#understanding",
            "#quietmind","#thoughtprocess","#selfgrowth",
            "#deepfeelings","#reflectiontime","#lifejourney"
        ],

        "excited and adventurous": [
            "#adventure","#explore","#travel","#journey","#thrill",
            "#wanderlust","#newexperience","#exploration",
            "#discover","#travelvibes","#excited","#wildspirit",
            "#lifeadventure","#outdoors","#exploring",
            "#travelgram","#roadtrip","#discovermore",
            "#traveladdict","#adventuretime"
        ]

    }

    if mood in hashtags:

        selected = random.sample(hashtags[mood], 6)

        return " ".join(selected)

    return "#life #moments #daily"