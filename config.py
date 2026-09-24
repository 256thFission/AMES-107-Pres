STAGES = ["opening_1894", "shimonoseki", "triple_intervention", "korean_empire",
          "russo_japanese_war", "portsmouth", "korea_japanese_rule",
          "qing_collapse", "russian_collapse", "siberian_intervention",
          "interwar", "mukden", "north_south", "sino_japanese_war",
          "khalkhin_gol", "pacific_war", "final_1945"]

STAGE_LABELS = {
    "opening_1894": ("1894", "A Crisis in Korea"),
    "shimonoseki": ("1895", "Terms of Peace"),
    "triple_intervention": ("1895–96", "The Peace Is Challenged"),
    "korean_empire": ("1897–98", "An Empire and a Port"),
    "russo_japanese_war": ("1904", "Russia in Manchuria"),
    "portsmouth": ("1905", "Peace and a Protectorate"),
    "korea_japanese_rule": ("1907–10", "Can Sovereignty Be Defended?"),
    "qing_collapse": ("1912", "After the Dynasty"),
    "russian_collapse": ("1917", "After the Tsar"),
    "siberian_intervention": ("1918", "Intervention in Siberia"),
    "interwar": ("1919–24", "Self-Determination—for Whom?"),
    "mukden": ("1931", "The Mukden Crisis"),
    "north_south": ("1930s", "Expansion and Control"),
    "sino_japanese_war": ("1937", "Marco Polo Bridge"),
    "khalkhin_gol": ("1939", "The Northern Frontier"),
    "pacific_war": ("1941", "A Choice of Directions"),
    "final_1945": ("1945", "The End of the War"),
}

STAGE_INDEX = {name: i for i, name in enumerate(STAGES)}

FACTION_ORDER = ["china", "taiwan", "japan", "korea", "russia", "britain", "usa"]

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
    # One diplomat each: a lone voice deciding for an empire.
    14: {"group": "britain"},
    15: {"group": "usa"},
}

FACTION_COLORS = {
    "china":   ["#b3402f", "#d9764f"],
    "taiwan":  ["#2a9d8f", "#52b788"],
    "japan":   ["#bc002d", "#e07a5f"],
    "korea":   ["#3a6ea5", "#5f8cc0"],
    "russia":  ["#4a4e69", "#8e9aaf"],
    "britain": ["#6c584c", "#9c8461"],
    "usa":     ["#6a4c93", "#9d79bc"],
}

TRANSITIONS = [
    {"id": "taiwan_bargained", "stage": "shimonoseki",
     "applies": lambda p: p.get("group") == "china" and p.get("region") == "taiwan",
     "title": "TAIWAN IS ON THE TABLE AT SHIMONOSEKI",
     "lines": ["Japan is demanding the island. No one from Taiwan is in the room.",
               "You may still vote when asked.",
               "Your vote does not control state policy."]},
    {"id": "korea_independence", "stage": "shimonoseki",
     "applies": lambda p: p.get("group") == "korea",
     "title": "THE QING CAN NO LONGER SPEAK FOR KOREA",
     "lines": ["Your group may now make its own state decisions."]},
    {"id": "taiwan_transfer", "stage": "triple_intervention",
     "applies": lambda p: p.get("group") == "china" and p.get("region") == "taiwan",
     "title": "TAIWAN HAS BEEN CEDED TO JAPAN",
     "lines": ["Your political identity has changed.",
               "Your vote does not control Japanese state policy."]},
    {"id": "korea_japanese_rule", "stage": "qing_collapse",
     "applies": lambda p: p.get("group") == "korea",
     "title": "JAPAN HAS ANNEXED KOREA",
     "lines": ["You may still express a preference.",
               "Your vote no longer determines official policy."]},
    {"id": "qing_collapse", "stage": "qing_collapse",
     "applies": lambda p: p.get("group") == "china" and p.get("region") == "mainland",
     "title": "THE QING DYNASTY IS FINISHED",
     "lines": ["You may now vote."]},
    {"id": "russian_collapse", "stage": "russian_collapse",
     "applies": lambda p: p.get("group") == "russia",
     "title": "THE TSAR HAS FALLEN",
     "lines": ["You may now vote."]},
    {"id": "korea_exile", "stage": "mukden",
     "applies": lambda p: p.get("group") == "korea",
     "title": "A KOREAN GOVERNMENT-IN-EXILE HAS BEEN FORMED",
     "lines": ["Exiles in Shanghai have proclaimed a provisional republic.",
               "It speaks for Korea abroad. It governs nothing at home.",
               "Your vote remains advisory."]},
]

ROUNDS = {
    "1894_korea": {
        "stage": "opening_1894", "title": "1894: A Crisis in Korea",
        "questions": {
            "china": {
                "question": "Japan is landing troops in Korea, your tributary. What should the Qing court do?",
                "options": {"A": "Withdraw and negotiate joint oversight",
                            "B": "Reinforce Korea and hold Qing suzerainty",
                            "C": "Strike Japan's forces first"}},
            "japan": {
                "question": "China and Japan both have troops in Korea. What does Japan do?",
                "options": {"A": "Withdraw together and leave Korea to the Koreans",
                            "B": "Push the Qing out of Korea by force",
                            "C": "Wait and let the Western powers mediate"}},
            "russia": {
                "question": "China and Japan are about to fight over Korea. What should the Tsar do?",
                "options": {"A": "Stay out and let them exhaust each other",
                            "B": "Warn both of them off Korea",
                            "C": "Move troops toward the Korean frontier now"}},
            "britain": {
                "question": "Japan wants a new treaty ending your consular courts and treating it as an equal. War over Korea is days away.",
                "options": {"A": "Sign it, and treat Japan as a partner",
                            "B": "Delay until the war is decided",
                            "C": "Refuse, and keep your privileges"}},
            "usa": {
                "question": "China and Japan are about to fight over Korea. What should Washington do?",
                "options": {"A": "Stay strictly neutral",
                            "B": "Offer your good offices to both sides",
                            "C": "Lean toward Japan, the modernising power"}}}},
    "1895_shimonoseki": {
        "stage": "shimonoseki", "title": "1895: Terms of Peace",
        "questions": {
            "japan": {
                "question": "What should Japan demand from the defeated Qing?",
                "options": {"A": "Money and Korean independence only",
                            "B": "Also take Taiwan",
                            "C": "Take Taiwan and the Liaodong Peninsula"}},
            "china": {
                "question": "Japan's terms are on the table at Shimonoseki. What should the court do?",
                "options": {"A": "Sign whatever is demanded and end the war",
                            "B": "Refuse the territorial clauses and fight on",
                            "C": "Stall, and beg the powers to intervene"}},
            "taiwan": {
                "question": "Japan is demanding Taiwan at Shimonoseki. What should the island do if it is handed over?",
                "options": {"A": "Accept Japanese rule",
                            "B": "Proclaim the Republic of Formosa and resist",
                            "C": "Wage guerrilla war without a republic"}},
            "korea": {
                "question": "Japan is demanding that the Qing give up every claim to Korea. What should the court do with its new freedom?",
                "options": {"A": "Sign reform treaties with Japan and modernise fast",
                            "B": "Court Russia as a counterweight",
                            "C": "Declare strict neutrality and take nothing from anyone"}},
            "russia": {
                "question": "Japan is dictating terms. What should the Tsar do while there is still time?",
                "options": {"A": "Wait and see what Japan actually takes",
                            "B": "Sound out France and Germany about joint pressure",
                            "C": "Warn Japan off the mainland alone"}},
            "britain": {
                "question": "Japan's terms are published. What should Britain do?",
                "options": {"A": "Accept them: new ports opened to Japan are open to you too",
                            "B": "Join Russia's pressure on Japan",
                            "C": "Warn Japan privately to moderate its demands"}},
            "usa": {
                "question": "Your diplomats have carried the peace messages between Beijing and Tokyo. What now?",
                "options": {"A": "Carry messages and nothing more",
                            "B": "Press Japan to moderate its terms",
                            "C": "Welcome Japan's gains as progress"}}}},
    "1895_triple": {
        "stage": "triple_intervention", "title": "1895–96: The Peace Is Challenged",
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
                "question": "Russia is rallying France and Germany against your gains. What does Japan do if they demand Liaodong back?",
                "options": {"A": "Appeal to the other powers for support",
                            "B": "Give it back, and build up for next time",
                            "C": "Refuse, and risk war with all three"}},
            "china": {
                "question": "Russia is sounding out the powers about Japan's gains. What should the court do?",
                "options": {"A": "Thank them and ask for nothing more",
                            "B": "Seek a formal alliance with Russia",
                            "C": "Use the breathing space to rebuild the army"}},
            "taiwan": {
                "question": "The Republic of Formosa has fallen. What now?",
                "options": {"A": "Keep resisting from the mountains",
                            "B": "Surrender and accept the new order",
                            "C": "Flee across the strait to the mainland"}},
            "britain": {
                "question": "Russia, France and Germany ask you to join them against Japan. What should Britain do?",
                "options": {"A": "Join the intervention",
                            "B": "Refuse, and keep Japan friendly",
                            "C": "Refuse, and take a concession of your own"}},
            "usa": {
                "question": "Russia is rallying Europe against Japan's gains.",
                "options": {"A": "Stay out: this is Europe's game",
                            "B": "Protest European meddling in Asia",
                            "C": "Offer to arbitrate"}}}},
    "1897_empire_and_port": {
        "stage": "korean_empire", "title": "1897–98: An Empire and a Port",
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
                "question": "Russian warships have anchored at Port Arthur, the harbour you were made to give back. What does Japan do?",
                "options": {"A": "Grab a port of your own in China",
                            "B": "Accept it for now, and keep building the fleet",
                            "C": "Look for a Western ally against Russia"}},
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
            "britain": {
                "question": "Germany has seized Jiaozhou, and Russian warships are at Port Arthur. What should Britain do?",
                "options": {"A": "Lease Weihaiwei to watch Port Arthur",
                            "B": "Demand an open door and no leases for anyone",
                            "C": "Take the land behind Kowloon instead"}},
            "usa": {
                "question": "War with Spain may leave the Philippines in your hands. What then?",
                "options": {"A": "Keep the Philippines as a colony",
                            "B": "Free them and stay out of Asia",
                            "C": "Keep them, and demand equal trade in China for all"}}}},
    "1904_manchuria": {
        "stage": "russo_japanese_war", "title": "1904: Russia in Manchuria",
        "questions": {
            "japan": {
                "question": "Russia will not leave Manchuria. What does Japan do?",
                "options": {"A": "Keep negotiating: Manchuria for Russia, Korea for Japan",
                            "B": "Strike Russia first",
                            "C": "Accept Russian power in the region"}},
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
            "britain": {
                "question": "Your ally Japan is about to go to war with Russia. What should Britain do?",
                "options": {"A": "Hold to the alliance: stay neutral, and keep France out",
                            "B": "Restrain Japan before it drags you in",
                            "C": "Tell Japan it is on its own"}},
            "usa": {
                "question": "Japan wants loans to fight Russia.",
                "options": {"A": "Stay neutral",
                            "B": "Let American bankers fund Japan's war",
                            "C": "Press both sides to settle"}}}},
    "1905_portsmouth": {
        "stage": "portsmouth", "title": "1905: Peace and a Protectorate",
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
                "question": "You have won, but the treasury is empty. What should Japan take at the peace?",
                "options": {"A": "Control of Korea and southern Manchuria, and peace now",
                            "B": "Hold out for a large cash payment as well",
                            "C": "Keep fighting for more"}},
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
            "britain": {
                "question": "Japan has won, and your alliance is up for renewal.",
                "options": {"A": "Renew it: Japan gets Korea, you get help defending India",
                            "B": "Renew it, but leave Korea out",
                            "C": "Let it lapse; Japan is strong enough now"}},
            "usa": {
                "question": "Roosevelt is offering to mediate. What should the US do?",
                "options": {"A": "Broker a peace that leaves both sides standing",
                            "B": "Mediate, and quietly accept Japan in Korea for safety in the Philippines",
                            "C": "Stay out of it"}}}},
    "1910_korea": {
        "stage": "korea_japanese_rule", "title": "1907–10: Can Sovereignty Be Defended?",
        "questions": {
            "japan": {
                "question": "Korea is already your protectorate. What happens next?",
                "options": {"A": "Keep ruling indirectly, through Korean officials",
                            "B": "Annex Korea as a colony",
                            "C": "Loosen control and let Korea govern itself"}},
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
                "question": "The colonial government is building railways and schools, and policing every village.",
                "options": {"A": "Send your children to the Japanese school",
                            "B": "Keep them at the old Chinese academy",
                            "C": "Join the armed rising in the hills"}},
            "russia": {
                "question": "Japan is about to annex Korea. What should the Tsar do?",
                "options": {"A": "Object formally, and no more",
                            "B": "Trade recognition of Korea for a free hand in northern Manchuria",
                            "C": "Rebuild in the Far East and prepare for the next round"}},
            "britain": {
                "question": "Korean envoys have come to The Hague, and your ally is preparing to annex Korea.",
                "options": {"A": "Turn the envoys away and accept annexation",
                            "B": "Hear their case",
                            "C": "Accept annexation, but protect your trade in Korea"}},
            "usa": {
                "question": "Korea reminds you of the 'good offices' you promised in the 1882 treaty.",
                "options": {"A": "Honour it: take Korea's case to the powers",
                            "B": "Treat Korea as having no foreign policy now",
                            "C": "Protest quietly"}}}},
    "1912_republic": {
        "stage": "qing_collapse", "title": "1912: After the Dynasty",
        "questions": {
            "china": {
                "question": "The revolt has spread and the dynasty cannot survive it. Who should govern the republic?",
                "options": {"A": "Hand power to Yuan Shikai to hold the country together",
                            "B": "Build a parliament and hold elections, whatever the risk",
                            "C": "Let the provinces govern themselves for now"}},
            "japan": {
                "question": "China's last dynasty has fallen. What does Japan want from the new China?",
                "options": {"A": "Back the strongman in Beijing and collect favours",
                            "B": "Back the revolutionaries and a new, modern China",
                            "C": "Keep China weak and divided"}},
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
            "britain": {
                "question": "China's new republic needs money, and your banks lead the lenders.",
                "options": {"A": "Lend to Yuan Shikai to keep order",
                            "B": "Recognise the republic and lend nothing",
                            "C": "Lend, but take control of the salt tax as security"}},
            "usa": {
                "question": "The banks want Washington's backing for a loan to Yuan Shikai.",
                "options": {"A": "Back the banks and stay in the consortium",
                            "B": "Pull out: the terms insult China's sovereignty",
                            "C": "Recognise the republic first, alone"}}}},
    "1917_revolution": {
        "stage": "russian_collapse", "title": "1917: After the Tsar",
        "questions": {
            "russia": {
                "question": "The Tsar is gone and the empire is coming apart. What should the revolution do in the Far East?",
                "options": {"A": "Hold the whole Far East, whatever it costs",
                            "B": "Trade territory for survival in the west",
                            "C": "Call on the workers of Asia to rise with you"}},
            "japan": {
                "question": "Revolution has broken Russia apart. What does Japan do?",
                "options": {"A": "Send troops into Siberia now, alone",
                            "B": "Wait and act with the Allies",
                            "C": "Stay out, and strengthen your hold in China instead"}},
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
            "britain": {
                "question": "You need Japan's navy in the Mediterranean, and Japan wants Germany's holdings in Shandong.",
                "options": {"A": "Promise Shandong to Japan in secret",
                            "B": "Refuse, and leave it to the peace conference",
                            "C": "Promise it, and tell China"}},
            "usa": {
                "question": "You have entered the war. Japan wants you to recognise its 'special interests' in China.",
                "options": {"A": "Recognise them to keep Japan in the war",
                            "B": "Refuse, and insist on the Open Door",
                            "C": "Sign something vague that each side can read its own way"}}}},
    "1918_siberia": {
        "stage": "siberian_intervention", "title": "1918: Intervention in Siberia",
        "questions": {
            "russia": {
                "question": "The Allies are preparing to land troops in your Far East. What should the Soviets do?",
                "options": {"A": "Come to terms with the intervening powers and buy time",
                            "B": "Arm the partisans and fight them out",
                            "C": "Give up Siberia until the war in the west is won"}},
            "japan": {
                "question": "The Allies ask you to send troops into Siberia. How far do you go?",
                "options": {"A": "A small force, as agreed with the Americans",
                            "B": "A large force, and stay as long as you can",
                            "C": "None. Problems at home come first"}},
            "china": {
                "question": "Foreign armies may soon move through Manchuria again.",
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
            "britain": {
                "question": "You want Japan and America to send troops into Siberia.",
                "options": {"A": "Arm the anti-Bolshevik Whites",
                            "B": "Stay out and leave Russia to itself",
                            "C": "Go in, and keep watch on Japan"}},
            "usa": {
                "question": "Britain and France want American troops in Siberia.",
                "options": {"A": "Send a small force to guard the railway and fight no one",
                            "B": "Send troops to fight the Bolsheviks alongside the Whites",
                            "C": "Stay out"}}}},
    "1924_united_front": {
        "stage": "interwar", "title": "1919–24: Self-Determination—for Whom?",
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
                "question": "Koreans are preparing to declare independence. What does Japan do if they march?",
                "options": {"A": "Crush it, and make an example",
                            "B": "Crush it, then soften colonial rule",
                            "C": "Promise Koreans a real say in their government"}},
            "china": {
                "question": "The peace conference is about to hand Germany's holdings in Shandong to Japan.",
                "options": {"A": "Sign the treaty and take what else is offered",
                            "B": "Refuse to sign, and let the students march",
                            "C": "Turn to Moscow for help against the warlords"}},
            "taiwan": {
                "question": "The petition for a Taiwanese parliament is collecting names again.",
                "options": {"A": "Sign it",
                            "B": "Sign it, and speak at the meeting",
                            "C": "Stay off the list"}},
            "britain": {
                "question": "Your alliance with Japan is up for renewal, and America and Canada want it ended.",
                "options": {"A": "Renew the alliance with Japan",
                            "B": "Replace it with a four-power pact at Washington",
                            "C": "Renew it, and bring the Americans in"}},
            "usa": {
                "question": "Wilson promised self-determination. Japan threatens to walk out of Paris over Shandong.",
                "options": {"A": "Give Japan Shandong to save the League",
                            "B": "Stand firm for China",
                            "C": "Hear the Korean delegation as well"}}}},
    "1931_manchuria": {
        "stage": "mukden", "title": "1931: The Mukden Crisis",
        "questions": {
            "japan": {
                "question": "Your army in Manchuria has attacked without orders. What does the government do?",
                "options": {"A": "Rein the army in and punish the officers",
                            "B": "Accept what has happened, but stop there",
                            "C": "Take all of Manchuria and make it a new state"}},
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
            "britain": {
                "question": "Japan's army is moving across Manchuria. What should Britain do at the League?",
                "options": {"A": "Back sanctions against Japan",
                            "B": "Send a commission of inquiry and wait",
                            "C": "Accept it: Japan keeps order, and you keep Shanghai"}},
            "usa": {
                "question": "You are not in the League, but Manchuria matters.",
                "options": {"A": "Refuse to recognise any conquest, and do nothing more",
                            "B": "Embargo Japan",
                            "C": "Accept it and keep trading"}}}},
    "1930s_north_south": {
        "stage": "north_south", "title": "1930s: Expansion and Control",
        "questions": {
            "china": {
                "question": "Japanese puppets in the north, Communists in the hills, your government in the south.",
                "options": {"A": "Destroy the Communists first, then face Japan",
                            "B": "Make a united front with the Communists against Japan",
                            "C": "Buy time with Tokyo and build the army"}},
            "japan": {
                "question": "You have left the League of Nations. How much further do you push into China?",
                "options": {"A": "Stop, and hold what you have",
                            "B": "Expand slowly through local puppet regimes",
                            "C": "Prepare for full war with China"}},
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
            "britain": {
                "question": "Japan presses into north China while Germany rearms.",
                "options": {"A": "Rearm, and finish the Singapore base",
                            "B": "Seek a deal with Japan over China",
                            "C": "Pull back to defend Europe"}},
            "usa": {
                "question": "Congress wants no more foreign wars.",
                "options": {"A": "Pass the Neutrality Acts",
                            "B": "Build up the Pacific fleet",
                            "C": "Free the Philippines and step back from Asia"}}}},
    "1937_china": {
        "stage": "sino_japanese_war", "title": "1937: Marco Polo Bridge",
        "questions": {
            "china": {
                "question": "How should the Nationalist government respond?",
                "options": {"A": "Negotiate a local settlement",
                            "B": "Full national resistance",
                            "C": "Cede the north, hold the south"}},
            "japan": {
                "question": "Fighting has broken out near Beijing. How far does Japan go?",
                "options": {"A": "Settle it locally and pull back",
                            "B": "Take north China and stop there",
                            "C": "Fight until China's government gives in"}},
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
            "britain": {
                "question": "Fighting has broken out near Beiping, and your China trade centres on Shanghai.",
                "options": {"A": "Call for joint action with the United States",
                            "B": "Protect your concessions and stay out",
                            "C": "Supply China through Hong Kong and Burma"}},
            "usa": {
                "question": "Fighting has broken out near Beiping. American gunboats patrol the Yangzi.",
                "options": {"A": "Protest, keep trading, and avoid a clash",
                            "B": "Embargo Japan",
                            "C": "Quarantine the aggressors with the other powers"}}}},
    "1939_khalkhin_gol": {
        "stage": "khalkhin_gol", "title": "1939: The Northern Frontier",
        "questions": {
            "russia": {
                "question": "Japanese troops are probing the Mongolian border. How should the USSR answer?",
                "options": {"A": "Pull back and negotiate the border",
                            "B": "Counterattack in force and destroy them",
                            "C": "Take it to the League of Nations"}},
            "japan": {
                "question": "Your army is fighting the Soviets on the Mongolian border without Tokyo's orders. Which way should the empire go?",
                "options": {"A": "North, against the Soviet Union",
                            "B": "South, for Southeast Asia's oil and rubber",
                            "C": "Neither. Finish the war in China first"}},
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
            "britain": {
                "question": "Japan's army is blockading your concession at Tianjin and strip-searching Britons.",
                "options": {"A": "Give way to Japan",
                            "B": "Stand firm and send ships",
                            "C": "Ask Washington for help"}},
            "usa": {
                "question": "Your trade treaty with Japan can be ended on six months' notice.",
                "options": {"A": "Give notice and end it",
                            "B": "Keep it",
                            "C": "Keep it, but restrict war exports"}}}},
    "1941_pacific": {
        "stage": "pacific_war", "title": "1941: A Choice of Directions",
        "questions": {
            "japan": {
                "question": "America is threatening to cut off your oil. What does Japan do?",
                "options": {"A": "Pull out of China to get the oil back",
                            "B": "Seize Southeast Asia's oil and avoid America",
                            "C": "Attack the United States"}},
            "russia": {
                "question": "Germany is massing in the west. What should the USSR do about Japan?",
                "options": {"A": "Sign a neutrality pact with Tokyo",
                            "B": "Join China in open war against Japan",
                            "C": "Demand Japan leave Manchuria before anything is signed"}},
            "china": {
                "question": "Tokyo is talking to Moscow, and Washington is weighing an oil embargo.",
                "options": {"A": "Hold on and wait for America",
                            "B": "Sue for peace while Japan will still talk",
                            "C": "Attack now, before Japan turns south"}},
            "korea": {
                "question": "The great powers are busy with their own wars. No one is coming for Korea.",
                "options": {"A": "Join the exiles in Chongqing",
                            "B": "Join the partisans on the Manchurian border",
                            "C": "Endure, and wait"}},
            "taiwan": {
                "question": "The war is total now.",
                "options": {"A": "Donate your kitchen pots to the war effort",
                            "B": "Volunteer for labour service",
                            "C": "Eat taro and keep your head down"}},
            "britain": {
                "question": "Japan is moving south toward Indochina and your colonies.",
                "options": {"A": "Join an American oil embargo",
                            "B": "Keep supplying China over the Burma Road",
                            "C": "Buy time: close the Burma Road again"}},
            "usa": {
                "question": "Japan is moving into Indochina. Oil is your lever.",
                "options": {"A": "Freeze Japan's assets and embargo oil",
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
                "question": "Japan is losing, and the Allies demand unconditional surrender. What now?",
                "options": {"A": "Surrender on any terms",
                            "B": "Surrender only if the Emperor is kept",
                            "C": "Fight on for better terms"}},
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
                "question": "The empire is collapsing. First meal when the war ends?",
                "options": {"A": "Taro",
                            "B": "Mantou",
                            "C": "Rice — finally"}},
            "britain": {
                "question": "Japan is collapsing. What should Britain do in Asia?",
                "options": {"A": "Race to retake Hong Kong before Chinese forces arrive",
                            "B": "Let Chiang Kai-shek take Hong Kong's surrender",
                            "C": "Move the colonies toward self-rule"}},
            "usa": {
                "question": "The war is ending. What shape should postwar Asia take?",
                "options": {"A": "Occupy Japan alone and keep the Soviets out",
                            "B": "Divide Korea with the Soviets at the 38th parallel",
                            "C": "Use the atomic bomb to end the war before the Soviets arrive"}}}},
}

# What each government actually did, for the accuracy leaderboard. A string
# of letters when more than one option happened. Personal choices (Taiwan's
# dinners, Korean villagers) have no single historical answer and are left out.
HISTORY = {
    "1894_korea":          {"china": "B", "japan": "B", "russia": "A", "britain": "A", "usa": "AB"},
    "1895_shimonoseki":    {"japan": "C", "china": "A", "taiwan": "B", "korea": "A", "russia": "B",
                            "britain": "A", "usa": "A"},
    "1895_triple":         {"russia": "B", "korea": "B", "japan": "B", "china": "B", "taiwan": "A",
                            "britain": "B", "usa": "A"},
    "1897_empire_and_port": {"korea": "B", "russia": "B", "japan": "B", "china": "A",
                            "britain": "AC", "usa": "C"},
    "1904_manchuria":      {"japan": "B", "russia": "B", "korea": "A", "china": "A",
                            "britain": "A", "usa": "B"},
    "1905_portsmouth":     {"russia": "B", "korea": "B", "japan": "A", "china": "A",
                            "britain": "A", "usa": "B"},
    "1910_korea":          {"japan": "B", "korea": "A", "china": "B", "russia": "B",
                            "britain": "A", "usa": "B"},
    "1912_republic":       {"china": "A", "japan": "A", "russia": "B", "britain": "C", "usa": "B"},
    "1917_revolution":     {"russia": "B", "japan": "B", "china": "B", "britain": "A", "usa": "AC"},
    "1918_siberia":        {"russia": "B", "japan": "B", "china": "A", "britain": "A", "usa": "A"},
    "1924_united_front":   {"russia": "B", "korea": "A", "japan": "B", "china": "B",
                            "britain": "B", "usa": "A"},
    "1931_manchuria":      {"japan": "C", "china": "B", "russia": "A", "britain": "B", "usa": "A"},
    "1930s_north_south":   {"china": "A", "japan": "B", "russia": "A", "britain": "A", "usa": "A"},
    "1937_china":          {"china": "B", "japan": "C", "russia": "B", "britain": "AB", "usa": "A"},
    "1939_khalkhin_gol":   {"russia": "B", "japan": "C", "china": "A", "britain": "A", "usa": "A"},
    "1941_pacific":        {"japan": "C", "russia": "A", "china": "A", "britain": "A", "usa": "A"},
    "1945_ussr":           {"russia": "B", "japan": "B", "china": "B", "korea": "B",
                            "britain": "A", "usa": "ABC"},
}

BRIEFINGS = {
    "opening_1894": {
        "china": [
            "You are the Qing court, and Korea is your tributary. Japan has landed troops there on the pretext of putting down a rebellion.",
            "Decide: withdraw, reinforce to hold your suzerainty, or strike first.",
        ],
        "taiwan": [
            "You live on Taiwan, a frontier province of the Qing Empire.",
            "War is coming to the waters around you. No one in Beijing asks what islanders think.",
        ],
        "japan": [
            "Home front: Western powers still hold unequal treaties over Japan. Many believe the only way to be treated as an equal is to act like the Western empires.",
            "Korea: some Japanese want Korea reformed as a partner against the West; others want it under Japanese control before China or Russia can take it.",
            "Front lines: Chinese and Japanese troops are both in Korea. Your army and navy are ready.",
        ],
        "korea": [
            "You serve the Joseon court, long a Qing tributary.",
            "Japanese and Chinese soldiers are on your soil, fighting over your future. You cannot stop either of them.",
        ],
        "russia": [
            "You serve the Tsar, whose empire is pushing into Manchuria and Korea.",
            "A war between China and Japan may weaken both. That could open doors for you.",
        ],
        "britain": [
            "You are the British Empire, the largest trading power in China, with Hong Kong and the Yangtze trade to protect.",
            "Your worry is Russia, not Japan. Tokyo has asked you to give up your special courts in Japan and treat it as an equal.",
        ],
        "usa": [
            "You are the United States: a Pacific power with missionaries and merchants, and no colonies in Asia.",
            "Korea's king once hoped your 1882 treaty would protect him. You have no army to send.",
        ],
    },
    "shimonoseki": {
        "china": [
            "Your armies and fleet are shattered, and Japan dictates the terms at Shimonoseki.",
            "Li Hongzhang is in the room with a bullet wound in his cheek and nothing left to bargain with.",
        ],
        "taiwan": [
            "Japan is demanding Taiwan at Shimonoseki, and Beijing may give it up.",
            "Local leaders talk of proclaiming a Republic of Formosa if the island is handed over.",
            "Decide: accept Japanese rule, join the republic, or fight on without one.",
        ],
        "japan": [
            "Home front: the victory has made the public proud and hungry for more.",
            "Colonies: Taiwan would be Japan's first colony, and a test of how Japan rules other peoples. Its inhabitants have not been asked.",
            "Front lines: you have beaten China, the old centre of the East Asian order. The world is watching what you take.",
        ],
        "korea": [
            "Japan is demanding that the Qing give up every claim over Korea.",
            "You will be independent on paper, and surrounded by Japanese influence.",
            "For the first time, the court's decisions are its own.",
        ],
        "russia": [
            "Japan's victory alarms you.",
            "If Japan takes territory on the mainland, it blocks your own designs on Manchuria and a warm-water port.",
        ],
        "britain": [
            "Japan's victory surprised you, and its terms open new treaty ports your merchants will share.",
            "Russia is sounding out the powers about forcing Japan to give ground.",
        ],
        "usa": [
            "American ministers in Beijing and Tokyo carried the messages that led to peace talks.",
            "Washington wants no Chinese territory, only trade and influence.",
        ],
    },
    "triple_intervention": {
        "china": [
            "You would be grateful for any relief.",
            "Russia is talking to France and Germany about pressing Japan, though for its own interests, not yours.",
        ],
        "taiwan": [
            "The powers argue over Liaodong, but no one argues over Taiwan.",
            "Japanese troops have crushed the young Republic of Formosa.",
            "Decide what remains: fight on, surrender, or flee across the strait.",
        ],
        "japan": [
            "Home front: many conclude that only military strength counts. Others warn it means endless taxes and new enemies.",
            "Colonies: Taiwan is resisting Japanese troops. In Korea, the court is turning to Russia.",
            "Front lines: Russia is rallying France and Germany against your gains. You could not fight all three.",
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
        "britain": [
            "Russia, France and Germany have asked you to help force Japan off Liaodong.",
            "Russia is your great rival in Asia. Helping it would be a strange choice.",
        ],
        "usa": [
            "Russia is rallying Europe to make Japan give back its winnings.",
            "You have no treaty obligations here, and no fleet in Asia to speak of.",
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
            "Home front: your war winnings are going into warships, and taxpayers are asking who the empire is for.",
            "Colonies: in Korea your influence has collapsed; in Taiwan your officials are building railways, schools and police.",
            "Front lines: the European powers are carving up China's ports, and Russia is moving into Manchuria.",
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
        "britain": [
            "Germany has seized Jiaozhou and Russian warships are at Port Arthur. A scramble for leases is starting.",
            "Your trade is the biggest in China, and every new sphere shrinks it.",
        ],
        "usa": [
            "War with Spain has left American troops in Manila, and you annexed Hawaii this summer.",
            "Suddenly you are an Asian power, and the Europeans are carving up China's coast.",
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
            "Home front: critics call war a crime and warn about the debt. Many others say Russia will only stop if it is beaten.",
            "Colonies: Korea stands between you and Russia, and Koreans have no say in the outcome.",
            "Front lines: Russia is spreading across Manchuria. Britain is now your ally, and America is watching Russia warily.",
        ],
        "korea": [
            "Russia and Japan are about to fight over who controls your peninsula.",
            "Whatever the outcome, your independence is fading.",
        ],
        "russia": [
            "Japan proposes a trade: Manchuria for you, Korea for them.",
            "The Tsar's ministers think Tokyo is bluffing and would never dare fight a European power.",
        ],
        "britain": [
            "Since 1902 you have been Japan's ally. If a second power joins Russia, you must fight.",
            "Japan is about to test that promise.",
        ],
        "usa": [
            "New York bankers are being asked to lend Japan money for a war with Russia.",
            "Many Americans resent the Tsar's persecution of Jews and see Japan as the underdog.",
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
            "Home front: the war was paid for with foreign loans and heavy taxes, and the public expects a big payout.",
            "Colonies: Korea will be yours. Colonised peoples from Asia to Africa have noticed an Asian power beat a European one.",
            "Front lines: your army is exhausted. The American president is brokering the peace.",
        ],
        "korea": [
            "Japan has beaten Russia, and the last power that might have balanced Tokyo is gone.",
            "Japanese soldiers are in the palace grounds, and a treaty is on the table tonight.",
        ],
        "russia": [
            "Mukden is lost and the Baltic Fleet lies at the bottom of the Tsushima Strait.",
            "Workers are striking in every city, and the throne is not safe.",
        ],
        "britain": [
            "Japan beat Russia with your diplomatic cover.",
            "Tokyo wants the alliance renewed, with a free hand in Korea written into it.",
        ],
        "usa": [
            "Roosevelt has offered to host the peace talks at Portsmouth.",
            "Your Philippine colony lies next to Japan's new sea power.",
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
            "Home front: few Japanese question expansion, and police are cracking down on socialists and critics.",
            "Colonies: Emperor Gojong calls the 1905 treaty invalid, and armed bands fight in the hills. Some Japanese call Korea a partner; others, a possession.",
            "Front lines: the powers meet at The Hague this year. None has objected to your protectorate, much as you accept their colonies elsewhere.",
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
        "britain": [
            "Korea's emperor has sent secret envoys to the peace conference at The Hague.",
            "Your ally Japan says Korea's diplomacy is its business now.",
        ],
        "usa": [
            "In 1882 you promised Korea your good offices if it was treated unjustly.",
            "You closed your Seoul legation within days of the protectorate treaty.",
        ],
    },
    "qing_collapse": {
        "china": [
            "The revolt that began at Wuchang has spread, and the dynasty cannot survive it.",
            "Sun Yat-sen leads a provisional republic in Nanjing. For the first time, your voice counts in the state.",
            "Yuan Shikai commands the only army that matters.",
        ],
        "taiwan": [
            "The mainland has become a republic, and nothing changes for you.",
            "You remain a subject of Tokyo, watching China's revolution from across the strait.",
        ],
        "japan": [
            "Home front: some Japanese have long backed Chinese revolutionaries as fellow Asians; others see a weak China as an opportunity.",
            "Colonies: Korea and Taiwan are ruled by Japanese generals and police.",
            "Front lines: China's last dynasty has fallen, and the Western powers are distracted by rivalries in Europe.",
        ],
        "korea": [
            "From inside the Japanese Empire, you hear of China's revolution.",
            "Some of your compatriots dream that Korea, too, might one day throw off foreign rule.",
        ],
        "russia": [
            "The Qing collapse leaves Mongolia and Manchuria exposed.",
            "Your empire moves quietly to secure its northern frontier.",
        ],
        "britain": [
            "The Qing are gone. Yuan Shikai holds the army, and your banks lead the international loan consortium.",
            "A stable China pays its debts.",
        ],
        "usa": [
            "Americans cheer the fall of the Qing, and missionaries see hope in the republic.",
            "The consortium's loan would put China's taxes under foreign control.",
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
            "Home front: the world war has made Japan richer. Many fear communism more than any army.",
            "Colonies: Koreans and Taiwanese are hearing about revolution and self-rule.",
            "Front lines: the Tsar has fallen and Russia's new government is weak. Radicals in Petrograd promise revolution far beyond Russia.",
        ],
        "korea": [
            "Russia's revolution inspires the exiles.",
            "Socialism and nationalism begin to mix in the independence movement abroad.",
        ],
        "russia": [
            "The Tsar has fallen. A provisional government and the workers' and soldiers' councils both claim to rule.",
            "Your Far East is vulnerable, and no one is sure who is in charge.",
        ],
        "britain": [
            "German U-boats are sinking your ships, and Russia's war effort is collapsing.",
            "Japan will send destroyers to the Mediterranean, for a price.",
        ],
        "usa": [
            "The United States has entered the war against Germany.",
            "Japan's envoy Ishii has come to Washington to talk about China.",
        ],
    },
    "siberian_intervention": {
        "china": [
            "Your republic is already breaking into warlord fiefs.",
            "Foreign armies may soon move through Manchuria again, and nobody asks you.",
        ],
        "taiwan": [
            "Taiwanese students in Tokyo are writing about home rule.",
            "Their journal reaches the island by hand, a few copies at a time.",
        ],
        "japan": [
            "Home front: rice prices are soaring, and people are rioting across Japan.",
            "Colonies: Korea and Manchuria border revolutionary Russia.",
            "Front lines: the Allies are sending troops into Russia. Your generals want a buffer state; Washington suspects a land grab.",
        ],
        "korea": [
            "Revolution in Russia, and a peace conference promised in Paris.",
            "For the first time since 1910, the exiles think the world might listen.",
        ],
        "russia": [
            "You have made peace with Germany and are fighting a civil war.",
            "Allied war supplies sit at Vladivostok, and the Allies are talking about landing troops.",
        ],
        "britain": [
            "You want Russia back in the war against Germany, or failing that, rid of the Bolsheviks.",
            "British officers are arming White armies in Siberia.",
        ],
        "usa": [
            "Britain and France want troops sent to rescue the Czech Legion and guard supplies.",
            "You distrust Japan's intentions in Siberia more than the Bolsheviks'.",
        ],
    },
    "interwar": {
        "china": [
            "The peace conference is about to hand Germany's holdings in Shandong to Japan.",
            "The republic is a map of warlord armies, and the Nationalists are looking abroad for help.",
        ],
        "taiwan": [
            "Life under Japan is orderly and second-class.",
            "Petitions for a Taiwanese parliament go to Tokyo year after year, and are refused politely.",
        ],
        "japan": [
            "Home front: parties and newspapers are gaining power, and some call for gentler colonial rule.",
            "Colonies: Wilson's talk of self-determination has reached Korea. Others say an empire cannot bend.",
            "Front lines: at the peace conference Japan sits with the great powers and is asking for a clause on racial equality.",
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
        "britain": [
            "You promised Japan Shandong in 1917, and the peace conference must now decide.",
            "Washington sees your alliance with Japan as aimed at the United States.",
        ],
        "usa": [
            "Wilson has promised that peoples may choose their own governments.",
            "Korean, Chinese and Vietnamese petitioners are waiting outside the conference.",
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
            "Home front: the Great Depression has ruined farmers and exporters. Many see Manchuria as a lifeline, and the press cheers the army.",
            "Colonies: Korea and Manchuria are being tied into one Japanese economy.",
            "Front lines: the army has acted on its own. The League of Nations and Washington will judge what you do next.",
        ],
        "korea": [
            "Manchuria's fall brings Japan's armies to your northern border.",
            "Resistance abroad grows harder. The empire feels permanent.",
        ],
        "russia": [
            "Japan now sits on your Far Eastern frontier.",
            "You strengthen defences in Siberia, but you are in no shape for another war.",
        ],
        "britain": [
            "Your economy is in depression and your fleet is stretched.",
            "The League, which you lead, has been asked to judge Japan.",
        ],
        "usa": [
            "America never joined the League, but it signed the 1928 pact outlawing war.",
            "Your trade with Japan is larger than your trade with China.",
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
            "Home front: officers have murdered politicians who opposed them, and civilian government is losing ground.",
            "Colonies: Koreans and Taiwanese are being pushed to speak Japanese and worship at Japanese shrines.",
            "Front lines: Germany has also left the League and is rearming. The post-war order is breaking down.",
        ],
        "korea": [
            "Japan rules Manchukuo on your northern border as well.",
            "Inside Korea, assimilation policies erase names and language. Resistance survives in exile.",
        ],
        "russia": [
            "You consolidate a Soviet Far East and watch Japan nervously.",
            "Border clashes test both sides while Germany arms in the west.",
        ],
        "britain": [
            "Your investments in China are the largest of any power, most of them in Shanghai.",
            "The Singapore naval base is meant to protect the empire east of India. It still has no fleet.",
        ],
        "usa": [
            "The Depression dominates, and Congress blames bankers and arms-makers for the last war.",
            "You have promised the Philippines independence within ten years.",
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
            "Home front: your generals promise a quick victory, and the newspapers want China punished.",
            "Colonies: Korea and Taiwan will be expected to supply soldiers, workers and food for any war.",
            "Front lines: China is vast and its people are rallying against you. The Soviet Union and America may help China.",
        ],
        "korea": [
            "Japan's war consumes Korea's rice, minerals and labour.",
            "Your homeland has become a supply base for a war against your neighbours.",
        ],
        "russia": [
            "China's war with Japan serves your interests. Every Japanese division tied down in China is one fewer on your border.",
            "The question is how much to send, and how openly.",
        ],
        "britain": [
            "A clash near Beiping could spread to Shanghai, the heart of your China trade.",
            "You cannot fight Japan and Germany at the same time.",
        ],
        "usa": [
            "Congress has passed Neutrality Acts to keep America out of foreign wars.",
            "American oil and scrap iron feed Japan's war.",
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
            "Home front: rationing has begun, and the war in China has no end in sight.",
            "Colonies: Koreans are being drafted as labourers and sent to mines and factories in Japan.",
            "Front lines: the Soviets are fighting back hard. War in Europe looks close, and the European colonies in Asia would be left exposed.",
        ],
        "korea": [
            "The labour office has a quota for the mines in Kyushu.",
            "Your village has been given a number to fill.",
        ],
        "russia": [
            "Japanese troops are probing the Mongolian frontier you guarantee.",
            "Give ground and they will come again. Fight, and it could become a war in Asia while Germany arms in the west.",
        ],
        "britain": [
            "Japan has blockaded the British concession at Tianjin.",
            "Hitler threatens Poland, and your fleet cannot be in two oceans.",
        ],
        "usa": [
            "Japan is fighting Soviet troops in Mongolia and squeezing the British at Tianjin.",
            "Your 1911 trade treaty is the legal basis for selling Japan oil and steel.",
        ],
    },
    "pacific_war": {
        "china": [
            "Four years of war have bled your nation, and Moscow is talking to Tokyo.",
            "America's oil may yet do what your armies could not, if Washington cuts it off.",
        ],
        "taiwan": [
            "The empire is preparing to strike south, and Taiwan is its base.",
            "Taiwanese men are being recruited as labourers and interpreters for Japan's forces.",
        ],
        "japan": [
            "Home front: most of your oil comes from America. The navy says Japan can win quickly or not at all.",
            "Colonies: your leaders talk of freeing Asia from Western rule while planning to take its resources.",
            "Front lines: the war in China has no end in sight, and America wants you to leave.",
        ],
        "korea": [
            "Japan's war deepens your hardship: labour conscription, resource extraction, repression.",
            "No great power has promised you anything.",
        ],
        "russia": [
            "You are fighting for survival against Germany.",
            "A pact with Tokyo would free your Siberian divisions, and leave China to fight alone.",
        ],
        "britain": [
            "You are at war with Germany, and your navy is needed in the Atlantic.",
            "Hong Kong, Malaya and Burma lie open to Japan's army.",
        ],
        "usa": [
            "Japan buys most of its oil from you.",
            "Roosevelt must choose between pressure and time.",
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
            "Home front: most large cities have been burned out and food is running short. Some leaders fear revolution at home more than defeat.",
            "Colonies: the Allies have declared that Korea and Taiwan will be taken from Japan. Whoever occupies them will shape Asia after the war.",
            "Front lines: the Americans are close enough to invade. Moscow is still neutral, and it and Washington are already rivals over what comes after.",
        ],
        "korea": [
            "Liberation may be close, but Soviet and American armies are both coming.",
            "Your freedom may arrive already divided.",
        ],
        "russia": [
            "Germany has surrendered.",
            "Your government must decide whether to honour the neutrality pact with Japan or invade Manchuria for territory, ports and influence.",
        ],
        "britain": [
            "Germany has surrendered and your empire is exhausted.",
            "Hong Kong, Malaya and Burma were all lost to Japan. Who will take them back?",
        ],
        "usa": [
            "You carry the Pacific war, and a new weapon has been tested in New Mexico.",
            "The Soviets have promised to enter the war against Japan.",
        ],
    },
}
