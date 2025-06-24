import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler



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


# Encoder settings
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((EncRotA, EncRotB, EncButton, False),)
encoder_handler.map = (((KC.VOLD, KC.VOLU, KC.LALT(KC.TAB))


