# LM NR PTHKS UAOIE *
KEYS = (
    'L-', 'M-',
    '-N', '-R',
    'P-', 'T-', 'H-', 'K-', 'S-',
    '-U', '-A', '-O', '-I', '-E',
    '#'
)

IMPLICIT_HYPHEN_KEYS = KEYS

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = '#'

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'TX Bolt': {
        '#': '#',
        'P-': 'S-',
        'T-': ('T-', 'K-'),
        'H-': ('P-', 'W-'),
        'K-': ('H-','R-'),
        'S-': '*',
        'L-': 'A-',
        'M-': 'O-',
        '-N': '-E',
        '-R': '-U',
        '-U': ('-F','-R'),
        '-A': ('-P','-B'),
        '-O': ('-L','-G'),
        '-I': ('-T','-S'),
        '-E': ('-D','-Z'),
    },
    'Keyboard': {
        '#': ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'),
        'P-': 'a',
        'T-': 's',
        'H-': 'd',
        'K-': 'f',
        'S-': 'g',
        'L-': 'c',
        'M-': 'v',
        '-N': 'n',
        '-R': 'm',
        '-U': 'h',
        '-A': 'j',
        '-O': 'k',
        '-I': 'l',
        '-E': ';',
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op'     : ('z', 'x', 'b', ',', '.', '/'),
    },
}

DICTIONARIES_ROOT = 'asset:plover_japanese_stenoword:dictionaries'
DEFAULT_DICTIONARIES = (
    'user.json',
    'commands.json',
    'StenoWord.json',
)

