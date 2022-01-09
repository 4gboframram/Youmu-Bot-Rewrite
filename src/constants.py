from collections import namedtuple
from dataclasses import dataclass


@dataclass(init=False, frozen=True)
class Constants:
    ping_messages = [
        'There\'s nothing my Roukanken can\'t cut!',
        "Everyone talks about my sword Roukanken, but not my other sword Hakurouken. *Sad Hakurouken noises* ",
        "Everyone always says \"Youmu best girl\", but not \"How is best girl?\" :(",
        "Me or Reimu? That's like asking \"Would you rather a brown-haired broke girl or a sweet wife?\"",
        'Dammit Yuyuko-sama. The fridge is empty again. You need to stop eating so much!',
        'If it taste bad I can always shove this up your ass~',
        'I cut the heavens. I cut reason. I even cut time itself.',
        'The things that cannot be cut by my Roukanken, forged by youkai, are close to none!',
        "Well I don't know how it look but for some reason I want a sperm emoji... like this I can say \"Hey look... it's Myon!\"",
        "Error 404: Ping message not found.",
        "I am half-human, half-sperm. I mean ghost!",
        "Watermelon"
    ]

    presences = [
        'Gardening at the Hakugyokurou',
        "Cooking Yuyuko-sama's dinner",
        "Filling up the fridge for Yuyuko-sama",
        "Myon uwu",
        "Eating watermelon with Yuyuko-sama",
        "Myon?",
        "Being best girl",
        "Needing some sleep",
        "Wanting headpats"
    ]
    test_guild_id = [855529286953467945, 853924716178571294, 870200621947559956, 779441131150245908]


Character = namedtuple('Character', ['name', 'description', 'tag', 'use_score'])


class CommandList:
    character_list = [Character(*i) for i in (
        ("reimu", "A broke shrine maiden that can turn you into fumo",
         'hakurei_reimu', True),
        ("marisa", "An ordinary magician that does shrooms, ze~", "kirisame_marisa", True),
        ("youmu", "A half human, half sperm, that can cut anything with her two swords. I mean half ghost!",
         "konpaku_youmu", False),
        ("yuyuko", "A cute spooky ghost that some people call \"fat fuck\" because she eats a lot",
         "saigyouji_yuyuko", False),
        ("sakuya", "The maid of the Scarlet Devil Mansion that most certainly pads her chest",
         "izayoi_sakuya+-id:5237460+", True),
        ("flandre", "A cute, yet deadly loli with an overplayed theme that can destroy anything",
         "flandre_scarlet", False),
        ("remilia", "A cute loli that can manipulate fate itself, but still loses in a fight against a broke girl",
         "remilia_scarlet", False),
        ("patchouli", "A smart bookworm that writes magic books, but has asthma so she can't recite her own spells",
         "patchouli_knowledge", False),
        ("cirno", "A cool baka that has 9 as her lucky number",
         "cirno", False),
        ('tenshi', "Peaches", 'hinanawi_tenshi', True),
        ('meiling',
         "Chinese girl obsessed with sleeping instead of working her job as guard of the Scarlet Devil Mansion.",
         'hong_meiling', True),
        ('rumia', "T-pose and lightspeed dance", 'rumia', False),
        ('rinnosuke', "A half human, half youkai that can tell you the difference between a rubber glove and a condom.",
         'morichika_rinnosuke', False),
        ('murasa', "A spirit that can somehow lead a ship", 'murasa_minamitsu', False),
        ('mamizou', "A youkai tanuki that turn into you, but actually hot.", 'futatsuiwa_mamizou', False),
        ('shou', "A disciple of the god Bishamonten", 'toramaru_shou', False),
        ('nemuno', "A yamanba who lives in secluded areas of Youkai Mountain.", 'sakata_nemuno', False),
        ('eternity', "Butterfly?", 'eternity_larva', False),
        ('narumi', "(Touhou 16) (add description)", 'yatadera_narumi', False),
        ('daiyousei', "Baka's greatest friend", 'daiyousei', False),
        ('ringo', "Feed her more dangos", 'ringo_(touhou)', False),
        ('kosuzu', "Main character of Forbidden Scrollery, but who tf reads comics", 'motoori_kosuzu', False),
        ('akyuu', "She'll remember everything you tell her, including after death~", 'hieda_no_akyuu', False),
        ('hatate', "Kakashi Spirit News", 'himekaidou_hatate', False),
        ('mima', "Error 404: Character not found", 'mima_(touhou)', False),
        ('sariel', "Angel of Death", 'sariel_(touhou)', False),
        ('yumemi', "A human that wants to kidnap you and use you for \"research\"", 'okazaki_yumemi', False),
        ('shinki', "Demon world, anyone?", 'shinki', False),
        ('lily', "Spring fairy that fills up with \"spring\" and moans in Touhou LostWord", 'lily_white', False),
        ('shion', "The goddess of gacha players", 'yorigami_shion', False),
        ('seiran', "placeholder description", 'seiran_(touhou)', False),
        ('koakuma', "Funny little devil that works for Patchouli", 'koakuma', False),
        ('raiko', "placeholder description", 'horikawa_raiko', False),
        ('okina', "placeholder description", 'matara_okina', False),
        ('mai', "placeholder description", 'teireida_mai', False),
        ('satono', "placeholder description", 'nishida_satono', False),
        ('aunn', "placeholder description", 'komano_aun', False),
        ('komachi', "placeholder description", 'onozuka_komachi', False),
        ('wakasagihime', "placeholder description", 'wakasagihime', False),
        ('toyohime', "placeholder description", 'watatsuki_no_toyohime', False),
        ('yorihime', "placeholder description", 'watatsuki_no_yorihime', False),
        ('renko', "placeholder description", 'usami_renko', False),
        ('maribel', "placeholder description", 'maribel_hearn', False),
        ('nue', "placeholder description", 'houjuu_nue', False),
        ('iku', "placeholder description", 'nagae_iku', False),
        ('elly', "placeholder description", 'elly_(touhou)', False),
        ('kasen', "placeholder description", 'ibaraki_kasen', False),
        ('keine', "placeholder description", 'kamishirasawa_keine', False),
        ('konngara', "placeholder description", 'konngara', False),
        ('aya', "A friendly tengu that is reeaaaaallly fast", 'shameimaru_aya', True),
        ('nitori', "placeholder description", 'kawashiro_nitori', False),
        ('sumireko', "placeholder description", 'usami_sumireko', False),
        ('okuu', "placeholder description", 'reiuji_utsuho', False),
        ('koishi', "Shrimp fry?", 'komeiji_koishi', True),
        ('mokou', "Cute fire girl that can endure more pain than your dad can exert with his belt",
         'fujiwara_no_mokou+-jokanhiyou', True),
        ('satori', "A cute pink-haired girl that always knows what hentai you've been watching",
         'komeiji_satori', True),
        ('wan', "placeholder description", 'inubashiri_momiji', False),
        ('momiji', "placeholder description", 'inubashiri_momiji', False),
        ('ran', "Shikigami of the Gap Youkai that evolves from Vulpix with a Fire Stone", 'yakumo_ran', False),
        ('kagerou', "placeholder description", 'imaizumi_kagerou', False),
        ('reisen', "placeholder description", 'reisen_udongein_inaba', True),
        ('reisen2', "placeholder description", 'reisen', False),
        ('rei', "placeholder description", 'reisen', False),
        ('letty', "placeholder description", 'letty_whiterock', False),
        ('suwako', "placeholder description", 'moriya_suwako', False),
        ('shizuha', "placeholder description", 'aki_shizuha', False),
        ('sanae', "Most of the time called \"Green Reimu,\" she's a sister in law and a slut.", 'kochiya_sanae', False),
        ('clownpiece', "placeholder description", 'clownpiece', False),
        ('yukari', "A youkai that can manipulate gaps and is often known as \"Gap Hag.\"", 'yakumo_yukari', False),
        ('yuuka', "placeholder description", 'kazami_yuuka', False),
        ('suika', "An alcoholic oni that could beat your dad in a drinking contest.", 'ibuki_suika', False),
        ('sekibanki', "placeholder description", 'sekibanki', False),
        ('wriggle', "placeholder description", 'wriggle_nightbug', False),
        ('hina', "placeholder description", 'kagiyama_hina', False),
        ('alice', "placeholder description", 'alice_margatroid', False),
        ('kyouko', "placeholder description", 'kasodani_kyouko', False),
        ('kisume', "placeholder description", 'kisume', False),
        ('nazrin', "placeholder description", 'nazrin', False),
        ('sukuna', "placeholder description", 'sukuna_shinmyoumaru', False),
        ('kokoro', "placeholder description", 'hata_no_kokoro', False),
        ('yoshika', "placeholder description", 'miyako_yoshika', False),
        ('seiga', "placeholder description", 'kaku_seiga', False),
        ('kogasa', "placeholder description", 'tatara_kogasa', False),
        ('futo', "placeholder description", 'mononobe_no_futo', False),
        ('miko', "placeholder description", 'toyosatomimi_no_miko', False),
        ('tojiko', "placeholder description", 'soga_no_tojiko', False),
        ('mystia', "placeholder description", 'mystia_lorelei', False),
        ('genjii', "placeholder description", 'genjii_(touhou)', False),
        ('byakuren', "placeholder description", 'hijiri_byakuren', False),
        ('hecatia', "placeholder description", 'hecatia_lapislazuli', False),
        ('junko', "placeholder description", 'junko_(touhou)', False),
        ('sagume', "placeholder description", 'kishin_sagume', False),
        ('doremy', "placeholder description", 'doremy_sweet', False),
        ('minoriko', "placeholder description", 'aki_minoriko', False),
        ('yamame', "placeholder description", 'kurodani_yamame', False),
        ('yuugi', "placeholder description", 'hoshiguma_yuugi', False),
        ('parsee', "placeholder description", 'mizuhashi_parsee', False),
        ('tewi', "placeholder description", 'inaba_tewi', False),
        ('medicine', "placeholder description", 'medicine_melancholy', False),
        ('eiki', "Judges Hell. Honestly I have no idea what to say about her.", 'shiki_eiki', False),
        ('orin', "placeholder description", 'kaenbyou_rin', False),
        ('kaguya', "placeholder description", 'houraisan_kaguya+-jokanhiyou', True),
        ('eirin', "placeholder description", 'yagokoro_eirin', True),
        ('kanako', "placeholder description", 'yasaka_kanako', False),
        ('chen', "placeholder description", 'chen', False),
        ('star', "placeholder description", 'star_sapphire', False),
        ('luna', "placeholder description", 'luna_child', False),
        ('sunny', "\"Get Sunnymilked\" -The entire LostWord Discord server", 'sunny_milk', False),
        ('eika', "placeholder description", 'ebisu_eika', False),
        ('urumi', "placeholder description", 'ushizaki_urumi', False),
        ('kutaka', "placeholder description", 'niwatari_kutaka', False),
        ('lunasa', "The Violinist of the Prismriver sisters", 'lunasa_prismriver', False),
        ('lyrica', "The keyboardist of the Prismriver sisters", 'lyrica_prismriver', False),
        ('merlin', "Doot", 'merlin_prismriver', False),
        ('prismriver', "Merlin, Lunasa, and Lyrica :o", 'lunasa_prismriver+lyrica_prismriver+merlin_prismriver', False),
        ('keiki', "placeholder description", 'haniyasushin_keiki', False),
        ('saki', "placeholder description", 'kurokoma_saki', False),
        ('mayumi', "placeholder description", 'joutouguu_mayumi', False),
        ('yachie', "placeholder description", 'kicchou_yachie', False),
        ('ichirin', "placeholder description", 'kumoi_ichirin', False),
        ('miyoi', "placeholder description", 'okunoda_miyoi', False),
        ('chiyuri', "placeholder description", 'kitashirakawa_chiyuri', False),
        ('pc98', "placeholder description", 'touhou_(pc-98)', False),
        ('satsuki', "placeholder description", 'satsuki_rin', False),
        ('tokiko', "placeholder description", 'tokiko_(touhou)', False),
        ('mimiqwertyuiop', "placeholder description", 'mimi-chan', False),
        ('kotohime', "placeholder description", 'kotohime', False),
        ('rikako', "placeholder description", 'asakura_rikako', False),
        ('ruukoto', "placeholder description", 'ruukoto', False),
        ('elis', "placeholder description", 'elis_(touhou)', False),
        ('ellen', "placeholder description", 'ellen', False),
        ('orange', "placeholder description", 'orange_(touhou)', False),
        ('benben', "placeholder description", 'tsukumo_benben', False),
        ('yatsuhashi', "placeholder description", 'tsukumo_yatsuhashi', False),
        ('mike', "placeholder description", 'goutokuji_mike', False),
        ('takane', "placeholder description", 'yamashiro_takane', False),
        ('sannyo', "placeholder description", 'komakusa_sannyo', False),
        ('chimata', "placeholder description", 'tenkyuu_chimata', False),
        ('tsukasa', "placeholder description", 'kudamaki_tsukasa', False),
        ('momoyo', "placeholder description", 'himemushi_momoyo', False),
        ('misumaru', "placeholder description", 'tamatsukuri_misumaru', False),
        ('youka', "placeholder description", 'kazami_youka', False),
        ('kokuu', "placeholder description", 'kokuu_haruto', False),
        ('hei', "placeholder description", 'hei_meiling', False),
        ('kongou', "placeholder description", 'kongou_(kantai_collection)', False),
        ('haruna', "placeholder description", 'haruna_(kantai_collection)', False),
        ('hiei', "placeholder description", 'hiei_(kantai_collection)', False),
        ('kirishima', "placeholder description", 'kirishima_(kantai_collection)', False)
    )]
    alias_commands = (
        ('reimu', 'A broke shrine maiden that can turn you into fumo', 'hakurei_reimu', True),
        ('marisa', 'An ordinary magician that does shrooms, ze~', 'kirisame_marisa', True),
        ('youmu', 'A half human, half sperm, that can cut anything with her two swords. I mean half ghost!',
         'konpaku_youmu', False),
        ('yuyuko', 'A cute spooky ghost that some people call "fat fuck" because she eats a lot', 'saigyouji_yuyuko', False),
        ('sakuya', 'The maid of the Scarlet Devil Mansion that pads her chest', 'izayoi_sakuya+-id:5237460+', True),
        ('flandre', 'A cute, yet deadly loli with an overplayed theme that can destroy anything.', 'flandre_scarlet', False),
        ('remilia', 'A cute loli that can manipulate fate itself, but still loses in a fight against a broke girl',
         'remilia_scarlet', False),
        ('patchouli', "A smart bookworm that writes magic books, but has asthma so she can't recite her own spells",
         'patchouli_knowledge', False),
        ('cirno', 'A cool baka that has 9 as her lucky number', 'cirno', False),
        ('tenshi', 'Peaches?', 'hinanawi_tenshi', True),
        ('meiling','Chinese girl obsessed with sleeping instead of working her job.',
         'hong_meiling', True),
        ('rumia', 'T-pose and lightspeed justice', 'rumia', False),
        ('rinnosuke','A half human, half youkai that can tell you the difference between a rubber glove and a condom.',
         'morichika_rinnosuke', False),
        ('aya', 'A friendly tengu that is reeaaaaallly fast', 'shameimaru_aya', True),
        ('koishi', 'Shrimp fry?', 'komeiji_koishi', True),
        ('mokou', 'Cute fire girl that can endure more pain than your dad can exert with his belt',
         'fujiwara_no_mokou+-jokanhiyou', True),
        ('satori', "A cute pink-haired human that always knows what hentai you've been watching", 'komeiji_satori',
         True),
        ('sanae', 'Most of the time called "Green Reimu," she\'s a sister in law and a slut.', 'kochiya_sanae', False),
        ('yukari', 'A youkai that can manipulate gaps and is often known as "Gap Hag."', 'yakumo_yukari', False),
        ('suika', 'An alcoholic oni that could beat your dad in a drinking contest.', 'ibuki_suika', False),
        ('lunasa', "The Violinist of the Prismriver sisters", 'lunasa_prismriver', False),
        ('lyrica', "The keyboardist of the Prismriver sisters", 'lyrica_prismriver', False),
        ('merlin', "Doot", 'merlin_prismriver', False),
        ('prismriver', "Merlin, Lunasa, and Lyrica :o", 'lunasa_prismriver+lyrica_prismriver+merlin_prismriver', False),
        ('eiki', "Judges Hell. Honestly I have no idea what to say about her.", 'shiki_eiki', False),
        ('ran', "Shikigami of the Gap Youkai that evolves from Vulpix with a Fire Stone", 'yakumo_ran', False),
        ('daiyousei', "Baka's greatest friend", 'daiyousei', False),
        ('ringo', "Feed her more dangos!", 'ringo_(touhou)', False),
        ('akyuu', "She'll remember everything you tell her, including after death~", 'hieda_no_akyuu', False),
        ('yumemi', "A human that wants to kidnap you and use you for \"research\"", 'okazaki_yumemi', False),
        ('lily', "Spring fairy that fills up with \"spring\" and moans in Touhou LostWord", 'lily_white', False),
        ('koakuma', "Funny little devil that works for Patchouli", 'koakuma', False),

    )
