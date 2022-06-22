import random

def get_presets():
    
    presets = {}

    presets['lavender'] = {
        0:{
            'id':random.randint(0,512),
            'alpha':100
        },
        1:{
            'id':random.randint(0,512),
            'alpha':100
        },
        2:{
            'id':random.randint(0,512),
            'alpha':100
        },
        3:{
            'id':49,
            'alpha':100
        },
        4:{
            'id':49,
            'alpha':100
        },
        5:{
            'id':49,
            'alpha':100
        }
    }

    presets['sunset'] = {
        0:{
            'id':random.randint(0,512),
            'alpha':100
        },
        1:{
            'id':random.randint(0,512),
            'alpha':100
        },
        2:{
            'id':random.randint(0,512),
            'alpha':100
        },
        3:{
            'id':153,
            'alpha':100
        },
        4:{
            'id':153,
            'alpha':100
        },
        5:{
            'id':153,
            'alpha':100
        }
    }

    presets['golden'] = {
        0:{
            'id':random.randint(0,512),
            'alpha':100
        },
        1:{
            'id':random.randint(0,512),
            'alpha':100
        },
        2:{
            'id':random.randint(0,512),
            'alpha':100
        },
        3:{
            'id':31,
            'alpha':100
        },
        4:{
            'id':31,
            'alpha':100
        },
        5:{
            'id':31,
            'alpha':100
        }
    }

    presets['dark'] = {
        0:{
            'id':random.randint(0,512),
            'alpha':100
        },
        1:{
            'id':random.randint(0,512),
            'alpha':100
        },
        2:{
            'id':random.randint(0,512),
            'alpha':100
        },
        3:{
            'id':115,
            'alpha':-100
        },
        4:{
            'id':115,
            'alpha':-100
        },
        5:{
            'id':115,
            'alpha':-100
        }
    }
    
    return presets