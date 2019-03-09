import random
import ui 


root = ['A', 'Ab', 'A#', 'B', 'Bb', 'C', 'C#', 'D','Db', 'D#', 'E','Eb', 'F', 'F#', 'G', 'Gb', 'G#']
scale = [ '', 'm',  '7',  'maj7', '6', 'm6', '5', '9', 'm9', 'maj9', '11', 'm11', '13', 'm13', 'add2', '11dim9','13dim11','13dim9','6/9','6aug5', '6dim5', '7#5', '7#9', '7+5','7-5','7-9', '7aug', '7aug5', '7b5', '7b9','7dim5', '7dim9', '7sus', '7sus2', '9aug5', '9dim5','9sus', 'add2','add4','add9', '6add9', 'aug','dim','dim11','dim13','dim7','dim9','m11dim9','m13dim11','m13dim9','m6','m7','m7b5','m7dim5','m7dim9','m9','maj11','maj13','maj9','mb5','mdim11','mdim13','mdim9','mmaj7','sus','sus2']
randroot = random.randint(0,len(root)-1)
randscale = random.randint(0,len(scale)-1)
chord = root[randroot]+scale[randscale]

view=ui.View()
view.background_color = 'white'
view.flex = 'WH'


chordtxt = ui.Label()
chordtxt.text = chord
chordtxt.alignment = ui.ALIGN_CENTER

def quit(sender):
    view.close()
    view.present()

quitbuttom = ui.button()
quitbutton.title = 'QUIT'
quitbutton.action = ui.quit



view.present()