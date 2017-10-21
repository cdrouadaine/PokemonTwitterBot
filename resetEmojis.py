# -*- coding: UTF-8 -*-

import time, random, re, datetime, sys, os
from toolbox import *
import bddAccess as bdd

corrections = [
["Bulbizarre", ["bulbizard", "bulbizzarre", "bulbizzare", "bulbizzard"], "🌳"],
["Herbizarre", ["herbizard", "herbizzarre", "herbizzare", "herbizzard"], "🌷"],
["Florizarre", ["florrizarre", "florrizare", "florrizard", "florrizzare", "florizare", "florizzare", "florizzarre"], "🌴"],
["Salamèche", ["salamech"], "🦎"],
["Dracaufeu", ["dragofeu", "dragonfeu", "dracofeu"], "🐲"],
["Carabaffe", ["carabafe"], "🐢"],
["Chrysacier", ["crisacier", "chrisacier", "crysacier"], "🐛"],
["Coconfort", ["coconfor"], "🐛"],
["Dardargnan", ["dardagnan"], "🐝"],
["Papilusion", ["papylusion", "papillusion"], "🦋"],
["Roucool", ["roucoul", "roocoul"], "🐤"],
["Rattata", ["ratatta", "rattatta", "ratata"], "🐭"],
["Rattatac", ["ratattac", "rattattac", "ratatac", "ratattaque", "rattattaque", "ratataque", "rattataque"], "🐀"],
["Pikachu", ["pikatchu", "pikatchou -draw -what", "pikachou"], "🐹"],
["Goupix", ["goupyx"], "🦊"],
["Feunard", ["feunar"], "🦊"],
["Mystherbe", ["misterbe", "mysterbe", "mistherbe"], "🌿"],
["Rafflésia", ["raflesia"]],
["Parasect", ["parasecte -secte"], "🍄"],
["Mimitoss", ["mimitosse"]],
["Taupiqueur", ["topiqueur", "taupikeur", "topikeur -marc"]],
["Triopikeur", ["triopiqueur"]],
["Psykokwak", ["psikokwak", "psycokwak", "psyckokwak", "psychokwak"], "🦆"],
["Akwakwak", ["aquakwak", "akwaquak"], "🦆"],
["Férosinge", ["ferossinge", "ferrosinge"], "🐵"],
["Colossinge", ["colosinge", "collosinge", "collossinge"], "💢"],
["Ptitard", ["ptitar", "ptitart"], "🐸"],
["Alakazam", ["alakasam"], "🥄"],
["Mackogneur", ["macogneur", "makogneur"], "💪"],
["Chétiflor", ["chetiflore"], "🌱"],
["Boustiflor", ["boustiflore"]],
["Empiflor", ["empiflore"]],
["Tentacool", ["tentacoul", "tentacoule", "tantacoul", "tantacool"], "🐙"],
["Tentacruel", ["tantacruel", "tentacruelle"], "🐙"],
["Gravalanch", ["gravalanche"]],
["Ramoloss", ["ramolosse"]],
["Flagadoss", ["flagadosse"], "🐚"],
["Canarticho", ["canartichau", "canartichaud", "canartichaut"], "🦆"],
["Tadmorv", ["tasdmorv, tasdmorve, tadmorve -gros"], "😷"],
["Grotadmorv", ["grotadmorve", "gros tadmorve", "grostadmorv", "grostasdmorv", "grotasdmorv", "grostasdmorve", "grotasdmorve"], "😷"],
["Krabboss", ["kraboss", "craboss", "crabboss"], "🦀"],
["Nœunœuf", ["neuneuf", "neneuf", "noeuneuf", "nœuneuf"], "🥚"],
["Noadkoko", ["noidkoko", "noadcoco", "noidcoco"], "🌴"],
["Excelangue", ["exelangue", "excellangue", "exellangue"], "👅"],
["Rhinocorne", ["rhynocorne"], "🦏"],
["Rhinoféros", ["rhinoferoce", "rhinoferosse", "rhynoferos", "rhynoferoce", "rinoferos", "rinoferoce"], "🦏"],
["Leveinard", ["leveinar", "levenard -philippe"], "🏥"],
["Saquedeneu", ["sacdeneu"]],
["Hypotrempe", ["hipotrempe","hyppotrempe", "hippotrempe"]],
["Hypocéan", ["hipocean", "hyppocean", "hippocean"]],
["Poissirène", ["poissireine", "poisirène", "poisireine"], "🎣"],
["Poissoroy", ["poisoroy", "poissonroi", "poissonroy", "poisonroi"], "🐟"],
["Lippoutou", ["lipoutou", "lippouttou", "lipouttou"], "👄"],
["Élektek", ["electek -ru -delhi"], "🔋"],
["Magicarpe", ["magikarpe"], "🎣"],
["Léviator", ["leviathor"], "🐉"],
["Évoli", ["evolie", "evoly"]],
["Aquali", ["aqualy", "aqualie"], "💧"],
["Voltali", ["voltaly", "voltalie"]],
["Pyroli", ["piroli", "piroly", "pyrolie"], "🔥"],
["Lokhlass", ["locklass", "lockhlass", "lohklass"]],
["Artikodin", ["articodin"], "🐦"],
["Électhor", ["elekthor"], "🐥"],
["Mewtwo", ["mewtou","mewtow", "mewto"]],
["Héricendre", ["ericendre"], "🦔"],
["Typhlosion", ["tiphlosion", "tyflosion", "thyphlosion"], "🔥"],
["Kaiminus", ["caiminus"], "🐊"],
["Hoothoot", ["hootoot"], "🦉"],
["Noarfang", ["noirfang"], "🦉"],
["Mimigal", ["mimigale"], "🕷️"],
["Migalos", ["migalosse", "migaloss"], "🕷️"],
["Wattouat", ["wattouate", "watwatt"], "🐏"],
["Pharamp", ["pharampe"], "🌟"],
["Azumarill", ["azumaril"]],
["Simularbre", ["simulabre"], "🌲"],
["Tarpaud", ["tarpau"], "🐸"],
["Granivol", ["granivole"]],
["Floravol", ["floravole"]],
["Cotovol", ["cotovole"]],
["Tournegrin", ["tournegrain"], "🌱"],
["Héliatronc", ["heliatron", "eliatronc"], "🌻"],
["Axoloto", ["axolotto", "axolloto", "axollotto"]],
["Maraiste", ["maraistre"]],
["Mentali", ["mentalie", "mentaly"], "🌞"],
["Noctali", ["noctalie", "noctaly"], "🌝"],
["Cornèbre", ["cornerbre"]],
["Qulbutoké", ["qulbutoque"]],
["Pomdepik", ["pomdepic"]],
["Foretress", ["foretresse"]],
["Snubull", ["snubul"], "🐶"],
["Granbull", ["granbul"], "🐶"],
["Qwilfish", ["quilfish", "quillfish", "qwillfish"], "🐡"],
["Cizayox", ["cisayox", "cysayox"], "✂"],
["Scarhino", ["scarino", "scarhyno"]],
["Teddiursa", ["tediursa"], "🐻"],
["Volcaropod", ["volcaropode"], "🐌"],
["Corayon", ["coraillon"]],
["Rémoraid", ["remoraide"], "🐟"],
["Octillery", ["octillerie", "octilery"], "🐙"],
["Cadoizo", ["cadoiso", "cadoiseau", "cadoizeau"], "🎅🎁"],
["Hyporoi", ["hipporoi", "hypporoi", "hiporoi"]],
["Phanpy", ["phanpi", "phampi", "phampy"], "🐘"],
["Donphan", ["domphan", "donfant", "domphant"], "🐘"],
["Queulorior", ["quelorior"], "🎨"],
["Débugant", ["debugan"], "🥋"],
["Lippouti", ["lipouti", "lippoutti", "lipoutti"], "⛄"],
["Écrémeuh", ["ecremeu"], "🐄"],
["Leuphorie", ["leuphory", "leuforie", "lephorie"]],
["Suicune", ["siucune"]],
["Embrylex", ["embrilex", "ambrylex", "ambrilex"]],
["Ymphect", ["imphect", "ymfect", "ymphecte"]],
["Tyranocif", ["tiranocif","tyranossif"], "🦖"],
["Poussifeu", ["pousifeu"], "🐔"],
["Galifeu", ["gallifeu"], "🐔"],
["Braségali", ["brasegalli"], "🍗"],
["Gobou", ["gobbou"], "🐸"],
["Laggron", ["lagron -yves"]],
["Medhyèna", ["medyena", "medhiena", "mehdiena", "mehdiena", "mediena"]],
["Grahyéna", ["grayena", "grahiena", "grayhena"]],
["Zigzaton", ["zigzatton"]],
["Chenipotte", ["chenipote"], "🐛"],
["Armulys", ["armulisse", "armulis", "armulysse"]],
["Charmillon", ["charmilon", "charmillion", "charmilion"], "🦋"],
["Papinox", ["papynox"], "🦋"],
["Nénupiot", ["nenupio", "nenupiaut"]],
["Ludicolo", ["ludicollo"], "🍍"],
["Grainipiot", ["grainipio", "granipiot"], "🌰"],
["Pifeuil", ["pifeuille", "piffeuil", "pifueil"], "👹"],
["Tengalice", ["tengalis", "tangalice", "tangalis"], "👺"],
["Hélédelle", ["eledelle", "heledel"], "🐦"],
["Gardevoir", ["gardevoire"], "😏"],
["Maskadra", ["mascadra"]],
["Parécool", ["parecoul", "parecoule"], "😴"],
["Ningale", ["ningal"]],
["Chuchmur", ["chuchmure"], "🔈"],
["Brouhabam", ["brouabam", "brouhabame", "brouabame"], "📢"],
["Makuhita", ["makuita"], "👊"],
["Azurill", ["azuril"]],
["Delcatty", ["delcaty"], "🐈"],
["Mysdibule", ["mysdibulle", "misdibule", "misdibulle"]],
["Méditikka", ["meditika", "medittika", "medditika", "medditikka", "meddittika"], "🧘"],
["Dynavolt", ["dinavolt", "dynavolte"]],
["Carvanha", ["carvanna", "carvana", "carvahna"], "🐟"],
["Sharpedo", ["charpedo"], "🐟"],
["Camérupt", ["camerupte"], "🌋"],
["Chartor", ["chartror"], "🐢"],
["Kraknoix", ["kracnoix", "cracnoix", "craknoix"]],
["Vibraninf", ["vibranif"]],
["Cacturne", ["cacturn"], "🌵"],
["Mangriff", ["mangrif"], "😺"],
["Colhomard", ["colomard", "cohlomard", "colhommard"]],
["Anorith", ["anorithe"]],
["Milobellus", ["millobelus", "millobellus", "milobelus"], "🎀"],
["Kecleon", ["keckleon"]],
["Polichombr", ["polichombre"], "👻"],
["Coquiperl", ["coquiperle"], "🐚"],
["Drackhaus", ["drackaus", "drakhaus", "drahkaus"]],
["Drattak", ["dratak"], "🐲"],
["Terhal", ["tehral"]],
["Regirock", ["regiroc"]],
["Registeel", ["registyle"]],
["Kyogre", ["kiogre", "kryogre", "kiogr", "kyogr"]],
["Rayquaza", ["raykaza", "rayquasa"], "🐉"],
["Deoxys", ["deoxis -rapper"], "👽"],
["Tortipouss", ["tortipousse"], "🐢"],
["Torterra", ["tortera"], "🐢"],
["Ouisticram", ["ouisticrame"], "🐒"],
["Chimpenfeu", ["chimpanfeu"], "🐒"],
["Simiabraz", ["simiabrase"], "🐒"],
["Tiplouf", ["tiplouff"], "🐧"],
["Keunotor", ["queunotor", "kenotor", "quenotor"]],
["Luxray", ["luxrai"]],
["Kranidos", ["cranidos -the -a"]],
["Cheniti", ["chenitti"]],
["Mustéflott", ["musteflot", "musteflotte"]],
["Cériflor", ["ceriflore"], "🌸"],
["Sancoki", ["sankoki", "sancocki", "sankocki"], "🐌"],
["Tritosor", ["tritosaure", "tritosore"], "🐌"],
["Lockpin", ["locpin", "lokpin"], "🐰"],
["Moufflair", ["mouflair"], "😷"],
["Carchacrok", ["carchacroc", "carchacroque"], "🦈"],
["Lucario", ["lukario"]],
["Hippopotas", ["hipopotas", "hipoppotas"]],
["Hippodocus", ["hipodocus"]],
["Drascore", ["drascor"], "🦂"],
["Cradopaud", ["cradopeau", "cradopau",], "🐸"],
["Blizzaroi", ["blizaroi", "blizarroi"], "⛄"],
["Rhinastoc", ["rinastoc"], "🦏"],
["Bouldeneu", ["bouledeneu"], "🍜"],
["Élékable", ["elecable", "eleckable"], "🔌"],
["Phyllali", ["phylali", "phylalli", "phyllaly", "phillali", "philali", "philaly"], "🍃"],
["Givrali", ["givralli"], "❄️"],
["Scorvol", ["scorvole"], "🦂"],
["Mammochon", ["mamochon"], "🐘"],
["Gallame", ["gallam", "galame -parc"]],
["Noctunoir", ["noctunoire"], "🌀"],
["Momartik", ["momartique", "momartic", "momartick"], "☃️"],
["Créhelf", ["crehelfe"]],
["Créfollet", ["crefolet"]],
["Heatran", ["hetran"]],
["Cresselia", ["creselia", "cresellia"], "🌕"],
["Manaphy", ["manaphi", "manaphie"]],
["Darkrai", ["darkai"], "🌑"],
["Shaymin", ["shaimin", "shaymine"], "🌿"],
["Vipélierre", ["vipeliere", "vipelliere"], "🐍"],
["Majaspic", ["majaspique"], "🐍"],
["Guikui", ["gruicui"], "🐽"],
["Roitiflam", ["roitiflamme", "roitiflame"], "🐗"],
["Ratentif", ["rattentif"], "🐀"],
["Chacripan", ["chacripant"], "😼"],
["Feuiloutan", ["feuilloutan"]],
["Mushana", ["mushanna"], "🍅"],
["Nodulithe", ["nodulite"]],
["Chovsourir", ["chovsourire", "chauvsourire"], "😃"],
["Nanméouïe", ["nanmeoui"]],
["Judokrak", ["judocrak"], "🥋"],
["Manternel", ["manternelle"]],
["Chlorobule", ["clorobule", "chlorobulle"]],
["Fragilady", ["fragillady"]],
["Darumarond", ["darumaron"], "🔴"],
["Baggiguane", ["bagiguane", "baggyguane"]],
["Baggaïd", ["bagaide", "baggaide", "bagaid"]],
["Tutankafer", ["toutankafer"], "👻"],
["Aéroptéryx", ["aeropterix"]],
["Pashmilla", ["pachmilla"]],
["Scrutella", ["scrutela"]],
["Lakmécygne", ["lacmecygne", "lakmecigne"]],
["Sorboul", ["sorboule"], "🍨"],
["Sorbouboul", ["sorbouboule"], "🍨"],
["Haydaim", ["haidaim"], "🦌"],
["Mamanbo", ["mamambo"]],
["Mygavolt", ["migavolt"], "🕸️"],
["Grindur", ["graindur"], "🍈"],
["Polarhume", ["polarume", "polarhum"], "🐻"],
["Polagriffe", ["polagriff"], "🐻"],
["Drakkarmin", ["drakarmin", "dracarmin"], "🐲"],
["Gueriaigle", ["guerriaigle"], "🦅"],
["Vaututrice", ["votutrice"]],
["Aflamanoir", ["afflamanoir"]],
["Trioxhydre", ["trioxydre", "tryoxydre", "tryoxhydre"], "🐲"],
["Pyronille", ["pironille"], "🐛"],
["Terrakium", ["terakium", "terakkium"]],
["Meloetta", ["meloeta", "meleotta"], "💃"],
["Marisson", ["marrisson", "marison"], "🌰"],
["Boguérisse", ["bogerisse"], "🌰"],
["Feunnec", ["feunec"]],
["Goupelin", ["goupellin"], "🐱"],
["Croâporal", ["craporal"], "🐸"],
["Amphinobi", ["amphynobi", "amphinoby"], "🐸"],
["Braisillon", ["braisilion", "braisillion", "brasillon"], "🐤"],
["Flambusard", ["flambusar", "flambuzard"]],
["Prismillon", ["prismillion", "prismilion"], "🦋"],
["Pandarbare", ["panbarbare", "pandarbar"], "🐼"],
["Couafarel", ["couaffarel", "couafarelle"], "🐩"],
["Ptyranidur", ["ptiranidur", "ptiranydur"], "🦖"],
["Rexillius", ["rexilius", "rexillus"], "🦖"],
["Nymphali", ["nymphalli"], "🎀"],
["Banshitrouye", ["banshitrouille"], "🎃"],
["Bruyverne", ["bruiverne"], "🔊"],
["Xerneas", ["xernaes"], "🦌"],
["Yveltal", ["yvetal", "ylvetal"]],
["Zygarde", ["zigarde", "zygard"]],
["Brindibou", ["brindhibou"], "🐥"],
["Efflèche", ["efleche"], "🦉"],
["Flamiaou", ["flamaiou"], "😸"],
["Manglouton", ["mangloutton"]],
["Picassaut", ["picassault"], "🐦"],
["Lunala", ["lunalla"], "🌚"],
["Solgaleo", ["solgalleo"], "🌞"],
["Tokorico", ["tocorico", "tokoriko", "tocoriko"]],
["Larvibule", ["larvibulle"], "🐛"],
["Chrysapile", ["chrisapile", "crisapile", "crysapile", "chrisapille", "crisapille", "crysapille", "chrysapille"]],
["Lucanon", ["lucannon"]],
["Draïeul", ["drayeul"]],
["Denticrisse", ["denticrise"], "🐠"],
["Bombydou", ["bombidou", "bonbidou", "bonbydou"]],
["Rocabot", ["rocabo", "rocabeau"], "🐕"],
["Dodoala", ["dodoalla", "doddoala"], "🐨"],
["Tritox", ["tritoxe"], "🐊"],
["Sovkipou", ["sauvkipou", "sovkipu", "sauvkipu"]],
["Bourrinos", ["bourinos", "bourinnos", "bourrinnos", "bourinoss", "bourinnoss", "bourrinnoss", "bourrinoss", "bourinosse", "bourinnosse", "bourrinnosse", "bourrinosse"], "🐴"],
["Mimiqui", ["mimiki", "mimmiki", "mimmiqui"], "👻"],
["Chelours", ["chelourse"], "🐻"],
["Plumeline", ["plumelline", "plumelinne"], "🐦"],
["Météno", ["metenno"], "🌟"],
["Argouste", ["hargouste"], "👱"],
["Mimantis", ["mimantiss", "mimantisse"]],
["Floramantis", ["floramantiss", "floramantisse"]],
["Tiboudet", ["tibaudet"], "🐎"],
["Ossatueur", ["osatueur", "ossatuer", "ossateur"], "💀"],
["Cocombaffe", ["coconbaffe", "coconbafe", "cocombafe", "cocombaff"], "🍈"],
["Froussardine", ["frousardine"], "🐟"],
["Nounourson", ["nounoursson"], "🐻"],
["Trépassable", ["trepasable"], "🌅"],
["Bacabouh", ["bacabout", "bacabou", "bacaboue"], "🌅"],
["Crabagarre", ["crabbagarre", "crabagare", "crabbagare"], "🦀"],
["Boumata", ["boumatta"]]
]

(cur,conn) = bdd.ouvrirConnexion()
try:
    for row in corrections:
        emoji = ""
        if len(row) > 2:
            emoji = row[2]
        bdd.executerReq(cur, "UPDATE corrections SET emoji = '%s' WHERE correct = '%s';" % (emoji, row[0]))
    bdd.validerModifs(conn)
except Exception:
    raise
finally:
    bdd.fermerConnexion(cur, conn)