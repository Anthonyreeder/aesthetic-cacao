"""
Build all channel subpages + homepage for bdsanthony.com.
Generates interactive "generators" on each channel page and a redesigned homepage.
Run: python _build_site.py
"""
import os, json
from pathlib import Path

BASE = Path(__file__).parent

GA_ID = "G-V3Q88DLJ8K"
ADSENSE = '<script async src=https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8279041593834700 crossorigin=anonymous></script>'
DISCORD = "https://discord.gg/qJBwnHHUYc"

# ─── Channel data ───────────────────────────────────────────────────────────

CHANNELS = {
    "glitchzone": {
        "name": "GlitchZone",
        "tag": "gaming",
        "yt": "@GlitchZone",
        "accent": "#00ff80",
        "accent_bg": "rgba(0,255,128,.12)",
        "hook": "Game-breaking glitches the devs don't want you to know.",
        "desc": "The wildest exploits, bugs, and glitches across every game.",
        "content": [
            {"t": "The Minecraft X-Ray Glitch Still Works", "p": "Place a composter against a wall, push yourself into it with a piston, and you can see through any block. Mojang has 'fixed' this three times. It still works."},
            {"t": "GTA V's Infinite Money Glitch History", "p": "Every single GTA Online update has shipped with at least one money glitch. Rockstar patches them within 48 hours, but the community finds new ones faster."},
            {"t": "The Fortnite Under-Map Exploit", "p": "In Chapter 2 Season 3, players could phase through the map at specific coordinates and shoot players from below. Epic banned 10,000 accounts."},
        ],
        "generators": [
            {
                "id": "glitch_name",
                "title": "Glitch Name Generator",
                "btn": "Generate Glitch",
                "loading": ["Scanning memory addresses...", "Corrupting save data...", "Bypassing anti-cheat...", "Injecting exploit code...", "Overflowing the buffer..."],
                "pool": [
                    "The Phantom Wall Clip", "Infinite Jump Cascade", "Shadow Realm Teleport", "The Backwards Long Jump",
                    "Null Pointer Noclip", "Texture Corruption Warp", "Out of Bounds Void Skip", "The Invisible Hitbox",
                    "Memory Leak Duplication", "The Respawn Loop", "Gravity Inversion Bug", "The Unloaded Chunk Exploit",
                    "Animation Cancel Dash", "The Floating Point Error", "Desync Teleportation", "The Frozen Timer Glitch",
                    "Collision Mesh Bypass", "Ragdoll Physics Break", "The God Mode Overflow", "Inventory Corruption Dupe",
                    "The Boundary Break", "Asset Streaming Exploit", "The Camera Clip Trick", "Server Tick Manipulation",
                    "The Negative Health Bug", "Render Distance Abuse", "The Checkpoint Warp", "Input Buffer Overflow",
                    "The Shadow Clone Glitch", "Map Geometry Exploit", "The Zero Gravity Bug", "Packet Loss Teleport",
                ],
            },
            {
                "id": "glitch_challenge",
                "title": "Random Glitch Challenge",
                "btn": "Get Challenge",
                "loading": ["Loading challenge parameters...", "Calibrating difficulty...", "Selecting game..."],
                "pool": [
                    "Beat a boss using only glitched weapons", "Clip through 5 walls in under 60 seconds",
                    "Complete a level entirely out of bounds", "Win a match while invisible",
                    "Duplicate an item without getting caught", "Skip an entire area using a single glitch",
                    "Reach the final boss in under 3 minutes using exploits", "Play an entire session upside down (camera glitch)",
                    "Beat a raid using only unpatched bugs", "Get to the map boundary and survive for 5 minutes",
                    "Win a PvP fight using only movement glitches", "Complete a speedrun category using a newly found skip",
                    "Stack 3 different glitches in one run", "Clip into a developer room nobody was meant to see",
                    "Beat the tutorial using an end-game exploit", "Trigger 10 different glitches in a single session",
                    "Find a glitch that hasn't been documented yet", "Use a physics bug to launch yourself across the map",
                    "Complete a no-damage run using only bugs", "Break the game's economy with a single dupe glitch",
                ],
            },
        ],
    },
    "blocksarebuildable": {
        "name": "BlocksAreBuildable",
        "tag": "gaming",
        "yt": "@BlocksAreBuildable",
        "accent": "#ffff00",
        "accent_bg": "rgba(255,255,0,.12)",
        "hook": "Things about Minecraft you definitely didn't know.",
        "desc": "Minecraft facts, myths, and viral gaming content.",
        "content": [
            {"t": "Endermen speak English backwards", "p": "Record an Enderman's idle sounds, reverse the audio, and you'll hear distorted words like 'hello' and 'what's up.' Mojang confirmed this."},
            {"t": "The world is 8x the size of Earth", "p": "A Minecraft world is 60 million blocks wide. That's over 60,000km, roughly 8 times the surface area of Earth."},
            {"t": "Creepers were a coding accident", "p": "Notch was trying to make a pig model and accidentally swapped the height and length values. The result was so creepy he kept it."},
        ],
        "generators": [
            {
                "id": "build_idea",
                "title": "Minecraft Build Idea Generator",
                "btn": "Generate Build",
                "loading": ["Mining resources...", "Placing blocks...", "Crafting blueprints...", "Consulting the architects..."],
                "pool": [
                    "Underwater glass dome city", "Floating steampunk airship", "Medieval castle with working drawbridge",
                    "Nether portal room disguised as a library", "Giant treehouse village", "Redstone-powered hidden base",
                    "Pixel art museum", "Underground mushroom kingdom", "Japanese shrine on a mountain",
                    "Working train station with minecarts", "Haunted mansion with secret rooms", "Futuristic space station",
                    "Viking longhouse with a dock", "Desert pyramid with booby traps", "Hobbit hole village",
                    "Working elevator using honey blocks", "Massive aquarium with tropical fish", "Wizard tower with enchanting room",
                    "Ancient Roman colosseum", "Cloud city above the build limit", "Working lighthouse on a cliff",
                    "Underground bunker with farms", "Pirate ship with cannons", "Modern skyscraper with glass walls",
                    "Jungle temple restoration", "Ice palace with packed ice floors", "Working clock tower with redstone",
                    "Mushroom island resort", "End city replica in the overworld", "Dragon's lair in a mountain",
                    "Underwater submarine base", "Volcanic island fortress",
                ],
            },
            {
                "id": "mob_quiz",
                "title": "What Minecraft Mob Are You?",
                "btn": "Find Out",
                "loading": ["Scanning your soul...", "Checking your biome...", "Calculating hostility level..."],
                "pool": [
                    "Enderman -- you're tall, mysterious, and hate eye contact",
                    "Creeper -- you sneak up on people and leave a lasting impression",
                    "Wolf -- loyal to the core, but cross your friends and it's over",
                    "Iron Golem -- quiet protector, strong but gentle",
                    "Phantom -- you don't sleep enough and everyone knows it",
                    "Axolotl -- adorable, helpful, and slightly chaotic",
                    "Wither -- you showed up and chose violence",
                    "Villager -- just trying to trade and mind your own business",
                    "Bee -- productive, social, and will fight if provoked",
                    "Ender Dragon -- the final boss, everyone knows your name",
                    "Cat -- you scare creepers away just by existing",
                    "Skeleton -- you shoot your shot even when you miss",
                    "Blaze -- hot-headed and hard to approach",
                    "Allay -- you find things people lost and bring them back",
                    "Fox -- sneaky, fast, and you steal things",
                    "Parrot -- you repeat everything everyone says",
                    "Warden -- you hear everything and nobody escapes you",
                    "Pig -- underestimated but secretly the OG",
                    "Snow Golem -- you mean well but you're kinda useless",
                    "Zombie -- just vibing, slowly, in a group",
                ],
            },
        ],
    },
    "rbxrogebait": {
        "name": "RBX RogeBait",
        "tag": "gaming",
        "yt": "@RBXRogeBait",
        "accent": "#ff3333",
        "accent_bg": "rgba(255,51,51,.12)",
        "hook": "Roblox hot takes that'll make you rage.",
        "desc": "The most controversial Roblox opinions on the internet.",
        "content": [
            {"t": "Adopt Me ruined Roblox", "p": "Before Adopt Me, Roblox was about creativity. Now it's all pet trading and scams. The game single-handedly turned the platform into a marketplace."},
            {"t": "Blox Fruits is just grinding simulator", "p": "You spend 400 hours grinding levels to... grind more levels. There's no endgame. It's a hamster wheel with anime effects."},
        ],
        "generators": [
            {
                "id": "hot_take",
                "title": "Roblox Hot Take Generator",
                "btn": "Drop a Hot Take",
                "loading": ["Heating up the take...", "Preparing for backlash...", "Loading controversial opinion...", "Consulting the comment section..."],
                "pool": [
                    "Adopt Me has better trading than the actual stock market",
                    "90% of Roblox games are just the same obby reskinned",
                    "Blox Fruits players have never touched grass",
                    "Old Roblox was peak gaming and nothing comes close",
                    "Robux is a better currency than most crypto",
                    "Tower Defense Simulator is the only good Roblox game",
                    "Murder Mystery 2 is rigged and everyone knows it",
                    "Roblox moderation is run by actual bots with no training",
                    "Brookhaven roleplayers are the backbone of Roblox",
                    "If you play Roblox on mobile you're automatically at a disadvantage",
                    "The Roblox avatar shop is a bigger scam than NFTs",
                    "Jailbreak was the best game Roblox ever had",
                    "Anime games on Roblox are all the same game with different skins",
                    "Free items are always better than paid ones",
                    "Roblox Premium is a waste of money",
                    "Natural Disaster Survival is the most underrated Roblox game",
                    "Piggy was only good for the first 3 chapters",
                    "Arsenal players think they're pro but would get destroyed in any real FPS",
                    "Roblox should have stayed blocky -- the new avatars are creepy",
                    "Every Roblox YouTuber plays the same 5 games",
                    "Slenders ruined the Roblox community forever",
                    "Pet Simulator X is literally designed to be addictive",
                    "Doors is the only good horror game on Roblox",
                    "Roblox voice chat was a mistake",
                    "The old death sound was better and it's not even close",
                ],
            },
            {
                "id": "rage_rating",
                "title": "Your Rage Rating Today",
                "btn": "Check Rage Level",
                "loading": ["Measuring salt levels...", "Scanning rage hormones...", "Calculating tilt factor..."],
                "pool": [
                    "2/10 -- Zen mode. Nothing can break you today.",
                    "3/10 -- Mildly annoyed. One more thing and you'll snap.",
                    "4/10 -- Simmering. The rage is building quietly.",
                    "5/10 -- Average gamer rage. Keyboard is safe... for now.",
                    "6/10 -- One lagspike away from alt+F4.",
                    "7/10 -- You've already said 'this game is trash' twice today.",
                    "8/10 -- Controller throw risk: HIGH.",
                    "9/10 -- You googled 'how to report everyone in a lobby'.",
                    "10/10 -- MAXIMUM RAGE. You're one kill away from uninstalling.",
                    "11/10 -- Beyond rage. You've achieved inner chaos.",
                    "1/10 -- Suspiciously calm. Are you even a gamer?",
                    "6.5/10 -- That weird zone where you're mad but still queueing.",
                    "7.7/10 -- You told someone 'GG' but didn't mean it.",
                    "3.5/10 -- Annoyed but too lazy to actually rage.",
                    "8.8/10 -- You blamed lag for something that was 100% your fault.",
                ],
            },
        ],
    },
    "mcrogebait": {
        "name": "MC RogeBait",
        "tag": "gaming",
        "yt": "@MCRogeBait",
        "accent": "#ff6600",
        "accent_bg": "rgba(255,102,0,.12)",
        "hook": "Minecraft opinions that will trigger the entire fanbase.",
        "desc": "The hottest Minecraft takes on the internet.",
        "content": [
            {"t": "Diamonds are overrated", "p": "Netherite exists. Diamonds are literally just a stepping stone now. Stop acting like finding them is a big deal."},
            {"t": "Bedrock is better than Java", "p": "Cross-play, better performance, marketplace. Java players just cope because they had it first."},
        ],
        "generators": [
            {
                "id": "mc_hot_take",
                "title": "Minecraft Hot Take Generator",
                "btn": "Drop a Hot Take",
                "loading": ["Mining for controversy...", "Crafting an opinion...", "Loading TNT takes..."],
                "pool": [
                    "Netherite tools aren't worth the grind",
                    "The Warden is the worst mob they've ever added",
                    "Minecraft peaked at 1.8 and it's been downhill since",
                    "Redstone is just coding for people who won't learn to code",
                    "Hardcore mode is the only real way to play",
                    "Building in creative doesn't count as real building",
                    "The End is the most boring dimension",
                    "Mojang adds too much useless stuff nobody asked for",
                    "Copper is completely pointless",
                    "PvP was better before 1.9 combat update",
                    "Minecraft mods are better than official updates",
                    "Survival multiplayer is toxic and everyone cheats",
                    "Bedrock edition runs better and that's just facts",
                    "The phantom was a mistake and the community voted for it",
                    "Herobrine was never real and you were always lying",
                    "TNT cannons are a waste of time",
                    "Every Minecraft build looks the same on TikTok",
                    "Enchanting is just gambling with extra steps",
                    "You don't need a farm for everything -- just play the game",
                    "Dream SMP was cringe and you know it",
                    "Ocean monuments are not worth raiding",
                    "Minecraft should have seasons and weather",
                    "Caves & Cliffs was overhyped and underdelivered",
                    "The allay is useless compared to what we could have had",
                ],
            },
            {
                "id": "mc_worst_teammate",
                "title": "Worst Teammate Generator",
                "btn": "Generate Teammate",
                "loading": ["Scanning lobbies...", "Finding the worst player...", "Measuring incompetence..."],
                "pool": [
                    "The one who mines straight down and falls in lava with all the diamonds",
                    "The one who 'accidentally' hits you off a cliff",
                    "The one who takes all the food and never shares",
                    "The one who builds a dirt house next to your mansion",
                    "The one who aggros the Enderman inside your base",
                    "The one who uses all your XP on Bane of Arthropods",
                    "The one who lets creepers into the base 'for fun'",
                    "The one who steals from chests and says 'I thought it was communal'",
                    "The one who breaks your nether portal as a prank",
                    "The one who sleeps in the Nether because 'they forgot'",
                    "The one who griefs your farm and replants nothing",
                    "The one who brings a Wither to spawn near your base",
                    "The one who enchants YOUR pickaxe with Silk Touch when you wanted Fortune",
                    "The one who kills your dog and says it was an accident",
                    "The one who joins, asks for items, then logs off forever",
                ],
            },
        ],
    },
    "fnrogebait": {
        "name": "FN RogeBait",
        "tag": "gaming",
        "yt": "@FNRogeBait",
        "accent": "#ff44aa",
        "accent_bg": "rgba(255,68,170,.12)",
        "hook": "Fortnite takes so hot they'll get you banned from Reddit.",
        "desc": "The most unhinged Fortnite opinions ever.",
        "content": [
            {"t": "Building should have never been in Fortnite", "p": "The game would have been better as a pure shooter. Building just turned it into a sweaty architect simulator."},
            {"t": "OG skins don't make you good", "p": "Having a Renegade Raider doesn't mean you're skilled. It means you played in 2017 and probably still can't aim."},
        ],
        "generators": [
            {
                "id": "fn_hot_take",
                "title": "Fortnite Hot Take Generator",
                "btn": "Drop a Hot Take",
                "loading": ["Loading the battle bus...", "Scanning the loot pool...", "Consulting the sweat lords..."],
                "pool": [
                    "Zero Build is the best thing that ever happened to Fortnite",
                    "Every collab skin is lazy and unoriginal",
                    "Tilted Towers was never that good -- you just have nostalgia",
                    "Controller aim assist is basically aimbot",
                    "Chapter 1 was mid and you only miss it because you were young",
                    "The mythic weapons system is terrible game design",
                    "SBMM doesn't work and never has",
                    "Fortnite peaked at Chapter 2 Season 2",
                    "Building sweats ruined the game for casuals",
                    "Battle passes are just FOMO manipulation",
                    "OG Fortnite was buggy trash and you just remember the vibes",
                    "V-Bucks are overpriced for what you get",
                    "Fortnite tournaments are rigged toward controller players",
                    "The storyline makes zero sense and never has",
                    "Arena mode is just pubs with extra steps",
                    "Fortnite should stop adding new weapons and fix the old ones",
                    "Creative mode is the only good part of Fortnite now",
                    "Every Fortnite dance is stolen and you know it",
                    "Pump shotgun meta was the only real meta",
                    "Mobile players deserve respect and never get it",
                    "The item shop rotations are designed to create artificial scarcity",
                    "Bots in lobbies make wins meaningless",
                ],
            },
            {
                "id": "fn_rage_rating",
                "title": "Your Tilt Level Today",
                "btn": "Check Tilt",
                "loading": ["Measuring sweat output...", "Scanning rage levels...", "Counting broken keyboards..."],
                "pool": [
                    "1/10 -- Casual vibes only. You're playing for fun today.",
                    "3/10 -- Slightly annoyed. Someone took your landing spot.",
                    "5/10 -- You've already switched to Zero Build once.",
                    "6/10 -- You watched a kill cam and said 'HOW'.",
                    "7/10 -- You've blamed Epic Games twice in the last hour.",
                    "8/10 -- You reported someone for being 'too good'.",
                    "9/10 -- You're one crank away from alt-F4.",
                    "10/10 -- You uninstalled... then reinstalled 20 minutes later.",
                    "4/10 -- Manageable. You only screamed once.",
                    "6.5/10 -- You typed 'dead game' in someone's chat.",
                    "8.5/10 -- You switched to keyboard mid-game out of rage.",
                    "2/10 -- Peaceful. Probably playing creative.",
                ],
            },
        ],
    },
    "lootlore": {
        "name": "LootLore",
        "tag": "gaming",
        "yt": "@LootLore",
        "accent": "#ffc800",
        "accent_bg": "rgba(255,200,0,.12)",
        "hook": "The stories behind gaming's rarest loot.",
        "desc": "Hidden lore, rare items, and gaming secrets you missed.",
        "content": [
            {"t": "The rarest Fortnite skin has only been seen 3 times", "p": "The Honor Guard skin was exclusive to a limited phone deal. Fewer than 50,000 exist worldwide."},
            {"t": "Destiny's Gjallarhorn was accidentally overpowered", "p": "Bungie didn't realize how broken Wolfpack Rounds were until the community figured out stacking mechanics."},
        ],
        "generators": [
            {
                "id": "loot_drop",
                "title": "Loot Drop Simulator",
                "btn": "Open Loot Box",
                "loading": ["Spinning the RNG...", "Calculating drop rates...", "Praying to RNGesus...", "Loading loot tables...", "Rolling the dice..."],
                "pool": [
                    "COMMON -- Rusty Sword (sells for 2 gold)",
                    "COMMON -- Wooden Shield (blocks nothing)",
                    "COMMON -- Health Potion (expired last week)",
                    "UNCOMMON -- Steel Dagger (+5 stealth)",
                    "UNCOMMON -- Leather Boots of Speed (+10% movement)",
                    "UNCOMMON -- Fire Arrows (x12)",
                    "RARE -- Shadow Cloak (turns you invisible for 3 seconds)",
                    "RARE -- Enchanted Bow of the North Wind",
                    "RARE -- Crystal Staff (+30 magic damage)",
                    "RARE -- Dragon Scale Armor (fire resistant)",
                    "EPIC -- Thunderstrike Hammer (chain lightning on hit)",
                    "EPIC -- Void Walker Boots (phase through walls briefly)",
                    "EPIC -- Phoenix Feather (auto-revive once per game)",
                    "EPIC -- Cursed Blade of the Fallen King",
                    "LEGENDARY -- The Infinity Edge (1% drop rate)",
                    "LEGENDARY -- Celestial Wings (+100% flight speed)",
                    "LEGENDARY -- Time Stopper Amulet (freeze enemies for 5s)",
                    "LEGENDARY -- Kraken's Tentacle Whip",
                    "MYTHIC -- The World Ender (0.01% drop rate, deletes everything)",
                    "MYTHIC -- Developer's Console (literally breaks the game)",
                    "COMMON -- Empty Crate (better luck next time)",
                    "UNCOMMON -- Shiny Rock (does nothing but looks cool)",
                    "RARE -- Gamer Fuel (+50% reaction speed for 10s)",
                    "EPIC -- Ban Hammer (one-shot any player, single use)",
                    "COMMON -- Tutorial Sword (you already have 47 of these)",
                ],
            },
            {
                "id": "mystery_weapon",
                "title": "Mystery Weapon Generator",
                "btn": "Generate Weapon",
                "loading": ["Forging in the void...", "Enchanting with dark magic...", "Tempering the blade..."],
                "pool": [
                    "Frostbite Katana -- freezes enemies on critical hits",
                    "The Pixel Shredder -- fires 8-bit projectiles",
                    "Gravity Hammer MK2 -- sends enemies into orbit",
                    "Shadow Daggers -- double damage from behind",
                    "Plasma Rifle of the Old World -- melts armor",
                    "The Lag Spike -- causes enemies to rubber-band",
                    "Banhammer Deluxe -- removes enemies from the server",
                    "Rubber Duck Launcher -- surprisingly lethal",
                    "The Broken Sword of Patch Notes -- nerfed but still hits",
                    "Dual Wield Chaos Blades -- attack speed +200%",
                    "The RNG Cannon -- damage is random between 1 and 99999",
                    "Sniper Rifle of Patience -- one shot, one hour cooldown",
                    "Shield of Lag Compensation -- blocks based on your ping",
                    "The Keyboard Smasher -- deals damage equal to your APM",
                    "Sword of a Thousand Bugs -- each hit triggers a random glitch",
                    "The Nerf Gun -- was good last patch, not anymore",
                ],
            },
        ],
    },
    "robloxbeliever": {
        "name": "RobloxBeliever",
        "tag": "gaming",
        "yt": "@RobloxBeliever",
        "accent": "#ffcc00",
        "accent_bg": "rgba(255,204,0,.12)",
        "hook": "The Roblox stories nobody tells you about.",
        "desc": "Creepy Roblox stories, myths, and community secrets.",
        "content": [
            {"t": "The John Doe myth was almost real", "p": "John Doe (user #2) was just a test account, but in 2017 someone actually hacked it and started joining random servers."},
            {"t": "Roblox once accidentally gave everyone free Robux", "p": "A 2020 bug briefly allowed unlimited Robux purchases at $0. It lasted 12 minutes. Some users got millions."},
        ],
        "generators": [
            {
                "id": "roblox_game_idea",
                "title": "Roblox Game Idea Generator",
                "btn": "Generate Game Idea",
                "loading": ["Brainstorming in Roblox Studio...", "Loading assets...", "Checking if name is taken..."],
                "pool": [
                    "Obby but the floor is actually the ceiling", "Tower defense but YOU are the enemy",
                    "Tycoon where you build a school and the NPCs keep rebelling", "Murder mystery on a sinking ship",
                    "Simulator where you simulate other simulators", "Horror game set inside Roblox Studio itself",
                    "Battle royale but everyone is a different Roblox classic character", "Roleplay game where everyone has amnesia",
                    "Parkour game that gets harder based on how good you are in real-time", "Cooking game but everything explodes",
                    "Pet collecting but the pets collect YOU", "Escape room that changes layout every time you fail",
                    "Racing game where the track builds itself as you drive", "Survival game on a single Roblox baseplate",
                    "Fashion show judged by AI", "Tycoon where you run a Roblox game studio inside Roblox",
                    "Hide and seek in a massive procedurally generated city", "Fighting game where your avatar's accessories are your weapons",
                    "Social deduction game but in a haunted Roblox server", "Obby that rewinds time every 30 seconds",
                ],
            },
            {
                "id": "roblox_character",
                "title": "What Roblox Character Are You?",
                "btn": "Find Out",
                "loading": ["Scanning your avatar...", "Checking your play history...", "Analyzing your vibe..."],
                "pool": [
                    "The Tryhard -- you own every limited item and flex on newbies",
                    "The Builder -- you spend 6 hours in Studio and forget to eat",
                    "The Trader -- you know the value of every limited better than your homework",
                    "The Roleplayer -- Brookhaven is your second home",
                    "The Noob -- you've been playing for 3 years and still don't know what R6 means",
                    "The Grinder -- you have max level in 14 different games",
                    "The Troll -- your entire purpose is making people rage in chat",
                    "The Collector -- your inventory has 10,000 items and you've worn 12 of them",
                    "The OG -- you remember Tix and you'll never let anyone forget it",
                    "The Creator -- you've published 30 games and 29 of them have 0 visits",
                    "The Socializer -- you join servers to chat, not play",
                    "The Speedrunner -- you've beaten every obby in record time",
                    "The Fashionista -- your avatar outfit costs more than your actual wardrobe",
                    "The AFK Farmer -- you leave games running overnight for rewards",
                    "The Youtuber -- you record everything hoping to go viral",
                ],
            },
        ],
    },
    "braindrap": {
        "name": "BrainDrap",
        "tag": "knowledge",
        "yt": "@BrainDrap",
        "accent": "#00ccff",
        "accent_bg": "rgba(0,204,255,.12)",
        "hook": "Psychology facts that change how you see people.",
        "desc": "Dark psychology, manipulation tactics, and mind-bending facts.",
        "content": [
            {"t": "The Doorway Effect is why you forget", "p": "Walking through a doorway literally resets your short-term memory. Your brain treats each room as a new 'episode.'"},
            {"t": "You're more honest when tired", "p": "Sleep deprivation weakens the prefrontal cortex, making it harder to filter what you say. Interrogators know this."},
        ],
        "generators": [
            {
                "id": "psych_fact",
                "title": "Dark Psychology Fact",
                "btn": "Generate Fact",
                "loading": ["Accessing your subconscious...", "Decoding human behavior...", "Loading dark truths..."],
                "pool": [
                    "People who give unsolicited advice are often trying to control, not help",
                    "Mirroring someone's body language makes them trust you 40% more",
                    "The most manipulative people are often the most charming in the first 5 minutes",
                    "If someone always plays the victim, they're usually the aggressor",
                    "People reveal their true character by how they treat those who can't benefit them",
                    "The 'door-in-the-face' technique: ask for something huge, get rejected, then ask for what you actually want",
                    "Narcissists love-bomb you first and devalue you once you're attached",
                    "If someone says 'trust me' a lot, your brain automatically trusts them less",
                    "People who gossip to you will gossip about you. Always.",
                    "The sunk cost fallacy keeps people in bad relationships for years",
                    "Smiling when delivering bad news makes people accept it more easily",
                    "People with power speak slower because they know you'll wait",
                    "The 'Benjamin Franklin effect' -- asking someone for a favor makes them like you more",
                    "Your brain can't tell the difference between rejection and physical pain",
                    "People who interrupt constantly see conversations as competitions, not connections",
                    "Silence after a question creates pressure that makes people reveal more",
                    "Gaslighting starts so subtly you'll question your own memory before questioning them",
                    "The 'foot-in-the-door' technique: small yeses lead to big yeses",
                    "People instinctively trust deeper voices more than higher ones",
                    "Complimenting someone before asking a favor doubles your success rate",
                    "Your first impression is formed in 7 seconds and almost never changes",
                    "People who always need to be right are usually the most insecure",
                    "Anchoring bias: the first number you hear affects every number after it",
                    "Emotional vampires drain your energy and blame you for being tired",
                ],
            },
            {
                "id": "shadow_personality",
                "title": "What's Your Shadow Personality?",
                "btn": "Reveal Shadow",
                "loading": ["Peering into the void...", "Analyzing your dark side...", "Consulting Carl Jung..."],
                "pool": [
                    "The Puppet Master -- you see people as pieces on a board, even when you don't mean to",
                    "The Ghost -- you vanish when things get real, leaving people wondering what happened",
                    "The Mirror -- you reflect whatever people want to see, hiding your true self",
                    "The Critic -- you judge others harshly because you judge yourself harder",
                    "The Performer -- you need an audience to feel alive, and silence terrifies you",
                    "The Hermit -- you push people away before they can leave, then wonder why you're alone",
                    "The Rebel -- you break rules just to prove you can, even when it hurts you",
                    "The Perfectionist -- nothing is ever good enough, including yourself",
                    "The Chameleon -- you become whoever the room needs, but you've lost who you actually are",
                    "The Savior -- you fix everyone else to avoid fixing yourself",
                    "The Storm -- your emotions control you, and everyone around you feels the weather change",
                    "The Observer -- you watch life from the sidelines, too afraid to actually participate",
                    "The Collector -- you hoard relationships, possessions, and achievements to fill a void",
                    "The Mask -- you're so good at pretending you've forgotten what's real",
                ],
            },
        ],
    },
    "quizdrop": {
        "name": "QuizDrop",
        "tag": "trivia",
        "yt": "@QuizDropHQ",
        "accent": "#00d2b4",
        "accent_bg": "rgba(0,210,180,.12)",
        "hook": "Trivia questions that make you feel dumb.",
        "desc": "Random trivia, brain teasers, and quiz content.",
        "content": [
            {"t": "Honey never spoils", "p": "Archaeologists found 3,000-year-old honey in Egyptian tombs that was still perfectly edible."},
            {"t": "Octopuses have three hearts", "p": "Two pump blood to the gills, one pumps it to the rest of the body. And their blood is blue."},
        ],
        "generators": [
            {
                "id": "trivia",
                "title": "Random Trivia Question",
                "btn": "Get Question",
                "loading": ["Searching the knowledge vault...", "Picking a brain teaser...", "Loading obscure facts..."],
                "pool": [
                    "Q: What planet rains diamonds? -- A: Neptune and Uranus",
                    "Q: How many bones does a shark have? -- A: Zero. They're all cartilage.",
                    "Q: What country has the most islands? -- A: Sweden, with 267,570 islands",
                    "Q: What's the loudest animal on Earth? -- A: The sperm whale at 230 decibels",
                    "Q: How long is one day on Venus? -- A: Longer than one year on Venus (243 vs 225 Earth days)",
                    "Q: What percentage of the ocean has been explored? -- A: About 5%",
                    "Q: What animal can survive in space? -- A: Tardigrades (water bears)",
                    "Q: How many muscles does a cat have in each ear? -- A: 32",
                    "Q: What's the most stolen food in the world? -- A: Cheese",
                    "Q: What color is a mirror? -- A: Slightly green",
                    "Q: How fast does a sneeze travel? -- A: About 100 mph",
                    "Q: What fruit floats in water? -- A: Apples (they're 25% air)",
                    "Q: What country invented ice cream? -- A: China, around 200 BC",
                    "Q: How many taste buds does a catfish have? -- A: Over 100,000 (all over its body)",
                    "Q: What's the shortest war in history? -- A: Anglo-Zanzibar War, 38 minutes",
                    "Q: Can you hum while holding your nose? -- A: No. Try it.",
                    "Q: What animal never sleeps? -- A: Bullfrogs",
                    "Q: What's the most common letter in English? -- A: E",
                    "Q: How many Earths could fit inside the Sun? -- A: About 1.3 million",
                    "Q: What element makes up most of the human body? -- A: Oxygen (65%)",
                    "Q: What animal has the longest pregnancy? -- A: Elephants (22 months)",
                    "Q: What's the hardest natural substance? -- A: Diamond",
                    "Q: How many languages are spoken worldwide? -- A: Over 7,000",
                    "Q: What phobia is the fear of long words? -- A: Hippopotomonstrosesquippedaliophobia",
                ],
            },
        ],
    },
    "sigmavault": {
        "name": "SigmaVault",
        "tag": "motivation",
        "yt": "@SigmaVault",
        "accent": "#b070ff",
        "accent_bg": "rgba(176,112,255,.12)",
        "hook": "Sigma quotes that hit different at 3AM.",
        "desc": "Motivational quotes, grindset wisdom, and sigma energy.",
        "content": [
            {"t": "Discipline beats motivation every time", "p": "Motivation gets you started. Discipline keeps you going when motivation disappears. Every successful person knows this."},
            {"t": "Your circle determines your future", "p": "You are the average of the 5 people you spend the most time with. Choose wisely or stay average."},
        ],
        "generators": [
            {
                "id": "sigma_quote",
                "title": "Sigma Quote Generator",
                "btn": "Generate Quote",
                "loading": ["Channeling sigma energy...", "Consulting the grindset...", "Loading wisdom...", "Tuning into alpha frequency..."],
                "pool": [
                    "They laughed at the plan. They won't laugh at the results.",
                    "Your comfort zone is a beautiful place, but nothing grows there.",
                    "Work in silence. Let your success make the noise.",
                    "They don't hate you. They hate that they can't ignore you.",
                    "Discipline is choosing between what you want now and what you want most.",
                    "The lion doesn't turn around when the small dog barks.",
                    "You're not behind. You're on a different timeline.",
                    "Average people have average habits. Decide which one you are.",
                    "Pain is temporary. Quitting lasts forever.",
                    "They'll ignore you until they need you. Remember that.",
                    "Your biggest competition is the person you were yesterday.",
                    "Stop telling people your plans. Show them your results.",
                    "The grind doesn't care about your feelings.",
                    "Rich people have big libraries. Poor people have big TVs.",
                    "If they don't know your next move, they can't stop it.",
                    "Being alone is better than being in bad company.",
                    "A lion doesn't lose sleep over the opinions of sheep.",
                    "Your network is your net worth.",
                    "The best revenge is massive success.",
                    "Fall seven times, stand up eight.",
                    "Don't watch the clock. Do what it does -- keep going.",
                    "Champions train. Losers complain.",
                    "If it was easy, everyone would do it. That's why it's worth it.",
                    "Weak people revenge. Strong people forgive. Intelligent people ignore.",
                    "Talk is cheap. Execution is expensive. That's why most people are broke.",
                ],
            },
            {
                "id": "grindset_level",
                "title": "What's Your Grindset Level?",
                "btn": "Check Level",
                "loading": ["Scanning hustle metrics...", "Measuring sigma energy...", "Calculating grind score..."],
                "pool": [
                    "Level 1: Spectator -- you watch other people win from the couch",
                    "Level 2: Dreamer -- you have ideas but zero execution",
                    "Level 3: Starter -- you begin things but never finish them",
                    "Level 4: Worker -- you put in hours but not smart hours",
                    "Level 5: Hustler -- you're getting results but burning out",
                    "Level 6: Strategist -- you work smarter, not harder",
                    "Level 7: Machine -- nothing stops you, sleep is optional",
                    "Level 8: Sigma -- you move in silence, results speak for themselves",
                    "Level 9: Legend -- people study your methods",
                    "Level 10: Transcended -- you've achieved a level of discipline most people can't comprehend",
                    "Level 0: NPC -- you follow the crowd and wonder why you're average",
                    "Level 3.5: Procrastinator -- you grind... tomorrow",
                    "Level 6.5: Almost There -- one more push and you break through",
                    "Level 11: Off the Charts -- the grindset has consumed you entirely",
                ],
            },
        ],
    },
    "tinypawstales": {
        "name": "TinyPawsTales",
        "tag": "comedy",
        "yt": "@TinyPawsTales",
        "accent": "#ff9933",
        "accent_bg": "rgba(255,153,51,.12)",
        "hook": "Adorable animal stories with unexpected twists.",
        "desc": "Cute animal tales, pet facts, and wholesome content.",
        "content": [
            {"t": "Cats have over 100 vocal sounds", "p": "Dogs have about 10. Your cat is basically running a symphony while your dog is stuck on repeat."},
            {"t": "A group of flamingos is called a 'flamboyance'", "p": "Because of course it is. They're the most extra birds alive."},
        ],
        "generators": [
            {
                "id": "pet_name",
                "title": "Pet Name Generator",
                "btn": "Generate Name",
                "loading": ["Consulting the animals...", "Browsing the name vault...", "Finding the perfect name..."],
                "pool": [
                    "Sir Fluffington III", "Biscuit McWhiskers", "Captain Snuggles", "Lord Borkington",
                    "Princess Noodle", "Mr. Wobbles", "Duke of Zoomies", "Lady Purrington",
                    "Sergeant Floofbottom", "Nugget von Chaos", "Professor Whiskerface", "Queen Butterbean",
                    "Agent Snoot", "Baron von Floof", "Pickles McFluffbutt", "General Mischief",
                    "Sir Barks-a-Lot", "Duchess of Naptime", "Commander Boop", "Tiny Thunder",
                    "Pancake", "Waffles", "Mochi", "Tofu",
                    "Beans", "Noodle", "Pudding", "Boba",
                    "Churro", "Pretzel", "Dumpling", "Muffin",
                ],
            },
            {
                "id": "animal_quiz",
                "title": "What Animal Are You?",
                "btn": "Find Out",
                "loading": ["Sniffing your vibe...", "Checking your spirit animal...", "Consulting nature..."],
                "pool": [
                    "Cat -- independent, secretly affectionate, and judges everyone from a distance",
                    "Golden Retriever -- enthusiastic, loyal, and you make everyone smile",
                    "Owl -- wise, nocturnal, and you see things others miss",
                    "Fox -- clever, adaptable, and you always find a way",
                    "Sloth -- relaxed, unbothered, and you move at your own pace",
                    "Dolphin -- social, intelligent, and you love showing off",
                    "Wolf -- loyal to your pack, fierce when challenged",
                    "Otter -- playful, curious, and you hold hands with your friends",
                    "Penguin -- well-dressed, slightly clumsy, and committed to your partner",
                    "Red Panda -- adorable, underestimated, and surprisingly fierce",
                    "Capybara -- everyone loves you and you get along with literally anyone",
                    "Raccoon -- resourceful, nocturnal, and you eat trash at 2AM",
                    "Axolotl -- unique, regenerative, and you smile even when things are bad",
                    "Crow -- intelligent, holds grudges, and remembers everything",
                ],
            },
        ],
    },
    "craftrank": {
        "name": "CraftRank",
        "tag": "gaming",
        "yt": "@CraftRank",
        "accent": "#ff6666",
        "accent_bg": "rgba(255,102,102,.12)",
        "hook": "Ranking everything in gaming. No mercy.",
        "desc": "Game rankings, tier lists, and controversial ratings.",
        "content": [
            {"t": "Minecraft mobs ranked by usefulness", "p": "S-tier: Iron Golem, Villager, Horse. F-tier: Bat, Polar Bear, Silverfish. Fight me."},
        ],
        "generators": [
            {
                "id": "rank_gen",
                "title": "Random Game Ranking",
                "btn": "Generate Ranking",
                "loading": ["Calculating tier list...", "Measuring game quality...", "Consulting the council..."],
                "pool": [
                    "Minecraft PvP: A-tier -- skill ceiling is insane but the combat update divided everyone",
                    "Fortnite Building: S-tier mechanic trapped in a C-tier community",
                    "Roblox Obbies: B-tier -- simple but somehow always fun at 3AM",
                    "Battle Royale genre: was S-tier, now C-tier from oversaturation",
                    "Survival games: A-tier concept, D-tier when you're alone",
                    "Speedrunning: S-tier -- pure skill, no excuses",
                    "Loot boxes: F-tier -- gambling for kids with extra steps",
                    "Open world games: B-tier -- great until you realize it's just walking",
                    "Minecraft Redstone: S-tier for 2% of players, confusing noise for the rest",
                    "Co-op games: A-tier if you have friends, unranked if you don't",
                    "Mobile gaming: D-tier for quality, S-tier for accessibility",
                    "Indie games: A-tier -- more innovation than AAA studios combined",
                    "MMORPGs: B-tier -- incredible worlds, terrible communities",
                    "Fighting games: S-tier skill gap, F-tier new player experience",
                    "Horror games: A-tier until you realize you're just walking through doors",
                    "Sandbox games: S-tier for creativity, D-tier for people who need objectives",
                ],
            },
            {
                "id": "hot_or_not",
                "title": "Hot or Not? Game Feature Edition",
                "btn": "Rate a Feature",
                "loading": ["Loading game feature...", "Preparing judgment...", "Consulting the tier list gods..."],
                "pool": [
                    "Double jump -- HOT. Should be in every game. No exceptions.",
                    "Fall damage -- NOT. Nobody asked to be punished for gravity.",
                    "Grappling hooks -- HOT. Instantly makes any game 10x better.",
                    "Escort missions -- NOT. The NPC walks too slow and has a death wish.",
                    "Photo mode -- HOT. Turning games into art galleries.",
                    "Unskippable cutscenes -- NOT. Respect my time.",
                    "New Game+ -- HOT. Reward me for beating your game.",
                    "Inventory limits -- NOT. Let me hoard in peace.",
                    "Day/night cycles -- HOT. Makes worlds feel alive.",
                    "Quick time events -- NOT. I came to play, not to play Simon Says.",
                    "Character customization -- HOT. I need to spend 3 hours on my eyebrows.",
                    "Microtransactions -- NOT. The worst thing to happen to gaming.",
                    "Fishing minigames -- HOT. Inexplicably relaxing in every game.",
                    "Water levels -- NOT. Nobody in the history of gaming has enjoyed a water level.",
                    "Boss rush mode -- HOT. Skip the filler, give me the fights.",
                    "Weapon durability -- NOT. Let me use the cool sword without anxiety.",
                ],
            },
        ],
    },
    "wouldyourather": {
        "name": "WouldYouRather",
        "tag": "trivia",
        "yt": "@WouldYouRather",
        "accent": "#ff8800",
        "accent_bg": "rgba(255,136,0,.12)",
        "hook": "Impossible choices. No good answers.",
        "desc": "Would You Rather dilemmas that break your brain.",
        "content": [],
        "generators": [
            {
                "id": "wyr",
                "title": "Would You Rather",
                "btn": "Get Dilemma",
                "loading": ["Creating impossible choice...", "Loading moral dilemma...", "Preparing brain damage..."],
                "pool": [
                    "Would you rather have unlimited money but no friends, or unlimited friends but no money?",
                    "Would you rather know how you die or when you die?",
                    "Would you rather be able to fly but only 3 feet off the ground, or run at 100mph but only in a straight line?",
                    "Would you rather have every song you listen to be slightly off-key, or every movie you watch be 10 minutes too long?",
                    "Would you rather always be 10 minutes late or 20 minutes early?",
                    "Would you rather live without music or without movies?",
                    "Would you rather have a rewind button or a pause button for your life?",
                    "Would you rather be famous but hated, or unknown but loved?",
                    "Would you rather eat only pizza for a year or never eat pizza again?",
                    "Would you rather fight one horse-sized duck or 100 duck-sized horses?",
                    "Would you rather have unlimited battery on your phone or unlimited fuel in your car?",
                    "Would you rather be able to talk to animals or speak every human language?",
                    "Would you rather always say what's on your mind or never speak again?",
                    "Would you rather have no internet for a month or no phone for a month?",
                    "Would you rather live in a world with no rules or a world where you make all the rules?",
                    "Would you rather have a photographic memory or be able to forget anything on command?",
                    "Would you rather relive the same day forever or fast-forward 10 years?",
                    "Would you rather be the smartest person alive but unhappy, or average intelligence but always happy?",
                    "Would you rather live in the past with future knowledge, or the future with no knowledge?",
                    "Would you rather have x-ray vision or super hearing?",
                ],
            },
        ],
    },
    "justgerald": {
        "name": "JustGerald",
        "tag": "comedy",
        "yt": "@JustGerald",
        "accent": "#77dd00",
        "accent_bg": "rgba(119,221,0,.12)",
        "hook": "Gerald does things. Regrets follow.",
        "desc": "Awkward moments, relatable fails, and Gerald being Gerald.",
        "content": [],
        "generators": [
            {
                "id": "gerald_moment",
                "title": "Gerald Moment Generator",
                "btn": "What Did Gerald Do?",
                "loading": ["Gerald is thinking...", "This can't end well...", "Gerald has entered the chat..."],
                "pool": [
                    "Gerald waved back at someone who wasn't waving at him. In a meeting.",
                    "Gerald tried to push a pull door. Twice. While people watched.",
                    "Gerald said 'you too' when the waiter said 'enjoy your meal.'",
                    "Gerald accidentally liked a photo from 3 years ago while stalking someone.",
                    "Gerald walked into a glass door at full speed in front of his crush.",
                    "Gerald sent a text about someone... to that someone.",
                    "Gerald confidently gave wrong directions to a tourist. For 5 minutes.",
                    "Gerald tried to high-five someone who was reaching for something behind him.",
                    "Gerald accidentally joined a zoom meeting with his camera on in bed.",
                    "Gerald called his teacher 'mom' in high school. He was in college.",
                    "Gerald laughed at a joke that wasn't a joke.",
                    "Gerald said 'goodbye' on the phone and then kept talking.",
                    "Gerald stood up to leave and walked the wrong direction. Twice.",
                    "Gerald tried to be cool leaning on a wall. The wall was a door.",
                    "Gerald wore his shirt inside out for an entire day and nobody told him.",
                    "Gerald replied 'lol' to a serious message about someone's feelings.",
                    "Gerald forgot someone's name 3 seconds after being introduced.",
                    "Gerald tried to tell a joke. Nobody laughed. He explained it. Still nothing.",
                    "Gerald accidentally screen-shared his search history in a presentation.",
                    "Gerald pointed at someone and said 'that's the guy' when the guy was standing right behind him.",
                ],
            },
            {
                "id": "awkward_scenario",
                "title": "Awkward Scenario Generator",
                "btn": "Generate Scenario",
                "loading": ["Loading cringe...", "Preparing secondhand embarrassment...", "Activating awkward mode..."],
                "pool": [
                    "You're in a quiet elevator and your stomach makes a noise that sounds like a whale",
                    "You accidentally FaceTimed someone while talking about them",
                    "You're singing in the car and lock eyes with someone at a red light",
                    "You go for a handshake and they go for a fist bump. You grab their fist.",
                    "You tell a long story and realize halfway through you already told them yesterday",
                    "Someone holds the door for you but you're too far away. Now you have to jog.",
                    "You wave at someone in public and a stranger waves back thinking it was for them",
                    "You're on a video call and realize your camera has been on the whole time",
                    "You say 'see you later' to someone and then walk the same direction",
                    "You're eating alone and someone asks 'are you waiting for someone?' No. Just eating. Alone.",
                    "You laugh out loud at your phone in a silent waiting room",
                    "You're walking towards someone and you both keep moving the same direction to dodge each other",
                    "Someone asks you what you do for fun and your mind goes completely blank",
                    "You accidentally send a voice message instead of deleting it",
                ],
            },
        ],
    },
    "mindworm": {
        "name": "MindWorm",
        "tag": "knowledge",
        "yt": "@MindWorm",
        "accent": "#ff5577",
        "accent_bg": "rgba(255,85,119,.12)",
        "hook": "Thoughts that burrow into your brain and never leave.",
        "desc": "Intrusive thoughts, brain teasers, and things you can't unthink.",
        "content": [],
        "generators": [
            {
                "id": "brain_worm",
                "title": "Brain Worm of the Day",
                "btn": "Infect My Brain",
                "loading": ["Burrowing into your consciousness...", "Planting the thought...", "No going back now..."],
                "pool": [
                    "Your tongue never sits comfortably in your mouth. You're thinking about it now.",
                    "You've never seen your own face -- only reflections and photos.",
                    "Every decision you've ever made led you to reading this exact sentence right now.",
                    "You breathe manually now. You're welcome.",
                    "Somewhere, the oldest person alive was once the youngest person alive.",
                    "You've walked past at least one person who remembers you but you've completely forgotten.",
                    "The voice in your head has been narrating your entire life and you never asked it to.",
                    "Nothing is on fire. Fire is on things.",
                    "Your skeleton is wet right now.",
                    "You've never actually been in a 'room'. You're always in the universe.",
                    "At some point your parents put you down and never picked you up again.",
                    "There's a day every year that's the anniversary of your death. You just don't know which one yet.",
                    "Every mirror you've ever bought was used.",
                    "You can't hum while holding your nose closed.",
                    "Your brain named itself.",
                    "The word 'bed' looks like a bed.",
                    "You're the only person who will ever know what your internal voice sounds like.",
                    "Somewhere right now, a random stranger is using a mug that used to be yours.",
                    "You've never been in an empty room. You were always in it.",
                    "Everything you see is actually the past because light takes time to reach your eyes.",
                    "The letter W starts with 'double-u' but looks like 'double-v'.",
                    "You trust your chair more than you trust most people.",
                    "Clapping is just hitting yourself because you like something.",
                    "Sand is called sand because it's between the sea and the land.",
                ],
            },
        ],
    },
    "factoryfiles": {
        "name": "FactoryFiles",
        "tag": "knowledge",
        "yt": "@FactoryFiles",
        "accent": "#aabb00",
        "accent_bg": "rgba(170,187,0,.12)",
        "hook": "The files they don't want you to open.",
        "desc": "Conspiracies, cover-ups, and things that make you go hmm.",
        "content": [],
        "generators": [
            {
                "id": "conspiracy",
                "title": "Conspiracy Theory Generator",
                "btn": "Generate Conspiracy",
                "loading": ["Accessing classified files...", "Decrypting redacted documents...", "The truth is loading...", "They're watching us load this..."],
                "pool": [
                    "What if WiFi signals are slowly rewriting our memories and nobody notices because... we can't remember?",
                    "Every time you get deja vu, it's because the simulation reset and you're catching a glitch",
                    "The reason we yawn is because the simulation needs to sync our consciousness with the server",
                    "Pigeons are government drones. Have you ever seen a baby pigeon? Exactly.",
                    "Dreams are just trailers for alternate timelines you didn't choose",
                    "The Bermuda Triangle is just an area where the render distance of reality drops too low",
                    "Cats already know everything. They're just not telling us.",
                    "What if history is just being updated and nobody remembers the old version?",
                    "The reason you sometimes feel like you're being watched is because NPCs glitch when they stare too long",
                    "Trees are alien data towers harvesting our CO2 as a power source",
                    "Parallel parking was invented to keep us distracted from the real issues",
                    "Every time you forget why you walked into a room, someone accessed your save file",
                    "The ocean is only explored 5% because they know what's in the other 95%",
                    "Autocorrect is slowly training us to speak a language only AI understands",
                    "Shopping carts have one bad wheel on purpose to slow you down so you buy more",
                    "What if clouds are just nature's pop-up ads?",
                    "The snooze button was designed to make you late so the economy depends on coffee",
                    "Elevators don't actually move. The building moves around the elevator.",
                ],
            },
            {
                "id": "secret",
                "title": "What Secret Are You Hiding?",
                "btn": "Reveal Secret",
                "loading": ["Scanning your browser history...", "Analyzing micro-expressions...", "Decoding your vibe..."],
                "pool": [
                    "You have a playlist you'd never let anyone see.",
                    "You've googled something so weird you immediately cleared your history.",
                    "You pretend to like something just because everyone else does.",
                    "You have a backup plan for a situation that will literally never happen.",
                    "You've rehearsed an argument in the shower that you'll never actually have.",
                    "You know the WiFi password at a place you're no longer welcome at.",
                    "You have an opinion so controversial you've never said it out loud.",
                    "You've pretended not to see someone in public to avoid talking to them.",
                    "You keep a mental list of people you've silently judged.",
                    "You've stayed up until 4AM reading about something completely useless.",
                    "You've faked a phone call to avoid a conversation.",
                    "You have a screenshot on your phone that could start a war.",
                    "You've said 'I'm fine' at least 2,000 times when you were not fine.",
                    "You have a talent nobody knows about because you're too shy to show it.",
                ],
            },
        ],
    },
    "darkdecisions": {
        "name": "Dark Decisions",
        "tag": "drama",
        "yt": "@DarkDecisions",
        "accent": "#cc44ff",
        "accent_bg": "rgba(204,68,255,.12)",
        "hook": "Every choice has a cost. What would you do?",
        "desc": "Moral dilemmas, dark choices, and impossible scenarios.",
        "content": [],
        "generators": [
            {
                "id": "dark_dilemma",
                "title": "Dark Dilemma Generator",
                "btn": "Get Dilemma",
                "loading": ["Loading moral crisis...", "Preparing impossible choice...", "There are no good options..."],
                "pool": [
                    "You can save 5 strangers or 1 person you love. You have 10 seconds to choose.",
                    "You're offered $10 million but someone you'll never meet loses 10 years of their life.",
                    "You can know exactly when everyone around you will die, but you can never tell them.",
                    "You find proof your best friend committed a crime. Do you turn them in?",
                    "You can erase one painful memory, but you'll also lose the lesson it taught you.",
                    "You discover your entire life has been a simulation. Do you want to wake up?",
                    "You can read everyone's thoughts for 24 hours. After that, they can read yours for a week.",
                    "You're given a button that gives you $1,000 every time you press it, but shortens a stranger's life by 1 day.",
                    "You can restart your life from age 10 with all your current knowledge, but everyone else forgets you.",
                    "You find out a close friend has been lying to you for years to protect your feelings. Do you confront them?",
                    "You can guarantee your child becomes wildly successful, but they'll never be truly happy.",
                    "You can live forever but you'll watch everyone you love grow old and die.",
                    "You can prevent one historical tragedy but something equally bad will happen elsewhere.",
                    "You overhear a stranger planning something terrible. If you intervene, your life is at risk.",
                    "You can have perfect health forever but you can never form deep relationships again.",
                    "Everyone you've ever wronged suddenly remembers exactly what you did. How do you face them?",
                ],
            },
            {
                "id": "alignment",
                "title": "Moral Alignment Check",
                "btn": "Check Alignment",
                "loading": ["Scanning your soul...", "Weighing your karma...", "Consulting the moral compass..."],
                "pool": [
                    "Lawful Good -- you follow the rules AND do the right thing. Boring but respectable.",
                    "Neutral Good -- you do what's right regardless of rules. The hero nobody asked for.",
                    "Chaotic Good -- you break rules to help people. Robin Hood energy.",
                    "Lawful Neutral -- you follow rules even when they're dumb. Order above all.",
                    "True Neutral -- you just want to be left alone. Switzerland in human form.",
                    "Chaotic Neutral -- you do whatever benefits you. Wild card.",
                    "Lawful Evil -- you use the system against people. Corporate villain energy.",
                    "Neutral Evil -- you'll do anything to get ahead. No loyalty, no code.",
                    "Chaotic Evil -- you just want to watch the world burn. Joker mode.",
                    "Unaligned -- you don't have consistent morals. You're basically an NPC.",
                    "Lawful Chaotic -- you make your own rules and follow them religiously. Confusing but iconic.",
                    "True Good -- you're annoyingly nice and everyone suspects you're hiding something.",
                ],
            },
        ],
    },
    "lovestruck": {
        "name": "Lovestruck",
        "tag": "drama",
        "yt": "@Lovestruck",
        "accent": "#ff6699",
        "accent_bg": "rgba(255,102,153,.12)",
        "hook": "Love stories that hit you right in the feels.",
        "desc": "Romantic stories, relationship drama, and love advice.",
        "content": [],
        "generators": [
            {
                "id": "ship_name",
                "title": "Ship Name Generator",
                "btn": "Generate Ship Name",
                "loading": ["Combining souls...", "Merging destinies...", "Calculating chemistry..."],
                "pool": [
                    "Stardust & Chaos", "Neon Hearts", "Midnightflame", "Velvet Thunder",
                    "Eclipse & Dawn", "Crimson Whisper", "Lunar Tide", "Ember & Frost",
                    "Silken Storm", "Phantom Kiss", "Electric Honey", "Golden Ruin",
                    "Twisted Bloom", "Savage Grace", "Neon Noir", "Bitter Sweet Symphony",
                    "Dark Orchid", "Wild Compass", "Silver Tongue & Iron Heart", "Starfall",
                    "Burning Patience", "Quiet Riot", "Midnight Sun", "Paper Crown",
                    "Ghost & Flame", "Velvet Knife", "Sugar Venom", "Broken Halo",
                    "Electric Storm", "Frostfire", "Thorn & Rose", "Atlas & Echo",
                ],
            },
            {
                "id": "romance_scenario",
                "title": "Romantic Scenario Generator",
                "btn": "Generate Scenario",
                "loading": ["Writing the script...", "Setting the mood...", "Choosing the soundtrack..."],
                "pool": [
                    "You bump into your ex at a coffee shop. They're with someone new. Your song starts playing.",
                    "You find a love letter in a library book that's addressed to someone with your name.",
                    "Your best friend confesses feelings for you on the last day of summer.",
                    "A stranger gives you their number on a napkin, but you can only read half of it.",
                    "You match with your roommate on a dating app. Neither of you swipe right... yet.",
                    "You realize you've been in love with your best friend after they start dating someone else.",
                    "A delayed flight means you spend 8 hours talking to a stranger. You never get their last name.",
                    "You receive a text meant for someone else that says 'I can't stop thinking about you.'",
                    "Someone dedicates a song to you at a concert. You have no idea who they are.",
                    "You find your name written in someone's journal. You've only met them twice.",
                    "Your childhood best friend moves back to town after 10 years. Everything is different. Nothing has changed.",
                    "You're stuck in an elevator with someone you've had a crush on for months.",
                    "A fortune teller says you'll meet the love of your life tomorrow. You wake up terrified.",
                    "You overhear someone describing their perfect partner. They're describing you exactly.",
                ],
            },
        ],
    },
    "mythboosted": {
        "name": "MythBoosted",
        "tag": "trivia",
        "yt": "@MythBoosted",
        "accent": "#44ddff",
        "accent_bg": "rgba(68,221,255,.12)",
        "hook": "Think you know what's real? Prove it.",
        "desc": "Myth vs fact challenges that trick even smart people.",
        "content": [],
        "generators": [
            {
                "id": "myth_or_fact",
                "title": "Myth or Fact?",
                "btn": "Get Claim",
                "loading": ["Loading suspicious claim...", "Preparing to trick you...", "This one's tricky..."],
                "pool": [
                    "Goldfish have a 3-second memory -- MYTH! They can remember things for months.",
                    "Lightning never strikes the same place twice -- MYTH! The Empire State Building gets hit ~25 times a year.",
                    "Humans only use 10% of their brain -- MYTH! Brain scans show we use virtually all of it.",
                    "Cracking your knuckles causes arthritis -- MYTH! Studies found zero connection.",
                    "Chameleons change color to blend in -- MYTH! They change color based on mood and temperature.",
                    "The Great Wall of China is visible from space -- MYTH! It's too narrow to see without aid.",
                    "Bananas grow on trees -- MYTH! Banana plants are technically giant herbs.",
                    "Bulls are angered by the color red -- MYTH! Bulls are colorblind to red. They charge the movement.",
                    "Bats are blind -- MYTH! Most bats can see perfectly well.",
                    "Humans swallow 8 spiders a year in their sleep -- MYTH! Vibrations from breathing keep spiders away.",
                    "Octopuses have blue blood -- FACT! It contains copper instead of iron.",
                    "A day on Venus is longer than a year on Venus -- FACT! 243 Earth days vs 225 Earth days.",
                    "Honey never expires -- FACT! 3,000-year-old honey was found edible in Egyptian tombs.",
                    "Scotland's national animal is the unicorn -- FACT! It has been since the 12th century.",
                    "Strawberries are not actually berries -- FACT! But bananas are.",
                    "There are more trees on Earth than stars in the Milky Way -- FACT! ~3 trillion trees vs ~400 billion stars.",
                    "A group of crows is called a murder -- FACT! And a group of flamingos is a flamboyance.",
                    "Cleopatra lived closer to the Moon landing than the building of the Great Pyramid -- FACT!",
                    "Oxford University is older than the Aztec Empire -- FACT! Oxford started in 1096, Aztec Empire in 1428.",
                    "Sharks are older than trees -- FACT! Sharks have existed for ~450 million years, trees for ~350 million.",
                ],
            },
        ],
    },
}

TAG_STYLES = {
    "gaming": ("rgba(255,80,80,.12)", "#ff6b6b"),
    "horror": ("rgba(160,80,255,.12)", "#b070ff"),
    "knowledge": ("rgba(80,200,255,.12)", "#50c8ff"),
    "relatable": ("rgba(255,200,50,.12)", "#f0c040"),
    "comedy": ("rgba(100,220,100,.12)", "#60dd60"),
    "drama": ("rgba(255,100,150,.12)", "#ff7090"),
    "motivation": ("rgba(255,160,60,.12)", "#ffa040"),
    "trivia": ("rgba(0,210,180,.12)", "#00d2b4"),
}

# Generator visual styles:
# "spin"   = slot-machine text scramble then lands on result
# "loot"   = chest opening with rarity-colored result + particles
# "meter"  = animated gauge that bounces then settles
# "type"   = typewriter text reveal
# "flip"   = card flip animation
# "reveal" = blurred text, click/wait to unblur

GEN_STYLE_MAP = {
    "glitch_name": "spin", "glitch_challenge": "spin",
    "build_idea": "spin", "mob_quiz": "flip",
    "hot_take": "spin", "rage_rating": "meter", "mc_hot_take": "spin",
    "mc_worst_teammate": "flip", "fn_hot_take": "spin", "fn_rage_rating": "meter",
    "loot_drop": "loot", "mystery_weapon": "spin",
    "roblox_game_idea": "spin", "roblox_character": "flip",
    "psych_fact": "type", "shadow_personality": "flip",
    "trivia": "reveal", "sigma_quote": "type", "grindset_level": "spin",
    "pet_name": "spin", "animal_quiz": "flip",
    "rank_gen": "spin", "hot_or_not": "flip",
    "wyr": "type", "gerald_moment": "type", "awkward_scenario": "type",
    "brain_worm": "type", "conspiracy": "type", "secret": "flip",
    "dark_dilemma": "type", "alignment": "flip",
    "ship_name": "spin", "romance_scenario": "type",
    "myth_or_fact": "reveal",
}

# ─── Channel page template ──────────────────────────────────────────────────

def build_channel_page(slug, ch):
    tag_bg, tag_color = TAG_STYLES.get(ch["tag"], ("rgba(128,128,128,.12)", "#888"))

    content_html = ""
    for item in ch.get("content", []):
        content_html += f'    <div class="item"><h3>{item["t"]}</h3><p>{item["p"]}</p></div>\n'

    content_section = ""
    if content_html.strip():
        content_section = f'''<div class="section">
    <h2>Did You Know?</h2>
{content_html}</div>'''

    generators_html = ""
    for gen in ch.get("generators", []):
        style = GEN_STYLE_MAP.get(gen["id"], "spin")
        generators_html += f'''
    <div class="gen-card" id="gen-{gen['id']}" data-style="{style}">
        <h3>{gen['title']}</h3>
        <button class="gen-btn" id="btn-{gen['id']}" onclick="runGen_{gen['id']}()">
            {gen['btn']}
        </button>
        <div class="gen-stage" id="stage-{gen['id']}" style="display:none">
            <div class="gen-spinner"></div>
            <div class="gen-scramble" id="scramble-{gen['id']}"></div>
            <p class="gen-status" id="status-{gen['id']}"></p>
        </div>
        <div class="gen-result-wrap" id="result-{gen['id']}" style="display:none">
            <div class="gen-result-inner" id="inner-{gen['id']}"></div>
        </div>
        <button class="gen-btn gen-again" id="again-{gen['id']}" style="display:none" onclick="runGen_{gen['id']}()">
            Go Again
        </button>
        <div class="confetti-container" id="confetti-{gen['id']}"></div>
    </div>
'''

    gen_scripts = ""
    for gen in ch.get("generators", []):
        pool_js = json.dumps(gen["pool"])
        loading_js = json.dumps(gen["loading"])
        style = GEN_STYLE_MAP.get(gen["id"], "spin")
        gen_scripts += f'''
function runGen_{gen['id']}() {{
    var pool={pool_js};
    var msgs={loading_js};
    var style="{style}";
    _runGenerator("{gen['id']}",pool,msgs,style,"{slug}","{gen['id']}");
}}
'''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{ch["name"]} &mdash; BDS Anthony</title>
    <meta name="description" content="{ch["desc"]}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Mono:wght@700&display=swap" rel="stylesheet">
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA_ID}');</script>
    <style>
        *,*::before,*::after{{margin:0;padding:0;box-sizing:border-box}}
        :root{{--bg:#0b0b0f;--card:#14141b;--border:#1f1f2b;--text:#eae8f2;--muted:#8b89a0;--accent:{ch["accent"]};--discord:#5865F2}}
        body{{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);line-height:1.6;overflow-x:hidden}}
        a{{color:var(--accent);text-decoration:none}}
        .back{{display:inline-block;padding:1rem 1.5rem;font-size:.85rem}}.back:hover{{text-decoration:underline}}
        .hero{{text-align:center;padding:3rem 1.5rem 2rem}}
        .badge{{display:inline-block;font-size:.7rem;text-transform:uppercase;letter-spacing:.1em;padding:.3rem .8rem;border-radius:50px;font-weight:700;margin-bottom:1rem;background:{tag_bg};color:{tag_color}}}
        .hero h1{{font-size:clamp(2rem,7vw,3.2rem);font-weight:800;letter-spacing:-.02em;margin-bottom:.6rem}}
        .hero .hook{{color:var(--muted);font-size:clamp(1rem,2.5vw,1.15rem);max-width:520px;margin:0 auto 1.5rem}}
        .btn{{display:inline-block;padding:.7rem 1.8rem;border-radius:50px;font-weight:700;font-size:.9rem;transition:transform .15s,box-shadow .15s;cursor:pointer;border:none}}
        .btn:hover{{transform:translateY(-2px)}}
        .btn-primary{{background:var(--accent);color:#111}}.btn-primary:hover{{box-shadow:0 6px 20px {ch["accent_bg"]}}}
        .btn-discord{{background:var(--discord);color:#fff;margin-left:.5rem}}.btn-discord:hover{{box-shadow:0 6px 20px rgba(88,101,242,.3)}}
        .hero-buttons{{display:flex;gap:.6rem;justify-content:center;flex-wrap:wrap}}
        .section{{max-width:720px;margin:0 auto;padding:2rem 1.5rem}}
        .section h2{{font-size:1.15rem;font-weight:700;margin-bottom:1.2rem;text-transform:uppercase;letter-spacing:.08em;color:var(--accent)}}
        .item{{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:1.2rem 1.4rem;margin-bottom:.8rem}}
        .item h3{{font-size:1rem;font-weight:700;margin-bottom:.3rem}}.item p{{color:var(--muted);font-size:.88rem;line-height:1.55}}

        .gen-section{{max-width:720px;margin:0 auto;padding:1rem 1.5rem 2rem}}
        .gen-section h2{{font-size:1.15rem;font-weight:700;margin-bottom:1.2rem;text-transform:uppercase;letter-spacing:.08em;color:var(--accent);text-align:center}}
        .gen-card{{background:var(--card);border:2px solid var(--border);border-radius:18px;padding:2rem 1.5rem;margin-bottom:1.2rem;text-align:center;position:relative;overflow:hidden;transition:border-color .4s,box-shadow .4s}}
        .gen-card.active{{border-color:var(--accent);box-shadow:0 0 30px {ch["accent_bg"]},0 0 60px {ch["accent_bg"]}}}
        .gen-card h3{{font-size:1.15rem;font-weight:800;margin-bottom:1.2rem;letter-spacing:-.01em}}
        .gen-btn{{background:var(--accent);color:#111;border:none;padding:.85rem 2.4rem;border-radius:50px;font-weight:800;font-size:1rem;cursor:pointer;transition:transform .15s,box-shadow .15s;letter-spacing:.01em}}
        .gen-btn:hover{{transform:translateY(-3px) scale(1.02);box-shadow:0 8px 25px {ch["accent_bg"]}}}
        .gen-btn:active{{transform:scale(.97)}}
        .gen-again{{background:transparent;color:var(--text);margin-top:1.2rem;font-size:.88rem;padding:.65rem 1.8rem;border:1px solid var(--border)}}
        .gen-again:hover{{background:var(--accent);color:#111;border-color:var(--accent)}}

        .gen-stage{{margin:1.5rem 0 .5rem;min-height:80px}}
        .gen-spinner{{width:40px;height:40px;border:3px solid var(--border);border-top-color:var(--accent);border-radius:50%;margin:0 auto .8rem;animation:spin .6s linear infinite}}
        @keyframes spin{{to{{transform:rotate(360deg)}}}}
        .gen-scramble{{font-family:'Space Mono',monospace;font-size:1.1rem;color:var(--accent);min-height:1.4em;letter-spacing:.02em;opacity:.7}}
        .gen-status{{color:var(--muted);font-size:.78rem;margin-top:.6rem;font-style:italic}}

        .gen-result-wrap{{margin-top:1.2rem;perspective:800px}}
        .gen-result-inner{{font-size:1.2rem;font-weight:700;color:#fff;padding:1.5rem 1.2rem;border-radius:14px;line-height:1.5;position:relative}}
        .gen-result-inner.style-spin{{background:linear-gradient(135deg,rgba(255,255,255,.06),rgba(255,255,255,.02));border:1px solid var(--accent);animation:resultSlam .4s cubic-bezier(.17,.67,.29,1.4)}}
        .gen-result-inner.style-loot{{border:2px solid;animation:lootReveal .5s ease}}
        .gen-result-inner.style-meter{{background:var(--bg);border:1px solid var(--border);padding:0;overflow:hidden;border-radius:14px}}
        .gen-result-inner.style-type{{background:linear-gradient(135deg,rgba(255,255,255,.04),rgba(255,255,255,.01));border:1px solid var(--border);font-family:'Inter',sans-serif;font-weight:500;font-size:1.05rem;text-align:left}}
        .gen-result-inner.style-flip{{animation:cardFlip .6s ease;transform-origin:center;background:linear-gradient(135deg,rgba(255,255,255,.06),rgba(255,255,255,.02));border:1px solid var(--accent)}}
        .gen-result-inner.style-reveal{{background:linear-gradient(135deg,rgba(255,255,255,.05),rgba(255,255,255,.02));border:1px solid var(--accent);animation:resultSlam .4s ease}}

        .meter-bar-outer{{height:48px;background:var(--card);position:relative}}
        .meter-bar-inner{{height:100%;transition:width 1.5s cubic-bezier(.34,1.56,.64,1);display:flex;align-items:center;justify-content:flex-end;padding-right:12px;font-weight:800;font-size:1.1rem;color:#111}}
        .meter-label{{padding:1rem;font-weight:700;font-size:1rem}}

        .loot-common .gen-result-inner{{border-color:#888;color:#aaa}}
        .loot-uncommon .gen-result-inner{{border-color:#44cc44;color:#66ee66;box-shadow:0 0 15px rgba(68,204,68,.2)}}
        .loot-rare .gen-result-inner{{border-color:#4488ff;color:#66aaff;box-shadow:0 0 20px rgba(68,136,255,.25)}}
        .loot-epic .gen-result-inner{{border-color:#aa44ff;color:#cc77ff;box-shadow:0 0 25px rgba(170,68,255,.3)}}
        .loot-legendary .gen-result-inner{{border-color:#ffaa00;color:#ffcc44;box-shadow:0 0 30px rgba(255,170,0,.35),0 0 60px rgba(255,170,0,.15)}}
        .loot-mythic .gen-result-inner{{border-color:#ff2244;color:#ff6677;box-shadow:0 0 40px rgba(255,34,68,.4),0 0 80px rgba(255,34,68,.2)}}
        .loot-rarity-tag{{display:inline-block;font-size:.65rem;text-transform:uppercase;letter-spacing:.12em;padding:.25rem .7rem;border-radius:50px;font-weight:800;margin-bottom:.6rem}}

        @keyframes resultSlam{{0%{{transform:scale(0)translateY(20px);opacity:0}}60%{{transform:scale(1.05)translateY(-5px)}}100%{{transform:scale(1)translateY(0);opacity:1}}}}
        @keyframes lootReveal{{0%{{transform:scale(0)rotateY(90deg);opacity:0}}50%{{transform:scale(1.1)rotateY(-10deg)}}100%{{transform:scale(1)rotateY(0);opacity:1}}}}
        @keyframes cardFlip{{0%{{transform:rotateY(180deg)scale(.8);opacity:0}}100%{{transform:rotateY(0)scale(1);opacity:1}}}}
        @keyframes typeChar{{from{{width:0}}to{{width:100%}}}}
        @keyframes shake{{0%,100%{{transform:translateX(0)}}20%{{transform:translateX(-4px)}}40%{{transform:translateX(4px)}}60%{{transform:translateX(-3px)}}80%{{transform:translateX(2px)}}}}
        .shake{{animation:shake .4s ease}}

        .confetti-container{{position:absolute;inset:0;pointer-events:none;overflow:hidden;z-index:10}}
        .confetti-piece{{position:absolute;width:8px;height:8px;border-radius:2px;animation:confettiFall 1.5s ease-out forwards;opacity:0}}
        @keyframes confettiFall{{0%{{transform:translateY(0)rotate(0deg)scale(0);opacity:1}}50%{{opacity:1}}100%{{transform:translateY(200px)rotate(720deg)scale(1);opacity:0}}}}

        .discord-box{{background:linear-gradient(135deg,rgba(88,101,242,.12),rgba(88,101,242,.04));border:1px solid rgba(88,101,242,.25);border-radius:14px;padding:1.8rem;text-align:center;margin:2rem auto;max-width:720px}}
        .discord-box h2{{color:#fff;font-size:1.2rem;font-weight:700;margin-bottom:.5rem;text-transform:none;letter-spacing:normal}}
        .discord-box p{{color:var(--muted);font-size:.9rem;margin-bottom:1rem;max-width:480px;margin-left:auto;margin-right:auto}}
        .discord-box .btn-discord{{font-size:1rem;padding:.8rem 2.2rem}}
        footer{{text-align:center;padding:2rem 1rem;color:var(--muted);font-size:.75rem;border-top:1px solid var(--border);margin-top:1rem}}
        footer a{{color:var(--muted)}}
        @media(max-width:600px){{.section,.gen-section{{padding:1.5rem 1rem}}.hero{{padding:2rem 1rem 1.5rem}}}}
    </style>
    {ADSENSE}
</head>
<body>

<a class="back" href="/channels/">&larr; All Channels</a>

<div class="hero">
    <span class="badge">{ch["tag"].upper()}</span>
    <h1>{ch["name"]}</h1>
    <p class="hook">{ch["hook"]}</p>
    <div class="hero-buttons">
        <a class="btn btn-primary" href="https://youtube.com/{ch["yt"]}">Watch on YouTube &rarr;</a>
        <a class="btn btn-discord" href="{DISCORD}">Join Discord</a>
    </div>
</div>

{content_section}

<div class="gen-section">
    <h2>Try These</h2>
{generators_html}
</div>

<div class="discord-box">
    <h2>Play Swords &mdash; Free RPG on Discord</h2>
    <p>Create a character, accept quests, fight monsters, and level up. A full RPG running inside Discord. Join and type <strong>/start</strong> to play.</p>
    <a class="btn btn-discord" href="{DISCORD}">Join &amp; Play Free &rarr;</a>
</div>

<footer>
    <a href="/">Home</a> &middot; <a href="/channels/">Channels</a> &middot; <a href="/privacy.html">Privacy</a>
</footer>

<script>
function _spawnConfetti(containerId){{
    var c=document.getElementById(containerId);if(!c)return;
    c.innerHTML='';
    var colors=['#ff5c87','#7c5cff','#00d2b4','#ffcc00','#ff6b6b','#50c8ff','#60dd60','#ffa040'];
    for(var i=0;i<30;i++){{
        var p=document.createElement('div');p.className='confetti-piece';
        p.style.left=Math.random()*100+'%';p.style.top=Math.random()*30+'%';
        p.style.background=colors[Math.floor(Math.random()*colors.length)];
        p.style.animationDelay=Math.random()*0.5+'s';
        p.style.width=(4+Math.random()*8)+'px';p.style.height=(4+Math.random()*8)+'px';
        c.appendChild(p);
    }}
}}

function _getLootRarity(text){{
    var t=text.toUpperCase();
    if(t.indexOf('MYTHIC')===0)return 'mythic';
    if(t.indexOf('LEGENDARY')===0)return 'legendary';
    if(t.indexOf('EPIC')===0)return 'epic';
    if(t.indexOf('RARE')===0)return 'rare';
    if(t.indexOf('UNCOMMON')===0)return 'uncommon';
    return 'common';
}}

var _lootColors={{common:'#888',uncommon:'#44cc44',rare:'#4488ff',epic:'#aa44ff',legendary:'#ffaa00',mythic:'#ff2244'}};

function _typewriterEffect(el,text,speed){{
    el.textContent='';el.style.display='block';
    var i=0;var iv=setInterval(function(){{
        if(i>=text.length){{clearInterval(iv);return;}}
        el.textContent+=text[i];i++;
    }},speed||25);
}}

function _runGenerator(id,pool,msgs,style,slug,genType){{
    var card=document.getElementById('gen-'+id);
    var btn=document.getElementById('btn-'+id);
    var stage=document.getElementById('stage-'+id);
    var scramble=document.getElementById('scramble-'+id);
    var status=document.getElementById('status-'+id);
    var resultWrap=document.getElementById('result-'+id);
    var inner=document.getElementById('inner-'+id);
    var again=document.getElementById('again-'+id);

    btn.style.display='none';again.style.display='none';resultWrap.style.display='none';
    stage.style.display='block';card.classList.add('active');
    card.className=card.className.replace(/loot-\\w+/g,'').trim();

    var pick=pool[Math.floor(Math.random()*pool.length)];
    var step=0;

    if(style==='spin'){{
        var scrambleIv=setInterval(function(){{
            scramble.textContent=pool[Math.floor(Math.random()*pool.length)].substring(0,40);
        }},80);
        status.textContent=msgs[0];
        var msgIv=setInterval(function(){{
            step++;if(step>=msgs.length){{step=msgs.length-1;}}
            status.textContent=msgs[step];
        }},400);
        setTimeout(function(){{
            clearInterval(scrambleIv);clearInterval(msgIv);
            scramble.textContent='';stage.style.display='none';
            inner.className='gen-result-inner style-spin';inner.textContent=pick;
            resultWrap.style.display='block';again.style.display='inline-block';
            card.classList.remove('active');card.classList.add('shake');
            setTimeout(function(){{card.classList.remove('shake');}},400);
            _spawnConfetti('confetti-'+id);
            if(typeof gtag!=='undefined')gtag('event','generator_click',{{event_category:'generators',event_label:slug+'_'+genType,channel:slug,generator_type:genType}});
        }},msgs.length*400+600);

    }}else if(style==='loot'){{
        scramble.textContent='Opening...';
        status.textContent=msgs[0];
        var msgIv2=setInterval(function(){{step++;if(step<msgs.length)status.textContent=msgs[step];}},500);
        setTimeout(function(){{
            clearInterval(msgIv2);stage.style.display='none';
            var rarity=_getLootRarity(pick);
            card.classList.add('loot-'+rarity);
            var rarityLabel=rarity.toUpperCase();
            var color=_lootColors[rarity]||'#888';
            inner.className='gen-result-inner style-loot';
            inner.innerHTML='<span class="loot-rarity-tag" style="background:'+color+'22;color:'+color+'">'+rarityLabel+'</span><br>'+pick;
            resultWrap.style.display='block';again.style.display='inline-block';
            card.classList.remove('active');
            if(rarity==='legendary'||rarity==='mythic'||rarity==='epic')_spawnConfetti('confetti-'+id);
            if(typeof gtag!=='undefined')gtag('event','generator_click',{{event_category:'generators',event_label:slug+'_'+genType,channel:slug,generator_type:genType}});
        }},msgs.length*500+500);

    }}else if(style==='meter'){{
        scramble.textContent='Measuring...';
        status.textContent=msgs[0];
        var msgIv3=setInterval(function(){{step++;if(step<msgs.length)status.textContent=msgs[step];}},400);
        setTimeout(function(){{
            clearInterval(msgIv3);stage.style.display='none';
            var parts=pick.match(/(\\d+\\.?\\d*)\\/10/);
            var val=parts?parseFloat(parts[1]):5;
            var pct=Math.min(val/10*100,100);
            var hue=120-(val/10*120);
            var barColor='hsl('+hue+',80%,50%)';
            inner.className='gen-result-inner style-meter';
            inner.innerHTML='<div class="meter-bar-outer"><div class="meter-bar-inner" id="mbar-'+id+'" style="width:0%;background:'+barColor+'">'+val+'/10</div></div><div class="meter-label">'+pick.replace(/\\d+\\.?\\d*\\/10\\s*--?\\s*/,'')+'</div>';
            resultWrap.style.display='block';
            setTimeout(function(){{document.getElementById('mbar-'+id).style.width=pct+'%';}},50);
            again.style.display='inline-block';card.classList.remove('active');
            if(val>=8)_spawnConfetti('confetti-'+id);
            if(typeof gtag!=='undefined')gtag('event','generator_click',{{event_category:'generators',event_label:slug+'_'+genType,channel:slug,generator_type:genType}});
        }},msgs.length*400+500);

    }}else if(style==='type'){{
        scramble.textContent='';
        status.textContent=msgs[0];
        var msgIv4=setInterval(function(){{step++;if(step<msgs.length)status.textContent=msgs[step];}},500);
        setTimeout(function(){{
            clearInterval(msgIv4);stage.style.display='none';
            inner.className='gen-result-inner style-type';inner.textContent='';
            resultWrap.style.display='block';
            _typewriterEffect(inner,pick,30);
            again.style.display='inline-block';card.classList.remove('active');
            if(typeof gtag!=='undefined')gtag('event','generator_click',{{event_category:'generators',event_label:slug+'_'+genType,channel:slug,generator_type:genType}});
        }},msgs.length*500+400);

    }}else if(style==='flip'){{
        scramble.textContent='?';scramble.style.fontSize='2rem';
        status.textContent=msgs[0];
        var msgIv5=setInterval(function(){{step++;if(step<msgs.length)status.textContent=msgs[step];}},400);
        setTimeout(function(){{
            clearInterval(msgIv5);scramble.style.fontSize='';stage.style.display='none';
            inner.className='gen-result-inner style-flip';inner.textContent=pick;
            resultWrap.style.display='block';again.style.display='inline-block';
            card.classList.remove('active');_spawnConfetti('confetti-'+id);
            if(typeof gtag!=='undefined')gtag('event','generator_click',{{event_category:'generators',event_label:slug+'_'+genType,channel:slug,generator_type:genType}});
        }},msgs.length*400+600);

    }}else if(style==='reveal'){{
        scramble.textContent='';
        status.textContent=msgs[0];
        var msgIv6=setInterval(function(){{step++;if(step<msgs.length)status.textContent=msgs[step];}},500);
        setTimeout(function(){{
            clearInterval(msgIv6);stage.style.display='none';
            inner.className='gen-result-inner style-reveal';inner.textContent=pick;
            resultWrap.style.display='block';again.style.display='inline-block';
            card.classList.remove('active');
            if(typeof gtag!=='undefined')gtag('event','generator_click',{{event_category:'generators',event_label:slug+'_'+genType,channel:slug,generator_type:genType}});
        }},msgs.length*500+400);
    }}
}}
{gen_scripts}
</script>
</body>
</html>'''


# ─── Homepage ────────────────────────────────────────────────────────────────

def build_homepage():
    # Top 5 get "trending" cards
    trending_keys = ["glitchzone", "rbxrogebait", "mcrogebait", "blocksarebuildable", "lootlore"]
    other_keys = [k for k in CHANNELS if k not in trending_keys]
    
    # Group others by category
    gaming = [k for k in other_keys if CHANNELS[k]["tag"] == "gaming"]
    knowledge = [k for k in other_keys if CHANNELS[k]["tag"] in ("knowledge", "trivia")]
    entertainment = [k for k in other_keys if CHANNELS[k]["tag"] in ("comedy", "drama", "motivation", "relatable")]
    
    def channel_card(slug, ch, big=False):
        tag_bg, tag_color = TAG_STYLES.get(ch["tag"], ("rgba(128,128,128,.12)", "#888"))
        size_class = "ch-big" if big else "ch"
        fire = ' <span class="fire">Trending</span>' if big else ""
        return f'''<a class="{size_class}" href="/{slug}/">
            <span class="tag" style="background:{tag_bg};color:{tag_color}">{ch["tag"].upper()}</span>{fire}
            <h3>{ch["name"]}</h3>
            <p>{ch["hook"]}</p>
        </a>'''
    
    trending_html = "\n".join(channel_card(k, CHANNELS[k], big=True) for k in trending_keys)
    
    def section_html(title, keys):
        if not keys:
            return ""
        cards = "\n".join(channel_card(k, CHANNELS[k]) for k in keys)
        return f'''<div class="cat-section">
        <h3 class="cat-title">{title}</h3>
        <div class="channels">{cards}</div>
    </div>'''
    
    gaming_section = section_html("Gaming", gaming)
    knowledge_section = section_html("Knowledge &amp; Trivia", knowledge)
    entertainment_section = section_html("Entertainment", entertainment)

    # Channel picker pool
    all_names = [(k, CHANNELS[k]["name"], CHANNELS[k]["hook"]) for k in CHANNELS]
    picker_pool = json.dumps(all_names)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BDS Anthony &mdash; Entertainment Hub</title>
    <meta name="description" content="Explore channels, stories, quizzes, and more from the BDS Anthony entertainment network.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA_ID}');</script>
    <style>
        *,*::before,*::after{{margin:0;padding:0;box-sizing:border-box}}
        :root{{--bg:#0b0b0f;--card:#14141b;--border:#1f1f2b;--text:#eae8f2;--muted:#8b89a0;--accent:#7c5cff;--accent2:#ff5c87;--discord:#5865F2;--glow:rgba(124,92,255,.12)}}
        body{{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);line-height:1.6;overflow-x:hidden}}
        a{{text-decoration:none}}

        .hero{{min-height:45vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:3rem 1.5rem 1rem;position:relative}}
        .hero::before{{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 70% 50% at 50% 40%,var(--glow),transparent),radial-gradient(ellipse 50% 40% at 70% 60%,rgba(255,92,135,.06),transparent);pointer-events:none}}
        .hero h1{{font-size:clamp(2.4rem,8vw,4.5rem);font-weight:800;letter-spacing:-.03em;line-height:1.1;margin-bottom:.6rem;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
        .hero p{{color:var(--muted);font-size:clamp(.95rem,2.5vw,1.15rem);max-width:520px;margin-bottom:.5rem}}
        .rotating-text{{color:var(--accent);font-weight:700}}

        .stats-bar{{display:flex;justify-content:center;gap:2.5rem;padding:1rem 1.5rem 2rem;flex-wrap:wrap}}
        .stat{{text-align:center}}
        .stat .num{{font-size:1.5rem;font-weight:800;color:#fff}}
        .stat .label{{font-size:.75rem;color:var(--muted);text-transform:uppercase;letter-spacing:.08em}}

        .picker{{max-width:500px;margin:0 auto 2rem;text-align:center;padding:0 1.5rem}}
        .picker-btn{{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border:none;padding:.85rem 2.2rem;border-radius:50px;font-weight:700;font-size:1rem;cursor:pointer;transition:transform .15s,box-shadow .15s}}
        .picker-btn:hover{{transform:translateY(-2px);box-shadow:0 8px 30px var(--glow)}}
        .picker-loader{{margin:.8rem 0;display:none}}
        .picker-bar{{height:5px;background:var(--border);border-radius:3px;overflow:hidden}}
        .picker-bar-fill{{height:100%;width:0;background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:3px;transition:width .3s ease}}
        .picker-status{{color:var(--muted);font-size:.8rem;margin-top:.4rem;font-style:italic}}
        .picker-result{{display:none;background:var(--card);border:1px solid var(--border);border-radius:14px;padding:1.3rem;margin-top:1rem;text-align:center}}
        .picker-result h3{{margin-bottom:.3rem;font-size:1.1rem}}
        .picker-result p{{color:var(--muted);font-size:.88rem;margin-bottom:.8rem}}
        .picker-result a{{display:inline-block;padding:.55rem 1.5rem;background:var(--accent);color:#111;border-radius:50px;font-weight:700;font-size:.85rem}}
        .picker-result.pop{{animation:popIn .35s ease}}
        @keyframes popIn{{0%{{transform:scale(.9);opacity:0}}100%{{transform:scale(1);opacity:1}}}}

        .adopt-banner{{max-width:600px;margin:0 auto 2rem;padding:1.2rem 1.5rem;background:linear-gradient(135deg,rgba(124,92,255,.12),rgba(0,212,255,.08));border:1px solid rgba(124,92,255,.3);border-radius:16px;display:flex;align-items:center;gap:1rem;transition:all .2s}}
        .adopt-banner:hover{{border-color:rgba(124,92,255,.6);transform:translateY(-2px);box-shadow:0 8px 25px rgba(124,92,255,.15)}}
        .adopt-emoji{{font-size:2.2rem;flex-shrink:0}}
        .adopt-title{{font-weight:800;font-size:1rem;margin-bottom:.15rem}}
        .adopt-desc{{color:var(--muted);font-size:.78rem;line-height:1.4}}
        .adopt-arrow{{font-size:1.5rem;color:var(--accent2);flex-shrink:0;margin-left:auto}}
        .trending-section{{max-width:1100px;margin:0 auto;padding:0 1.5rem 2rem}}
        .trending-section>h2{{font-size:.85rem;text-transform:uppercase;letter-spacing:.15em;color:var(--accent2);font-weight:700;margin-bottom:1.2rem;text-align:center}}
        .trending-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1rem}}
        .ch-big{{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:1.5rem;color:var(--text);transition:transform .2s,border-color .2s,box-shadow .2s;display:block;position:relative}}
        .ch-big:hover{{transform:translateY(-3px);border-color:var(--accent2);box-shadow:0 8px 30px rgba(255,92,135,.12)}}
        .ch-big h3{{font-size:1.15rem;font-weight:700;margin-bottom:.3rem}}
        .ch-big p{{color:var(--muted);font-size:.85rem;line-height:1.45}}
        .fire{{position:absolute;top:1rem;right:1rem;font-size:.6rem;text-transform:uppercase;letter-spacing:.08em;padding:.2rem .6rem;border-radius:50px;font-weight:700;background:rgba(255,92,135,.15);color:var(--accent2)}}

        .grid-section{{max-width:1100px;margin:0 auto;padding:0 1.5rem 2rem}}
        .cat-section{{margin-bottom:2rem}}
        .cat-title{{font-size:.85rem;text-transform:uppercase;letter-spacing:.12em;color:var(--muted);font-weight:600;margin-bottom:.8rem;padding-left:.2rem}}
        .channels{{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:.8rem}}
        .ch{{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:1.1rem 1.2rem;color:var(--text);transition:transform .2s,border-color .2s,box-shadow .2s;display:block}}
        .ch:hover{{transform:translateY(-2px);border-color:var(--accent);box-shadow:0 6px 24px var(--glow)}}
        .tag{{display:inline-block;font-size:.6rem;text-transform:uppercase;letter-spacing:.08em;padding:.18rem .55rem;border-radius:50px;font-weight:700;margin-bottom:.4rem}}
        .ch h3,.ch-big h3{{margin-top:.2rem}}
        .ch h3{{font-size:.95rem;font-weight:700;margin-bottom:.2rem}}
        .ch p{{color:var(--muted);font-size:.8rem;line-height:1.4}}

        .discord-banner{{background:linear-gradient(135deg,rgba(88,101,242,.15),rgba(88,101,242,.05));border:1px solid rgba(88,101,242,.2);max-width:800px;margin:1rem auto 2rem;border-radius:16px;padding:2rem;display:flex;align-items:center;gap:2rem;flex-wrap:wrap;justify-content:center}}
        .discord-banner .text{{flex:1;min-width:260px}}
        .discord-banner h2{{color:#fff;font-size:1.3rem;font-weight:800;margin-bottom:.4rem}}
        .discord-banner .sub{{color:var(--muted);font-size:.92rem}}
        .discord-banner .features{{display:flex;gap:.6rem;flex-wrap:wrap;margin-top:.8rem}}
        .discord-banner .feat{{background:rgba(88,101,242,.12);border-radius:8px;padding:.3rem .7rem;font-size:.72rem;font-weight:600;color:#99a5ff}}
        .btn-discord{{display:inline-block;padding:.8rem 2rem;background:var(--discord);color:#fff;border-radius:50px;font-weight:700;font-size:.95rem;transition:transform .15s,box-shadow .15s;white-space:nowrap}}
        .btn-discord:hover{{transform:translateY(-2px);box-shadow:0 6px 24px rgba(88,101,242,.3)}}

        footer{{text-align:center;padding:2rem 1rem;color:var(--muted);font-size:.75rem;border-top:1px solid var(--border)}}
        footer a{{color:var(--accent)}}
        @media(max-width:600px){{.channels{{grid-template-columns:1fr}}.trending-grid{{grid-template-columns:1fr}}.grid-section,.trending-section{{padding:0 1rem 2rem}}.discord-banner{{margin:1rem 1rem 2rem;padding:1.5rem;flex-direction:column;text-align:center}}.discord-banner .features{{justify-content:center}}.stats-bar{{gap:1.5rem}}}}
    </style>
    {ADSENSE}
</head>
<body>

<div class="hero">
    <h1>BDS Anthony</h1>
    <p>Stories. Quizzes. Hot Takes. Gaming. <span class="rotating-text" id="rotator"></span></p>
</div>

<div class="stats-bar">
    <div class="stat"><div class="num">400K+</div><div class="label">Total Views</div></div>
    <div class="stat"><div class="num">19</div><div class="label">Channels</div></div>
    <div class="stat"><div class="num">950+</div><div class="label">Videos</div></div>
    <div class="stat"><div class="num">400+</div><div class="label">Subscribers</div></div>
</div>

<div class="picker">
    <button class="picker-btn" onclick="runPicker()">What Should I Watch?</button>
    <div class="picker-loader" id="picker-loader">
        <div class="picker-bar"><div class="picker-bar-fill" id="picker-bar"></div></div>
        <p class="picker-status" id="picker-status">Scanning channels...</p>
    </div>
    <div class="picker-result" id="picker-result"></div>
</div>

<div class="trending-section">
    <h2>Trending Now</h2>
    <div class="trending-grid">
        {trending_html}
    </div>
</div>

<div class="grid-section">
    {gaming_section}
    {knowledge_section}
    {entertainment_section}
</div>

<div class="discord-banner">
    <div class="text">
        <h2>Play Swords &mdash; Free RPG on Discord</h2>
        <p class="sub">Create a character, accept quests, fight monsters, and level up. A full RPG running inside Discord.</p>
        <div class="features">
            <span class="feat">Create a Character</span>
            <span class="feat">Fight Monsters</span>
            <span class="feat">Accept Quests</span>
            <span class="feat">Level Up</span>
            <span class="feat">Party System</span>
        </div>
    </div>
    <a class="btn-discord" href="{DISCORD}">Join &amp; Play Free &rarr;</a>
</div>

<footer>
    <a href="/privacy.html">Privacy Policy</a>
</footer>

<script>
var pool = {picker_pool};
var msgs = ["Scanning channels...","Analyzing your vibe...","Finding the perfect match...","Almost there..."];
function runPicker(){{
    var loader=document.getElementById('picker-loader');
    var result=document.getElementById('picker-result');
    var bar=document.getElementById('picker-bar');
    var status=document.getElementById('picker-status');
    result.style.display='none';loader.style.display='block';bar.style.width='0%';
    var step=0;status.textContent=msgs[0];
    var iv=setInterval(function(){{
        step++;
        if(step>=msgs.length){{
            clearInterval(iv);bar.style.width='100%';
            setTimeout(function(){{
                loader.style.display='none';
                var pick=pool[Math.floor(Math.random()*pool.length)];
                result.innerHTML='<h3>'+pick[1]+'</h3><p>'+pick[2]+'</p><a href="/'+pick[0]+'/">Check it out &rarr;</a>';
                result.style.display='block';
                result.classList.remove('pop');void result.offsetWidth;result.classList.add('pop');
                if(typeof gtag!=='undefined')gtag('event','generator_click',{{event_category:'generators',event_label:'homepage_picker',channel:'homepage',generator_type:'channel_picker'}});
            }},300);
            return;
        }}
        bar.style.width=((step/msgs.length)*100)+'%';
        status.textContent=msgs[step];
    }},500);
}}
var words=["Glitches.","Hot Takes.","Dark Facts.","Loot Drops.","Brain Worms.","Sigma Quotes.","Moral Dilemmas.","Trivia.","Rankings."];
var wi=0;var rotEl=document.getElementById('rotator');
setInterval(function(){{wi=(wi+1)%words.length;rotEl.style.opacity=0;setTimeout(function(){{rotEl.textContent=words[wi];rotEl.style.opacity=1;}},300);}},2500);
rotEl.style.transition='opacity .3s';rotEl.textContent=words[0];
</script>
</body>
</html>'''


# ─── Adopt page (Tamagotchi-lite pet game) ───────────────────────────────────

def build_adopt_page():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>BDS Anthony &mdash; Adopt Your Character</title>
<meta name="description" content="Adopt a Fortnite, Minecraft, or Roblox character. Feed, train, and level them up!">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA_ID}');</script>
{ADSENSE}
<style>
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box}}
:root{{--bg:#08080e;--card:#10101a;--border:#1a1a2c;--text:#eae8f2;--muted:#7a788e;--accent:#7c5cff}}
body{{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);min-height:100vh;overflow-x:hidden}}
a{{color:var(--accent);text-decoration:none}}

/* ── Screens ── */
.screen{{display:none}}.screen.active{{display:block}}

/* ── Pick / Landing Screen ── */
.pick-hero{{text-align:center;padding:clamp(2rem,8vh,5rem) 1.5rem 1.5rem;position:relative;overflow:hidden}}
.pick-hero::before{{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 0%,rgba(124,92,255,.12) 0%,transparent 60%);pointer-events:none}}
.pick-hero h1{{font-size:clamp(2rem,7vw,3.5rem);font-weight:900;letter-spacing:-.04em;line-height:1.1;margin-bottom:.6rem;position:relative}}
.pick-hero h1 span{{background:linear-gradient(135deg,#7c5cff,#00d4ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent}}
.pick-hero .sub{{color:var(--muted);font-size:clamp(.9rem,2.5vw,1.1rem);max-width:500px;margin:0 auto;position:relative}}

.game-banner{{position:relative;overflow:hidden;cursor:pointer;transition:transform .25s,box-shadow .25s}}
.game-banner:hover{{transform:scale(1.01);z-index:2}}
.game-banner:active{{transform:scale(.99)}}

.gb-inner{{max-width:1000px;margin:0 auto;padding:clamp(2.5rem,5vh,4rem) 1.5rem;display:flex;align-items:center;gap:clamp(1.5rem,3vw,3rem);position:relative;z-index:1}}
.gb-left{{flex:1;min-width:0}}
.gb-tag{{display:inline-block;font-size:.65rem;text-transform:uppercase;letter-spacing:.14em;padding:.25rem .8rem;border-radius:50px;font-weight:800;margin-bottom:.8rem}}
.gb-title{{font-size:clamp(1.6rem,5vw,2.5rem);font-weight:900;letter-spacing:-.03em;line-height:1.15;margin-bottom:.5rem}}
.gb-hook{{font-size:clamp(.85rem,2vw,1rem);line-height:1.5;margin-bottom:1.2rem;max-width:480px}}
.gb-stats{{display:flex;gap:1.5rem;font-size:.78rem;margin-bottom:1.2rem}}
.gb-stats span{{display:flex;align-items:center;gap:.3rem}}
.gb-btn{{display:inline-flex;align-items:center;gap:.5rem;padding:.85rem 2.2rem;border-radius:50px;font-weight:800;font-size:.95rem;border:none;cursor:pointer;transition:transform .15s,box-shadow .15s;letter-spacing:.01em}}
.gb-btn:hover{{transform:translateY(-2px)}}
.gb-btn:active{{transform:scale(.97)}}

.gb-right{{flex-shrink:0;display:flex;flex-wrap:wrap;gap:.5rem;max-width:200px;justify-content:center}}
.gb-char{{background:rgba(255,255,255,.06);border-radius:12px;width:52px;height:52px;display:flex;align-items:center;justify-content:center;font-size:1.6rem;border:1px solid rgba(255,255,255,.08);transition:transform .2s}}
.game-banner:hover .gb-char{{animation:charBounce .4s ease}}
@keyframes charBounce{{0%{{transform:scale(1)}}50%{{transform:scale(1.15)}}100%{{transform:scale(1)}}}}

.banner-fn{{background:linear-gradient(135deg,rgba(0,60,120,.6) 0%,rgba(0,20,50,.8) 100%);border-top:1px solid rgba(0,180,255,.15);border-bottom:1px solid rgba(0,180,255,.08)}}
.banner-fn .gb-tag{{background:rgba(0,212,255,.15);color:#00d4ff}}.banner-fn .gb-btn{{background:#00d4ff;color:#0a1a2a;box-shadow:0 4px 20px rgba(0,212,255,.25)}}.banner-fn .gb-btn:hover{{box-shadow:0 8px 30px rgba(0,212,255,.35)}}
.banner-mc{{background:linear-gradient(135deg,rgba(20,80,20,.6) 0%,rgba(10,30,10,.8) 100%);border-top:1px solid rgba(85,255,85,.12);border-bottom:1px solid rgba(85,255,85,.06)}}
.banner-mc .gb-tag{{background:rgba(85,255,85,.12);color:#55ff55}}.banner-mc .gb-btn{{background:#55ff55;color:#0a2a0a;box-shadow:0 4px 20px rgba(85,255,85,.2)}}.banner-mc .gb-btn:hover{{box-shadow:0 8px 30px rgba(85,255,85,.3)}}
.banner-rb{{background:linear-gradient(135deg,rgba(100,80,0,.5) 0%,rgba(40,30,0,.8) 100%);border-top:1px solid rgba(255,204,0,.15);border-bottom:1px solid rgba(255,204,0,.08)}}
.banner-rb .gb-tag{{background:rgba(255,204,0,.12);color:#ffcc00}}.banner-rb .gb-btn{{background:#ffcc00;color:#2a2000;box-shadow:0 4px 20px rgba(255,204,0,.2)}}.banner-rb .gb-btn:hover{{box-shadow:0 8px 30px rgba(255,204,0,.3)}}

.how-it-works{{max-width:800px;margin:0 auto;padding:3rem 1.5rem;text-align:center}}
.how-it-works h2{{font-size:1rem;text-transform:uppercase;letter-spacing:.15em;color:var(--accent);font-weight:700;margin-bottom:2rem}}
.steps{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:1.5rem}}
.step{{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:1.5rem 1rem}}
.step-num{{font-size:2rem;margin-bottom:.4rem}}.step-title{{font-weight:800;font-size:.9rem;margin-bottom:.3rem}}.step-desc{{color:var(--muted);font-size:.78rem;line-height:1.45}}

.pick-footer{{text-align:center;padding:1.5rem;color:var(--muted);font-size:.72rem;border-top:1px solid var(--border)}}
.pick-footer a{{color:var(--muted);margin:0 .4rem}}

@media(max-width:700px){{.gb-inner{{flex-direction:column;text-align:center}}.gb-right{{max-width:none;margin-top:.5rem}}.gb-stats{{justify-content:center}}.gb-hook{{margin-left:auto;margin-right:auto}}}}

/* ── Hatch Screen ── */
#screen-hatch{{padding-top:30vh;text-align:center}}
.egg{{font-size:5rem;display:inline-block;animation:eggShake 0.25s infinite alternate}}
@keyframes eggShake{{0%{{transform:rotate(-10deg)scale(1)}}50%{{transform:rotate(10deg)scale(1.08)}}100%{{transform:rotate(-10deg)scale(1)}}}}
.hatch-text{{color:var(--muted);font-size:.95rem;margin-top:1.5rem;animation:pulse 1s infinite}}
@keyframes pulse{{0%,100%{{opacity:.4}}50%{{opacity:1}}}}
.hatch-crack{{animation:crack .3s ease forwards}}
@keyframes crack{{0%{{transform:scale(1)}}50%{{transform:scale(1.3)}}100%{{transform:scale(0);opacity:0}}}}

/* ── Dashboard ── */
#screen-pet{{max-width:440px;margin:0 auto;padding:1rem 1.2rem 3rem;text-align:center}}
.pet-card{{background:var(--card);border:2px solid var(--border);border-radius:20px;padding:2rem 1.5rem 1.5rem;margin:1rem 0;position:relative;transition:border-color .5s,box-shadow .5s}}
.pet-card.rarity-common{{border-color:#555}}.pet-card.rarity-uncommon{{border-color:#44cc44;box-shadow:0 0 20px rgba(68,204,68,.1)}}
.pet-card.rarity-rare{{border-color:#4488ff;box-shadow:0 0 25px rgba(68,136,255,.15)}}.pet-card.rarity-epic{{border-color:#aa44ff;box-shadow:0 0 30px rgba(170,68,255,.2)}}
.pet-card.rarity-legendary{{border-color:#ffaa00;box-shadow:0 0 35px rgba(255,170,0,.2)}}
.pet-emoji{{font-size:3.5rem;margin-bottom:.3rem}}
.pet-name{{font-size:1.5rem;font-weight:900;letter-spacing:-.02em}}
.pet-level{{color:var(--muted);font-size:.85rem;margin-top:.2rem}}
.rarity-badge{{display:inline-block;font-size:.6rem;text-transform:uppercase;letter-spacing:.15em;padding:.2rem .7rem;border-radius:50px;font-weight:800;margin-top:.5rem}}
.rarity-common .rarity-badge{{background:rgba(128,128,128,.2);color:#999}}
.rarity-uncommon .rarity-badge{{background:rgba(68,204,68,.15);color:#66ee66}}
.rarity-rare .rarity-badge{{background:rgba(68,136,255,.15);color:#66aaff}}
.rarity-epic .rarity-badge{{background:rgba(170,68,255,.15);color:#cc77ff}}
.rarity-legendary .rarity-badge{{background:rgba(255,170,0,.15);color:#ffcc44}}
.mood-text{{font-size:.8rem;margin-top:.5rem}}

.xp-section{{margin:1.2rem 0}}
.xp-label{{display:flex;justify-content:space-between;font-size:.75rem;color:var(--muted);margin-bottom:.3rem}}
.xp-bar{{height:8px;background:var(--card);border-radius:4px;overflow:hidden;border:1px solid var(--border)}}
.xp-fill{{height:100%;background:linear-gradient(90deg,#7c5cff,#aa77ff);border-radius:4px;transition:width .6s cubic-bezier(.34,1.56,.64,1)}}

.stats{{display:flex;flex-direction:column;gap:.7rem;margin:1rem 0}}
.stat-row{{display:flex;align-items:center;gap:.6rem}}
.stat-icon{{font-size:1rem;width:1.5rem;text-align:center;flex-shrink:0}}
.stat-name{{font-size:.78rem;font-weight:600;width:4rem;text-align:left;flex-shrink:0}}
.stat-bar{{flex:1;height:10px;background:var(--card);border-radius:5px;overflow:hidden;border:1px solid var(--border)}}
.stat-fill{{height:100%;border-radius:5px;transition:width .5s ease,background .3s}}
.stat-val{{font-size:.72rem;font-weight:700;width:2.5rem;text-align:right;flex-shrink:0}}

.actions{{display:flex;flex-direction:column;gap:.6rem;margin:1.2rem 0}}
.action-btn{{background:var(--card);border:2px solid var(--border);border-radius:14px;padding:1rem;display:flex;align-items:center;gap:.8rem;cursor:pointer;transition:all .2s;text-align:left;width:100%;font-family:inherit;color:var(--text)}}
.action-btn:not(.on-cooldown):not(.no-energy):hover{{border-color:var(--accent);transform:translateY(-1px);box-shadow:0 4px 15px rgba(124,92,255,.12)}}
.action-btn.ready{{border-color:rgba(68,204,68,.4)}}
.action-btn.on-cooldown{{opacity:.55;cursor:default}}.action-btn.no-energy{{opacity:.4;cursor:default}}
.act-emoji{{font-size:1.5rem;flex-shrink:0}}
.act-info{{flex:1}}.act-name{{font-weight:700;font-size:.95rem}}.act-desc{{color:var(--muted);font-size:.75rem;margin-top:.1rem}}
.act-status{{font-size:.78rem;font-weight:600;color:var(--muted);flex-shrink:0}}
.act-status.ready-text{{color:#66ee66}}

.toast{{position:fixed;top:1.5rem;left:50%;transform:translateX(-50%)translateY(-120%);background:#1a1a2e;border:1px solid var(--accent);border-radius:12px;padding:.8rem 1.5rem;font-size:.88rem;font-weight:600;z-index:100;transition:transform .3s cubic-bezier(.34,1.56,.64,1);white-space:nowrap;box-shadow:0 8px 30px rgba(0,0,0,.5)}}
.toast.show{{transform:translateX(-50%)translateY(0)}}

.levelup-overlay{{position:fixed;inset:0;background:rgba(0,0,0,.85);display:none;z-index:200;align-items:center;justify-content:center;flex-direction:column}}
.levelup-overlay.show{{display:flex}}
.levelup-text{{font-size:clamp(2rem,10vw,3.5rem);font-weight:900;background:linear-gradient(135deg,#ffcc00,#ff6b6b,#aa44ff,#00d4ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;animation:lvlPulse .6s ease}}
.levelup-sub{{color:var(--muted);font-size:1rem;margin-top:.5rem}}.levelup-rarity{{font-size:1.2rem;font-weight:800;margin-top:.8rem}}
@keyframes lvlPulse{{0%{{transform:scale(0)}}60%{{transform:scale(1.15)}}100%{{transform:scale(1)}}}}
.lvl-confetti{{position:fixed;inset:0;pointer-events:none;z-index:201;overflow:hidden}}
.lvl-confetti .c{{position:absolute;width:8px;height:8px;border-radius:2px;animation:confDrop 2s ease-out forwards}}
@keyframes confDrop{{0%{{transform:translateY(-20px)rotate(0);opacity:1}}100%{{transform:translateY(100vh)rotate(720deg);opacity:0}}}}

.away-report{{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:1rem;margin:1rem 0;text-align:left}}
.away-report h3{{font-size:.82rem;color:var(--muted);font-weight:600;margin-bottom:.5rem;text-transform:uppercase;letter-spacing:.08em}}
.away-line{{font-size:.8rem;margin:.25rem 0;display:flex;justify-content:space-between}}
.away-line .change.neg{{color:#ff6b6b}}.away-line .change.pos{{color:#66ee66}}

.pet-footer{{margin-top:2rem;padding-top:1rem;border-top:1px solid var(--border);font-size:.72rem;color:var(--muted)}}
.pet-footer a{{color:var(--muted);margin:0 .3rem}}
.release-btn{{background:none;border:none;color:var(--muted);font-size:.7rem;cursor:pointer;margin-top:.5rem;text-decoration:underline;font-family:inherit}}.release-btn:hover{{color:#ff6b6b}}

@media(max-width:400px){{#screen-pet{{padding:1rem .8rem 3rem}}.pet-card{{padding:1.5rem 1rem 1rem}}}}
</style>
</head>
<body>

<!-- Pick Game - Full Width Landing -->
<div class="screen" id="screen-pick">
    <div class="pick-hero">
        <h1><span>Adopt.</span> Feed. Train.<br>Level Up.</h1>
        <p class="sub">Choose a world. Get a random character. Come back every day to keep them alive and watch them evolve.</p>
    </div>

    <div class="game-banner banner-fn" onclick="window._startAdopt('fortnite')">
        <div class="gb-inner">
            <div class="gb-left">
                <div class="gb-tag">Fortnite</div>
                <div class="gb-title">Storm Survivors</div>
                <div class="gb-hook">20 characters waiting in the storm. Shadow agents, peely clones, skull troopers, and more. Adopt one before they&rsquo;re gone.</div>
                <div class="gb-stats"><span>&#128100; 20 Characters</span><span>&#9889; 5 Rarities</span><span>&#128200; 20 Levels</span></div>
                <div class="gb-btn">Adopt a Fortnite Character &rarr;</div>
            </div>
            <div class="gb-right">
                <div class="gb-char">&#128374;&#65039;</div><div class="gb-char">&#127820;</div><div class="gb-char">&#128031;</div>
                <div class="gb-char">&#128128;</div><div class="gb-char">&#128081;</div><div class="gb-char">&#128640;</div>
                <div class="gb-char">&#128570;</div><div class="gb-char">&#9889;</div><div class="gb-char">&#10024;</div>
            </div>
        </div>
    </div>

    <div class="game-banner banner-mc" onclick="window._startAdopt('minecraft')">
        <div class="gb-inner">
            <div class="gb-left">
                <div class="gb-tag">Minecraft</div>
                <div class="gb-title">Block Companions</div>
                <div class="gb-hook">From diamond steves to axolotl friends. 20 mobs and miners need a home. Mine, craft, and raise them to legendary status.</div>
                <div class="gb-stats"><span>&#128100; 20 Characters</span><span>&#128142; 5 Rarities</span><span>&#128200; 20 Levels</span></div>
                <div class="gb-btn">Adopt a Minecraft Character &rarr;</div>
            </div>
            <div class="gb-right">
                <div class="gb-char">&#128142;</div><div class="gb-char">&#128154;</div><div class="gb-char">&#128126;</div>
                <div class="gb-char">&#128293;</div><div class="gb-char">&#128058;</div><div class="gb-char">&#128029;</div>
                <div class="gb-char">&#129422;</div><div class="gb-char">&#128055;</div><div class="gb-char">&#129418;</div>
            </div>
        </div>
    </div>

    <div class="game-banner banner-rb" onclick="window._startAdopt('roblox')">
        <div class="gb-inner">
            <div class="gb-left">
                <div class="gb-tag">Roblox</div>
                <div class="gb-title">Blox Buddies</div>
                <div class="gb-hook">Noob heroes, bacon hair legends, phantom cadets. 20 Roblox characters are waiting to be adopted. Will you raise a champion?</div>
                <div class="gb-stats"><span>&#128100; 20 Characters</span><span>&#11088; 5 Rarities</span><span>&#128200; 20 Levels</span></div>
                <div class="gb-btn">Adopt a Roblox Character &rarr;</div>
            </div>
            <div class="gb-right">
                <div class="gb-char">&#128522;</div><div class="gb-char">&#129363;</div><div class="gb-char">&#11088;</div>
                <div class="gb-char">&#127939;</div><div class="gb-char">&#128081;</div><div class="gb-char">&#128270;</div>
                <div class="gb-char">&#129370;</div><div class="gb-char">&#128120;</div><div class="gb-char">&#127918;</div>
            </div>
        </div>
    </div>

    <div class="how-it-works">
        <h2>How It Works</h2>
        <div class="steps">
            <div class="step"><div class="step-num">&#129370;</div><div class="step-title">Adopt</div><div class="step-desc">Pick a world and get a random character</div></div>
            <div class="step"><div class="step-num">&#127830;</div><div class="step-title">Feed &amp; Train</div><div class="step-desc">Keep them alive and earn XP</div></div>
            <div class="step"><div class="step-num">&#9200;</div><div class="step-title">Come Back</div><div class="step-desc">Actions have cooldowns &mdash; return to keep growing</div></div>
            <div class="step"><div class="step-num">&#11088;</div><div class="step-title">Evolve</div><div class="step-desc">Level up from Common to Legendary</div></div>
        </div>
    </div>

    <div class="pick-footer">
        <a href="/channels/">Our Channels</a> &middot; <a href="{DISCORD}">Discord</a> &middot; <a href="/privacy.html">Privacy</a>
    </div>
</div>

<!-- Hatching Animation -->
<div class="screen" id="screen-hatch" style="text-align:center">
    <div class="egg" id="hatch-egg">&#129370;</div>
    <p class="hatch-text" id="hatch-text">Hatching...</p>
</div>

<!-- Pet Dashboard -->
<div class="screen" id="screen-pet">
    <div id="away-box"></div>
    <div class="pet-card" id="pet-card">
        <div class="pet-emoji" id="pet-emoji"></div>
        <div class="pet-name" id="pet-name"></div>
        <div class="pet-level" id="pet-level"></div>
        <div class="rarity-badge" id="pet-rarity"></div>
        <div class="mood-text" id="pet-mood"></div>
    </div>
    <div class="xp-section">
        <div class="xp-label"><span id="xp-text">XP</span><span id="xp-next">Next level</span></div>
        <div class="xp-bar"><div class="xp-fill" id="xp-fill"></div></div>
    </div>
    <div class="stats">
        <div class="stat-row"><span class="stat-icon">&#127830;</span><span class="stat-name">Hunger</span><div class="stat-bar"><div class="stat-fill" id="bar-hunger"></div></div><span class="stat-val" id="val-hunger"></span></div>
        <div class="stat-row"><span class="stat-icon">&#9889;</span><span class="stat-name">Energy</span><div class="stat-bar"><div class="stat-fill" id="bar-energy"></div></div><span class="stat-val" id="val-energy"></span></div>
        <div class="stat-row"><span class="stat-icon">&#128150;</span><span class="stat-name">Happy</span><div class="stat-bar"><div class="stat-fill" id="bar-happy"></div></div><span class="stat-val" id="val-happy"></span></div>
    </div>
    <div class="actions">
        <button class="action-btn" id="btn-feed" onclick="window._doAction('feed')">
            <span class="act-emoji">&#127830;</span>
            <div class="act-info"><div class="act-name">Feed</div><div class="act-desc">Restores hunger &amp; a bit of happiness</div></div>
            <span class="act-status" id="cd-feed">Ready!</span>
        </button>
        <button class="action-btn" id="btn-train" onclick="window._doAction('train')">
            <span class="act-emoji">&#9876;&#65039;</span>
            <div class="act-info"><div class="act-name">Train</div><div class="act-desc">Earn XP, costs energy &amp; hunger</div></div>
            <span class="act-status" id="cd-train">Ready!</span>
        </button>
        <button class="action-btn" id="btn-rest" onclick="window._doAction('rest')">
            <span class="act-emoji">&#128564;</span>
            <div class="act-info"><div class="act-name">Rest</div><div class="act-desc">Restores energy &amp; happiness</div></div>
            <span class="act-status" id="cd-rest">Ready!</span>
        </button>
    </div>
    <div class="pet-footer">
        <div>Adopted <span id="pet-age"></span> ago</div>
        <a href="/">Home</a> &middot; <a href="/channels/">Channels</a> &middot; <a href="{DISCORD}">Discord</a>
        <br><button class="release-btn" onclick="window._releasePet()">Release this pet</button>
    </div>
</div>

<!-- Toast -->
<div class="toast" id="toast"></div>

<!-- Level Up Overlay -->
<div class="levelup-overlay" id="levelup">
    <div class="levelup-text" id="lvl-text">LEVEL UP!</div>
    <div class="levelup-sub" id="lvl-sub"></div>
    <div class="levelup-rarity" id="lvl-rarity"></div>
</div>
<div class="lvl-confetti" id="lvl-confetti"></div>

<script>
var GAMES={{
fortnite:{{color:'#00d4ff',chars:[
["\U0001f576\ufe0f","Shadow Agent"],["\U0001f34c","Peely Jr."],["\U0001f41f","Fishstick Clone"],["\u26a1","Drift Puppy"],
["\U0001f9f8","Cuddle Cub"],["\U0001f985","Raven Chick"],["\U0001f63a","Meowscles Kit"],["\U0001f431","Lynx Cub"],
["\U0001f680","Dark Voyager Mini"],["\U0001f480","Skull Pup"],["\u2744\ufe0f","Ice Prince"],["\U0001f527","Rust Recruit"],
["\u2728","Brite Baby"],["\U0001f451","Midas Spark"],["\U0001f31f","Omega Hatchling"],["\U0001f6e1","Knight Squire"],
["\U0001f3b8","Marshmello Mini"],["\U0001f43a","Dire Pup"],["\U0001f3a8","Abstrakt Jr."],["\U0001f47b","Ghoul Scout"]
]}},
minecraft:{{color:'#55ff55',chars:[
["\U0001f48e","Diamond Steve"],["\U0001f49a","Creeper Buddy"],["\U0001f47e","Ender Pup"],["\U0001f916","Iron Golem Jr."],
["\U0001f525","Blaze Sprite"],["\U0001f480","Wither Cub"],["\U0001f47b","Phantom Kit"],["\U0001f437","Piglin Pal"],
["\U0001f98e","Axolotl Friend"],["\U0001f5ff","Warden Whisper"],["\U0001f41d","Bee Buddy"],["\U0001f4a5","Ghast Baby"],
["\U0001f7e2","Slime Blob"],["\U0001f43a","Wolf Pup"],["\U0001f98a","Fox Kit"],["\U0001f338","Allay Sprite"],
["\U0001f983","Shulker Baby"],["\U0001f420","Guardian Guppy"],["\U0001f9d0","Villager Sprout"],["\U0001f424","Chicken Scout"]
]}},
roblox:{{color:'#ffcc00',chars:[
["\U0001f60a","Noob Hero"],["\U0001f953","Bacon Hair Legend"],["\u2b50","Guest Star"],["\U0001f3d7\ufe0f","Builder Bot"],
["\U0001f3d8","Bloxburg Baby"],["\U0001f95a","Adopt Me Egg"],["\U0001f3e0","Brookhaven Kid"],["\U0001f3c3","Jailbreak Runner"],
["\U0001f50e","Mystery Sleuth"],["\U0001f52b","Arsenal Rookie"],["\U0001f47b","Phantom Cadet"],["\U0001f977","Shindo Cub"],
["\U0001f34e","Blox Fruit Seed"],["\U0001f608","Doors Entity Jr."],["\U0001f437","Piggy Clone"],["\U0001f41d","Bee Swarm Drone"],
["\U0001f984","Pet Sim Hatchling"],["\U0001f451","Royal Star"],["\U0001f3ae","Tower Titan Jr."],["\U0001f47d","Alien Intern"]
]}}
}};

var XP_TABLE=[0,50,130,240,380,550,750,1000,1300,1650,2050,2500,3050,3700,4450,5300,6300,7450,8800,10400,12300];
var RARITY_LEVELS=[[1,'common','Common','#888'],[5,'uncommon','Uncommon','#44cc44'],[10,'rare','Rare','#4488ff'],[15,'epic','Epic','#aa44ff'],[20,'legendary','Legendary','#ffaa00']];
var CD_FEED=15*60000,CD_TRAIN=30*60000,CD_REST=45*60000;
var FEED_MSGS=["is feeling full!","loved that snack!","gobbled it up!","wants more already!"];
var TRAIN_MSGS=["pushed through the training!","is getting stronger!","broke a sweat!","leveled their skills!"];
var REST_MSGS=["is recharging nicely.","needed that nap.","feels refreshed!","is full of energy now!"];
var KEY='bds_pet_v1',pet=null;

function load(){{try{{pet=JSON.parse(localStorage.getItem(KEY));}}catch(e){{pet=null;}}}}
function save(){{localStorage.setItem(KEY,JSON.stringify(pet));}}
function show(id){{document.querySelectorAll('.screen').forEach(function(s){{s.classList.remove('active');}});document.getElementById(id).classList.add('active');}}
function getRarity(lv){{var r=RARITY_LEVELS[0];for(var i=0;i<RARITY_LEVELS.length;i++)if(lv>=RARITY_LEVELS[i][0])r=RARITY_LEVELS[i];return r;}}
function xpForNext(lv){{return lv>=XP_TABLE.length-1?99999:XP_TABLE[lv]-XP_TABLE[lv-1];}}
function xpInLevel(lv,xp){{return lv<=1?xp:xp-XP_TABLE[lv-1];}}
function levelFromXp(xp){{for(var i=1;i<XP_TABLE.length;i++)if(xp<XP_TABLE[i])return i;return XP_TABLE.length;}}
function getMood(){{
    if(pet.hunger<15)return['\U0001f629','Starving!','#ff4444'];
    if(pet.happiness<20)return['\U0001f622','Sad...','#ff6b6b'];
    if(pet.energy<15)return['\U0001f634','Exhausted','#8888ff'];
    if(pet.hunger<35)return['\U0001f615','Hungry','#ffaa44'];
    if(pet.happiness>80&&pet.hunger>60&&pet.energy>60)return['\U0001f929','Ecstatic!','#ffcc00'];
    if(pet.happiness>60)return['\U0001f60a','Happy','#66ee66'];
    return['\U0001f610','Okay','#7a788e'];
}}

function calcOffline(){{
    if(!pet||!pet.lastVisit)return null;
    var now=Date.now(),hrs=(now-pet.lastVisit)/3600000;
    if(hrs<0.01)return null;
    var r={{hours:hrs,oH:pet.hunger,oE:pet.energy,oP:pet.happiness}};
    pet.hunger=Math.max(0,Math.round(pet.hunger-hrs*8));
    pet.energy=Math.min(100,Math.round(pet.energy+hrs*4));
    pet.happiness=Math.max(0,Math.round(pet.happiness-hrs*(pet.hunger<25?5:1.5)));
    r.nH=pet.hunger;r.nE=pet.energy;r.nP=pet.happiness;
    pet.lastVisit=now;save();return r;
}}

function showAway(r){{
    if(!r||r.hours<0.05){{document.getElementById('away-box').innerHTML='';return;}}
    var h=r.hours,ts=h>=1?Math.floor(h)+'h '+Math.round((h%1)*60)+'m':Math.round(h*60)+'m';
    function d(o,n){{var v=Math.round(n-o);return v>=0?'+'+v:''+v;}}
    function c(o,n){{return n>=o?'pos':'neg';}}
    document.getElementById('away-box').innerHTML='<div class="away-report"><h3>While you were away ('+ts+')</h3>'+
        '<div class="away-line"><span>\U0001f356 Hunger</span><span class="change '+c(r.oH,r.nH)+'">'+d(r.oH,r.nH)+'% \u2192 '+r.nH+'%</span></div>'+
        '<div class="away-line"><span>\u26a1 Energy</span><span class="change '+c(r.oE,r.nE)+'">'+d(r.oE,r.nE)+'% \u2192 '+r.nE+'%</span></div>'+
        '<div class="away-line"><span>\U0001f496 Happy</span><span class="change '+c(r.oP,r.nP)+'">'+d(r.oP,r.nP)+'% \u2192 '+r.nP+'%</span></div></div>';
    setTimeout(function(){{document.getElementById('away-box').innerHTML='';}},8000);
}}

function updateUI(){{
    if(!pet)return;
    document.getElementById('pet-emoji').textContent=pet.emoji;
    document.getElementById('pet-name').textContent=pet.name;
    document.getElementById('pet-level').textContent='Level '+pet.level;
    var rar=getRarity(pet.level);
    document.getElementById('pet-rarity').textContent=rar[2];
    document.getElementById('pet-rarity').style.cssText='background:'+rar[3]+'22;color:'+rar[3];
    document.getElementById('pet-card').className='pet-card rarity-'+rar[1];
    var mood=getMood();
    document.getElementById('pet-mood').textContent=mood[0]+' '+mood[1];
    document.getElementById('pet-mood').style.color=mood[2];
    var needed=xpForNext(pet.level),inLvl=xpInLevel(pet.level,pet.xp),pct=Math.min(100,needed>0?(inLvl/needed)*100:100);
    document.getElementById('xp-fill').style.width=pct+'%';
    document.getElementById('xp-text').textContent=inLvl+'/'+needed+' XP';
    document.getElementById('xp-next').textContent='Level '+(pet.level+1);
    function sb(id,val,vid){{var el=document.getElementById(id);el.style.width=val+'%';el.style.background=val>60?'#44cc44':val>30?'#ddaa00':'#ff4444';document.getElementById(vid).textContent=Math.round(val)+'%';}}
    sb('bar-hunger',pet.hunger,'val-hunger');sb('bar-energy',pet.energy,'val-energy');sb('bar-happy',pet.happiness,'val-happy');
    var ms=Date.now()-(pet.created||Date.now()),dd=Math.floor(ms/86400000),hh=Math.floor((ms%86400000)/3600000);
    document.getElementById('pet-age').textContent=dd>0?dd+'d '+hh+'h':hh>0?hh+'h':'just now';
}}

function updateCD(){{
    if(!pet)return;var now=Date.now();
    function sc(a,cd,bi,ci){{var rem=Math.max(0,(pet['last_'+a]||0)+cd-now),b=document.getElementById(bi),c=document.getElementById(ci);
    b.classList.remove('ready','on-cooldown','no-energy');
    if(rem>0){{b.classList.add('on-cooldown');var m=Math.floor(rem/60000),s=Math.floor((rem%60000)/1000);c.textContent=m+':'+(s<10?'0':'')+s;c.classList.remove('ready-text');}}
    else if(a==='train'&&pet.energy<20){{b.classList.add('no-energy');c.textContent='Need energy';c.classList.remove('ready-text');}}
    else{{b.classList.add('ready');c.textContent='Ready!';c.classList.add('ready-text');}}}}
    sc('feed',CD_FEED,'btn-feed','cd-feed');sc('train',CD_TRAIN,'btn-train','cd-train');sc('rest',CD_REST,'btn-rest','cd-rest');
}}

function toast(msg){{var t=document.getElementById('toast');t.textContent=msg;t.classList.add('show');setTimeout(function(){{t.classList.remove('show');}},2500);}}

function confetti(){{
    var c=document.getElementById('lvl-confetti');c.innerHTML='';
    var cols=['#ff5c87','#7c5cff','#00d2b4','#ffcc00','#ff6b6b','#50c8ff','#60dd60','#ffa040','#aa44ff','#ffaa00'];
    for(var i=0;i<50;i++){{var p=document.createElement('div');p.className='c';p.style.left=Math.random()*100+'%';p.style.top='-10px';p.style.background=cols[i%cols.length];p.style.animationDelay=Math.random()*0.8+'s';p.style.width=(5+Math.random()*8)+'px';p.style.height=p.style.width;c.appendChild(p);}}
    setTimeout(function(){{c.innerHTML='';}},3000);
}}

function showLevelUp(lv,oldR,newR){{
    document.getElementById('lvl-text').textContent='LEVEL '+lv+'!';
    document.getElementById('lvl-sub').textContent=pet.name+' grew stronger!';
    document.getElementById('lvl-rarity').innerHTML=oldR[1]!==newR[1]?'Evolved to <span style="color:'+newR[3]+'">'+newR[2]+'</span>!':'';
    document.getElementById('levelup').classList.add('show');confetti();
    if(typeof gtag!=='undefined')gtag('event','pet_levelup',{{level:lv,rarity:newR[1],game:pet.game}});
    setTimeout(function(){{document.getElementById('levelup').classList.remove('show');}},2800);
}}

window._doAction=function(action){{
    if(!pet)return;var now=Date.now(),cd={{feed:CD_FEED,train:CD_TRAIN,rest:CD_REST}};
    if(now-(pet['last_'+action]||0)<cd[action])return;
    if(action==='train'&&pet.energy<20){{toast('Not enough energy! Rest first.');return;}}
    var oldLv=pet.level,oldR=getRarity(oldLv),msgs,res='';
    if(action==='feed'){{pet.hunger=Math.min(100,pet.hunger+25);pet.happiness=Math.min(100,pet.happiness+5);msgs=FEED_MSGS;}}
    else if(action==='train'){{var xp=15+Math.floor(Math.random()*11);pet.xp+=xp;pet.energy=Math.max(0,pet.energy-20);pet.hunger=Math.max(0,pet.hunger-10);pet.level=levelFromXp(pet.xp);msgs=TRAIN_MSGS;res='+'+xp+' XP! ';}}
    else{{pet.energy=Math.min(100,pet.energy+40);pet.happiness=Math.min(100,pet.happiness+10);msgs=REST_MSGS;}}
    pet['last_'+action]=now;pet.lastVisit=now;save();updateUI();updateCD();
    toast(res+pet.name+' '+msgs[Math.floor(Math.random()*msgs.length)]);
    if(typeof gtag!=='undefined')gtag('event','pet_action',{{action:action,game:pet.game,level:pet.level}});
    if(pet.level>oldLv)setTimeout(function(){{showLevelUp(pet.level,oldR,getRarity(pet.level));}},400);
}};

window._startAdopt=function(game){{
    var g=GAMES[game],pick=g.chars[Math.floor(Math.random()*g.chars.length)];
    show('screen-hatch');
    if(typeof gtag!=='undefined')gtag('event','pet_adopt_start',{{game:game}});
    setTimeout(function(){{document.getElementById('hatch-egg').style.animation='none';document.getElementById('hatch-egg').textContent='\u2728';document.getElementById('hatch-text').textContent='Here they come...';}},2000);
    setTimeout(function(){{
        pet={{game:game,emoji:pick[0],name:pick[1],level:1,xp:0,hunger:50,energy:100,happiness:70,created:Date.now(),lastVisit:Date.now(),last_feed:0,last_train:0,last_rest:0}};
        save();show('screen-pet');updateUI();updateCD();toast('Welcome, '+pet.name+'!');confetti();
        if(typeof gtag!=='undefined')gtag('event','pet_adopted',{{game:game,character:pick[1]}});
    }},3500);
}};

window._releasePet=function(){{
    if(!confirm('Release '+pet.name+'? This cannot be undone.'))return;
    localStorage.removeItem(KEY);pet=null;show('screen-pick');
}};

(function init(){{
    load();
    if(pet){{var r=calcOffline();show('screen-pet');updateUI();updateCD();if(r)showAway(r);}}
    else{{var p=new URLSearchParams(window.location.search),g=p.get('game');if(g&&GAMES[g])window._startAdopt(g);else show('screen-pick');}}
    setInterval(updateCD,1000);
}})();
</script>
</body>
</html>'''


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    # Build channel pages
    for slug, ch in CHANNELS.items():
        out_dir = BASE / slug
        out_dir.mkdir(exist_ok=True)
        html = build_channel_page(slug, ch)
        (out_dir / "index.html").write_text(html, encoding="utf-8")
        print(f"  Built {slug}/index.html ({len(ch.get('generators', []))} generators)")

    # Adopt page IS the homepage now
    html = build_adopt_page()
    (BASE / "index.html").write_text(html, encoding="utf-8")
    print(f"  Built index.html (adopt page = homepage)")

    # Old channel hub goes to /channels/
    html = build_homepage()
    channels_dir = BASE / "channels"
    channels_dir.mkdir(exist_ok=True)
    (channels_dir / "index.html").write_text(html, encoding="utf-8")
    print(f"  Built channels/index.html (channel hub)")

    # Also keep /adopt/ working as a redirect/copy
    adopt_dir = BASE / "adopt"
    adopt_dir.mkdir(exist_ok=True)
    adopt_html = build_adopt_page()
    (adopt_dir / "index.html").write_text(adopt_html, encoding="utf-8")
    print(f"  Built adopt/index.html (copy)")

    print(f"\nDone! {len(CHANNELS)} channel pages + homepage + channels hub built.")


if __name__ == "__main__":
    main()
