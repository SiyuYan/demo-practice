def solution(x, arr):
    if len(arr) == 0:
        return 0

    if x >= len(arr):
        return max(arr)

    max_num = 0
    for index, value in enumerate(arr):
        if index + x > len(arr):
            break
        else:
            current_min = min(arr[index:index + x])
            if max_num < current_min:
                max_num = current_min

    return max_num


if __name__ == '__main__':
    # print(solution(2, [3, 1, 1, 1]))
    print(solution(1000, [1000, 888450279, 414333100, 226069412, 997273308,
                          495622138, 242246692, 78731969, 483090980, 265550000,
                          688606351, 535518275, 574101163, 397812690,
                          214168202, 414790852, 766098598, 644798096,
                          285886900, 558292687, 965792933, 342987578,
                          649447909, 560689958, 548311316, 788041623,
                          698797439, 708706736, 226921437, 376988901,
                          314506460, 450949885, 540363819, 307536238,
                          122214631, 321593975, 245642314, 889657796,
                          371687111, 309001000, 62481834, 782614937, 983943861,
                          907658530, 552218883, 541839421, 829274606,
                          615627151, 581341330, 70047412, 398388676, 400161621,
                          449678977, 789475187, 287341520, 795215973,
                          513138020, 945733047, 698397506, 386162081,
                          646355680, 827727491, 787232601, 911103848,
                          546827366, 982389556, 873651437, 183216319,
                          521824797, 417525698, 232023337, 626518301, 39719390,
                          357553813, 743331159, 200617683, 634312705, 84618708,
                          232259094, 877021268, 101998944, 138461730, 28896426,
                          900149780, 119499723, 387006492, 842239021,
                          628333268, 874513013, 290671172, 254502654,
                          539287666, 447863971, 337857849, 100644808,
                          208824617, 965402956, 450617412, 681295279, 67915641,
                          684078665, 773498129, 670693141, 21122360, 962376826,
                          363001097, 154885712, 937765875, 883370111,
                          586054989, 951458770, 694438056, 998765394,
                          265895170, 798272898, 742408085, 502963599,
                          673961458, 456805319, 51099235, 366780297, 387932794,
                          573511480, 933195035, 774855104, 77514770, 312711513,
                          250539630, 845644410, 852463490, 616112556,
                          787217984, 597629315, 333185502, 222888214,
                          327728674, 832175992, 909704846, 816245991,
                          580819495, 569608941, 629765592, 384147599,
                          801720358, 432234732, 779364647, 710008994,
                          475884054, 844565525, 132558537, 559318999,
                          336388543, 310274610, 540872761, 324244954,
                          782981312, 778877168, 319440982, 994367836,
                          636367935, 270806140, 359604956, 216092611,
                          109722707, 736474068, 34634934, 521049007, 562015641,
                          54757259, 943163228, 577242679, 783662983, 820151935,
                          719302865, 838970104, 632042817, 296086985,
                          111542818, 138152684, 800103071, 107936497,
                          377650644, 398244239, 606076486, 867607886,
                          745833590, 953261099, 285472136, 850921364,
                          642782020, 744699091, 279571728, 339884497,
                          701898860, 856008135, 172278422, 189614992,
                          385744624, 512774389, 514147356, 359217238,
                          211448555, 874977398, 86440372, 215650207, 95929114,
                          76060945, 583434416, 304203563, 829373656, 714245609,
                          530284530, 504327004, 178518125, 660979468,
                          326415375, 265150227, 250072135, 903403304,
                          486640671, 609652151, 809737310, 738208035,
                          763769172, 151693841, 558421039, 784183827,
                          687647455, 769073519, 390674068, 981253764,
                          211239576, 882992071, 197247530, 841005555,
                          853775496, 277835156, 884659593, 587777969,
                          992399658, 357110, 961242549, 729765226, 332396070,
                          681337930, 179684781, 164912211, 897059640,
                          922407012, 268892961, 850168623, 639729260,
                          558579777, 682603391, 780007186, 900711762,
                          270980785, 191891204, 506187613, 726347503,
                          392871320, 90016498, 408430265, 13767896, 59943795,
                          349838569, 969489955, 620126552, 576519252,
                          191411088, 118209660, 257853584, 19233489, 678370033,
                          504817846, 847507576, 556999102, 725022977,
                          749790518, 933052027, 146728210, 865018396,
                          895740605, 359627416, 711513418, 67851192, 674795919,
                          469975645, 992364269, 210313351, 456760218,
                          597057773, 175979286, 51495748, 651821991, 838400806,
                          252118874, 845624705, 455011663, 450398467,
                          810480515, 459516760, 507361856, 615676790,
                          540254123, 153676720, 65383881, 704346227, 580368171,
                          925543222, 56372418, 624089728, 584450006, 151183905,
                          503782424, 552239887, 91133713, 575848308, 785211197,
                          407276003, 993422000, 497342792, 223669809,
                          995070003, 149223429, 735545762, 710495695,
                          134659850, 616458069, 186320933, 53070212, 641002509,
                          396670902, 757398359, 289955052, 132229648,
                          331010353, 566681726, 203093773, 69345989, 444810131,
                          629724067, 906178346, 731919759, 940900817,
                          402068853, 358562837, 884348117, 974711857,
                          740217449, 250390686, 753476959, 27552360, 65384447,
                          896269505, 540686868, 736943861, 993411866,
                          634608028, 365563527, 567355742, 812650397,
                          412806907, 981984873, 882442600, 237965870,
                          885224703, 45395747, 299333575, 986560519, 768044826,
                          738221999, 554210285, 73063257, 441240374, 454653187,
                          507279452, 110955765, 752955004, 261475317, 2259443,
                          514554024, 769169161, 644337342, 563217479,
                          413802835, 256524811, 19846230, 330854587, 957192450,
                          760593936, 559058688, 760804665, 428287963,
                          901117041, 698310410, 801495541, 148750085,
                          669835402, 400781731, 61699316, 627778670, 96275390,
                          140903768, 438090239, 120110811, 394176952,
                          247320103, 94584755, 115623116, 920929602, 790391733,
                          329803928, 610440315, 276017761, 397349380,
                          464717333, 772254916, 615852391, 723358680,
                          291885945, 800001988, 411714821, 693291373,
                          365275128, 105793813, 924135682, 586411163, 1475751,
                          168828613, 850173172, 529465829, 186881708,
                          982429318, 269942529, 549613386, 982394351,
                          798150503, 537429483, 210432670, 825047637,
                          944720928, 207915485, 87178641, 722362159, 617697773,
                          625582176, 567990693, 851063462, 414775828,
                          410967067, 574076363, 670048337, 283231254,
                          144628920, 858800536, 896721126, 393331826,
                          627449576, 638987305, 130400524, 807752720,
                          128529532, 813823632, 969106766, 859436625, 21205684,
                          585547257, 916868396, 82522544, 305178773, 640793438,
                          993158476, 42194197, 331537779, 280714978, 971545294,
                          77240758, 2136463, 827342542, 3669948, 891682009,
                          767637543, 950537376, 291568396, 53939158, 530617064,
                          534455600, 611589064, 393520284, 293039073, 40059941,
                          183070213, 825098747, 491330092, 541061674,
                          247004342, 505820743, 703156640, 592964847,
                          399619283, 543939420, 492248298, 808973728,
                          752072424, 490651619, 970337475, 826228293,
                          988446227, 932733422, 744880792, 392028653,
                          814481272, 685936514, 822808692, 970646361,
                          626891192, 338526585, 550645211, 902320631,
                          903217239, 440232723, 577519502, 772911491,
                          419119637, 444207339, 701834314, 513393852, 63595369,
                          460182299, 871154259, 500490059, 114679572,
                          250469577, 635931191, 892795251, 521794503, 98992936,
                          347935047, 638234751, 588790451, 160581691,
                          144261169, 262364763, 91938988, 91760568, 58392382,
                          179343935, 371652089, 264226823, 110806564,
                          144456838, 314687162, 171528041, 830195593,
                          411873693, 299066358, 988594998, 695965205,
                          117059094, 380345664, 870918462, 592273202,
                          260035036, 852899078, 245842257, 954529635,
                          502112897, 260877686, 617806043, 748060734,
                          134189748, 263160845, 418725031, 411512839,
                          973609678, 551000510, 690993860, 793575659,
                          547560075, 460254139, 503079045, 322330070,
                          962166741, 881370338, 753396897, 504344305,
                          301315772, 251868615, 358819707, 454981563,
                          218686083, 376252762, 910573949, 523928771,
                          148710356, 949920821, 450465693, 114016511,
                          139799571, 375971973, 109162498, 4157132, 102294991,
                          833241746, 252325055, 760798851, 617528917,
                          113760748, 505755325, 583867060, 888621151,
                          528114484, 799917240, 303244802, 729775594,
                          331547780, 511427680, 89292955, 294933797, 45764220,
                          414406559, 545631570, 992746, 715904506, 319669338,
                          152120821, 790171669, 583667217, 143569830,
                          703150400, 883606726, 662427414, 611149876,
                          391467368, 987558073, 476905160, 292105599,
                          329109207, 576227332, 141278782, 100844231,
                          268600659, 839275866, 741943067, 239825160,
                          556895622, 229797537, 925072676, 814546139,
                          467158860, 305475845, 890930201, 316119312,
                          853070299, 472894158, 177977231, 21072699, 87731712,
                          808575948, 511152872, 264737158, 386830781,
                          306065070, 611237485, 630549511, 250427885,
                          697634224, 116662554, 893001167, 826679324,
                          595898993, 402757631, 584637154, 5527136, 385980574,
                          24388954, 701210940, 703125058, 639022316, 522078151,
                          2038199, 184739582, 864627712, 575479027, 539892886,
                          260024397, 731430710, 456392353, 259172859,
                          730835106, 242867104, 475040259, 345188533,
                          778475119, 28432762, 405315377, 290632427, 29097799,
                          714678055, 675637609, 699606207, 198221688,
                          247756843, 121982588, 890496310, 321545319,
                          834850901, 851922062, 261260032, 912790112,
                          396586048, 142349252, 879221894, 569828341,
                          522465665, 741633174, 457282388, 317519790,
                          699331198, 309728646, 557567951, 34002614, 144162183,
                          896714834, 805235530, 136186476, 844032273,
                          581159995, 628018133, 553428837, 207997536,
                          899736387, 501681329, 449158839, 442221271,
                          583113014, 982443399, 897254259, 187225995,
                          102711609, 422257128, 986157856, 823458556,
                          131087868, 775601008, 932200242, 518037749,
                          831427457, 2379051, 881313174, 907219564, 834161354,
                          910632011, 314541088, 928436742, 912196944,
                          754780259, 915562592, 130000478, 473459382, 96188042,
                          910000396, 512325218, 676455106, 172109067,
                          861014826, 42610660, 556275370, 445915726, 516386382,
                          640761110, 308574985, 411371343, 506380365,
                          919910263, 986089831, 446111997, 255900081,
                          307054568, 725043301, 351252837, 619348911,
                          775495554, 342823784, 901117597, 752000948,
                          687699836, 270421189, 780302745, 482843110, 65189563,
                          882330202, 173411319, 510382796, 932285719,
                          436115250, 571233251, 889374379, 155478882,
                          942644370, 74879788, 775005903, 890073214, 490738516,
                          270214732, 450114019, 578753635, 210674061,
                          630749896, 490823483, 16423758, 274075710, 25302797,
                          129112823, 643642966, 520508004, 732530627, 76866876,
                          469950022, 781649877, 199761437, 289473984,
                          992474065, 135764630, 917542491, 85923109, 927543522,
                          499749868, 913488146, 219391729, 411058853, 40709911,
                          376984883, 487156148, 210574526, 481865312,
                          486285321, 775581451, 674440729, 623791865,
                          417963532, 930797692, 257557145, 727188614, 89869601,
                          15974247, 524541347, 34328411, 880178389, 780827723,
                          587008539, 12807869, 145861825, 921343940, 587825016,
                          530837265, 190074179, 761685456, 184162274,
                          627746284, 6307488, 468744196, 724268641, 992453101,
                          152888604, 581112404, 82860769, 225926546, 631858124,
                          353451649, 15520852, 617509513, 869692959, 864418550,
                          439057835, 948476672, 828681026, 423636140,
                          367001840, 67259623, 599120837, 963260294, 691857039,
                          517643082, 4533046, 493108836, 186061846, 331849987,
                          681000289, 531137972, 529706031, 711054920,
                          457310583, 801531481, 250398430, 168714079,
                          746021339, 495948455, 115037527, 622652012,
                          983913610, 901142923, 883415930, 690772075,
                          781351460, 545016264, 255459564, 478738744,
                          561890203, 590456668, 886440915, 125421771,
                          544768119, 472173825, 483433773, 965903311,
                          506679502, 887168919, 812317438, 825489652,
                          276710321, 870371651, 648567241, 533075848,
                          537947286, 516694038, 521831791, 39759604, 428295165,
                          151463624, 759539028, 571755675, 858954369,
                          335385993, 8097604, 641737466, 785188530, 254249127,
                          10772439, 84876633, 366893526, 969069295, 508257581,
                          222223469, 564656159, 582023262, 290124557,
                          232624706, 367223400, 814239909, 76342095, 496115293,
                          871473308, 653584855, 976681023, 487105157,
                          645145462, 311264413, 442230779, 615702659,
                          848059631, 986730818, 228678478, 189464551,
                          848539634, 938483353, 173285952, 736125141,
                          138876187, 81552726, 415997877, 763537185, 902357775,
                          790941439, 462855349, 262501032, 839455304,
                          731102662, 341249420, 768511060, 239107025,
                          193059750, 402591062, 460810993, 527259250,
                          412798868, 843044866, 753328129, 945423028,
                          450583622, 749974623, 204017730, 821386699, 34636744,
                          322990971, 90134948, 592533693, 829537692, 172516622,
                          560908394]))
