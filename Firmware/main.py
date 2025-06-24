import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Press, Release, Tap, Macros



Column1 = board.D0
Column2 = board.D1
Column3 = board.D4
Column4 = board.D5
Column5 = board.D6
Column6 = board.D7
Column7 = board.D9
Column8 = board.D10
Column9 = board.D11
Column10 = board.D12
Column11 = board.D14
Column12 = board.D15
Column13 = board.D16
Column14 = board.D17


EncButton = board.D20

Row1 = board.D16
Row2 = board.D22
Row3 = board.D24
Row4 = board.D25
Row5 = board.D26

EncRotA = board.D27
EncRotB = board.D29

# Keyboard Main Instance
keyboard = KMKKeyboard()
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Encoder settings
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((EncRotA, EncRotB, EncButton, False),)
encoder_handler.map = (((KC.VOLD, KC.VOLU, KC.MUTE)



#Defining the Pins
keyboard.keymap = [
    [KC.GRAVE, KC.KP_1, KC.KP_2, KC.KP_3, KC.KP_4, KC.KP_5, KC.KP_6, KC.KP_7, KC.KP_8, KC.KP_9, KC.KP_0, KC.MINUS	, KC.EQUAL, KC.BSPACE,
     KC.TAB	, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.KC.LBRACKET, KC.RBRACKET, KC.BSLASH,
     KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.KP_ENTER	
     KC.C, KC.V
    ]
]
                        



                        










                        
