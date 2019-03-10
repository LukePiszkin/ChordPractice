import random
import ui 


root = ['A', 'Ab', 'A#', 'B', 'Bb', 'C', 'C#', 'D','Db', 'D#', 'E','Eb', 'F', 'F#', 'G', 'Gb', 'G#']
scale = [ '', 'm',  '7',  'maj7', '6', 'm6', '5', '9', 'm9', 'maj9', '11', 'm11', '13', 'm13', 'add2','11dim9','13dim11','13dim9','6/9','6aug5', '6dim5', '7#5', '7#9', '7+5','7-5','7-9', '7aug', '7aug5', '7b5', '7b9','7dim5', '7dim9', '7sus', '7sus2', '9aug5', '9dim5','9sus', 'add2','add4','add9', '6add9', 'aug','dim','dim11','dim13','dim7','dim9','m11dim9','m13dim11','m13dim9','m6','m7','m7b5','m7dim5','m7dim9','m9','maj11','maj13','maj9','mb5','mdim11','mdim13','mdim9','mmaj7','sus','sus2']
randroot = random.randint(0,len(root)-1)
randscale = random.randint(0,len(scale)-1)
chord = root[randroot]+scale[randscale]
minor_txt = 'root, minor third, perfect fifth'
dom_txt = 'root, major third, pefect fifth, minor seventh, (add 9), (add 9,11), (add 9,11,13)'
major_7_9_11_13_txt = 'root, major third, perfect fifth, major seventh, (add 9), (add 9,11), (add 9,11,13)'
add_txt = 'take the root triad and add the desired note in the scale'
aug_txt = 'root, major third, augmented fifth'
dim_txt = 'root, minor third, flattened fifth'
sharp_flat_txt = 'sharp (+,#) or flat (-,b) the desired note and add it to the root triad'
minor_third_txt = 'An interval consisting of three semitones'
major_third_txt = 'An interval consisting of four semitones'
perfect_fourth_txt = 'An interval consisting of five semitones'
flattened_fifth_txt = 'An interval consisting of six semitones'
perfect_fifth_txt = 'An interval consisting of seven semitones'
augmented_fifth_txt = 'An interval consisting of eight semitones'
sixth_txt = 'An interval consisting of nine semitones'
minor_seventh_txt = 'An interval consisting of ten semitones'
major_seventh_txt = 'An interval consisting of eleven semitones'

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

quitbutton = ui.Button(title = 'QUIT')
quitbutton.frame = (140,250,100,50)
quitbutton.border_color = '#0000ff'
quitbutton.border_width = 10
quitbutton.action = quit   

def quit(sender):
	view.close()

resetbutton = ui.Button(title = 'RESET')
resetbutton.frame = (140, 200, 100, 50)
resetbutton.border_color = '#0000ff'
resetbutton.border_width = 10
resetbutton.action = reset

def minor(sender):
    view_minor = ui.View()
    view_minor.size_to_fit()
    view_minor.background_color = 'white'
    view_minor.flex = 'WH'
    minor_lab = ui.Label(text = minor_txt)
    view_minor.add_subview(minor_lab)
    def minorquit(sender):
        view_minor.close()
    quitbuttonminor = ui.Button(title = 'QUIT')
    quitbuttonminor.frame = (140,250,100,50)
    quitbuttonminor.border_color = '#0000ff'
    quitbuttonminor.border_width = 10
    quitbuttonminor.action = minorquit
    view_minor.add_subview(quitbuttonminor)





minor = ui.Button(title = 'm (minor)')
minor.frame = (140, 300, 100, 50)
minor.border_color = '#0000ff'
minor.border_width = 5 
minor.action = minor


view.add_subview(chordtxt)
view.add_subview(resetbutton)
view.add_subview(quitbutton)
view.add_subview(minor)
view.present(hide_title_bar=True)
