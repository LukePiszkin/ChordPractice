import random
import ui 

root = ['A', 'Ab', 'A#', 'B', 'Bb', 'C', 'C#', 'D','Db', 'D#', 'E','Eb', 'F', 'F#', 'G', 'Gb', 'G#']
scale = [ '', 'm',  '7',  'maj7', '6', 'm6', '5', '9', 'm9', 'maj9', '11', 'm11', '13', 'm13', 'add2','11dim9','13dim11','13dim9','6/9','6aug5', '6dim5', '7#5', '7#9', '7+5','7-5','7-9', '7aug', '7aug5', '7b5', '7b9','7dim5', '7dim9', '7sus', '7sus2', '9aug5', '9dim5','9sus', 'add2','add4','add9', '6add9', 'aug','dim','dim11','dim13','dim7','dim9','m11dim9','m13dim11','m13dim9','m6','m7','m7b5','m7dim5','m7dim9','m9','maj11','maj13','maj9','mb5','mdim11','mdim13','mdim9','mmaj7','sus','sus2']

randroot = random.randint(0,len(root)-1)
randscale = random.randint(0,len(scale)-1)
chord = root[randroot]+scale[randscale]

chordarrayindex = 0
chordarray = []
for i in range(1000):
        randroot = random.randint(0,len(root)-1)
        randscale = random.randint(0,len(scale)-1)
        chord = root[randroot]+scale[randscale]
        chordarray.append(chord)


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

def reset(sender):
        view.remove_subview(chordtxt)
        global chordarrayindex
        chordarrayindex = chordarrayindex + 1
        chordtxt.text = chordarray[chordarrayindex]
        view.add_subview(chordtxt)


chordtxt.text = chordarray[chordarrayindex]
chordtxt.font = ('Courier', 30)
chordtxt.border_color = '#198054'
chordtxt.border_width = 5
chordtxt.frame = (90,120,200,75)
chordtxt.alignment = ui.ALIGN_CENTER


def quit(sender):
        view.close()


quitbutton = ui.Button(title = 'QUIT')
quitbutton.frame = (140,250,100,50)
quitbutton.border_color = '#0000ff'
quitbutton.border_width = 10
quitbutton.action = quit   


resetbutton = ui.Button(title = 'GENERATE')
resetbutton.frame = (140, 200, 100, 50)
resetbutton.border_color = '#0000ff'
resetbutton.border_width = 10
resetbutton.action = reset

quitbuttonminor = ui.Button(title = 'EXIT')
quitbuttonminor.frame = (140, 200, 100, 50)
quitbuttonminor.border_color = '#0000ff'
quitbuttonminor.border_width = 10

def minorquit(sender):
         view.remove_subview(quitbuttonminor)
         view.remove_subview(minor_lab)
         view.add_subview(chordtxt)
         view.add_subview(resetbutton)
         view.add_subview(quitbutton)
         view.add_subview(minorbutton)

quitbuttonminor.action = minorquit

minor_lab = ui.Label(text = minor_txt)
minor_lab.frame=(20,30,400,100)

def minor(sender):
        view.add_subview(minor_lab)
        view.add_subview(quitbuttonminor)
        view.remove_subview(chordtxt)
        view.remove_subview(quitbutton)
        view.remove_subview(resetbutton)
        view.remove_subview(minorbutton)

minorbutton = ui.Button(title = 'm (minor)')
minorbutton.frame = (50, 330, 100, 50)
minorbutton.border_color = '#0000ff'
minorbutton.border_width = 5 
minorbutton.action = minor

view.add_subview(chordtxt)
view.add_subview(resetbutton)
view.add_subview(quitbutton)
view.add_subview(minorbutton)
view.present(hide_title_bar=True
