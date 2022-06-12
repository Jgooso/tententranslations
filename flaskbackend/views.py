import json
from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import datetime
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
config = {
'user': 'root',
'password': 'jeg4Iphone',
'host': '127.0.0.1',
'port': '3306',
'database': 'novels',
'raise_on_warnings': True,}
noveldb = mysql.connector.connect(**config)
novelcursor = noveldb.cursor(buffered=True)
genres = ['Action','Adult','Adventure','Comedy','Drame','Ecchi','Fantasy','Gender Bender','Harem',
'Historical','Horror','Josei','Martial Arts','Mature','Mecha','Mystery','Psychological','Romance',
'School Life','Sci-fi','Seinen','Shoujo','Shoujo Ai','Shounen Ai','Slice of Life','Smut',
'Sports','Supernatural','Tragedy','Wuxia','Xianxia','Xuanhuan','Yaoi','Yuri']
tags = ['Ability Steal','Absent Parents','Abusive Characters','Academy','Accelerated Growth','Acting','Adapted from Manga',
'Adapted from Manhua','Adapted to Anime','Adapted to Drama','Adapted to Drama CD','Adapted to Game','Adapted to Manga',
'Adapted to Manhua','Adapted to Manhwa','Adapted to Movie','Adapted to Visual Novel','Adopted Children','Adopted Protagonist',
'Adultery','Adventurers','Affair','Age Progression','Age Regression','Aggressive Characters','Alchemy','Aliens','All-Girls School',
'Alternate World','Amnesia','Amusement Park','Anal','Ancient China','Ancient Times','Androgynous Characters','Androids','Angels',
'Animal Characteristics','Animal Rearing','Anti-Magic','Anti-social Protagonist','Antihero Protagonist','Antique Shop',
'Apartment Life','Apathetic Protagonist','Apocalypse','Appearance Changes','Appearance Different from Actual Age','Archery',
'Aristocracy','Arms Dealers','Army','Army Building','Arranged Marriage','Arrogant Characters','Artifact Crafting','Artifacts',
'Artificial Intelligence','Artists','Assassins','Astrologers','Autism','Automatons','Average-looking Protagonist',
'Award-winning Work','Awkward Protagonist','Bands','Based on a Movie','Based on a Song','Based on a TV Show',
'Based on a Video Game','Based on a Visual Novel','Based on an Anime','Battle Academy','Battle Competition','BDSM',
'Beast Companions','Beastkin','Beasts','Beautiful Female Lead','Bestiality','Betrayal','Bickering Couple','Biochip',
'Bisexual Protagonist','Black Belly','Blackmail','Blacksmith','Blind Dates','Blind Protagonist','Blood Manipulation',
'Bloodlines','Body Swap','Body Tempering','Body-double','Bodyguards','Books','Bookworm','Boss-Subordinate Relationship',
'Brainwashing','Breast Fetish','Broken Engagement','Brother Complex','Brotherhood','Buddhism','Bullying','Business Management',
'Businessmen','Butlers','Calm Protagonist','Cannibalism','Card Games','Carefree Protagonist','Caring Protagonist',
'Cautious Protagonist','Celebrities','Character Growth','Charismatic Protagonist','Charming Protagonist','Chat Rooms',
'Cheats','Chefs','Child Abuse','Child Protagonist','Childcare','Childhood Friends','Childhood Love','Childhood Promise',
'Childish Protagonist','Chuunibyou','Clan Building','Classic','Clever Protagonist','Clingy Lover','Clones','Clubs',
'Clumsy Love Interests','Co-Workers','Cohabitation','Cold Love Interests','Cold Protagonist','Collection of Short Stories',
'College/University','Coma','Comedic Undertone','Coming of Age','Complex Family Relationships','Conditional Power',
'Confident Protagonist','Confinement','Conflicting Loyalties','Contracts','Cooking','Corruption','Cosmic Wars','Cosplay',
'Couple Growth','Court Official','Cousins','Cowardly Protagonist','Crafting','Crime','Criminals','Cross-dressing','Crossover',
'Cruel Characters','Cryostasis','Cultivation','Cunnilingus','Cunning Protagonist','Curious Protagonist','Curses','Cute Children',
'Cute Protagonist','Cute Story','Dancers','Dao Companion','Dao Comprehension','Daoism','Dark','Dead Protagonist','Death',
'Death of Loved Ones','Debts','Delinquents','Delusions','Demi-Humans','Demon Lord','Demonic Cultivation Technique','Demons',
'Dense Protagonist','Depictions of Cruelty','Depression','Destiny','Detectives','Determined Protagonist','Devoted Love Interests',
'Different Social Status','Disabilities','Discrimination','Disfigurement','Dishonest Protagonist','Distrustful Protagonist',
'Divination','Divine Protection','Divorce','Doctors','Dolls/Puppets','Domestic Affairs','Doting Love Interests',
'Doting Older Siblings','Doting Parents','Dragon Riders','Dragon Slayers','Dragons','Dreams','Drugs','Druids',
'Dungeon Master','Dungeons','Dwarfs','Dystopia','e-Sports','Early Romance','Earth Invasion','Easy Going Life',
'Economics','Editors','Eidetic Memory','Elderly Protagonist','Elemental Magic','Elves','Emotionally Weak Protagonist',
'Empires','Enemies Become Allies','Enemies Become Lovers','Engagement','Engineer','Enlightenment','Episodic','Eunuch',
'European Ambience','Evil Gods','Evil Organizations','Evil Protagonist','Evil Religions','Evolution','Exhibitionism',
'Exorcism','Eye Powers','Fairies','Fallen Angels','Fallen Nobility','Familial Love','Familiars','Family','Family Business',
'Family Conflict','Famous Parents','Famous Protagonist','Fanaticism','Fanfiction','Fantasy Creatures','Fantasy World',
'Farming','Fast Cultivation','Fast Learner','Fat Protagonist','Fat to Fit','Fated Lovers','Fearless Protagonist','Fellatio',
'Female Master','Female Protagonist','Female to Male','Feng Shui','Firearms','First Love','First-time Intercourse','Flashbacks',
'Fleet Battles','Folklore','Forced into a Relationship','Forced Living Arrangements','Forced Marriage','Forgetful Protagonist',
'Former Hero','Fox Spirits','Friends Become Enemies','Friendship','Fujoshi','Futanari','Futuristic Setting','Galge','Gambling',
'Game Elements','Game Ranking System','Gamers','Gangs','Gate to Another World','Genderless Protagonist','Generals',
'Genetic Modifications','Genies','Genius Protagonist','Ghosts','Gladiators','Glasses-wearing Love Interests',
'Glasses-wearing Protagonist','Goblins','God Protagonist','God-human Relationship','Goddesses','Godly Powers','Gods','Golems',
'Gore','Grave Keepers','Grinding','Guardian Relationship','Guilds','Gunfighters','Hackers','Half-human Protagonist','Handjob',
'Handsome Male Lead','Hard-Working Protagonist','Harem-seeking Protagonist','Harsh Training','Hated Protagonist','Healers',
'Heartwarming','Heaven','Heavenly Tribulation','Hell','Helpful Protagonist','Herbalist','Heroes','Heterochromia',
'Hidden Abilities','Hiding True Abilities','Hiding True Identity','Hikikomori','Homunculus','Honest Protagonist','Hospital',
'Hot-blooded Protagonist','Human Experimentation','Human Weapon','Human-Nonhuman Relationship','Humanoid Protagonist','Hunters',
'Hypnotism','Identity Crisis','Imaginary Friend','Immortals','Imperial Harem','Incest','Incubus','Indecisive Protagonist',
'Industrialization','Inferiority Complex','Inheritance','Inscriptions','Insects','Interconnected Storylines',
'Interdimensional Travel','Introverted Protagonist','Investigations','Invisibility','Jack of All Trades','Jealousy',
'Jiangshi','Jobless Class','JSDF','Kidnappings','Kind Love Interests','Kingdom Building','Kingdoms','Knights','Kuudere',
'Lack of Common Sense','Language Barrier','Late Romance','Lawyers','Lazy Protagonist','Leadership','Legends','Level System',
'Library','Limited Lifespan','Living Abroad','Living Alone','Loli','Loneliness','Loner Protagonist','Long Separations',
'Long-distance Relationship','Lost Civilizations','Lottery','Love at First Sight','Love Interest Falls in Love First',
'Love Rivals','Love Triangles','Lovers Reunited','Low-key Protagonist','Loyal Subordinates','Lucky Protagonist','Magic',
'Magic Beasts','Magic Formations','Magical Girls','Magical Space','Magical Technology','Maids','Male Protagonist','Male to Female',
'Male Yandere','Management','Mangaka','Manipulative Characters','Manly Gay Couple','Marriage','Marriage of Convenience',
'Martial Spirits','Masochistic Characters','Master-Disciple Relationship','Master-Servant Relationship','Masturbation',
'Matriarchy','Mature Protagonist','Medical Knowledge','Medieval','Mercenaries','Merchants','Military','Mind Break',
'Mind Control','Misandry','Mismatched Couple','Misunderstandings','MMORPG','Mob Protagonist','Models','Modern Day',
'Modern Knowledge','Money Grubber','Monster Girls','Monster Society','Monster Tamer','Monsters','Movies','Mpreg',
'Multiple Identities','Multiple Personalities','Multiple POV','Multiple Protagonists','Multiple Realms',
'Multiple Reincarnated Individuals','Multiple Timelines','Multiple Transported Individuals','Murders','Music',
'Mutated Creatures','Mutations','Mute Character','Mysterious Family Background','Mysterious Illness','Mysterious Past',
'Mystery Solving','Mythical Beasts','Mythology','Naive Protagonist','Narcissistic Protagonist','Nationalism',
'Near-Death Experience','Necromancer','Neet','Netorare','Netorase','Netori','Nightmares','Ninjas','Nobles',
'Non-humanoid Protagonist','Non-linear Storytelling','Nudity','Nurses','Obsessive Love','Office Romance',
'Older Love Interests','Omegaverse','Oneshot','Online Romance','Onmyouji','Orcs','Organized Crime','Orgy','Orphans','Otaku',
'Otome Game','Outcasts','Outdoor Intercourse','Outer Space','Overpowered Protagonist','Overprotective Siblings',
'Pacifist Protagonist','Paizuri','Parallel Worlds','Parasites','Parent Complex','Parody','Part-Time Job','Past Plays a Big Role',
'Past Trauma','Persistent Love Interests','Personality Changes','Perverted Protagonist','Pets','Pharmacist','Philosophical',
'Phobias','Phoenixes','Photography','Pill Based Cultivation','Pill Concocting','Pilots','Pirates','Playboys','Playful Protagonist',
'Poetry','Poisons','Police','Polite Protagonist','Politics','Polyandry','Polygamy','Poor Protagonist','Poor to Rich',
'Popular Love Interests','Possession','Possessive Characters','Post-apocalyptic','Power Couple','Power Struggle',
'Pragmatic Protagonist','Precognition','Pregnancy','Pretend Lovers','Previous Life Talent','Priestesses','Priests','Prison',
'Proactive Protagonist','Programmer','Prophecies','Prostitutes','Protagonist Falls in Love First',
'Protagonist Strong from the Start','Protagonist with Multiple Bodies','Psychic Powers','Psychopaths','Puppeteers',
'Quiet Characters','Quirky Characters','R-','R-','Race Change','Racism','Rape','Rape Victim Becomes Lover','Rebellion',
'Reincarnated as a Monster','Reincarnated as an Object','Reincarnated in a Game World','Reincarnated in Another World',
'Reincarnation','Religions','Reluctant Protagonist','Reporters','Restaurant','Resurrection','Returning from Another World',
'Revenge','Reverse Harem','Reverse Rape','Reversible Couple','Rich to Poor','Righteous Protagonist','Rivalry','Romantic Subplot',
'Roommates','Royalty','Ruthless Protagonist','Sadistic Characters','Saints','Salaryman','Samurai','Saving the World',
'Schemes And Conspiracies','Schizophrenia','Scientists','Sculptors','Sealed Power','Second Chance','Secret Crush',
'Secret Identity','Secret Organizations','Secret Relationship','Secretive Protagonist','Secrets','Sect Development','Seduction',
"Seeing Things Other Humans Can't",'Selfish Protagonist','Selfless Protagonist','Seme Protagonist','Senpai-Kouhai Relationship',
'Sentient Objects','Sentimental Protagonist','Serial Killers','Servants','Seven Deadly Sins','Seven Virtues','Sex Friends',
'Sex Slaves','Sexual Abuse','Sexual Cultivation Technique','Shameless Protagonist','Shapeshifters','Sharing A Body',
'Sharp-tongued Characters','Shield User','Shikigami','Short Story','Shota','Shoujo-Ai Subplot','Shounen-Ai Subplot',
'Showbiz','Shy Characters','Sibling Rivalry',"Sibling's Care",'Siblings','Siblings Not Related by Blood','Sickly Characters',
'Sign Language','Singers','Single Parent','Sister Complex','Skill Assimilation','Skill Books','Skill Creation','Slave Harem',
'Slave Protagonist','Slaves','Sleeping','Slow Growth at Start','Slow Romance','Smart Couple','Social Outcasts','Soldiers',
'Soul Power','Souls','Spatial Manipulation','Spear Wielder','Special Abilities','Spies','Spirit Advisor','Spirit Users','Spirits',
'Stalkers','Stockholm Syndrome','Stoic Characters','Store Owner','Straight Seme','Straight Uke','Strategic Battles','Strategist',
'Strength-based Social Hierarchy','Strong Love Interests','Strong to Stronger','Stubborn Protagonist','Student Council','Student-Teacher Relationship',
'Succubus','Sudden Strength Gain','Sudden Wealth','Suicides','Summoned Hero','Summoning Magic','Survival','Survival Game','Sword And Magic',
'Sword Wielder','System Administrator','Teachers','Teamwork','Technological Gap','Tentacles','Terminal Illness','Terrorists','Thieves','Threesome',
'Thriller','Time Loop','Time Manipulation','Time Paradox','Time Skip','Time Travel','Timid Protagonist','Tomboyish Female Lead','Torture','Toys','Tragic Past',
'Transformation Ability','Transmigration','Transplanted Memories','Transported into a Game World','Transported Modern Structure','Transported to Another World',
'Trap','Tribal Society','Trickster','Tsundere','Twins','Twisted Personality','Ugly Protagonist','Ugly to Beautiful','Unconditional Love','Underestimated Protagonist',
'Unique Cultivation Technique','Unique Weapon User','Unique Weapons','Unlimited Flow','Unlucky Protagonist','Unreliable Narrator','Unrequited Love','Valkyries','Vampires',
'Villainess Noble Girls','Virtual Reality','Vocaloid','Voice Actors','Voyeurism','Waiters','War Records','Wars','Weak Protagonist','Weak to Strong','Wealthy Characters','Werebeasts',
'Wishes','Witches','Wizards','World Hopping','World Travel','World Tree','Writers','Yandere','Youkai','Younger Brothers','Younger Love Interests','Younger Sisters','Zombies']
@app.route('/novels', methods = ['GET'])
def multiplenovels():
    tier= request.args.get('tier')
    novelsql = "SELECT * FROM novel"
    chaptersql = "SELECT chapternumber,date FROM chapters WHERE CONTENT IS NOT NULL AND active <= %s AND novelid = %s ORDER BY chapternumber+0 DESC"
    novelObject = []
    novelcursor.execute(novelsql)
    novelresults = novelcursor.fetchall()
    columnNames = [column[0] for column in novelcursor.description]
    for record in novelresults:
        novelObject.append( dict( zip( columnNames , record ) ) )
    for novel in novelObject:
        val = (tier,novel['novelid'])
        novelcursor.execute(chaptersql,val)
        chapterResults = novelcursor.fetchall()
        try:
            novel['firstChapter'] = chapterResults[0]
            novel['secondChapter']=chapterResults[1]
        except IndexError:
            try:
                novel['fristChapter'] = chapterResults[0]
            except IndexError:
                pass
    return jsonify(novelObject)
@app.route('/singlenovel', methods = ['GET'])
def singlenovel():
    novel = request.args.get('novel')
    tier = request.args.get('tier')
    novel_sql = "SELECT DISTINCT * FROM novel WHERE novelid = %s"
    novel_val = (novel,)
    novelcursor.execute(novel_sql,novel_val)
    novel_results=novelcursor.fetchall()
    chapter_list = []
    novelData = []
    columnNames = [column[0] for column in novelcursor.description]
    for record in novel_results:
        novelData.append( dict( zip( columnNames , record ) ) )
    chapter_list_sql = "SELECT title,date,chapternumber,section,novelid,chapterorder FROM chapters WHERE novelid = %s AND active <= %s ORDER BY chapterorder+0"
    chapter_list_val = (novel,tier)
    novelcursor.execute(chapter_list_sql,chapter_list_val)
    chapter_results = novelcursor.fetchall()
    chapter_column_names = [column[0] for column in novelcursor.description]
    chapter_list=[]
    for record in chapter_results:
        chapter_list.append( dict( zip( chapter_column_names , record ) ) )
    return jsonify({'Novel':novelData[0],'Chapters':chapter_list})

@app.route('/chapter', methods = ['GET'])
def get_chapter():
    chapter = request.args.get('chapter')
    novel = request.args.get('novel')
    chapter_sql = "SELECT DISTINCT content FROM Chapters WHERE chapternumber = %s AND novelid=%s;UPDATE novel SET views = views +1 WHERE novelid = %s"
    chapter_val = (chapter,novel,novel)
    novelcursor.execute(chapter_sql,chapter_val,multi = True)
    for result in novelcursor.execute(chapter_sql,chapter_val,multi=True):
        if result.with_rows:
            chapter_results = novelcursor.fetchall()[0][0]
    noveldb.commit()
    return jsonify(chapter_results) 

@app.route('/uploaddata',methods=['Get'])
def get_genres_and_tags():
    return jsonify({'genres':genres, 'tags':tags})
@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Origin, X-Requested-With, Content-Type, Accept, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD'
    return response
app.run()
