__BRYTHON__.VFS_timestamp = 1661722158613
if(typeof document !== 'undefined'){
    __BRYTHON__.brython_modules = $B.last(document.getElementsByTagName('script')).src
}
__BRYTHON__.use_VFS = true
var scripts = {"$timestamp": 1661722158612, "browser": [".py", "", [], 1], "_webworker": [".js", "// Web Worker implementation\n\nvar $module = (function($B){\n\nvar _b_ = $B.builtins\n\nvar VFS = $B.brython_modules ? 'brython_modules' : 'brython_stdlib'\n\nif($B.debug > 2){\n    var brython_scripts = [\n        'brython_builtins',\n        'version_info',\n        'python_tokenizer',\n        'py_ast',\n        'py2js',\n        'loaders',\n        'py_object',\n        'py_type',\n        'py_utils',\n        'py_sort',\n        'py_builtin_functions',\n        'py_exceptions',\n        'py_range_slice',\n        'py_bytes',\n        'py_set',\n        'js_objects',\n        'stdlib_paths',\n        'py_import',\n        'unicode_data',\n        'py_string',\n        'py_int',\n        'py_long_int',\n        'py_float',\n        'py_complex',\n        'py_dict',\n        'py_list',\n        'py_generator',\n        'py_dom',\n        'py_pattern_matching',\n        'builtin_modules',\n        'async',\n        'ast_to_js',\n        'symtable',\n        VFS]\n\n}else{\n    var brython_scripts = ['brython', VFS]\n}\nvar wclass = $B.make_class(\"Worker\",\n    function(worker){\n        var res = worker\n        res.send = res.postMessage\n        return res\n    }\n)\nwclass.__mro__ = [$B.JSObj, _b_.object]\n\n$B.set_func_names(wclass, \"browser.worker\")\n\nvar _Worker = $B.make_class(\"Worker\", function(id, onmessage, onerror){\n    var $ = $B.args(\"__init__\", 3, {id: null, onmessage: null, onerror: null},\n            ['id', 'onmessage', 'onerror'], arguments,\n            {onmessage: _b_.None, onerror: _b_.None}, null, null),\n        id = $.id,\n        src = $B.webworkers[id]\n\n        if(src === undefined){\n            throw _b_.KeyError.$factory(id)\n        }\n        var script_id = \"worker\" + $B.UUID(),\n            filename = $B.script_dir + \"#\" + id\n        $B.url2name[filename] = script_id\n\n        var js = $B.py2js({src, filename},\n                script_id).to_js(),\n            header = 'var $locals_' + script_id +' = {}\\n';\n        brython_scripts.forEach(function(script){\n            if(script != VFS || VFS == \"brython_stlib\"){\n                var url = $B.brython_path + script + \".js\"\n            }else{\n                // attribute $B.brython_modules is set to the path of\n                // brython_modules.js by the script itself\n                var url = $B.brython_modules\n            }\n            if(! $B.$options.cache){ // cf. issue 1954\n                url += '?' + (new Date()).getTime()\n            }\n            header += 'importScripts(\"' + url + '\")\\n'\n        })\n        // restore brython_path\n        header += '__BRYTHON__.brython_path = \"' + $B.brython_path +\n            '\"\\n'\n        // restore path for imports (cf. issue #1305)\n        header += '__BRYTHON__.path = \"' + $B.path +'\".split(\",\")\\n'\n        // Call brython() to initialize internal Brython values\n        header += `brython($B.debug)\\n`\n        js = header + js\n        js = `try{${js}}catch(err){$B.handle_error(err)}`\n        var blob = new Blob([js], {type: \"application/js\"}),\n            url = URL.createObjectURL(blob),\n            w = new Worker(url),\n            res = wclass.$factory(w)\n        return res\n})\n\nreturn {\n    Worker: _Worker\n}\n\n})(__BRYTHON__)\n"], "ngram_generated": [".py", "subnames = {\n\t\"tricorne\": ['sinner tricorne'],\n\t\"silk gloves\": ['fingerless silk gloves'],\n}\n\nngrams = {\n\t\"abyssal axe\": {\"sal a\"},\n\t\"agate amulet\": {\"agat\", \"amu\", \"e am\", \"gat\", \"te a\", \"ule\"},\n\t\"amber amulet\": {\"ambe\", \"amu\", \"ule\"},\n\t\"ambusher\": {\"sher\", \"ushe\"},\n\t\"amethyst ring\": {\"t ri\", \"t rin\", \"thy\", \"yst\"},\n\t\"ancient spirit shield\": {\"nt spi\"},\n\t\"antique greaves\": {\"e gr\"},\n\t\"antique rapier\": {\"ue r\", \"ue ra\"},\n\t\"apothecary's gloves\": {\"ary\", \"hec\", \"pot\", \"y'\"},\n\t\"arcanist gloves\": {\"ani\", \"arc\", \"rca\", \"st g\", \"st gl\", \"t gl\"},\n\t\"arcanist slippers\": {\"ani\", \"arc\", \"ist s\", \"rca\", \"t sl\"},\n\t\"archon kite shield\": {\"arc\", \"hon\", \"on k\"},\n\t\"assassin bow\": {\"sin b\"},\n\t\"assassin's garb\": {\"n's g\"},\n\t\"assassin's mitts\": {\"'s m\"},\n\t\"astral plate\": {\"astr\"},\n\t\"auric mace\": {\"aur\"},\n\t\"aventail helmet\": {\"tai\", \"ven\"},\n\t\"awl\": {\"wl\"},\n\t\"barbute helmet\": {\"rbu\", \"te h\"},\n\t\"baroque round shield\": {\"oq\", \"ue r\"},\n\t\"basket rapier\": {\"aske\"},\n\t\"bastard sword\": {\"asta\"},\n\t\"blazing arrow quiver\": {\"az\", \"g ar\", \"zi\"},\n\t\"blue pearl amulet\": {\"amu\", \"blu\", \"ear\", \"l am\", \"ule\"},\n\t\"blunt arrow quiver\": {\"blu\", \"blun\", \"lun\", \"nt a\"},\n\t\"bone armour\": {\"ne ar\"},\n\t\"bone circlet\": {\"cir\", \"cle\", \"e ci\", \"one c\"},\n\t\"bone helmet\": {\"bone h\"},\n\t\"boot blade\": {\"oot b\", \"t bl\"},\n\t\"boot knife\": {\"t k\"},\n\t\"branded kite shield\": {\"bra\", \"bran\", \"rand\"},\n\t\"brass maul\": {\"bra\", \"bras\", \"ss m\"},\n\t\"brass spirit shield\": {\"bra\", \"bras\", \"s sp\"},\n\t\"bronze gauntlets\": {\"ze g\"},\n\t\"bronze sceptre\": {\"ze s\"},\n\t\"bronzescale boots\": {\"escale b\", \"zes\"},\n\t\"bronzescale gauntlets\": {\"escale g\", \"zes\"},\n\t\"buckskin tunic\": {\"ckskin tu\", \"kskin tu\"},\n\t\"callous mask\": {\"lou\"},\n\t\"cardinal round shield\": {\"card\", \"ina\"},\n\t\"carnal armour\": {\"arn\", \"arna\", \"l ar\", \"l arm\", \"nal a\", \"rnal\"},\n\t\"carnal boots\": {\"al bo\", \"al boo\", \"arn\", \"arna\", \"nal b\", \"rnal\"},\n\t\"carnal mitts\": {\"al mi\", \"arn\", \"arna\", \"rnal\"},\n\t\"carnal sceptre\": {\"arn\", \"arna\", \"nal s\", \"nal sc\", \"rnal\"},\n\t\"carved wand\": {\"arve\", \"d w\", \"ed w\", \"ved w\"},\n\t\"cedar tower shield\": {\"eda\"},\n\t\"cerulean ring\": {\"eru\", \"n ri\", \"ule\"},\n\t\"chain belt\": {\"bel\", \"elt\", \"n be\"},\n\t\"chain gloves\": {\"ain g\"},\n\t\"champion kite shield\": {\"amp\", \"on k\"},\n\t\"chiming spirit shield\": {\"chi\", \"ng sp\"},\n\t\"citrine amulet\": {\"amu\", \"e am\", \"itr\", \"ule\"},\n\t\"clasped boots\": {\"clas\", \"sped b\"},\n\t\"clasped mitts\": {\"clas\", \"d mi\", \"sped m\"},\n\t\"cleaver\": {\"cle\", \"clea\"},\n\t\"close helmet\": {\"clo\", \"ose\"},\n\t\"cloth belt\": {\"bel\", \"clo\", \"clot\", \"elt\"},\n\t\"cobalt jewel\": {\"cob\", \"ewe\"},\n\t\"colossal tower shield\": {\"l to\"},\n\t\"compound spiked shield\": {\"nd sp\"},\n\t\"conjurer boots\": {\"rer b\", \"urer b\"},\n\t\"conjurer gloves\": {\"urer g\"},\n\t\"conquest chainmail\": {\"nq\"},\n\t\"convoking wand\": {\"nv\"},\n\t\"copper plate\": {\"er p\", \"per p\"},\n\t\"coral amulet\": {\"al am\", \"amu\", \"l am\", \"oral\", \"ule\"},\n\t\"coral ring\": {\"al ri\", \"oral\", \"ral r\"},\n\t\"corrugated buckler\": {\"gat\", \"rru\", \"ted bu\"},\n\t\"corsair sword\": {\"air\"},\n\t\"crimson jewel\": {\"ewe\", \"n j\", \"on j\"},\n\t\"crude bow\": {\"de bo\", \"rud\", \"ud\"},\n\t\"crusader chainmail\": {\"der c\", \"er c\", \"r c\", \"r ch\"},\n\t\"crusader gloves\": {\"der g\"},\n\t\"crusader plate\": {\"der p\", \"er p\"},\n\t\"crystal belt\": {\"bel\", \"crys\", \"elt\", \"l be\", \"yst\"},\n\t\"crystal sceptre\": {\"crys\", \"tal s\", \"yst\"},\n\t\"crystal wand\": {\"al w\", \"crys\", \"l w\", \"tal w\", \"yst\"},\n\t\"cutthroat's garb\": {\"hro\", \"oat'\", \"tth\"},\n\t\"death bow\": {\"deat\"},\n\t\"decimation bow\": {\"cim\", \"ima\", \"on b\"},\n\t\"decorative axe\": {\"ativ\"},\n\t\"deerskin boots\": {\"dee\", \"rskin b\"},\n\t\"deerskin gloves\": {\"dee\", \"rskin g\"},\n\t\"deicide mask\": {\"cid\", \"dei\"},\n\t\"demon dagger\": {\"dem\", \"n da\"},\n\t\"demon's horn\": {\"dem\", \"mon'\", \"on'\"},\n\t\"desert brigandine\": {\"des\", \"ert\", \"rt b\"},\n\t\"despot axe\": {\"des\", \"esp\", \"pot\"},\n\t\"destiny leather\": {\"des\", \"dest\", \"y l\"},\n\t\"destroyer regalia\": {\"des\", \"dest\", \"tro\"},\n\t\"diamond ring\": {\"amo\"},\n\t\"dragonscale boots\": {\"gonscale b\", \"nscale b\"},\n\t\"dragonscale gauntlets\": {\"gonscale g\", \"nscale g\"},\n\t\"dread maul\": {\"ad m\", \"dre\"},\n\t\"dream mace\": {\"dre\", \"eam\"},\n\t\"driftwood wand\": {\"d w\", \"od w\"},\n\t\"dusk blade\": {\"dus\"},\n\t\"ebony tower shield\": {\"bony\", \"eb\", \"ony\"},\n\t\"eelskin gloves\": {\"lskin g\"},\n\t\"elder sword\": {\"elde\"},\n\t\"elegant ringmail\": {\"nt r\", \"nt ri\", \"t ri\", \"t rin\"},\n\t\"elegant round shield\": {\"nt r\", \"nt ro\"},\n\t\"elegant sword\": {\"ant s\"},\n\t\"embroidered gloves\": {\"emb\", \"ider\", \"oid\", \"red g\"},\n\t\"engraved wand\": {\"aved w\", \"d w\", \"ed w\", \"ved w\"},\n\t\"estoc\": {\"toc\"},\n\t\"etched greatsword\": {\"hed g\"},\n\t\"eternal burgonet\": {\"ernal\", \"eter\", \"nal b\", \"nal bu\", \"rnal\"},\n\t\"eternal sword\": {\"ernal\", \"eter\", \"nal s\", \"nal sw\", \"rnal\", \"ternal s\"},\n\t\"exquisite leather\": {\"te l\"},\n\t\"ezomyte axe\": {\"te a\", \"te ax\"},\n\t\"ezomyte blade\": {\"yte b\", \"yte bl\"},\n\t\"ezomyte burgonet\": {\"e bur\", \"yte b\"},\n\t\"ezomyte dagger\": {\"te d\"},\n\t\"ezomyte staff\": {\"te st\"},\n\t\"feathered arrow quiver\": {\"ed arrow q\", \"fea\"},\n\t\"festival mask\": {\"fes\", \"l mas\"},\n\t\"fiend dagger\": {\"fien\"},\n\t\"fingerless silk gloves\": {\"erl\", \"inge\", \"k g\", \"lk g\", \"nger\"},\n\t\"fingerless silk gloves\u00a7silk gloves\": {\"erl\", \"inge\", \"nger\"},\n\t\"flaying knife\": {\"yi\"},\n\t\"fright claw\": {\"ht c\"},\n\t\"fugitive boots\": {\"fug\"},\n\t\"full dragonscale\": {\"l dr\"},\n\t\"full wyrmscale\": {\"l w\", \"l wy\"},\n\t\"gavel\": {\"gav\"},\n\t\"gilded sallet\": {\"ded sa\"},\n\t\"gladiator plate\": {\"or p\"},\n\t\"gladius\": {\"diu\"},\n\t\"glorious plate\": {\"s pl\"},\n\t\"gnarled branch\": {\"bra\", \"bran\", \"nch\"},\n\t\"goat's horn\": {\"goat'\", \"oat'\", \"t's h\"},\n\t\"goathide boots\": {\"de bo\", \"de boo\", \"thide bo\"},\n\t\"goathide gloves\": {\"thide g\"},\n\t\"gold amulet\": {\"amu\", \"d am\", \"ule\"},\n\t\"gold ring\": {\"ld ri\"},\n\t\"golden mask\": {\"den m\", \"en m\", \"n mas\"},\n\t\"golden plate\": {\"en p\"},\n\t\"goliath gauntlets\": {\"h ga\"},\n\t\"great crown\": {\"at c\", \"t cr\"},\n\t\"great helmet\": {\"at h\", \"t h\"},\n\t\"great mallet\": {\"at m\"},\n\t\"grinning fetish\": {\"eti\", \"gri\", \"grin\", \"nn\", \"nni\", \"tis\"},\n\t\"gripped gloves\": {\"gri\", \"grip\"},\n\t\"gut ripper\": {\"t ri\", \"ut r\"},\n\t\"harbinger bow\": {\"bi\", \"ger b\", \"inge\", \"nger\"},\n\t\"harlequin mask\": {\"leq\", \"n mas\"},\n\t\"harmonic spirit shield\": {\"c s\", \"c sp\"},\n\t\"headsman axe\": {\"ads\"},\n\t\"heavy arrow quiver\": {\"vy\", \"vy a\"},\n\t\"heavy belt\": {\"bel\", \"elt\", \"vy\", \"vy b\"},\n\t\"hellion's paw\": {\"hell\", \"lio\", \"llio\", \"on'\"},\n\t\"highborn staff\": {\"rn s\"},\n\t\"highland blade\": {\"hl\"},\n\t\"holy chainmail\": {\"oly\", \"y c\"},\n\t\"hubris circlet\": {\"cir\", \"cle\", \"hub\", \"s c\"},\n\t\"hydrascale gauntlets\": {\"ascale g\"},\n\t\"imbued wand\": {\"bue\", \"d w\", \"ed w\"},\n\t\"imperial bow\": {\"al bo\", \"al bow\", \"ial bo\"},\n\t\"imperial claw\": {\"ial c\", \"l cla\"},\n\t\"imperial maul\": {\"rial m\"},\n\t\"imperial skean\": {\"ial s\", \"ial sk\", \"l sk\", \"rial s\"},\n\t\"imperial staff\": {\"al sta\", \"ial s\", \"ial st\", \"rial s\", \"rial st\"},\n\t\"infernal axe\": {\"ernal\", \"fer\", \"nal a\", \"nal ax\", \"rnal\"},\n\t\"infernal sword\": {\"ernal\", \"fer\", \"fernal s\", \"nal s\", \"nal sw\", \"rnal\"},\n\t\"iolite ring\": {\"e ri\", \"iol\", \"te r\"},\n\t\"iron circlet\": {\"cir\", \"cle\", \"n ci\"},\n\t\"iron gauntlets\": {\"n gau\", \"on ga\"},\n\t\"iron hat\": {\"n hat\"},\n\t\"iron mask\": {\"n mas\", \"ron m\"},\n\t\"iron ring\": {\"n ri\", \"on ri\", \"ron r\"},\n\t\"iron staff\": {\"ron st\"},\n\t\"ironscale boots\": {\"nscale b\", \"rons\", \"ronscale b\"},\n\t\"ironscale gauntlets\": {\"nscale g\", \"rons\", \"ronscale g\"},\n\t\"jade amulet\": {\"amu\", \"de a\", \"e am\", \"ule\"},\n\t\"jade hatchet\": {\"de h\"},\n\t\"jagged foil\": {\"ged f\", \"jag\"},\n\t\"jagged maul\": {\"gged m\", \"jag\"},\n\t\"jasper chopper\": {\"er c\", \"per c\", \"r c\", \"r ch\"},\n\t\"jewelled foil\": {\"elle\", \"ewe\"},\n\t\"jingling spirit shield\": {\"ji\", \"ng sp\"},\n\t\"judgement staff\": {\"jud\", \"ud\"},\n\t\"karui chopper\": {\"i ch\"},\n\t\"karui maul\": {\"i m\"},\n\t\"karui sceptre\": {\"i s\"},\n\t\"lacewood spirit shield\": {\"cew\", \"ewo\", \"lac\"},\n\t\"lacquered buckler\": {\"cq\", \"lac\", \"uered b\"},\n\t\"lacquered garb\": {\"cq\", \"lac\", \"red g\", \"red ga\"},\n\t\"lacquered helmet\": {\"cq\", \"d helme\", \"lac\"},\n\t\"laminated kite shield\": {\"amin\", \"ina\"},\n\t\"lapis amulet\": {\"amu\", \"lap\", \"s a\", \"ule\"},\n\t\"lathi\": {\"lath\"},\n\t\"latticed ringmail\": {\"ice\"},\n\t\"leather belt\": {\"bel\", \"elt\", \"r be\"},\n\t\"leather cap\": {\"cap\", \"er c\", \"her c\", \"r c\"},\n\t\"leather hood\": {\"her h\"},\n\t\"legion boots\": {\"gion b\", \"on b\"},\n\t\"legion gloves\": {\"ion g\"},\n\t\"legion sword\": {\"gion s\", \"ion s\"},\n\t\"lion pelt\": {\"elt\", \"lio\", \"n pe\", \"pelt\"},\n\t\"lion sword\": {\"ion s\", \"lio\", \"lion s\"},\n\t\"long bow\": {\"g b\"},\n\t\"lunaris circlet\": {\"aris c\", \"cir\", \"cle\", \"lun\", \"s c\", \"una\"},\n\t\"maelstr\u00f6m staff\": {\"ae\", \"\u00f6\"},\n\t\"marble amulet\": {\"amu\", \"e am\", \"rbl\", \"ule\"},\n\t\"meatgrinder\": {\"gri\", \"grin\", \"tg\"},\n\t\"mesh boots\": {\"esh b\", \"mes\"},\n\t\"mesh gloves\": {\"mes\", \"sh g\"},\n\t\"midnight blade\": {\"dn\", \"ht bl\", \"t bl\"},\n\t\"military staff\": {\"ary\", \"ilit\", \"mil\"},\n\t\"mind cage\": {\"mind\"},\n\t\"mirrored spiked shield\": {\"irr\", \"ror\"},\n\t\"moonstone ring\": {\"e ri\", \"ne ri\", \"nst\"},\n\t\"mosaic kite shield\": {\"aic\"},\n\t\"murder mitts\": {\"der m\"},\n\t\"nailed fist\": {\"nai\"},\n\t\"necromancer circlet\": {\"cir\", \"cle\", \"ecr\", \"er c\", \"oma\", \"r c\", \"r ci\"},\n\t\"necromancer silks\": {\"ecr\", \"lks\", \"oma\"},\n\t\"nightmare bascinet\": {\"e ba\"},\n\t\"nubuck boots\": {\"ck b\", \"ck bo\", \"nub\"},\n\t\"nubuck gloves\": {\"ck g\", \"k g\", \"nub\"},\n\t\"occultist's vestment\": {\"cul\", \"tis\"},\n\t\"onyx amulet\": {\"amu\", \"ony\", \"ule\", \"yx\"},\n\t\"opal ring\": {\"al ri\", \"opa\", \"pal\", \"pal r\"},\n\t\"opal sceptre\": {\"opa\", \"pal\", \"pal s\"},\n\t\"opal wand\": {\"al w\", \"l w\", \"opa\", \"pal\", \"pal w\"},\n\t\"ornate mace\": {\"te m\"},\n\t\"ornate ringmail\": {\"ate r\", \"e ri\", \"te r\"},\n\t\"ornate sword\": {\"te sw\"},\n\t\"painted buckler\": {\"nted b\", \"ted bu\"},\n\t\"paua amulet\": {\"a a\", \"amu\", \"aua\", \"ule\"},\n\t\"paua ring\": {\"a ri\", \"aua\"},\n\t\"penetrating arrow quiver\": {\"g ar\", \"trati\"},\n\t\"pine buckler\": {\"ne bu\", \"pine\"},\n\t\"pinnacle tower shield\": {\"acl\", \"cle\", \"nn\"},\n\t\"plague mask\": {\"agu\"},\n\t\"plank kite shield\": {\"k k\"},\n\t\"plate vest\": {\"te v\"},\n\t\"plated greaves\": {\"d greav\", \"ted gr\"},\n\t\"platinum kris\": {\"inu\", \"m k\"},\n\t\"platinum sceptre\": {\"inu\", \"m sc\"},\n\t\"poleaxe\": {\"eax\", \"pol\"},\n\t\"polished spiked shield\": {\"lish\", \"pol\"},\n\t\"praetor crown\": {\"ae\", \"aet\", \"or c\", \"r c\"},\n\t\"primal arrow quiver\": {\"ima\", \"imal\", \"l ar\"},\n\t\"primordial staff\": {\"al sta\", \"ial s\", \"ial st\", \"imo\"},\n\t\"prophecy wand\": {\"ecy\", \"hec\", \"oph\"},\n\t\"prophet crown\": {\"et c\", \"oph\", \"t cr\"},\n\t\"quartz wand\": {\"z w\"},\n\t\"ranger bow\": {\"anger\", \"ger b\", \"nger\"},\n\t\"raven mask\": {\"en m\", \"n mas\", \"raven\", \"ven\"},\n\t\"rawhide boots\": {\"de bo\", \"de boo\", \"whide b\"},\n\t\"rawhide tower shield\": {\"de t\"},\n\t\"reaver sword\": {\"ver s\"},\n\t\"recurve bow\": {\"recu\"},\n\t\"regicide mask\": {\"cid\", \"gic\"},\n\t\"reinforced greaves\": {\"ced g\", \"d greav\"},\n\t\"reinforced tower shield\": {\"ced t\"},\n\t\"ritual sceptre\": {\"itu\"},\n\t\"riveted boots\": {\"eted b\"},\n\t\"rock breaker\": {\"bre\", \"ck b\", \"eak\", \"ker\"},\n\t\"rotted round shield\": {\"ott\"},\n\t\"royal axe\": {\"yal a\"},\n\t\"royal bow\": {\"al bo\", \"al bow\", \"yal bo\"},\n\t\"royal sceptre\": {\"yal s\", \"yal sc\"},\n\t\"royal skean\": {\"l sk\", \"yal s\", \"yal sk\"},\n\t\"royal staff\": {\"al sta\", \"yal s\", \"yal st\"},\n\t\"ruby ring\": {\"rub\"},\n\t\"rusted sword\": {\"ted sw\"},\n\t\"rustic sash\": {\"ash\", \"c s\"},\n\t\"sabre\": {\"bre\", \"sab\"},\n\t\"sadist garb\": {\"dis\", \"st g\"},\n\t\"sage wand\": {\"ge wa\", \"sag\"},\n\t\"sage's robe\": {\"e's r\", \"sag\"},\n\t\"saint's hauberk\": {\"int'\", \"sain\", \"t's h\"},\n\t\"saintly chainmail\": {\"sain\", \"tly\", \"y c\"},\n\t\"samite gloves\": {\"te g\"},\n\t\"samnite helmet\": {\"mn\", \"te h\"},\n\t\"sapphire ring\": {\"e ri\", \"hir\"},\n\t\"satin gloves\": {\"tin g\"},\n\t\"scholar boots\": {\"ar bo\", \"sch\"},\n\t\"scholar's robe\": {\"ar'\", \"sch\"},\n\t\"seaglass amulet\": {\"amu\", \"s a\", \"sea\", \"ule\"},\n\t\"secutor helm\": {\"uto\"},\n\t\"sentinel jacket\": {\"enti\", \"l j\"},\n\t\"serpentine staff\": {\"enti\", \"ine s\"},\n\t\"serpentscale gauntlets\": {\"tscale g\"},\n\t\"serrated arrow quiver\": {\"ed arrow q\", \"ted a\"},\n\t\"shadow axe\": {\"ado\", \"dow\", \"had\", \"w ax\"},\n\t\"shadow sceptre\": {\"ado\", \"dow\", \"had\", \"w sc\"},\n\t\"shagreen boots\": {\"een b\"},\n\t\"shagreen gloves\": {\"een g\"},\n\t\"sharkskin boots\": {\"kskin b\"},\n\t\"sharkskin tunic\": {\"kskin tu\", \"rkskin t\"},\n\t\"sharktooth arrow quiver\": {\"h ar\"},\n\t\"short bow\": {\"hort\", \"rt b\"},\n\t\"siege axe\": {\"ege a\"},\n\t\"silk gloves\": {\"k g\", \"lk g\"},\n\t\"silk slippers\": {\"k sl\"},\n\t\"silken hood\": {\"en h\"},\n\t\"silken vest\": {\"n v\"},\n\t\"simple robe\": {\"sim\"},\n\t\"sinner tricorne\": {\"nn\", \"nne\"},\n\t\"sinner tricorne\u00a7tricorne\": {\"nn\", \"nne\"},\n\t\"skinning knife\": {\"kinn\", \"nn\", \"nni\"},\n\t\"slaughter knife\": {\"aug\"},\n\t\"sledgehammer\": {\"edg\"},\n\t\"slink gloves\": {\"k g\", \"nk g\"},\n\t\"solaris circlet\": {\"aris c\", \"cir\", \"cle\", \"lari\", \"s c\"},\n\t\"soldier boots\": {\"ier b\"},\n\t\"soldier gloves\": {\"ier g\"},\n\t\"soldier helmet\": {\"ier h\"},\n\t\"sorcerer boots\": {\"erer b\", \"rer b\"},\n\t\"spidersilk robe\": {\"ider\", \"pid\", \"rsi\"},\n\t\"spike-point arrow quiver\": {\"-p\", \"e-\", \"nt a\"},\n\t\"spiked club\": {\"ked c\"},\n\t\"spiked gloves\": {\"ked g\"},\n\t\"spine bow\": {\"pine\", \"spine\"},\n\t\"spiraled wand\": {\"d w\", \"ed w\", \"led w\"},\n\t\"stealth boots\": {\"lth b\"},\n\t\"steel circlet\": {\"cir\", \"cle\", \"el c\", \"l ci\"},\n\t\"steel gauntlets\": {\"el ga\", \"l ga\"},\n\t\"steel kite shield\": {\"el k\"},\n\t\"steel ring\": {\"el r\"},\n\t\"steelhead\": {\"lh\"},\n\t\"steelscale gauntlets\": {\"lscale g\"},\n\t\"stiletto\": {\"ett\"},\n\t\"strapped boots\": {\"trapped b\"},\n\t\"strapped mitts\": {\"d mi\", \"pped m\", \"trapped m\"},\n\t\"studded belt\": {\"bel\", \"d be\", \"ed be\", \"elt\", \"tud\", \"ud\"},\n\t\"studded round shield\": {\"ded r\", \"tud\", \"ud\"},\n\t\"sun leather\": {\"n l\"},\n\t\"supreme spiked shield\": {\"up\"},\n\t\"tarnished spirit shield\": {\"arn\", \"arni\", \"tarn\"},\n\t\"teak round shield\": {\"ak r\", \"eak\"},\n\t\"terror claw\": {\"erro\", \"or c\", \"or cl\", \"r c\", \"r cl\", \"ror\"},\n\t\"terror maul\": {\"erro\", \"or m\", \"ror\"},\n\t\"thresher claw\": {\"er c\", \"eshe\", \"her c\", \"r c\", \"r cl\", \"sher\"},\n\t\"throat stabber\": {\"bbe\", \"hro\"},\n\t\"tiger sword\": {\"ger s\"},\n\t\"timeworn claw\": {\"ewo\", \"mew\"},\n\t\"titan gauntlets\": {\"an g\", \"an ga\", \"n gau\", \"tit\"},\n\t\"titan greaves\": {\"an g\", \"an gr\", \"tit\"},\n\t\"titanium spirit shield\": {\"ani\", \"niu\", \"tit\"},\n\t\"tomahawk\": {\"oma\", \"wk\"},\n\t\"topaz ring\": {\"az\", \"opa\", \"paz\"},\n\t\"tornado wand\": {\"ado\", \"nad\"},\n\t\"tribal circlet\": {\"al ci\", \"cir\", \"cle\", \"l ci\"},\n\t\"tricorne\": {\"tric\"},\n\t\"triumphant lamellar\": {\"mph\"},\n\t\"turquoise amulet\": {\"amu\", \"e am\", \"rq\", \"ule\"},\n\t\"twilight blade\": {\"ht bl\", \"ilig\", \"t bl\", \"wil\"},\n\t\"two-point arrow quiver\": {\"-p\", \"nt a\", \"o-p\"},\n\t\"two-stone ring\": {\"-s\", \"e ri\", \"ne ri\"},\n\t\"two-toned boots\": {\"-t\"},\n\t\"tyrant's sekhem\": {\"tyr\"},\n\t\"unset ring\": {\"nse\", \"t ri\", \"t rin\"},\n\t\"ursine pelt\": {\"elt\", \"pelt\", \"rsi\", \"urs\"},\n\t\"vaal axe\": {\"aal a\"},\n\t\"vaal blade\": {\"aal b\", \"l bl\"},\n\t\"vaal buckler\": {\"aal b\", \"aal bu\"},\n\t\"vaal claw\": {\"aal c\", \"l cla\"},\n\t\"vaal gauntlets\": {\"al ga\", \"l ga\"},\n\t\"vaal hatchet\": {\"al h\"},\n\t\"vaal mask\": {\"aal m\", \"l mas\"},\n\t\"vaal regalia\": {\"l reg\"},\n\t\"vaal sceptre\": {\"aal sc\"},\n\t\"vanguard belt\": {\"bel\", \"d be\", \"elt\", \"gua\"},\n\t\"varnished coat\": {\"arn\", \"arni\", \"varn\"},\n\t\"velvet gloves\": {\"et g\", \"lv\", \"t gl\"},\n\t\"velvet slippers\": {\"et s\", \"lv\", \"t sl\"},\n\t\"vermillion ring\": {\"erm\", \"lio\", \"llio\", \"mil\", \"n ri\", \"on ri\"},\n\t\"vile arrow quiver\": {\"ile ar\", \"vil\"},\n\t\"vile staff\": {\"ile s\", \"vil\"},\n\t\"vine circlet\": {\"cir\", \"cle\", \"e ci\", \"vine\"},\n\t\"viridian jewel\": {\"ewe\", \"ian\", \"n j\"},\n\t\"void axe\": {\"id a\", \"oid\", \"voi\"},\n\t\"void sceptre\": {\"id s\", \"oid\", \"voi\"},\n\t\"war buckler\": {\"ar bu\"},\n\t\"war hammer\": {\"ar h\"},\n\t\"war sword\": {\"ar sw\"},\n\t\"whalebone rapier\": {\"eb\", \"hal\"},\n\t\"widowsilk robe\": {\"dow\", \"ido\"},\n\t\"wild leather\": {\"wil\", \"wild\"},\n\t\"wolf pelt\": {\"elt\", \"lf\", \"pelt\"},\n\t\"woodsplitter\": {\"dsp\"},\n\t\"wool gloves\": {\"ol g\", \"ool\"},\n\t\"wool shoes\": {\"oe\", \"ool\"},\n\t\"wrapped mitts\": {\"d mi\", \"pped m\", \"wrapped m\"},\n\t\"wyrmscale doublet\": {\"mscale d\"},\n\t\"wyrmscale gauntlets\": {\"mscale g\"},\n\t\"zealot gloves\": {\"ot g\", \"t gl\"},\n\t\"zealot helmet\": {\"ot h\", \"t h\"},\n\t\"zodiac leather\": {\"c l\"},\n}", []], "browser.worker": [".py", "from _webworker import *\n", ["_webworker"]]}
__BRYTHON__.update_VFS(scripts)