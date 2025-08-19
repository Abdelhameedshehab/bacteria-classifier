bacteria_db = {
    "E. coli": {
        "indole": "+ve",
        "mr": "+ve",
        "vp": "-ve",
        "citrate": "-ve",
        "urease": "-ve",
        "h2s": "-ve",
        "lactose": "+ve",
        "motility": "+ve",
        "capsule": "variable",
        "kcn": "-ve"
    },

    "Klebsiella": {
        "indole": "-ve",
        "mr": "-ve",
        "vp": "+ve",
        "citrate": "+ve",
        "urease": "+ve",
        "h2s": "-ve",
        "lactose": "+ve",
        "motility": "-ve",
        "capsule": "+ve",
        "kcn": "+ve"
    },

    "Proteus": {
        "indole": "-ve",
        "mr": "+ve",
        "vp": "-ve",  # مصحح من الجدول الأصلي
        "citrate": "+ve",
        "urease": "+ve",
        "h2s": "+ve",
        "lactose": "-ve",
        "motility": "+ve",
        "capsule": "-ve",
        "kcn": "+ve"
    },

    "Salmonella": {
        "indole": "-ve",
        "mr": "+ve",
        "vp": "-ve",
        "citrate": "-ve",  # مصحح
        "urease": "-ve",
        "h2s": "+ve",
        "lactose": "-ve",
        "motility": "+ve",
        "capsule": "-ve",
        "kcn": "-ve"
    },

    "Shigella": {
        "indole": "variable",
        "mr": "+ve",
        "vp": "-ve",
        "citrate": "-ve",
        "urease": "-ve",
        "h2s": "-ve",
        "lactose": "-ve",
        "motility": "-ve",
        "capsule": "-ve",
        "kcn": "-ve"
    },

    "Serratia": {
        "indole": "-ve",
        "mr": "-ve",
        "vp": "+ve",
        "citrate": "+ve",
        "urease": "+ve",
        "h2s": "-ve",
        "lactose": "-ve",
        "motility": "+ve",
        "capsule": "-ve",
        "kcn": "+ve"
    },

    "Citrobacter": {
        "indole": "-ve",
        "mr": "+ve",
        "vp": "-ve",  # مصحح
        "citrate": "+ve",
        "urease": "variable",
        "h2s": "+ve",
        "lactose": "+ve",
        "motility": "+ve",
        "capsule": "-ve",
        "kcn": "+ve"
    },

    "Yersinia": {
        "indole": "-ve",
        "mr": "+ve",
        "vp": "-ve",
        "citrate": "-ve",
        "urease": "-ve",
        "h2s": "-ve",
        "lactose": "-ve",
        "motility": "-ve",
        "capsule": "+ve",
        "kcn": "-ve"
    },

    "Enterobacter": {
        "indole": "-ve",
        "mr": "-ve",
        "vp": "+ve",
        "citrate": "+ve",
        "urease": "-ve",
        "h2s": "-ve",
        "lactose": "+ve",
        "motility": "+ve",
        "capsule": "-ve",
        "kcn": "+ve"
    },

    "Morganella": {
        "indole": "+ve",
        "mr": "+ve",
        "vp": "-ve",
        "citrate": "-ve",
        "urease": "+ve",
        "h2s": "-ve",
        "lactose": "-ve",
        "motility": "+ve",
        "capsule": "-ve",
        "kcn": "+ve"
    },

    "Providencia": {
        "indole": "+ve",
        "mr": "+ve",
        "vp": "-ve",  # مصحح
        "citrate": "+ve",
        "urease": "-ve",  # مصحح
        "h2s": "-ve",
        "lactose": "-ve",
        "motility": "+ve",
        "capsule": "-ve",
        "kcn": "+ve"
    }
}

# قائمة الاختبارات بالترتيب
tests = ["indole", "mr", "vp", "citrate", "urease", "h2s", "lactose", "motility", "capsule", "kcn"]

# أسماء الاختبارات للعرض
test_names = {
    "indole": "Indole Test",
    "mr": "MR Test (Methyl Red)",
    "vp": "VP Test (Voges-Proskauer)",
    "citrate": "Citrate Test",
    "urease": "Urease Test",
    "h2s": "H2S Test",
    "lactose": "Lactose Fermentation",
    "motility": "Motility Test",
    "capsule": "Capsule Test",
    "kcn": "Growth on KCN"
}