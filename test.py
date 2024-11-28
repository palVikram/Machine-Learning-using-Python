# Construct the prompt
prompt = f"""
You are a gaming expert with extensive knowledge of games, their mechanics, vocabulary, and culture. For the game "{game_name}," answer the following question comprehensively. Your response should include at least 50 words and provide all important details, examples, and relevant context.

Question: {question_with_game}

- Be detailed and specific.
- Use examples from gameplay, player communication, or scenarios.
- Explain any terminology or phrases in the context of the game.
- If relevant, include how cultural, regional, or genre-specific factors may influence the answer.
"""

game_questions = [
    # Basic Information About the Game
    "What is [Game Name] about, and what is its main objective?",
    "Provide an overview of [Game Name], its genre, storyline, and primary objectives.",
    "What are the key features of [Game Name]?",
    "List the main features of [Game Name], such as game modes, gameplay mechanics, and special abilities.",
    "What is the target audience for [Game Name]?",
    "Who is the primary audience for [Game Name]? Include age group, skill level, and interests.",

    # In-Game Scenarios and Plays
    "What are the common in-game scenarios players encounter in [Game Name]?",
    "Describe common gameplay scenarios in [Game Name], such as missions, quests, or challenges players face.",
    "What are the different roles or playstyles available in [Game Name]?",
    "What roles or playstyles can players adopt in [Game Name]? Provide examples of how these roles affect gameplay.",
    "What strategies or tactics are commonly used in [Game Name]?",
    "Explain the common strategies and tactics players use to succeed in [Game Name]. Include examples for both beginners and advanced players.",

    # Gaming Currency and Economy
    "What in-game currencies are used in [Game Name], and what can they be spent on?",
    "What currencies are available in [Game Name]? Explain their purpose and how players can earn or use them.",
    "How does the game's economy function in [Game Name]?",
    "Describe the in-game economy of [Game Name], including trading systems, marketplaces, and player-to-player transactions.",
    "Are there any microtransactions or premium items in [Game Name]?",
    "What microtransactions or premium content are available in [Game Name]? Include details about their cost and how they enhance gameplay.",

    # Game Lore and Story
    "What is the backstory or lore of [Game Name]?",
    "Provide a detailed summary of the backstory or lore of [Game Name]. Include major events, characters, and factions.",
    "Who are the main characters or factions in [Game Name]?",
    "List and describe the main characters or factions in [Game Name]. Include their roles in the story or gameplay.",

    # Game Environment and Map
    "What are the main areas or maps in [Game Name]?",
    "Describe the primary areas, maps, or worlds in [Game Name]. Highlight their unique features and importance to gameplay.",
    "Are there any special environmental challenges in [Game Name]?",
    "What environmental challenges do players face in [Game Name]? Provide examples such as hazards, puzzles, or weather effects.",

    # Multiplayer and Social Aspects
    "How does the multiplayer aspect work in [Game Name]?",
    "Explain the multiplayer features of [Game Name], including co-op modes, competitive modes, and matchmaking systems.",
    "Are there guilds, clans, or player alliances in [Game Name]?",
    "What social or cooperative elements are present in [Game Name]? Include details about guilds, clans, or alliances.",
    "How do players communicate in [Game Name]?",
    "What communication options are available in [Game Name]? Include chat, voice, and any in-game emotes or signals.",

    # Rewards and Achievements
    "What rewards or achievements can players earn in [Game Name]?",
    "List the types of rewards and achievements available in [Game Name]. Include examples and how players can unlock them.",
    "Are there progression systems in [Game Name]?",
    "Explain the progression systems in [Game Name], such as leveling up, unlocking skills, or earning ranks.",

    # Challenges and Obstacles
    "What are the common challenges players face in [Game Name]?",
    "Describe the common challenges and obstacles in [Game Name], including enemies, puzzles, and time-based tasks.",
    "How do players overcome these challenges in [Game Name]?",
    "What tools, strategies, or resources can players use to overcome challenges in [Game Name]?",

    # Customization and Player Freedom
    "What customization options are available for players in [Game Name]?",
    "What customization options are available in [Game Name]? Include details about character appearance, weapons, and abilities.",
    "Can players create or modify content in [Game Name]?",
    "Does [Game Name] allow players to create or modify content? Include details about map editors, modding, or user-generated content.",

    # Unique Features and Differentiators
    "What makes [Game Name] unique compared to others in its genre?",
    "What features or mechanics make [Game Name] stand out from other games in the same genre?",
    "Are there any cultural or regional influences in the game design of [Game Name]?",
    "Describe any cultural or regional influences reflected in [Game Name]'s design, story, or mechanics.",

    # General Trivia and Miscellaneous
    "What are some fun or lesser-known facts about [Game Name]?",
    "List interesting or lesser-known facts about [Game Name], including Easter eggs or developer insights.",
    "What player behaviors or trends are popular in [Game Name]?",
    "What trends or behaviors are common among players in [Game Name]? Include examples like speed runs, role-playing, or specific gameplay challenges."
]


game_moderation_questions = [
    # 1. Toxic Behavior and Harassment
    "What forms of toxic behavior are most common in [Game Name]?",
    "How does trash talk differ from harassment in [Game Name]?",
    "What are some examples of phrases or behaviors that constitute bullying in [Game Name]?",
    "How can context determine whether a phrase is playful banter or toxic communication in [Game Name]?",

    # 2. Hate Speech and Discrimination
    "What types of hate speech are most commonly observed in [Game Name]?",
    "How can the system identify and flag discriminatory language specific to [Game Name]'s cultural or regional player base?",
    "What are some examples of region-specific hate speech or slurs in [Game Name]?",

    # 3. Child Protection and Age-Appropriate Content
    "What are examples of inappropriate conversations or content targeting younger players in [Game Name]?",
    "How does [Game Name] handle interactions between adult players and children?",
    "What safeguards should be in place to prevent predatory behavior in [Game Name]?",

    # 4. Violent and Threatening Language
    "How can violent language be distinguished from in-game communication in [Game Name]?",
    "What phrases or behaviors in [Game Name] might indicate real-world threats?",
    "How does the tone of violent-sounding phrases affect their interpretation in [Game Name]?",

    # 5. Cheating and Exploits
    "What language or behavior in [Game Name] might indicate cheating or exploiting the game mechanics?",
    "How do players typically discuss or share cheats and exploits in [Game Name]?",
    "What patterns of communication could signal organized cheating in [Game Name]?",

    # 6. Cultural Sensitivities
    "What cultural or regional sensitivities are important to consider for players in [Game Name]?",
    "How does language or slang vary across regions in [Game Name]?",
    "What phrases or terms in [Game Name] are offensive in certain cultures but benign in others?",

    # 7. Spam and Advertising
    "What types of spam messages are common in [Game Name] (e.g., bot messages, fake giveaways)?",
    "How can the system differentiate between spam and legitimate messages in [Game Name]?",
    "What are examples of harmful links or advertisements in [Game Name]?",

    # 8. Gameplay-Specific Communication
    "What in-game phrases or communication patterns in [Game Name] are critical for gameplay but may be misinterpreted by a content moderation system?",
    "How does player communication change during high-stakes moments in [Game Name]?",
    "What are examples of strategy discussions that could be mistaken for toxic behavior in [Game Name]?",

    # 9. Mental Health and Emotional Support
    "How can the system identify language in [Game Name] that indicates self-harm or mental distress?",
    "What are examples of supportive versus dismissive language in [Game Name]?",
    "How should the system handle sensitive conversations about mental health in [Game Name]?",

    # 10. Inappropriate Content Sharing
    "What are examples of inappropriate images, videos, or links shared in [Game Name]?",
    "How can the system identify and prevent the sharing of explicit or harmful media in [Game Name]?",
    "What language or patterns in [Game Name] suggest the sharing of inappropriate content?",

    # 11. Emerging Trends and Language Evolution
    "How has the player language in [Game Name] evolved over time?",
    "What new slang or terms are emerging in [Game Name], and how might they impact content moderation?",
    "How can the system adapt to rapidly evolving in-game language in [Game Name]?",

    # 12. Player Conflicts and Resolution
    "What are examples of conflicts between players in [Game Name] that do not escalate to toxicity?",
    "How does conflict resolution language differ from inflammatory language in [Game Name]?",
    "How can the system identify and support healthy discussions in [Game Name]?",

    # 13. Language Specific to In-Game Roles
    "What role-specific language is commonly used in [Game Name] (e.g., tank, healer, sniper)?",
    "How does communication vary between roles in [Game Name]?",
    "What role-specific terms could be mistaken for toxic behavior in [Game Name]?",

    # 14. Streamer and Influencer Interactions
    "How do player interactions with streamers differ from regular player interactions in [Game Name]?",
    "What are examples of trolling or harassment targeted at streamers in [Game Name]?",
    "How should the system handle messages aimed at popular influencers in [Game Name]?",

    # 15. False Positives and Appeals
    "What are examples of phrases in [Game Name] that might be incorrectly flagged as toxic?",
    "How can the system handle appeals for flagged messages in [Game Name]?",
    "What safeguards can prevent false positives in [Game Name]?"
]

game_moderation_scenarios = [
    # 1. In-Game Events and Seasonal Updates
    "How do seasonal events or updates in [Game Name] impact in-game communication?",
    "What new terms or phrases emerge during special events in [Game Name]?",
    
    # 2. Role of Game Lore and Narrative
    "How does the lore or story of [Game Name] influence player communication and interactions?",
    "What are examples of lore-based phrases or terms in [Game Name] that could be misinterpreted?",
    
    # 3. Competitive and Esports Terminology
    "What competitive or esports-related terms are commonly used in [Game Name]?",
    "How does the meta-game (strategies) influence in-game communication in [Game Name]?",
    
    # 4. Collaborative Gameplay and Team Dynamics
    "How does team communication in [Game Name] differ during collaborative versus competitive gameplay?",
    "What phrases or commands are essential for team coordination in [Game Name]?",
    
    # 5. Cross-Platform and Cross-Game Interactions
    "What are examples of cross-game references or terms that players commonly use in [Game Name]?",
    "How does cross-platform play in [Game Name] influence communication styles and terms?",
    
    # 6. Memes and Pop Culture References
    "What memes or pop culture references are common in the [Game Name] community?",
    "How do memes influence player communication in [Game Name]?",
    
    # 7. In-Game Economy and Virtual Goods
    "What terms are commonly used in [Game Name] to discuss trading, crafting, or acquiring virtual goods?",
    "How do discussions about in-game economy differ from real-world economic terms in [Game Name]?",
    
    # 8. Clan, Guild, and Social Group Dynamics
    "How do guilds or clans in [Game Name] influence player communication styles?",
    "What are common phrases or terms used in social group settings within [Game Name]?",
    
    # 9. Real-Time Situational Communication
    "What are examples of shorthand communication used during high-pressure moments in [Game Name]?",
    "How does situational context (e.g., an ongoing raid or match) influence the meaning of player messages in [Game Name]?",
    
    # 10. Role of Humor and Sarcasm
    "How can the system identify humorous or sarcastic comments in [Game Name]?",
    "What are examples of playful banter versus harmful language in [Game Name]?",
    
    # 11. Language Evolution and Player-Created Terms
    "What are examples of player-created terms in [Game Name], and how do they evolve over time?",
    "How can the system adapt to the fast-changing vocabulary of players in [Game Name]?",
    
    # 12. Regional and Linguistic Variations
    "What are examples of regional or linguistic variations in communication within [Game Name]?",
    "How does multilingual communication affect in-game moderation in [Game Name]?",
    
    # 13. Streamer-Driven Language and Trends
    "How do streamers influence the language and trends used in [Game Name]?",
    "What are examples of phrases popularized by streamers in [Game Name]?",
    
    # 14. Player Frustrations and Venting
    "What are examples of non-toxic expressions of frustration in [Game Name]?",
    "How can the system differentiate between venting and genuinely harmful language in [Game Name]?",
    
    # 15. Role-Specific Challenges and Dynamics
    "What are examples of role-specific challenges and how players discuss them in [Game Name]?",
    "How do communication patterns vary between player roles in [Game Name]?"
]
