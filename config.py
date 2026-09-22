STAGES = ["opening_1895", "shimonoseki", "triple_intervention", "korean_empire",
          "russo_japanese_war", "portsmouth", "korea_japanese_rule",
          "qing_collapse", "russian_collapse", "siberian_intervention",
          "interwar", "mukden", "north_south", "sino_japanese_war",
          "khalkhin_gol", "pacific_war", "final_1945"]

STAGE_LABELS = {
    "opening_1895": ("1894", "Eve of the First Sino-Japanese War"),
    "shimonoseki": ("1895", "Treaty of Shimonoseki"),
    "triple_intervention": ("1895", "Intervention and the Korean Court"),
    "korean_empire": ("1897", "The Empire and the Port"),
    "russo_japanese_war": ("1904", "Russo-Japanese War"),
    "portsmouth": ("1905", "Portsmouth and the Protectorate"),
    "korea_japanese_rule": ("1910", "The Hague and Annexation"),
    "qing_collapse": ("1912", "Fall of the Qing"),
    "russian_collapse": ("1917", "Russian Revolution"),
    "siberian_intervention": ("1918", "Intervention in Siberia"),
    "interwar": ("1920s", "March First and the United Front"),
    "mukden": ("1931", "Mukden"),
    "north_south": ("1930s", "North and South"),
    "sino_japanese_war": ("1937", "Marco Polo Bridge"),
    "khalkhin_gol": ("1939", "Khalkhin Gol"),
    "pacific_war": ("1941", "The Pact and the Pacific"),
    "final_1945": ("1945", "The End of the War"),
}

STAGE_INDEX = {name: i for i, name in enumerate(STAGES)}

FACTION_ORDER = ["china", "taiwan", "japan", "korea", "russia", "west"]

PARTICIPANTS = {
    # The Qing world, seated together at the start.
    1: {"group": "china", "region": "mainland", "special": "emperor"},
    2: {"group": "china", "region": "mainland"},
    3: {"group": "china", "region": "mainland"},
    4: {"group": "china", "region": "mainland"},
    # Taiwanese. Part of the China bloc until Shimonoseki, then their own.
    5: {"group": "china", "region": "taiwan"},
    6: {"group": "china", "region": "taiwan"},
    # Koreans. Their own court from the start, but seated with China
    # until independence in 1895.
    7: {"group": "korea"},
    8: {"group": "korea"},
    9: {"group": "japan"},
    10: {"group": "japan"},
    11: {"group": "japan"},
    12: {"group": "russia", "special": "tsar"},
    13: {"group": "russia"},
    14: {"group": "west"},
    15: {"group": "west"},
}

FACTION_COLORS = {
    "china":   ["#b3402f", "#d9764f"],
    "taiwan":  ["#2a9d8f", "#52b788"],
    "japan":   ["#bc002d", "#e07a5f"],
    "korea":   ["#3a6ea5", "#5f8cc0"],
    "russia":  ["#4a4e69", "#8e9aaf"],
    "west":    ["#6c584c", "#9c8461"],
}

TRANSITIONS = [
    {"id": "taiwan_transfer", "stage": "shimonoseki",
     "applies": lambda p: p.get("group") == "china" and p.get("region") == "taiwan",
     "title": "TAIWAN HAS BEEN CEDED TO JAPAN",
     "lines": ["Your political identity has changed.",
               "You may still vote when asked.",
               "Your vote does not control Japanese state policy."]},
    {"id": "korea_independence", "stage": "shimonoseki",
     "applies": lambda p: p.get("group") == "korea",
     "title": "KOREA IS NOW FORMALLY INDEPENDENT",
     "lines": ["Your group may now make its own state decisions."]},
    {"id": "korea_japanese_rule", "stage": "korea_japanese_rule",
     "applies": lambda p: p.get("group") == "korea",
     "title": "KOREA HAS LOST CONTROL OF STATE POLICY",
     "lines": ["You may still express a preference.",
               "Your vote no longer determines official policy."]},
    {"id": "qing_collapse", "stage": "qing_collapse",
     "applies": lambda p: p.get("group") == "china" and p.get("region") == "mainland",
     "title": "THE QING DYNASTY HAS FALLEN",
     "lines": ["You may now vote."]},
    {"id": "russian_collapse", "stage": "russian_collapse",
     "applies": lambda p: p.get("group") == "russia",
     "title": "THE TSAR HAS FALLEN",
     "lines": ["You may now vote."]},
    {"id": "korea_exile", "stage": "interwar",
     "applies": lambda p: p.get("group") == "korea",
     "title": "A KOREAN GOVERNMENT-IN-EXILE HAS BEEN FORMED",
     "lines": ["Exiles in Shanghai have proclaimed a provisional republic.",
               "It speaks for Korea abroad. It governs nothing at home.",
               "Your vote remains advisory."]},
]

ROUNDS = {
    "1894_korea": {
        "stage": "opening_1895", "title": "1894: Korea",
        "questions": {
            "china": {
                "question": "Japan is landing troops in Korea, your tributary. What should the Qing court do?",
                "options": {"A": "Withdraw and negotiate joint oversight",
                            "B": "Reinforce Korea and hold Qing suzerainty",
                            "C": "Strike Japan's forces first"}},
            "japan": {
                "question": "Qing troops are in Korea and your fleet is ready. What should Japan do?",
                "options": {"A": "Press for reform in Seoul and avoid war",
                            "B": "Force the Qing out of Korea by arms",
                            "C": "Wait and see where the Western powers stand"}},
            "russia": {
                "question": "China and Japan are about to fight over Korea. What should the Tsar do?",
                "options": {"A": "Stay out and let them exhaust each other",
                            "B": "Warn both of them off Korea",
                            "C": "Move troops toward the Korean frontier now"}},
            "west": {
                "question": "War is coming over Korea. What should the powers do?",
                "options": {"A": "Stay neutral and guard the treaty ports",
                            "B": "Mediate between the Qing and Japan",
                            "C": "Back Japan as a check on Russia, and say nothing"}}}},
    "1895_shimonoseki": {
        "stage": "shimonoseki", "title": "1895: Terms of Peace",
        "questions": {
            "japan": {
                "question": "What should Japan demand from the defeated Qing?",
                "options": {"A": "An indemnity and Korean independence only",
                            "B": "Also take Taiwan",
                            "C": "Take Taiwan and the Liaodong Peninsula"}},
            "china": {
                "question": "Japan's terms are on the table at Shimonoseki. What should the court do?",
                "options": {"A": "Sign whatever is demanded and end the war",
                            "B": "Refuse the territorial clauses and fight on",
                            "C": "Stall, and beg the powers to intervene"}},
            "taiwan": {
                "question": "The Qing have ceded Taiwan to Japan. What should the island do?",
                "options": {"A": "Accept Japanese rule",
                            "B": "Proclaim the Republic of Formosa and resist",
                            "C": "Wage guerrilla war without a republic"}},
            "korea": {
                "question": "The treaty has made you independent on paper. What should the court do with it?",
                "options": {"A": "Sign reform treaties with Japan and modernise fast",
                            "B": "Court Russia as a counterweight",
                            "C": "Declare strict neutrality and take nothing from anyone"}},
            "russia": {
                "question": "Japan is dictating terms. What should the Tsar do while there is still time?",
                "options": {"A": "Wait and see what Japan actually takes",
                            "B": "Sound out France and Germany about joint pressure",
                            "C": "Warn Japan off the mainland alone"}},
            "west": {
                "question": "Japan's terms are published. What should the powers do?",
                "options": {"A": "Accept them and protect your trade",
                            "B": "Join Russia's pressure on Japan",
                            "C": "Stand aside and let Japan keep its gains"}}}},
    "1895_triple": {
        "stage": "triple_intervention", "title": "1895: Intervention and the Korean Court",
        "questions": {
            "russia": {
                "question": "Japan has taken Liaodong. What should the Tsar do?",
                "options": {"A": "Accept Japan's gains",
                            "B": "Lead the powers in forcing Japan to return Liaodong",
                            "C": "Demand Japan give up all its mainland gains"}},
            "korea": {
                "question": "The queen is dead and the king is guarded by Japanese soldiers. What should the court do?",
                "options": {"A": "Work with Japan and keep what authority is left",
                            "B": "Get the king to the Russian legation",
                            "C": "Denounce Japan openly and call the country to arms"}},
            "japan": {
                "question": "Three powers demand you hand back Liaodong. What should Japan do?",
                "options": {"A": "Hand it back and say nothing",
                            "B": "Hand it back and start building for the next war",
                            "C": "Refuse, and fight whoever comes"}},
            "china": {
                "question": "The powers are pressing Japan to soften the treaty. What should the court do?",
                "options": {"A": "Thank them and ask for nothing more",
                            "B": "Seek a formal alliance with Russia",
                            "C": "Use the breathing space to rebuild the army"}},
            "taiwan": {
                "question": "The Republic of Formosa has fallen. What now?",
                "options": {"A": "Keep resisting from the mountains",
                            "B": "Surrender and accept the new order",
                            "C": "Flee across the strait to the mainland"}},
            "west": {
                "question": "Russia is rallying the powers against Japan's gains. What should you do?",
                "options": {"A": "Join the intervention",
                            "B": "Stand aside",
                            "C": "Take a concession of your own while China is weak"}}}},
    "1897_empire_and_port": {
        "stage": "korean_empire", "title": "1897: The Empire and the Port",
        "questions": {
            "korea": {
                "question": "Russia and Japan both circle the peninsula. How should Korea hold its sovereignty?",
                "options": {"A": "Stay the Joseon kingdom and provoke no one",
                            "B": "Proclaim the Korean Empire and modernise at speed",
                            "C": "Take Russian protection, whatever it costs in standing"}},
            "russia": {
                "question": "China is weak and Port Arthur never freezes. What should Russia do?",
                "options": {"A": "Respect China's sovereignty over Liaodong",
                            "B": "Lease Port Arthur and run the railway deeper into Manchuria",
                            "C": "Split Manchuria into spheres with Japan"}},
            "japan": {
                "question": "Russia is taking the very peninsula it forced you to give up. What should Japan do?",
                "options": {"A": "Protest, and accept it",
                            "B": "Build the fleet, and take it back later",
                            "C": "Seize a port of your own in China now"}},
            "china": {
                "question": "The powers are taking leases up and down your coast. What should the court do?",
                "options": {"A": "Grant the leases and keep the peace",
                            "B": "Refuse, and let them take them by force",
                            "C": "Play the powers against each other for better terms"}},
            "taiwan": {
                "question": "The grace period for leaving the island runs out this year.",
                "options": {"A": "Sell up and sail for Fujian",
                            "B": "Stay, and register as a subject of Japan",
                            "C": "Stay, and register nothing"}},
            "west": {
                "question": "Russia has Port Arthur and the scramble for concessions is on.",
                "options": {"A": "Take a leased port of your own",
                            "B": "Insist on an open door and equal trade for all",
                            "C": "Guarantee China's integrity and stop the scramble"}}}},
    "1904_manchuria": {
        "stage": "russo_japanese_war", "title": "1904: Russia in Manchuria",
        "questions": {
            "japan": {
                "question": "Russia will not leave Manchuria. How should Japan respond?",
                "options": {"A": "Negotiate a division of spheres",
                            "B": "Strike first at Port Arthur",
                            "C": "Accept Russian dominance in Manchuria"}},
            "russia": {
                "question": "Japan offers you Manchuria if Korea is theirs. What should Russia do?",
                "options": {"A": "Accept the exchange of spheres",
                            "B": "Stall the talks and reinforce the Far East",
                            "C": "Withdraw from Manchuria altogether"}},
            "korea": {
                "question": "Two empires are about to fight over your peninsula. What should the Emperor do?",
                "options": {"A": "Declare neutrality and hope it is respected",
                            "B": "Side with Japan and ask for guarantees",
                            "C": "Side with Russia"}},
            "china": {
                "question": "A foreign war is about to be fought on your territory. What should the court do?",
                "options": {"A": "Declare neutrality in your own Manchuria",
                            "B": "Side with Japan to get Manchuria back",
                            "C": "Side with Russia"}},
            "taiwan": {
                "question": "Dinner tonight?",
                "options": {"A": "Taro",
                            "B": "Mantou",
                            "C": "Rice — if the rationing office has any left"}},
            "west": {
                "question": "Russia and Japan are going to war. What should the powers do?",
                "options": {"A": "Stay neutral",
                            "B": "Lend Japan the money to fight",
                            "C": "Press both sides to settle before it starts"}}}},
    "1905_portsmouth": {
        "stage": "portsmouth", "title": "1905: Portsmouth and the Protectorate",
        "questions": {
            "russia": {
                "question": "The fleet is sunk and the cities are striking. What should the Tsar do?",
                "options": {"A": "Fight on until a victory can be claimed",
                            "B": "Make peace, and turn the army on the revolution",
                            "C": "Give up every Russian claim in East Asia"}},
            "korea": {
                "question": "Japanese soldiers are in the palace and the treaty must be signed tonight.",
                "options": {"A": "Sign, and keep what authority at home remains",
                            "B": "Refuse, and appeal to the powers",
                            "C": "Refuse in public and build a resistance in secret"}},
            "japan": {
                "question": "You have won, but the treasury is empty. What should Japan take at Portsmouth?",
                "options": {"A": "Korea and southern Manchuria, and peace now",
                            "B": "Hold out for a cash indemnity as well",
                            "C": "Break off talks and fight another year"}},
            "china": {
                "question": "The war on your soil is ending and you are not at the table.",
                "options": {"A": "Accept whatever the two of them agree",
                            "B": "Demand Manchuria back in full",
                            "C": "Reform the state at home and let the powers do as they like"}},
            "taiwan": {
                "question": "The island has been told to celebrate Japan's victory over Russia.",
                "options": {"A": "Hang the flag and walk in the lantern parade",
                            "B": "Hang the flag and stay indoors",
                            "C": "Hang nothing"}},
            "west": {
                "question": "Roosevelt is offering to mediate. What should the powers do?",
                "options": {"A": "Broker a peace that leaves both sides standing",
                            "B": "Back Japan's full demands",
                            "C": "Stay out of it"}}}},
    "1910_korea": {
        "stage": "korea_japanese_rule", "title": "1910: The Hague and Annexation",
        "questions": {
            "japan": {
                "question": "What should Japan do with its Korean protectorate?",
                "options": {"A": "Keep it a protectorate",
                            "B": "Annex Korea outright",
                            "C": "Withdraw and guarantee independence"}},
            "korea": {
                "question": "The powers are meeting at The Hague. What should the Emperor do?",
                "options": {"A": "Send secret envoys to put Korea's case",
                            "B": "Give Japan what it asks and protect the throne",
                            "C": "Ask Russia to intervene with troops"}},
            "china": {
                "question": "Korea is being swallowed and your own dynasty is shaking.",
                "options": {"A": "Protest, and do nothing else",
                            "B": "Accelerate constitutional reform at home",
                            "C": "Seek an alliance with Japan while you still can"}},
            "taiwan": {
                "question": "Colonial laws tighten. Your neighbours want to act.",
                "options": {"A": "Sign the petition for an elected assembly",
                            "B": "Join the march in Taipei",
                            "C": "Stay home and keep farming"}},
            "russia": {
                "question": "Japan is about to annex Korea. What should the Tsar do?",
                "options": {"A": "Object formally, and no more",
                            "B": "Trade recognition of Korea for a free hand in northern Manchuria",
                            "C": "Rebuild in the Far East and prepare for the next round"}},
            "west": {
                "question": "Japan is annexing Korea. What should the powers do?",
                "options": {"A": "Recognise it and say nothing",
                            "B": "Protest, without consequences",
                            "C": "Refuse recognition"}}}},
    "1912_republic": {
        "stage": "qing_collapse", "title": "1912: The Republic",
        "questions": {
            "china": {
                "question": "The dynasty is gone and the republic is days old. What should China do first?",
                "options": {"A": "Hand power to Yuan Shikai to hold the country together",
                            "B": "Build a parliament and hold elections, whatever the risk",
                            "C": "Let the provinces govern themselves for now"}},
            "japan": {
                "question": "China has collapsed into a shaky republic.",
                "options": {"A": "Support Yuan Shikai and collect the favours",
                            "B": "Fund the revolutionaries and keep China divided",
                            "C": "Stay out of it and trade"}},
            "russia": {
                "question": "The Qing collapse has left Mongolia and Manchuria loose.",
                "options": {"A": "Recognise the republic and keep your railways",
                            "B": "Detach Outer Mongolia under your protection",
                            "C": "Occupy northern Manchuria outright"}},
            "korea": {
                "question": "China's emperor has fallen. Yours fell two years ago.",
                "options": {"A": "Look to the Chinese republicans for help",
                            "B": "Build schools and newspapers instead",
                            "C": "Take up arms across the Yalu now"}},
            "taiwan": {
                "question": "The mainland is a republic. Nothing here has changed.",
                "options": {"A": "Cut your queue and dress as the Japanese do",
                            "B": "Keep the queue and keep quiet",
                            "C": "Cross the strait and join the revolution"}},
            "west": {
                "question": "China's new republic is fragile, and it owes you money.",
                "options": {"A": "Lend to Yuan Shikai to keep order",
                            "B": "Recognise the republic and demand nothing",
                            "C": "Withhold recognition until your concessions are guaranteed"}}}},
    "1917_revolution": {
        "stage": "russian_collapse", "title": "1917: The Tsar Falls",
        "questions": {
            "russia": {
                "question": "The Tsar is gone and the empire is coming apart. What should the revolution do in the Far East?",
                "options": {"A": "Hold the whole Far East, whatever it costs",
                            "B": "Trade territory for survival in the west",
                            "C": "Call on the workers of Asia to rise with you"}},
            "japan": {
                "question": "Russia is in chaos and its Far East is undefended.",
                "options": {"A": "Send troops into Siberia now",
                            "B": "Wait until the Allies ask you to",
                            "C": "Stay out, and secure Manchuria instead"}},
            "china": {
                "question": "Russia's revolution has thrown out new ideas along with the Tsar.",
                "options": {"A": "Take back the Russian concessions while you can",
                            "B": "Join the Allies and claim a seat at the peace",
                            "C": "Hold to the warlords' arrangements and change nothing"}},
            "korea": {
                "question": "Revolution in Russia. The exiles are arguing about what it means.",
                "options": {"A": "Look to the Bolsheviks for arms",
                            "B": "Look to America and its promises",
                            "C": "Build the movement at home and trust neither"}},
            "taiwan": {
                "question": "News of the revolution filters through the censors.",
                "options": {"A": "Pass the pamphlet on",
                            "B": "Burn it",
                            "C": "Write to the students in Tokyo about it"}},
            "west": {
                "question": "The Bolsheviks have taken Russia out of the war.",
                "options": {"A": "Send troops against them",
                            "B": "Recognise the new government and trade",
                            "C": "Contain them and wait for them to fall"}}}},
    "1918_siberia": {
        "stage": "siberian_intervention", "title": "1918: Siberia",
        "questions": {
            "russia": {
                "question": "Japanese and Allied troops have landed in the Far East. What should the Soviets do?",
                "options": {"A": "Come to terms with the intervening powers and buy time",
                            "B": "Arm the partisans and fight them out",
                            "C": "Give up Siberia until the war in the west is won"}},
            "japan": {
                "question": "Seventy thousand of your men are in Siberia, far more than the Allies agreed.",
                "options": {"A": "Withdraw when the Allies withdraw",
                            "B": "Stay, and build a buffer state in the Far East",
                            "C": "Push further west while Russia is broken"}},
            "china": {
                "question": "Foreign armies are moving through Manchuria again.",
                "options": {"A": "Send your own troops into Siberia alongside them",
                            "B": "Use the chaos to recover the Russian concessions",
                            "C": "Keep out of it entirely"}},
            "korea": {
                "question": "Korean fighters are forming units in Manchuria and Siberia.",
                "options": {"A": "Join them",
                            "B": "Send them money and stay home",
                            "C": "Organise at home and wait for the peace conference"}},
            "taiwan": {
                "question": "Taiwanese students in Tokyo are printing a journal about home rule.",
                "options": {"A": "Send them money",
                            "B": "Read it and pass it on",
                            "C": "Burn it before the police find it"}},
            "west": {
                "question": "Your troops are in Siberia with unclear orders.",
                "options": {"A": "Withdraw and leave Russia to itself",
                            "B": "Stay until the Bolsheviks fall",
                            "C": "Stay, and watch Japan rather than the Russians"}}}},
    "1924_united_front": {
        "stage": "interwar", "title": "1919-1924: March First and the United Front",
        "questions": {
            "russia": {
                "question": "China is broken into warlord fiefs. What should the USSR do?",
                "options": {"A": "Stay out of China's quarrels",
                            "B": "Broker an alliance between the Nationalists and the Communists",
                            "C": "Back the Chinese Communist Party alone"}},
            "korea": {
                "question": "Wilson has promised that peoples may choose their own governments. How should the movement act?",
                "options": {"A": "Declare independence and march, unarmed, in every town",
                            "B": "Wait for the Western powers to grant it",
                            "C": "Rise in arms now"}},
            "japan": {
                "question": "A peaceful declaration of independence has filled the streets in Korea.",
                "options": {"A": "Crush it, and make an example",
                            "B": "Crush it, then loosen the rules afterwards",
                            "C": "Concede an elected assembly in Seoul"}},
            "china": {
                "question": "Versailles has handed Germany's holdings in Shandong to Japan.",
                "options": {"A": "Sign the treaty and take what else is offered",
                            "B": "Refuse to sign, and let the students march",
                            "C": "Turn to Moscow for help against the warlords"}},
            "taiwan": {
                "question": "The petition for a Taiwanese parliament is collecting names again.",
                "options": {"A": "Sign it",
                            "B": "Sign it, and speak at the meeting",
                            "C": "Stay off the list"}},
            "west": {
                "question": "You are writing the postwar settlement.",
                "options": {"A": "Give Shandong to Japan and keep the alliance",
                            "B": "Return Shandong to China",
                            "C": "Apply self-determination to the colonies as well"}}}},
    "1931_manchuria": {
        "stage": "mukden", "title": "1931: Manchuria",
        "questions": {
            "japan": {
                "question": "After the Mukden incident, what should Japan do?",
                "options": {"A": "Limit the response",
                            "B": "Expand the occupation",
                            "C": "Take full control of Manchuria"}},
            "china": {
                "question": "Your northeast is being taken while your armies fight the Communists.",
                "options": {"A": "Fight the Japanese now",
                            "B": "Take it to the League of Nations and do not fight",
                            "C": "Settle with Japan and finish the Communists first"}},
            "russia": {
                "question": "Japan is now sitting on your Far Eastern frontier.",
                "options": {"A": "Sell Japan your Manchurian railway and step back",
                            "B": "Reinforce Siberia and hold the line",
                            "C": "Arm the resistance inside Manchuria"}},
            "korea": {
                "question": "Japan's army has marched past your border into Manchuria.",
                "options": {"A": "Join the guerrillas across the Yalu",
                            "B": "Organise quietly at home",
                            "C": "Petition the League of Nations"}},
            "taiwan": {
                "question": "Dinner, again?",
                "options": {"A": "Taro",
                            "B": "Sweet potato",
                            "C": "Whatever is left after the army takes the rice"}},
            "west": {
                "question": "The League has been asked to judge Japan.",
                "options": {"A": "Condemn Japan and impose sanctions",
                            "B": "Condemn Japan and impose nothing",
                            "C": "Recognise Manchukuo and keep trading"}}}},
    "1930s_north_south": {
        "stage": "north_south", "title": "1930s: North and South",
        "questions": {
            "china": {
                "question": "Japanese puppets in the north, Communists in the hills, your government in the south.",
                "options": {"A": "Destroy the Communists first, then face Japan",
                            "B": "Make a united front with the Communists against Japan",
                            "C": "Buy time with Tokyo and build the army"}},
            "japan": {
                "question": "You hold Taiwan, Korea and Manchuria. How much further?",
                "options": {"A": "Digest what you have and stop",
                            "B": "Detach north China without fighting for it",
                            "C": "Prepare for a full war in China"}},
            "korea": {
                "question": "Assimilation tightens: your language, your shrines, your names.",
                "options": {"A": "Comply in public and keep Korea at home",
                            "B": "Refuse, and take what follows",
                            "C": "Comply fully and claim the rights you were promised"}},
            "taiwan": {
                "question": "Tokyo is 'imperialising' the colonies.",
                "options": {"A": "Take a Japanese name and pray at the shrine",
                            "B": "Refuse, and keep your ancestors' tablets",
                            "C": "Speak only Japanese at home"}},
            "russia": {
                "question": "Japan probes your borders while Germany arms in the west.",
                "options": {"A": "Strengthen Siberia and avoid provocation",
                            "B": "Back Chiang Kai-shek against Japan",
                            "C": "Back Mao's Communists instead"}},
            "west": {
                "question": "Depression at home, aggression abroad.",
                "options": {"A": "Rearm, and draw a line in Asia",
                            "B": "Appease, and keep trading",
                            "C": "Withdraw from Asia and defend Europe only"}}}},
    "1937_china": {
        "stage": "sino_japanese_war", "title": "1937: Marco Polo Bridge",
        "questions": {
            "china": {
                "question": "How should the Nationalist government respond?",
                "options": {"A": "Negotiate a local settlement",
                            "B": "Full national resistance",
                            "C": "Cede the north, hold the south"}},
            "japan": {
                "question": "A skirmish near Beijing has become a war.",
                "options": {"A": "Settle it locally and pull back",
                            "B": "Take the north China plain and stop there",
                            "C": "Force China to surrender outright"}},
            "russia": {
                "question": "Every Japanese division in China is one that is not on your border.",
                "options": {"A": "Stay strictly neutral",
                            "B": "Send aircraft, weapons and volunteer pilots in secret",
                            "C": "Declare war on Japan now"}},
            "korea": {
                "question": "The rice you grew is loaded for Japan while your village goes short.",
                "options": {"A": "Hide part of the harvest",
                            "B": "Report the shortfall and take the ration",
                            "C": "Sabotage the loading"}},
            "taiwan": {
                "question": "Recruiters have come for military labourers to serve in China.",
                "options": {"A": "Volunteer, since the pay is real",
                            "B": "Let your name go forward if they ask",
                            "C": "Find work the recruiters will not touch"}},
            "west": {
                "question": "Japan has invaded China.",
                "options": {"A": "Embargo Japan now",
                            "B": "Condemn Japan and keep selling it oil and scrap",
                            "C": "Stay out, and protect your own concessions"}}}},
    "1939_khalkhin_gol": {
        "stage": "khalkhin_gol", "title": "1939: Khalkhin Gol",
        "questions": {
            "russia": {
                "question": "Japanese troops are probing the Mongolian border. How should the USSR answer?",
                "options": {"A": "Pull back and negotiate the border",
                            "B": "Counterattack in force and destroy them",
                            "C": "Take it to the League of Nations"}},
            "japan": {
                "question": "Your Kwantung Army is fighting the Soviets without Tokyo's orders. Where should the empire go?",
                "options": {"A": "North, against the Soviet Union",
                            "B": "South, for oil and rubber",
                            "C": "Neither. Finish China first"}},
            "china": {
                "question": "The war has settled into a stalemate and your government sits in Chongqing.",
                "options": {"A": "Hold, and wait for the world to join you",
                            "B": "Counterattack now, while Japan looks north",
                            "C": "Negotiate while you still have something to trade"}},
            "korea": {
                "question": "The labour office has a quota for the mines in Kyushu, and your village has a number to fill.",
                "options": {"A": "Put your name down and take the wage",
                            "B": "Disappear into the hills for the season",
                            "C": "Pay someone else to go"}},
            "taiwan": {
                "question": "The sugar quota has risen again, and the army sets the price.",
                "options": {"A": "Meet the quota",
                            "B": "Under-report the crop",
                            "C": "Sell what you can on the black market"}},
            "west": {
                "question": "War has broken out in Europe.",
                "options": {"A": "Hold the line in Asia as well",
                            "B": "Concentrate everything on Europe",
                            "C": "Buy Japan off with concessions in China"}}}},
    "1941_pacific": {
        "stage": "pacific_war", "title": "1941: The Pact and the Pacific",
        "questions": {
            "japan": {
                "question": "Faced with the oil embargo, what should Japan do?",
                "options": {"A": "Withdraw from China",
                            "B": "Strike south only",
                            "C": "Attack the United States"}},
            "russia": {
                "question": "Germany is massing in the west. What should the USSR do about Japan?",
                "options": {"A": "Sign a neutrality pact with Tokyo",
                            "B": "Join China in open war against Japan",
                            "C": "Demand Japan leave Manchuria before anything is signed"}},
            "china": {
                "question": "Moscow has signed with Tokyo, and America has embargoed Japan.",
                "options": {"A": "Hold on and wait for America",
                            "B": "Sue for peace while Japan will still talk",
                            "C": "Attack now, before Japan turns south"}},
            "korea": {
                "question": "Moscow has signed with Tokyo. No great power is coming for Korea.",
                "options": {"A": "Join the exiles in Chongqing",
                            "B": "Join the partisans on the Manchurian border",
                            "C": "Endure, and wait"}},
            "taiwan": {
                "question": "The war is total now.",
                "options": {"A": "Donate your kitchen pots to the war effort",
                            "B": "Volunteer for labour service",
                            "C": "Eat taro and keep your head down"}},
            "west": {
                "question": "Japan has taken southern Indochina.",
                "options": {"A": "Embargo oil and force the issue",
                            "B": "Keep talking, and keep the oil flowing",
                            "C": "Offer Japan a free hand in China in exchange for peace"}}}},
    "1945_ussr": {
        "stage": "final_1945", "title": "1945: The End of the War",
        "questions": {
            "russia": {
                "question": "With Germany defeated, what should the USSR do in Asia?",
                "options": {"A": "Honour the neutrality pact",
                            "B": "Invade Manchuria",
                            "C": "Invade Manchuria and Hokkaido"}},
            "japan": {
                "question": "The cities burn and the Allies demand unconditional surrender.",
                "options": {"A": "Surrender now, on any terms",
                            "B": "Surrender only if the Emperor is kept",
                            "C": "Fight on for a negotiated peace"}},
            "china": {
                "question": "Japan is finished. Who governs China?",
                "options": {"A": "A coalition with the Communists",
                            "B": "Take the Japanese surrender first, and everywhere",
                            "C": "Civil war now, while your armies are still armed"}},
            "korea": {
                "question": "The empire is collapsing. What should Koreans do first?",
                "options": {"A": "Raise the forbidden flag",
                            "B": "Form committees to govern before the powers arrive",
                            "C": "Wait to see what the Soviets and Americans allow"}},
            "taiwan": {
                "question": "The war is over. First meal as free people?",
                "options": {"A": "Taro",
                            "B": "Mantou",
                            "C": "Rice — finally"}},
            "west": {
                "question": "The war is ending. What shape should postwar Asia take?",
                "options": {"A": "Occupy Japan alone and keep the Soviets out",
                            "B": "Divide Korea with the Soviets at the 38th parallel",
                            "C": "Hand the colonies back to their prewar owners"}}}},
}

BRIEFINGS = {
    "opening_1895": {
        "china": [
            "You are the Qing court, and Korea is your tributary. Japan has landed troops there on the pretext of putting down a rebellion.",
            "Decide: withdraw, reinforce to hold your suzerainty, or strike first.",
        ],
        "taiwan": [
            "You live on Taiwan, a frontier province of the Qing Empire.",
            "War is coming to the waters around you. No one in Beijing asks what islanders think.",
        ],
        "japan": [
            "You lead a modernised Japan that has waited decades for this moment.",
            "War with the Qing over Korea is at hand. Your army and navy are ready.",
        ],
        "korea": [
            "You serve the Joseon court, long a Qing tributary.",
            "Japanese and Chinese soldiers are on your soil, fighting over your future. You cannot stop either of them.",
        ],
        "russia": [
            "You serve the Tsar, whose empire is pushing into Manchuria and Korea.",
            "A war between China and Japan may weaken both. That could open doors for you.",
        ],
        "west": [
            "You represent the Western powers, with treaty ports and trade in China.",
            "A Sino-Japanese war could reshape the whole region. Watch who wins, and what they demand.",
        ],
    },
    "shimonoseki": {
        "china": [
            "Your armies and fleet are shattered, and Japan dictates the terms at Shimonoseki.",
            "Li Hongzhang is in the room with a bullet wound in his cheek and nothing left to bargain with.",
        ],
        "taiwan": [
            "The Qing have ceded Taiwan to Japan, but the island is not going quietly.",
            "Local leaders want to proclaim a Republic of Formosa and resist the handover.",
            "Decide: accept Japanese rule, join the republic, or fight on without one.",
        ],
        "japan": [
            "You have won the war decisively.",
            "As the victor at Shimonoseki, decide what to demand from the beaten Qing: money, recognition of Korean independence, and perhaps territory.",
        ],
        "korea": [
            "The treaty strips away every Qing claim over Korea.",
            "You are independent on paper, and surrounded by Japanese influence.",
            "For the first time, the court's decisions are its own.",
        ],
        "russia": [
            "Japan's victory alarms you.",
            "If Japan takes territory on the mainland, it blocks your own designs on Manchuria and a warm-water port.",
        ],
        "west": [
            "Japan's victory surprised you.",
            "Now consider its peace terms. Some of your fellow powers are already discussing whether to intervene.",
        ],
    },
    "triple_intervention": {
        "china": [
            "You are grateful for any relief.",
            "Russia, France and Germany are pressing Japan to soften the treaty, though they act for their own interests, not yours.",
        ],
        "taiwan": [
            "The powers argue over Liaodong, but no one argues over Taiwan.",
            "Japanese troops have crushed the young Republic of Formosa.",
            "Decide what remains: fight on, surrender, or flee across the strait.",
        ],
        "japan": [
            "Your victory is being challenged. Russia, France and Germany demand you return the Liaodong Peninsula.",
            "You cannot fight all three. The humiliation will be remembered.",
            "In Seoul, meanwhile, your minister has taken matters into his own hands.",
        ],
        "korea": [
            "Queen Min has been killed inside the palace by men in Japanese pay.",
            "The king is alive, guarded, and every order that leaves the court is read by a Japanese adviser.",
            "The Russian legation is a short walk away.",
        ],
        "russia": [
            "Japan's foothold at Liaodong blocks your designs on Manchuria and a warm-water port.",
            "The Tsar must decide: accept it, or lead France and Germany in forcing Japan to give it back.",
        ],
        "west": [
            "Russia is rallying the powers against Japan's gains.",
            "Your trade interests favour a strong Japan as a counterweight, but you will not fight to defend Liaodong.",
        ],
    },
    "korean_empire": {
        "china": [
            "You have no standing in Korea at all now.",
            "Meanwhile the powers are queuing at your coast for leased ports of their own.",
        ],
        "taiwan": [
            "The grace period for leaving the island expires this year.",
            "Stay, and you are a subject of Japan. Go, and you leave the graves behind.",
        ],
        "japan": [
            "Your position in Seoul has slipped since the murder.",
            "The king sheltered with the Russians, and Russia is now taking the very peninsula you were forced to give back.",
        ],
        "korea": [
            "The king has come home from a year inside the Russian legation.",
            "Foreign advisers sit in your treasury, and the court holds no rank the world recognises.",
            "Decide how Korea holds what sovereignty it has left.",
        ],
        "russia": [
            "China is weak, and Port Arthur is the warm-water harbour your empire has wanted for a century.",
            "Take it, and the Triple Intervention starts to look like self-interest rather than rescue.",
        ],
        "west": [
            "Russia is helping itself to Liaodong, and the others are queuing behind it.",
            "Your governments would rather take a port than object to one.",
        ],
    },
    "russo_japanese_war": {
        "china": [
            "Two foreign powers are about to fight over Manchuria, which is yours.",
            "The court can only choose which way to look.",
        ],
        "taiwan": [
            "As subjects of Japan, you watch your new rulers go to war with Russia.",
            "Japanese victories are celebrated around you.",
        ],
        "japan": [
            "Russia will not leave Manchuria and threatens your position in Korea.",
            "You have offered to trade Manchuria for Korea. St Petersburg is stalling.",
        ],
        "korea": [
            "Russia and Japan are about to fight over who controls your peninsula.",
            "Whatever the outcome, your independence is fading.",
        ],
        "russia": [
            "Japan proposes a trade: Manchuria for you, Korea for them.",
            "The Tsar's ministers think Tokyo is bluffing and would never dare fight a European power.",
        ],
        "west": [
            "A war between Russia and Japan could reorder East Asia.",
            "Your banks and fleets are watching closely. A Japanese win would be a sensation.",
        ],
    },
    "portsmouth": {
        "china": [
            "The war fought on your soil is ending.",
            "You are not at the table where it ends.",
        ],
        "taiwan": [
            "The island has been told to celebrate Japan's victory over Russia.",
            "Lanterns, flags, and a day off the fields.",
        ],
        "japan": [
            "You have won, but the treasury is empty and the army is at its limit.",
            "Peace now, on good terms, may be worth more than another year of fighting.",
        ],
        "korea": [
            "Japan has beaten Russia, and the last power that might have balanced Tokyo is gone.",
            "Japanese soldiers are in the palace grounds, and a treaty is on the table tonight.",
        ],
        "russia": [
            "Mukden is lost and the Baltic Fleet lies at the bottom of the Tsushima Strait.",
            "Workers are striking in every city, and the throne is not safe.",
        ],
        "west": [
            "Roosevelt has offered to mediate.",
            "A settlement that leaves both sides standing suits you better than either of them winning outright.",
        ],
    },
    "korea_japanese_rule": {
        "china": [
            "Japan has beaten Russia and is tightening its grip on Korea.",
            "Your former tributary is being swallowed while your own dynasty teeters.",
        ],
        "taiwan": [
            "You have lived under Japanese rule for fifteen years.",
            "Now you watch Korea, next door, being drawn into the same empire.",
        ],
        "japan": [
            "Victory over Russia gave you a free hand, and Korea is a protectorate in all but name.",
            "Its emperor has just tried to appeal to the powers behind your back.",
        ],
        "korea": [
            "Japan holds your foreign affairs, your police and your army.",
            "The powers are meeting at The Hague to talk about law and peace.",
            "The protectorate treaty was signed under guns, and no one outside Korea knows it.",
        ],
        "russia": [
            "Defeated in Manchuria, your empire has withdrawn to lick its wounds.",
            "What you can still salvage is a free hand in the north.",
        ],
        "west": [
            "Japan's annexation of Korea proceeds with your quiet assent.",
            "You have colonies of your own, and protest would be awkward.",
        ],
    },
    "qing_collapse": {
        "china": [
            "The dynasty has fallen and a republic is proclaimed.",
            "You are no longer subjects but citizens. For the first time, your voice counts in the state.",
            "Yuan Shikai commands the only army that matters.",
        ],
        "taiwan": [
            "The mainland has become a republic, and nothing changes for you.",
            "You remain a subject of Tokyo, watching China's revolution from across the strait.",
        ],
        "japan": [
            "China's empire has collapsed into a shaky republic.",
            "Instability on the mainland is an opportunity, if you back the right man.",
        ],
        "korea": [
            "From inside the Japanese Empire, you hear of China's revolution.",
            "Some of your compatriots dream that Korea, too, might one day throw off foreign rule.",
        ],
        "russia": [
            "The Qing collapse leaves Mongolia and Manchuria exposed.",
            "Your empire moves quietly to secure its northern frontier.",
        ],
        "west": [
            "China's new republic looks fragile.",
            "Your concessions, railways and loans must be protected, whoever rules in Beijing.",
        ],
    },
    "russian_collapse": {
        "china": [
            "The Tsar's fall barely registers amid your own struggles.",
            "Russia's revolution sends new ideas into China, and they find young readers.",
        ],
        "taiwan": [
            "News of revolution in Russia filters through the Japanese censors.",
            "A few students take note.",
        ],
        "japan": [
            "The Tsar is gone and Russia is in chaos.",
            "Your generals see opportunity in Siberia, even as they fear what the revolution might spread.",
        ],
        "korea": [
            "Russia's revolution inspires the exiles.",
            "Socialism and nationalism begin to mix in the independence movement abroad.",
        ],
        "russia": [
            "The Tsar has fallen. You are revolutionaries building a Soviet state in the middle of a civil war.",
            "Your Far East is vulnerable, and your cause is new.",
        ],
        "west": [
            "Revolution in Russia terrifies your governments.",
            "The Bolsheviks have taken Russia out of the war against Germany.",
        ],
    },
    "siberian_intervention": {
        "china": [
            "Your republic is already breaking into warlord fiefs.",
            "Foreign armies are moving through Manchuria again, and nobody asks you.",
        ],
        "taiwan": [
            "Taiwanese students in Tokyo are writing about home rule.",
            "Their journal reaches the island by hand, a few copies at a time.",
        ],
        "japan": [
            "Seventy thousand of your troops are in Siberia, far more than the Allies agreed.",
            "Your generals see a buffer state. Your allies see a land grab.",
        ],
        "korea": [
            "Revolution in Russia, and a peace conference promised in Paris.",
            "For the first time since 1910, the exiles think the world might listen.",
        ],
        "russia": [
            "The revolution is surrounded. Japanese, American, British and French troops have landed in the Far East.",
            "They say they are guarding stores. They are propping up your enemies.",
        ],
        "west": [
            "Your troops are in Siberia with unclear orders and no appetite for a Russian war.",
            "Japan's contingent is several times the size that was agreed.",
        ],
    },
    "interwar": {
        "china": [
            "Versailles handed Germany's holdings in Shandong to Japan, and your students filled the streets.",
            "The republic is a map of warlord armies, and the Nationalists are looking abroad for help.",
        ],
        "taiwan": [
            "Life under Japan is orderly and second-class.",
            "Petitions for a Taiwanese parliament go to Tokyo year after year, and are refused politely.",
        ],
        "japan": [
            "You sit among the victors at Versailles with Shandong in hand.",
            "In Korea, a peaceful declaration of independence has brought your army onto the streets.",
        ],
        "korea": [
            "A generation has grown up under Japanese rule.",
            "Wilson has promised that peoples may choose their own governments.",
            "Students, pastors and elders are drafting a declaration of independence.",
        ],
        "russia": [
            "You have survived the civil war: isolated, feared, rebuilding.",
            "In China you see warlords, a weak republic, and a revolution waiting to be organised.",
        ],
        "west": [
            "You wrote the postwar settlement, and gave Shandong to Japan.",
            "Colonial petitions from Korea and elsewhere are filed and forgotten.",
        ],
    },
    "mukden": {
        "china": [
            "An explosion near Mukden has become a Japanese invasion of Manchuria.",
            "Your government is divided, exhausted and unprepared. Three northeastern provinces hang in the balance.",
        ],
        "taiwan": [
            "From Taiwan, you watch Japan seize Manchuria.",
            "The empire you live under is growing bolder, and the world is doing little.",
        ],
        "japan": [
            "Your Kwantung Army has staged an incident at Mukden and occupied Manchuria.",
            "The cabinet must decide whether to restrain the army or embrace the conquest.",
        ],
        "korea": [
            "Manchuria's fall brings Japan's armies to your northern border.",
            "Resistance abroad grows harder. The empire feels permanent.",
        ],
        "russia": [
            "Japan now sits on your Far Eastern frontier.",
            "You strengthen defences in Siberia, but you are in no shape for another war.",
        ],
        "west": [
            "The League of Nations protests, but your governments will not fight for Manchuria.",
            "Condemnation without action teaches a dangerous lesson.",
        ],
    },
    "north_south": {
        "china": [
            "The country remains split: a Nationalist government in the south, Japanese puppets in the north, Communists in the hills.",
            "Holding the nation together is your daily struggle.",
        ],
        "taiwan": [
            "Under Japan's 'imperial subject' policies you are pressed to adopt Japanese names, language and religion.",
            "Assimilation tightens as war spreads.",
        ],
        "japan": [
            "Your empire now includes Taiwan, Korea and Manchuria.",
            "The question is how to digest your gains, and how much further to push into China.",
        ],
        "korea": [
            "Japan rules Manchukuo on your northern border as well.",
            "Inside Korea, assimilation policies erase names and language. Resistance survives in exile.",
        ],
        "russia": [
            "You consolidate a Soviet Far East and watch Japan nervously.",
            "Border clashes test both sides while Germany arms in the west.",
        ],
        "west": [
            "Depression-era politics dominate.",
            "You recognise China's Nationalists but hedge everywhere. No one wants a new Asian war.",
        ],
    },
    "sino_japanese_war": {
        "china": [
            "Fighting has erupted at the Marco Polo Bridge. This time it may be full war.",
            "Your armies are outmatched, but surrender means dismemberment. The nation looks to you.",
        ],
        "taiwan": [
            "The empire calls on its subjects to support the war in China.",
            "Recruiters are already in the villages looking for military labourers.",
        ],
        "japan": [
            "A skirmish near Beijing has exploded into open war with China.",
            "Your generals promise a quick victory, but the country is vast.",
        ],
        "korea": [
            "Japan's war consumes Korea's rice, minerals and labour.",
            "Your homeland has become a supply base for a war against your neighbours.",
        ],
        "russia": [
            "China's war with Japan serves your interests. Every Japanese division tied down in China is one fewer on your border.",
            "The question is how much to send, and how openly.",
        ],
        "west": [
            "You condemn Japan's invasion but offer little concrete help to China.",
            "Your attention is fixed on rising dangers in Europe.",
        ],
    },
    "khalkhin_gol": {
        "china": [
            "Your war has ground into stalemate and your government sits in Chongqing.",
            "A Japanese defeat anywhere is worth hearing about.",
        ],
        "taiwan": [
            "The sugar quota has risen again.",
            "The army buys at a price it sets itself.",
        ],
        "japan": [
            "Your Kwantung Army is testing the Mongolian border without waiting for Tokyo.",
            "The argument between striking north and striking south is about to be settled for you.",
        ],
        "korea": [
            "The labour office has a quota for the mines in Kyushu.",
            "Your village has been given a number to fill.",
        ],
        "russia": [
            "Japanese troops are probing the Mongolian frontier you guarantee.",
            "Give ground and they will come again. Fight, and it could become a war in Asia while Germany arms in the west.",
        ],
        "west": [
            "A border war in Mongolia barely registers.",
            "Your governments are watching Prague and Warsaw.",
        ],
    },
    "pacific_war": {
        "china": [
            "Four years of war have bled your nation, and Moscow has just signed a pact with Tokyo.",
            "America's embargo may yet do what your armies could not.",
        ],
        "taiwan": [
            "The empire is at war with the whole Pacific.",
            "Taiwanese men serve in Japan's armies while American submarines close the seas around the island.",
        ],
        "japan": [
            "America's oil embargo is strangling your war machine.",
            "Your northern flank is secure. That leaves the south, and the American fleet at Pearl Harbor.",
        ],
        "korea": [
            "Japan's war deepens your hardship: labour conscription, resource extraction, repression.",
            "No great power has promised you anything.",
        ],
        "russia": [
            "You are fighting for survival against Germany.",
            "A pact with Tokyo would free your Siberian divisions, and leave China to fight alone.",
        ],
        "west": [
            "Japan has taken southern Indochina, and your colonies are next in line.",
            "The oil tap is the only weapon you have short of war.",
        ],
    },
    "final_1945": {
        "china": [
            "Japan is collapsing. After eight years of war, victory is near.",
            "So is the question of who controls China afterward: Nationalists or Communists.",
        ],
        "taiwan": [
            "Japanese rule is ending. Fifty years as a colony close.",
            "Soon you will be Chinese again, though what that will mean is unclear.",
        ],
        "japan": [
            "Cities burn, the fleet is sunk, and the Allies demand unconditional surrender.",
            "Your empire is finished. Only the terms of defeat remain.",
        ],
        "korea": [
            "Liberation is at hand, but Soviet troops enter from the north as Americans land in the south.",
            "Your freedom may arrive already divided.",
        ],
        "russia": [
            "Germany has surrendered.",
            "Your government must decide whether to honour the neutrality pact with Japan or invade Manchuria for territory, ports and influence.",
        ],
        "west": [
            "The war is ending. You plan the occupation of Japan and the shape of postwar Asia.",
            "You quietly worry about Soviet advances.",
        ],
    },
}
