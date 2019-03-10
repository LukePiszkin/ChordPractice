import random
import ui 


root = ['A', 'Ab', 'A#', 'B', 'Bb', 'C', 'C#', 'D','Db', 'D#', 'E','Eb', 'F', 'F#', 'G', 'Gb', 'G#']
scale = [ '', 'm',  '7',  'maj7', '6', 'm6', '5', '9', 'm9', 'maj9', '11', 'm11', '13', 'm13', 'add2','11dim9','13dim11','13dim9','6/9','6aug5', '6dim5', '7#5', '7#9', '7+5','7-5','7-9', '7aug', '7aug5', '7b5', '7b9','7dim5', '7dim9', '7sus', '7sus2', '9aug5', '9dim5','9sus', 'add2','add4','add9', '6add9', 'aug','dim','dim11','dim13','dim7','dim9','m11dim9','m13dim11','m13dim9','m6','m7','m7b5','m7dim5','m7dim9','m9','maj11','maj13','maj9','mb5','mdim11','mdim13','mdim9','mmaj7','sus','sus2']
randroot = random.randint(0,len(root)-1)
randscale = random.randint(0,len(scale)-1)
chord = root[randroot]+scale[randscale]

view=ui.View()
view.size_to_fit()
view.background_color = 'white'
view.flex = 'WH'

chordtxt = ui.Label()
chordtxt.text = chord
chordtxt.font = ('Courier', 30)
chordtxt.border_color = '#198054'
chordtxt.border_width = 5
chordtxt.frame = (90,120,200,75)
chordtxt.alignment = ui.ALIGN_CENTER

def reset(sender):
    exec(open("ChordPractice.py").read())
    
def quit(sender):
	view.close()
	
quitbutton = ui.Button(title = 'QUIT')
quitbutton.frame = (140,250,100,50)
quitbutton.border_color = '#0000ff'
quitbutton.border_width = 10
quitbutton.action = quit

resetbutton = ui.Button(title = 'RESET')
resetbutton.frame = (140, 200, 100, 50)
resetbutton.border_color = '#0000ff'
resetbutton.border_width = 10
resetbutton.action = reset

view.add_subview(chordtxt)
view.add_subview(resetbutton)
view.add_subview(quitbutton)
view.present(hide_title_bar=True)
