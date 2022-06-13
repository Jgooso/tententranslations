import json
from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import datetime
from scripts import download
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
tags = ['Ability&nbsp;Steal','Absent&nbsp;Parents','Abusive&nbsp;Characters','Academy','Accelerated&nbsp;Growth','Acting','Adapted&nbsp;from&nbsp;Manga',
'Adapted&nbsp;from&nbsp;Manhua','Adapted&nbsp;to&nbsp;Anime','Adapted&nbsp;to&nbsp;Drama','Adapted&nbsp;to&nbsp;Drama&nbsp;CD','Adapted&nbsp;to&nbsp;Game','Adapted&nbsp;to&nbsp;Manga',
'Adapted&nbsp;to&nbsp;Manhua','Adapted&nbsp;to&nbsp;Manhwa','Adapted&nbsp;to&nbsp;Movie','Adapted&nbsp;to&nbsp;Visual&nbsp;Novel','Adopted&nbsp;Children','Adopted&nbsp;Protagonist',
'Adultery','Adventurers','Affair','Age&nbsp;Progression','Age&nbsp;Regression','Aggressive&nbsp;Characters','Alchemy','Aliens','All-Girls&nbsp;School',
'Alternate&nbsp;World','Amnesia','Amusement&nbsp;Park','Anal','Ancient&nbsp;China','Ancient&nbsp;Times','Androgynous&nbsp;Characters','Androids','Angels',
'Animal&nbsp;Characteristics','Animal&nbsp;Rearing','Anti-Magic','Anti-social&nbsp;Protagonist','Antihero&nbsp;Protagonist','Antique&nbsp;Shop',
'Apartment&nbsp;Life','Apathetic&nbsp;Protagonist','Apocalypse','Appearance&nbsp;Changes','Appearance&nbsp;Different&nbsp;from&nbsp;Actual&nbsp;Age','Archery',
'Aristocracy','Arms&nbsp;Dealers','Army','Army&nbsp;Building','Arranged&nbsp;Marriage','Arrogant&nbsp;Characters','Artifact&nbsp;Crafting','Artifacts',
'Artificial&nbsp;Intelligence','Artists','Assassins','Astrologers','Autism','Automatons','Average-looking&nbsp;Protagonist',
'Award-winning&nbsp;Work','Awkward&nbsp;Protagonist','Bands','Based&nbsp;on&nbsp;a&nbsp;Movie','Based&nbsp;on&nbsp;a&nbsp;Song','Based&nbsp;on&nbsp;a&nbsp;TV&nbsp;Show',
'Based&nbsp;on&nbsp;a&nbsp;Video&nbsp;Game','Based&nbsp;on&nbsp;a&nbsp;Visual&nbsp;Novel','Based&nbsp;on&nbsp;an&nbsp;Anime','Battle&nbsp;Academy','Battle&nbsp;Competition','BDSM',
'Beast&nbsp;Companions','Beastkin','Beasts','Beautiful&nbsp;Female&nbsp;Lead','Bestiality','Betrayal','Bickering&nbsp;Couple','Biochip',
'Bisexual&nbsp;Protagonist','Black&nbsp;Belly','Blackmail','Blacksmith','Blind&nbsp;Dates','Blind&nbsp;Protagonist','Blood&nbsp;Manipulation',
'Bloodlines','Body&nbsp;Swap','Body&nbsp;Tempering','Body-double','Bodyguards','Books','Bookworm','Boss-Subordinate&nbsp;Relationship',
'Brainwashing','Breast&nbsp;Fetish','Broken&nbsp;Engagement','Brother&nbsp;Complex','Brotherhood','Buddhism','Bullying','Business&nbsp;Management',
'Businessmen','Butlers','Calm&nbsp;Protagonist','Cannibalism','Card&nbsp;Games','Carefree&nbsp;Protagonist','Caring&nbsp;Protagonist',
'Cautious&nbsp;Protagonist','Celebrities','Character&nbsp;Growth','Charismatic&nbsp;Protagonist','Charming&nbsp;Protagonist','Chat&nbsp;Rooms',
'Cheats','Chefs','Child&nbsp;Abuse','Child&nbsp;Protagonist','Childcare','Childhood&nbsp;Friends','Childhood&nbsp;Love','Childhood&nbsp;Promise',
'Childish&nbsp;Protagonist','Chuunibyou','Clan&nbsp;Building','Classic','Clever&nbsp;Protagonist','Clingy&nbsp;Lover','Clones','Clubs',
'Clumsy&nbsp;Love&nbsp;Interests','Co-Workers','Cohabitation','Cold&nbsp;Love&nbsp;Interests','Cold&nbsp;Protagonist','Collection&nbsp;of&nbsp;Short&nbsp;Stories',
'College/University','Coma','Comedic&nbsp;Undertone','Coming&nbsp;of&nbsp;Age','Complex&nbsp;Family&nbsp;Relationships','Conditional&nbsp;Power',
'Confident&nbsp;Protagonist','Confinement','Conflicting&nbsp;Loyalties','Contracts','Cooking','Corruption','Cosmic&nbsp;Wars','Cosplay',
'Couple&nbsp;Growth','Court&nbsp;Official','Cousins','Cowardly&nbsp;Protagonist','Crafting','Crime','Criminals','Cross-dressing','Crossover',
'Cruel&nbsp;Characters','Cryostasis','Cultivation','Cunnilingus','Cunning&nbsp;Protagonist','Curious&nbsp;Protagonist','Curses','Cute&nbsp;Children',
'Cute&nbsp;Protagonist','Cute&nbsp;Story','Dancers','Dao&nbsp;Companion','Dao&nbsp;Comprehension','Daoism','Dark','Dead&nbsp;Protagonist','Death',
'Death&nbsp;of&nbsp;Loved&nbsp;Ones','Debts','Delinquents','Delusions','Demi-Humans','Demon&nbsp;Lord','Demonic&nbsp;Cultivation&nbsp;Technique','Demons',
'Dense&nbsp;Protagonist','Depictions&nbsp;of&nbsp;Cruelty','Depression','Destiny','Detectives','Determined&nbsp;Protagonist','Devoted&nbsp;Love&nbsp;Interests',
'Different&nbsp;Social&nbsp;Status','Disabilities','Discrimination','Disfigurement','Dishonest&nbsp;Protagonist','Distrustful&nbsp;Protagonist',
'Divination','Divine&nbsp;Protection','Divorce','Doctors','Dolls/Puppets','Domestic&nbsp;Affairs','Doting&nbsp;Love&nbsp;Interests',
'Doting&nbsp;Older&nbsp;Siblings','Doting&nbsp;Parents','Dragon&nbsp;Riders','Dragon&nbsp;Slayers','Dragons','Dreams','Drugs','Druids',
'Dungeon&nbsp;Master','Dungeons','Dwarfs','Dystopia','e-Sports','Early&nbsp;Romance','Earth&nbsp;Invasion','Easy&nbsp;Going&nbsp;Life',
'Economics','Editors','Eidetic&nbsp;Memory','Elderly&nbsp;Protagonist','Elemental&nbsp;Magic','Elves','Emotionally&nbsp;Weak&nbsp;Protagonist',
'Empires','Enemies&nbsp;Become&nbsp;Allies','Enemies&nbsp;Become&nbsp;Lovers','Engagement','Engineer','Enlightenment','Episodic','Eunuch',
'European&nbsp;Ambience','Evil&nbsp;Gods','Evil&nbsp;Organizations','Evil&nbsp;Protagonist','Evil&nbsp;Religions','Evolution','Exhibitionism',
'Exorcism','Eye&nbsp;Powers','Fairies','Fallen&nbsp;Angels','Fallen&nbsp;Nobility','Familial&nbsp;Love','Familiars','Family','Family&nbsp;Business',
'Family&nbsp;Conflict','Famous&nbsp;Parents','Famous&nbsp;Protagonist','Fanaticism','Fanfiction','Fantasy&nbsp;Creatures','Fantasy&nbsp;World',
'Farming','Fast&nbsp;Cultivation','Fast&nbsp;Learner','Fat&nbsp;Protagonist','Fat&nbsp;to&nbsp;Fit','Fated&nbsp;Lovers','Fearless&nbsp;Protagonist','Fellatio',
'Female&nbsp;Master','Female&nbsp;Protagonist','Female&nbsp;to&nbsp;Male','Feng&nbsp;Shui','Firearms','First&nbsp;Love','First-time&nbsp;Intercourse','Flashbacks',
'Fleet&nbsp;Battles','Folklore','Forced&nbsp;into&nbsp;a&nbsp;Relationship','Forced&nbsp;Living&nbsp;Arrangements','Forced&nbsp;Marriage','Forgetful&nbsp;Protagonist',
'Former&nbsp;Hero','Fox&nbsp;Spirits','Friends&nbsp;Become&nbsp;Enemies','Friendship','Fujoshi','Futanari','Futuristic&nbsp;Setting','Galge','Gambling',
'Game&nbsp;Elements','Game&nbsp;Ranking&nbsp;System','Gamers','Gangs','Gate&nbsp;to&nbsp;Another&nbsp;World','Genderless&nbsp;Protagonist','Generals',
'Genetic&nbsp;Modifications','Genies','Genius&nbsp;Protagonist','Ghosts','Gladiators','Glasses-wearing&nbsp;Love&nbsp;Interests',
'Glasses-wearing&nbsp;Protagonist','Goblins','God&nbsp;Protagonist','God-human&nbsp;Relationship','Goddesses','Godly&nbsp;Powers','Gods','Golems',
'Gore','Grave&nbsp;Keepers','Grinding','Guardian&nbsp;Relationship','Guilds','Gunfighters','Hackers','Half-human&nbsp;Protagonist','Handjob',
'Handsome&nbsp;Male&nbsp;Lead','Hard-Working&nbsp;Protagonist','Harem-seeking&nbsp;Protagonist','Harsh&nbsp;Training','Hated&nbsp;Protagonist','Healers',
'Heartwarming','Heaven','Heavenly&nbsp;Tribulation','Hell','Helpful&nbsp;Protagonist','Herbalist','Heroes','Heterochromia',
'Hidden&nbsp;Abilities','Hiding&nbsp;True&nbsp;Abilities','Hiding&nbsp;True&nbsp;Identity','Hikikomori','Homunculus','Honest&nbsp;Protagonist','Hospital',
'Hot-blooded&nbsp;Protagonist','Human&nbsp;Experimentation','Human&nbsp;Weapon','Human-Nonhuman&nbsp;Relationship','Humanoid&nbsp;Protagonist','Hunters',
'Hypnotism','Identity&nbsp;Crisis','Imaginary&nbsp;Friend','Immortals','Imperial&nbsp;Harem','Incest','Incubus','Indecisive&nbsp;Protagonist',
'Industrialization','Inferiority&nbsp;Complex','Inheritance','Inscriptions','Insects','Interconnected&nbsp;Storylines',
'Interdimensional&nbsp;Travel','Introverted&nbsp;Protagonist','Investigations','Invisibility','Jack&nbsp;of&nbsp;All&nbsp;Trades','Jealousy',
'Jiangshi','Jobless&nbsp;Class','JSDF','Kidnappings','Kind&nbsp;Love&nbsp;Interests','Kingdom&nbsp;Building','Kingdoms','Knights','Kuudere',
'Lack&nbsp;of&nbsp;Common&nbsp;Sense','Language&nbsp;Barrier','Late&nbsp;Romance','Lawyers','Lazy&nbsp;Protagonist','Leadership','Legends','Level&nbsp;System',
'Library','Limited&nbsp;Lifespan','Living&nbsp;Abroad','Living&nbsp;Alone','Loli','Loneliness','Loner&nbsp;Protagonist','Long&nbsp;Separations',
'Long-distance&nbsp;Relationship','Lost&nbsp;Civilizations','Lottery','Love&nbsp;at&nbsp;First&nbsp;Sight','Love&nbsp;Interest&nbsp;Falls&nbsp;in&nbsp;Love&nbsp;First',
'Love&nbsp;Rivals','Love&nbsp;Triangles','Lovers&nbsp;Reunited','Low-key&nbsp;Protagonist','Loyal&nbsp;Subordinates','Lucky&nbsp;Protagonist','Magic',
'Magic&nbsp;Beasts','Magic&nbsp;Formations','Magical&nbsp;Girls','Magical&nbsp;Space','Magical&nbsp;Technology','Maids','Male&nbsp;Protagonist','Male&nbsp;to&nbsp;Female',
'Male&nbsp;Yandere','Management','Mangaka','Manipulative&nbsp;Characters','Manly&nbsp;Gay&nbsp;Couple','Marriage','Marriage&nbsp;of&nbsp;Convenience',
'Martial&nbsp;Spirits','Masochistic&nbsp;Characters','Master-Disciple&nbsp;Relationship','Master-Servant&nbsp;Relationship','Masturbation',
'Matriarchy','Mature&nbsp;Protagonist','Medical&nbsp;Knowledge','Medieval','Mercenaries','Merchants','Military','Mind&nbsp;Break',
'Mind&nbsp;Control','Misandry','Mismatched&nbsp;Couple','Misunderstandings','MMORPG','Mob&nbsp;Protagonist','Models','Modern&nbsp;Day',
'Modern&nbsp;Knowledge','Money&nbsp;Grubber','Monster&nbsp;Girls','Monster&nbsp;Society','Monster&nbsp;Tamer','Monsters','Movies','Mpreg',
'Multiple&nbsp;Identities','Multiple&nbsp;Personalities','Multiple&nbsp;POV','Multiple&nbsp;Protagonists','Multiple&nbsp;Realms',
'Multiple&nbsp;Reincarnated&nbsp;Individuals','Multiple&nbsp;Timelines','Multiple&nbsp;Transported&nbsp;Individuals','Murders','Music',
'Mutated&nbsp;Creatures','Mutations','Mute&nbsp;Character','Mysterious&nbsp;Family&nbsp;Background','Mysterious&nbsp;Illness','Mysterious&nbsp;Past',
'Mystery&nbsp;Solving','Mythical&nbsp;Beasts','Mythology','Naive&nbsp;Protagonist','Narcissistic&nbsp;Protagonist','Nationalism',
'Near-Death&nbsp;Experience','Necromancer','Neet','Netorare','Netorase','Netori','Nightmares','Ninjas','Nobles',
'Non-humanoid&nbsp;Protagonist','Non-linear&nbsp;Storytelling','Nudity','Nurses','Obsessive&nbsp;Love','Office&nbsp;Romance',
'Older&nbsp;Love&nbsp;Interests','Omegaverse','Oneshot','Online&nbsp;Romance','Onmyouji','Orcs','Organized&nbsp;Crime','Orgy','Orphans','Otaku',
'Otome&nbsp;Game','Outcasts','Outdoor&nbsp;Intercourse','Outer&nbsp;Space','Overpowered&nbsp;Protagonist','Overprotective&nbsp;Siblings',
'Pacifist&nbsp;Protagonist','Paizuri','Parallel&nbsp;Worlds','Parasites','Parent&nbsp;Complex','Parody','Part-Time&nbsp;Job','Past&nbsp;Plays&nbsp;a&nbsp;Big&nbsp;Role',
'Past&nbsp;Trauma','Persistent&nbsp;Love&nbsp;Interests','Personality&nbsp;Changes','Perverted&nbsp;Protagonist','Pets','Pharmacist','Philosophical',
'Phobias','Phoenixes','Photography','Pill&nbsp;Based&nbsp;Cultivation','Pill&nbsp;Concocting','Pilots','Pirates','Playboys','Playful&nbsp;Protagonist',
'Poetry','Poisons','Police','Polite&nbsp;Protagonist','Politics','Polyandry','Polygamy','Poor&nbsp;Protagonist','Poor&nbsp;to&nbsp;Rich',
'Popular&nbsp;Love&nbsp;Interests','Possession','Possessive&nbsp;Characters','Post-apocalyptic','Power&nbsp;Couple','Power&nbsp;Struggle',
'Pragmatic&nbsp;Protagonist','Precognition','Pregnancy','Pretend&nbsp;Lovers','Previous&nbsp;Life&nbsp;Talent','Priestesses','Priests','Prison',
'Proactive&nbsp;Protagonist','Programmer','Prophecies','Prostitutes','Protagonist&nbsp;Falls&nbsp;in&nbsp;Love&nbsp;First',
'Protagonist&nbsp;Strong&nbsp;from&nbsp;the&nbsp;Start','Protagonist&nbsp;with&nbsp;Multiple&nbsp;Bodies','Psychic&nbsp;Powers','Psychopaths','Puppeteers',
'Quiet&nbsp;Characters','Quirky&nbsp;Characters','R-','R-','Race&nbsp;Change','Racism','Rape','Rape&nbsp;Victim&nbsp;Becomes&nbsp;Lover','Rebellion',
'Reincarnated&nbsp;as&nbsp;a&nbsp;Monster','Reincarnated&nbsp;as&nbsp;an&nbsp;Object','Reincarnated&nbsp;in&nbsp;a&nbsp;Game&nbsp;World','Reincarnated&nbsp;in&nbsp;Another&nbsp;World',
'Reincarnation','Religions','Reluctant&nbsp;Protagonist','Reporters','Restaurant','Resurrection','Returning&nbsp;from&nbsp;Another&nbsp;World',
'Revenge','Reverse&nbsp;Harem','Reverse&nbsp;Rape','Reversible&nbsp;Couple','Rich&nbsp;to&nbsp;Poor','Righteous&nbsp;Protagonist','Rivalry','Romantic&nbsp;Subplot',
'Roommates','Royalty','Ruthless&nbsp;Protagonist','Sadistic&nbsp;Characters','Saints','Salaryman','Samurai','Saving&nbsp;the&nbsp;World',
'Schemes&nbsp;And&nbsp;Conspiracies','Schizophrenia','Scientists','Sculptors','Sealed&nbsp;Power','Second&nbsp;Chance','Secret&nbsp;Crush',
'Secret&nbsp;Identity','Secret&nbsp;Organizations','Secret&nbsp;Relationship','Secretive&nbsp;Protagonist','Secrets','Sect&nbsp;Development','Seduction',
"Seeing&nbsp;Things&nbsp;Other&nbsp;Humans&nbsp;Can't",'Selfish&nbsp;Protagonist','Selfless&nbsp;Protagonist','Seme&nbsp;Protagonist','Senpai-Kouhai&nbsp;Relationship',
'Sentient&nbsp;Objects','Sentimental&nbsp;Protagonist','Serial&nbsp;Killers','Servants','Seven&nbsp;Deadly&nbsp;Sins','Seven&nbsp;Virtues','Sex&nbsp;Friends',
'Sex&nbsp;Slaves','Sexual&nbsp;Abuse','Sexual&nbsp;Cultivation&nbsp;Technique','Shameless&nbsp;Protagonist','Shapeshifters','Sharing&nbsp;A&nbsp;Body',
'Sharp-tongued&nbsp;Characters','Shield&nbsp;User','Shikigami','Short&nbsp;Story','Shota','Shoujo-Ai&nbsp;Subplot','Shounen-Ai&nbsp;Subplot',
'Showbiz','Shy&nbsp;Characters','Sibling&nbsp;Rivalry',"Sibling's&nbsp;Care",'Siblings','Siblings&nbsp;Not&nbsp;Related&nbsp;by&nbsp;Blood','Sickly&nbsp;Characters',
'Sign&nbsp;Language','Singers','Single&nbsp;Parent','Sister&nbsp;Complex','Skill&nbsp;Assimilation','Skill&nbsp;Books','Skill&nbsp;Creation','Slave&nbsp;Harem',
'Slave&nbsp;Protagonist','Slaves','Sleeping','Slow&nbsp;Growth&nbsp;at&nbsp;Start','Slow&nbsp;Romance','Smart&nbsp;Couple','Social&nbsp;Outcasts','Soldiers',
'Soul&nbsp;Power','Souls','Spatial&nbsp;Manipulation','Spear&nbsp;Wielder','Special&nbsp;Abilities','Spies','Spirit&nbsp;Advisor','Spirit&nbsp;Users','Spirits',
'Stalkers','Stockholm&nbsp;Syndrome','Stoic&nbsp;Characters','Store&nbsp;Owner','Straight&nbsp;Seme','Straight&nbsp;Uke','Strategic&nbsp;Battles','Strategist',
'Strength-based&nbsp;Social&nbsp;Hierarchy','Strong&nbsp;Love&nbsp;Interests','Strong&nbsp;to&nbsp;Stronger','Stubborn&nbsp;Protagonist','Student&nbsp;Council','Student-Teacher&nbsp;Relationship',
'Succubus','Sudden&nbsp;Strength&nbsp;Gain','Sudden&nbsp;Wealth','Suicides','Summoned&nbsp;Hero','Summoning&nbsp;Magic','Survival','Survival&nbsp;Game','Sword&nbsp;And&nbsp;Magic',
'Sword&nbsp;Wielder','System&nbsp;Administrator','Teachers','Teamwork','Technological&nbsp;Gap','Tentacles','Terminal&nbsp;Illness','Terrorists','Thieves','Threesome',
'Thriller','Time&nbsp;Loop','Time&nbsp;Manipulation','Time&nbsp;Paradox','Time&nbsp;Skip','Time&nbsp;Travel','Timid&nbsp;Protagonist','Tomboyish&nbsp;Female&nbsp;Lead','Torture','Toys','Tragic&nbsp;Past',
'Transformation&nbsp;Ability','Transmigration','Transplanted&nbsp;Memories','Transported&nbsp;into&nbsp;a&nbsp;Game&nbsp;World','Transported&nbsp;Modern&nbsp;Structure','Transported&nbsp;to&nbsp;Another&nbsp;World',
'Trap','Tribal&nbsp;Society','Trickster','Tsundere','Twins','Twisted&nbsp;Personality','Ugly&nbsp;Protagonist','Ugly&nbsp;to&nbsp;Beautiful','Unconditional&nbsp;Love','Underestimated&nbsp;Protagonist',
'Unique&nbsp;Cultivation&nbsp;Technique','Unique&nbsp;Weapon&nbsp;User','Unique&nbsp;Weapons','Unlimited&nbsp;Flow','Unlucky&nbsp;Protagonist','Unreliable&nbsp;Narrator','Unrequited&nbsp;Love','Valkyries','Vampires',
'Villainess&nbsp;Noble&nbsp;Girls','Virtual&nbsp;Reality','Vocaloid','Voice&nbsp;Actors','Voyeurism','Waiters','War&nbsp;Records','Wars','Weak&nbsp;Protagonist','Weak&nbsp;to&nbsp;Strong','Wealthy&nbsp;Characters','Werebeasts',
'Wishes','Witches','Wizards','World&nbsp;Hopping','World&nbsp;Travel','World&nbsp;Tree','Writers','Yandere','Youkai','Younger&nbsp;Brothers','Younger&nbsp;Love&nbsp;Interests','Younger&nbsp;Sisters','Zombies']
@app.route('/novel/multiple', methods = ['GET'])
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
@app.route('/novel/single', methods = ['GET','POST','PUT','DELETE'])
def singlenovel():
    novel = request.args.get('novel')
    tier = request.args.get('tier')
    if request.method == 'GET':
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
    if request.method == 'POST':
        data = request.get_json()
        input_tags = data['tags']
        input_genres = data['genres']
        input_url = data['url']
        download(URL=input_url,tags=input_tags,genres=input_genres)
        return data
    if request.method == 'PUT':
        data = request.get_json()
        sql = 'UPDATE novel SET description = %s, genres = %s, tags = %s, completed = %s WHERE novelid = %s'
        val = (data['description'],data['genres'],data['tags'],data['completed'],novel)
        novelcursor.execute(sql,val)
        return data
    if request.method == 'DELETE':
        sql = 'DELETE FROM novel WHERE novelid=%s'
        val = (novel,)
        novelcursor.execute(sql,val)
    

@app.route('/chapter', methods = ['GET','PUT'])
def get_chapter():
    chapter = request.args.get('chapter')
    novel = request.args.get('novel')
    if request.method == 'GET':
        chapter_sql = "SELECT DISTINCT content FROM Chapters WHERE chapternumber = %s AND novelid=%s;UPDATE novel SET views = views +1 WHERE novelid = %s"
        chapter_val = (chapter,novel,novel)
        novelcursor.execute(chapter_sql,chapter_val,multi = True)
        for result in novelcursor.execute(chapter_sql,chapter_val,multi=True):
            if result.with_rows:
                chapter_results = novelcursor.fetchall()[0][0]
        noveldb.commit()
        return jsonify(chapter_results) 
    if request.method == 'PUT':
        data = request.get_json()
        sql = 'UPDATE chapters SET content = %s WHERE chapternumber = %s AND novelid = %s'
        val = (data['content'],chapter,novel)
        novelcursor.execute(sql,val)
        print(data)
        return data
@app.route('/uploaddata',methods=['GET'])
def get_genres_and_tags():
    if request.method == 'GET':
        return jsonify({'genres':genres, 'tags':tags})
@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Origin, X-Requested-With, Content-Type, Accept, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD'
    return response
app.run()
