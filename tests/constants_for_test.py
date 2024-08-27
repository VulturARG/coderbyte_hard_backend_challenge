SAMPLE_INPUT_JSON = '[{"name": "John", "age": 30, "city": "New York", "country": "USA", "Hobbies": ["reading", "swimming", "hiking", "swimming"], "occupation": "programmer", "favorite_foods": {"Breakfast": "pancakes", "Lunch": "", "dinner": "pasta", "Snack": ""}, "gear": {"type": "", "material": "", "color": null}, "affiliations": ["", "", ""], "friends": [{"name": "Jane", "age": 28, "city": "New York", "country": "USA", "occupation": null}, {"name": "Tom", "age": 32, "city": "London", "country": "UK", "occupation": "teacher"}, {"name": "Jane", "age": 28, "city": "New York", "country": "USA", "occupation": null}]}]'

SAMPLE_INPUT_DATA = [
    {
        "name": "John",
        "age": 30,
        "city": "New York",
        "country": "USA",
        "Hobbies": ["reading", "swimming", "hiking", "swimming"],
        "occupation": "programmer",
        "favorite_foods": {
            "Breakfast": "pancakes",
            "Lunch": "",
            "dinner": "pasta",
            "Snack": "",
        },
        "gear": {"type": "", "material": "", "color": None},
        "affiliations": ["", "", ""],
        "friends": [
            {
                "name": "Jane",
                "age": 28,
                "city": "New York",
                "country": "USA",
                "occupation": None,
            },
            {
                "name": "Tom",
                "age": 32,
                "city": "London",
                "country": "UK",
                "occupation": "teacher",
            },
            {
                "name": "Jane",
                "age": 28,
                "city": "New York",
                "country": "USA",
                "occupation": None,
            },
        ],
    }
]

SAMPLE_FINAL_DATA = [
    {
        "age": 30,
        "city": "New York",
        "country": "USA",
        "favorite_foods": {"Breakfast": "pancakes", "dinner": "pasta"},
        "friends": [
            {"age": 28, "city": "New York", "country": "USA", "name": "Jane"},
            {
                "age": 32,
                "city": "London",
                "country": "UK",
                "name": "Tom",
                "occupation": "teacher",
            },
        ],
        "gear": {},
        "Hobbies": ["reading", "swimming", "hiking", "swimming"],
        "name": "John",
        "occupation": "programmer",
    }
]

SAMPLE_ORDERED_DATA = [
    {
        "Hobbies": ["reading", "swimming", "hiking", "swimming"],
        "age": 30,
        "affiliations": ["", "", ""],
        "city": "New York",
        "country": "USA",
        "favorite_foods": {
            "Breakfast": "pancakes",
            "Lunch": "",
            "Snack": "",
            "dinner": "pasta",
        },
        "friends": [
            {
                "age": 28,
                "city": "New York",
                "country": "USA",
                "name": "Jane",
                "occupation": None,
            },
            {
                "age": 32,
                "city": "London",
                "country": "UK",
                "name": "Tom",
                "occupation": "teacher",
            },
            {
                "age": 28,
                "city": "New York",
                "country": "USA",
                "name": "Jane",
                "occupation": None,
            },
        ],
        "gear": {"color": None, "material": "", "type": ""},
        "name": "John",
        "occupation": "programmer",
    }
]

SAMPLE_DUPLICATE_REMOVED = [
    {
        "Hobbies": ["reading", "swimming", "hiking", "swimming"],
        "age": 30,
        "affiliations": ["", "", ""],
        "city": "New York",
        "country": "USA",
        "favorite_foods": {
            "Breakfast": "pancakes",
            "Lunch": "",
            "Snack": "",
            "dinner": "pasta",
        },
        "friends": [
            {
                "age": 28,
                "city": "New York",
                "country": "USA",
                "name": "Jane",
                "occupation": None,
            },
            {
                "age": 32,
                "city": "London",
                "country": "UK",
                "name": "Tom",
                "occupation": "teacher",
            },
        ],
        "gear": {"color": None, "material": "", "type": ""},
        "name": "John",
        "occupation": "programmer",
    }
]

SAMPLE_CLEANED = [
    {
        "Hobbies": ["reading", "swimming", "hiking", "swimming"],
        "age": 30,
        "city": "New York",
        "country": "USA",
        "favorite_foods": {
            "Breakfast": "pancakes",
            "dinner": "pasta",
        },
        "friends": [
            {
                "age": 28,
                "city": "New York",
                "country": "USA",
                "name": "Jane",
            },
            {
                "age": 32,
                "city": "London",
                "country": "UK",
                "name": "Tom",
                "occupation": "teacher",
            },
        ],
        "gear": {},
        "name": "John",
        "occupation": "programmer",
    }
]

ORIGINAL_JSON_INPUT = '[{"name": "HarryPotter", "age": 18, "house": "", "wand": {"wood": "Holly", "core": "Phoenixfeather", "length": 11}, "friends": [{"name": "HermioneGranger", "age": 18, "house": "Gryffindor", "wand": {"wood": "Vine", "core": "Dragonheartstring", "length": 10.75}, "occupation": null}, {"name": "RonWeasley", "age": 18, "house": "Gryffindor", "wand": {"wood": "Willow", "core": "Unicornhair", "length": 14}, "occupation": "student"}, {"name": "HermioneGranger", "age": 18, "house": "Gryffindor", "wand": {"wood": "Vine", "core": "Dragonheartstring", "length": 10.75}, "occupation": null}], "enemies": ["LordVoldemort", "DracoMalfoy"], "patronus": "Stag"}, {"name": "HermioneGranger", "age": 18, "house": "Gryffindor", "wand": {"wood": "", "core": "", "length": null}, "friends": [{"name": "HarryPotter", "age": 18, "house": "Gryffindor", "wand": {"wood": "Holly", "core": "Phoenixfeather", "length": 11}, "occupation": "student"}, {"name": "RonWeasley", "age": 18, "house": "Gryffindor", "wand": {"wood": "Willow", "core": "Unicornhair", "length": 14}, "occupation": "student"}, {"name": "LunaLovegood", "age": 18, "house": "Ravenclaw", "wand": {"wood": "Unknown", "core": "Unknown", "length": "Unknown"}, "occupation": "student"}], "enemies": ["", ""], "patronus": "Otter"}, {"name": "RonWeasley", "age": 18, "house": "Gryffindor", "wand": {"wood": "Willow", "core": "Unicornhair", "length": 14}, "friends": [{"name": "HarryPotter", "age": 18, "house": ""}, {"name": "HermioneGranger", "age": 18, "house": "Gryffindor"}, {"name": "HermioneGranger", "age": 18, "house": "Gryffindor"}], "enemies": [{"name": "DracoMalfoy", "age": 18, "house": "Slytherin"}, {"name": "VincentCrabbe", "age": 18, "house": "Slytherin"}], "patronus": "JackRussellTerrier"}, {"name": "GinnyWeasley", "age": null, "house": "Gryffindor", "wand": {"wood": "Yew", "core": "Phoenixfeather", "length": 9}, "friends": [{"name": "HarryPotter", "age": 18, "house": "Gryffindor", "occupation": "Auror"}, {"name": "LunaLovegood", "age": 17, "house": "Ravenclaw", "occupation": "Magizoologist"}, {"name": "NevilleLongbottom", "age": 18, "house": "Gryffindor", "occupation": "ProfessorofHerbology"}], "enemies": [{"name": "TomRiddle", "alias": "LordVoldemort"}, {"name": "BellatrixLestrange", "alias": "Bella"}], "patronus": "Horse"}, {"name": "DracoMalfoy", "age": 18, "house": "Slytherin", "wand": {"wood": "Hawthorn", "core": "Unicornhair", "length": 10}, "friends": [{"name": "VincentCrabbe", "age": 18, "city": "England", "country": "UK", "occupation": null}, {"name": "GregoryGoyle", "age": 18, "city": "England", "country": "UK", "occupation": null}], "enemies": [{"name": "HarryPotter", "age": 17, "house": "Gryffindor", "occupation": null}, {"name": "HermioneGranger", "age": 17, "house": "Gryffindor", "occupation": null}, {"name": "RonWeasley", "age": 17, "house": "Gryffindor", "occupation": null}], "patronus": null}]'

ORIGINAL_INPUT = [
    {
        "name": "HarryPotter",
        "age": 18,
        "house": "",
        "wand": {"wood": "Holly", "core": "Phoenixfeather", "length": 11},
        "friends": [
            {
                "name": "HermioneGranger",
                "age": 18,
                "house": "Gryffindor",
                "wand": {"wood": "Vine", "core": "Dragonheartstring", "length": 10.75},
                "occupation": None,
            },
            {
                "name": "RonWeasley",
                "age": 18,
                "house": "Gryffindor",
                "wand": {"wood": "Willow", "core": "Unicornhair", "length": 14},
                "occupation": "student",
            },
            {
                "name": "HermioneGranger",
                "age": 18,
                "house": "Gryffindor",
                "wand": {"wood": "Vine", "core": "Dragonheartstring", "length": 10.75},
                "occupation": None,
            },
        ],
        "enemies": ["LordVoldemort", "DracoMalfoy"],
        "patronus": "Stag",
    },
    {
        "name": "HermioneGranger",
        "age": 18,
        "house": "Gryffindor",
        "wand": {"wood": "", "core": "", "length": None},
        "friends": [
            {
                "name": "HarryPotter",
                "age": 18,
                "house": "Gryffindor",
                "wand": {"wood": "Holly", "core": "Phoenixfeather", "length": 11},
                "occupation": "student",
            },
            {
                "name": "RonWeasley",
                "age": 18,
                "house": "Gryffindor",
                "wand": {"wood": "Willow", "core": "Unicornhair", "length": 14},
                "occupation": "student",
            },
            {
                "name": "LunaLovegood",
                "age": 18,
                "house": "Ravenclaw",
                "wand": {"wood": "Unknown", "core": "Unknown", "length": "Unknown"},
                "occupation": "student",
            },
        ],
        "enemies": ["", ""],
        "patronus": "Otter",
    },
    {
        "name": "RonWeasley",
        "age": 18,
        "house": "Gryffindor",
        "wand": {"wood": "Willow", "core": "Unicornhair", "length": 14},
        "friends": [
            {"name": "HarryPotter", "age": 18, "house": ""},
            {"name": "HermioneGranger", "age": 18, "house": "Gryffindor"},
            {"name": "HermioneGranger", "age": 18, "house": "Gryffindor"},
        ],
        "enemies": [
            {"name": "DracoMalfoy", "age": 18, "house": "Slytherin"},
            {"name": "VincentCrabbe", "age": 18, "house": "Slytherin"},
        ],
        "patronus": "JackRussellTerrier",
    },
    {
        "name": "GinnyWeasley",
        "age": None,
        "house": "Gryffindor",
        "wand": {"wood": "Yew", "core": "Phoenixfeather", "length": 9},
        "friends": [
            {
                "name": "HarryPotter",
                "age": 18,
                "house": "Gryffindor",
                "occupation": "Auror",
            },
            {
                "name": "LunaLovegood",
                "age": 17,
                "house": "Ravenclaw",
                "occupation": "Magizoologist",
            },
            {
                "name": "NevilleLongbottom",
                "age": 18,
                "house": "Gryffindor",
                "occupation": "ProfessorofHerbology",
            },
        ],
        "enemies": [
            {"name": "TomRiddle", "alias": "LordVoldemort"},
            {"name": "BellatrixLestrange", "alias": "Bella"},
        ],
        "patronus": "Horse",
    },
    {
        "name": "DracoMalfoy",
        "age": 18,
        "house": "Slytherin",
        "wand": {"wood": "Hawthorn", "core": "Unicornhair", "length": 10},
        "friends": [
            {
                "name": "VincentCrabbe",
                "age": 18,
                "city": "England",
                "country": "UK",
                "occupation": None,
            },
            {
                "name": "GregoryGoyle",
                "age": 18,
                "city": "England",
                "country": "UK",
                "occupation": None,
            },
        ],
        "enemies": [
            {
                "name": "HarryPotter",
                "age": 17,
                "house": "Gryffindor",
                "occupation": None,
            },
            {
                "name": "HermioneGranger",
                "age": 17,
                "house": "Gryffindor",
                "occupation": None,
            },
            {
                "name": "RonWeasley",
                "age": 17,
                "house": "Gryffindor",
                "occupation": None,
            },
        ],
        "patronus": None,
    },
]

ORIGINAL_OUTPUT = [
    {
        "age": 18,
        "enemies": ["LordVoldemort", "DracoMalfoy"],
        "friends": [
            {
                "age": 18,
                "house": "Gryffindor",
                "name": "HermioneGranger",
                "wand": {"core": "Dragonheartstring", "length": 10.75, "wood": "Vine"},
            },
            {
                "age": 18,
                "house": "Gryffindor",
                "name": "RonWeasley",
                "occupation": "student",
                "wand": {"core": "Unicornhair", "length": 14, "wood": "Willow"},
            },
        ],
        "name": "HarryPotter",
        "patronus": "Stag",
        "wand": {"core": "Phoenixfeather", "length": 11, "wood": "Holly"},
    },
    {
        "age": 18,
        "friends": [
            {
                "age": 18,
                "house": "Gryffindor",
                "name": "HarryPotter",
                "occupation": "student",
                "wand": {"core": "Phoenixfeather", "length": 11, "wood": "Holly"},
            },
            {
                "age": 18,
                "house": "Gryffindor",
                "name": "RonWeasley",
                "occupation": "student",
                "wand": {"core": "Unicornhair", "length": 14, "wood": "Willow"},
            },
            {
                "age": 18,
                "house": "Ravenclaw",
                "name": "LunaLovegood",
                "occupation": "student",
                "wand": {"core": "Unknown", "length": "Unknown", "wood": "Unknown"},
            },
        ],
        "house": "Gryffindor",
        "name": "HermioneGranger",
        "patronus": "Otter",
        "wand": {},
    },
    {
        "age": 18,
        "enemies": [
            {"age": 18, "house": "Slytherin", "name": "DracoMalfoy"},
            {"age": 18, "house": "Slytherin", "name": "VincentCrabbe"},
        ],
        "friends": [
            {"age": 18, "name": "HarryPotter"},
            {"age": 18, "house": "Gryffindor", "name": "HermioneGranger"},
        ],
        "house": "Gryffindor",
        "name": "RonWeasley",
        "patronus": "JackRussellTerrier",
        "wand": {"core": "Unicornhair", "length": 14, "wood": "Willow"},
    },
    {
        "enemies": [
            {"alias": "LordVoldemort", "name": "TomRiddle"},
            {"alias": "Bella", "name": "BellatrixLestrange"},
        ],
        "friends": [
            {
                "age": 18,
                "house": "Gryffindor",
                "name": "HarryPotter",
                "occupation": "Auror",
            },
            {
                "age": 17,
                "house": "Ravenclaw",
                "name": "LunaLovegood",
                "occupation": "Magizoologist",
            },
            {
                "age": 18,
                "house": "Gryffindor",
                "name": "NevilleLongbottom",
                "occupation": "ProfessorofHerbology",
            },
        ],
        "house": "Gryffindor",
        "name": "GinnyWeasley",
        "patronus": "Horse",
        "wand": {"core": "Phoenixfeather", "length": 9, "wood": "Yew"},
    },
    {
        "age": 18,
        "enemies": [
            {
                "age": 17,
                "house": "Gryffindor",
                "name": "HarryPotter",
            },
            {
                "age": 17,
                "house": "Gryffindor",
                "name": "HermioneGranger",
            },
            {
                "age": 17,
                "house": "Gryffindor",
                "name": "RonWeasley",
            },
        ],
        "friends": [
            {
                "age": 18,
                "city": "England",
                "country": "UK",
                "name": "VincentCrabbe",
            },
            {
                "age": 18,
                "city": "England",
                "country": "UK",
                "name": "GregoryGoyle",
            },
        ],
        "house": "Slytherin",
        "name": "DracoMalfoy",
        "wand": {"core": "Unicornhair", "length": 10, "wood": "Hawthorn"},
    },
]
