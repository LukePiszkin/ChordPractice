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

def remove_subview_all(sender):
        view.remove_subview(chordtxt)
        view.remove_subview(quitbutton)
        view.remove_subview(resetbutton)
        view.remove_subview(minorbutton)
        view.remove_subview(dombutton)
        view.remove_subview(majbutton)
        view.remove_subview(addbutton)
        view.remove_subview(dimbutton)
        view.remove_subview(sharpflatbutton)
        view.remove_subview(minorthirdbutton)
        view.remove_subview(majorthirdbutton)
        view.remove_subview(perfectfourthbutton)
        view.remove_subview(flatfifthbutton)
        view.remove_subview(perfectfifthbutton)
        view.remove_subview(augfifthbutton)
        view.remove_subview(sixthbutton)
        view.remove_subview(minorseventhbutton)
        view.remove_subview(majorseventhbutton)

def add_subview_all(sender):
        view.add_subview(chordtxt)
        view.add_subview(quitbutton)
        view.add_subview(resetbutton)
        view.add_subview(minorbutton)
        view.add_subview(dombutton)
        view.add_subview(majbutton)
        view.add_subview(addbutton)
        view.add_subview(dimbutton)
        view.add_subview(sharpflatbutton)
        view.add_subview(minorthirdbutton)
        view.add_subview(majorthirdbutton)
        view.add_subview(perfectfourthbutton)
        view.add_subview(flatfifthbutton)
        view.add_subview(perfectfifthbutton)
        view.add_subview(augfifthbutton)
        view.add_subview(sixthbutton)
        view.add_subview(minorseventhbutton)
        view.add_subview(majorseventhbutton)


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
         add_subview_all(sender)

quitbuttonminor.action = minorquit

minor_lab = ui.Label(text = minor_txt)
minor_lab.frame=(20,30,400,100)

def minor(sender):
        view.add_subview(minor_lab)
        view.add_subview(quitbuttonminor)
        remove_subview_all(sender)

minorbutton = ui.Button(title = 'm (minor)')
minorbutton.frame = (50, 330, 100, 50)
minorbutton.border_color = '#0000ff'
minorbutton.border_width = 5 
minorbutton.action = minor

quitbuttondom = ui.Button(title = 'EXIT')
quitbuttondom.frame = (140, 200, 100, 50)
quitbuttondom.border_color = '#0000ff'
quitbuttondom.border_width = 10

def domquit(sender):
         view.remove_subview(quitbuttondom)
         view.remove_subview(dom_lab)
         add_subview_all(sender)

quitbuttondom.action = domquit

dom_lab = ui.Label(text = dom_txt, number_of_lines = 0)
dom_lab.frame=(20,30,350,100)

def dom(sender):
        view.add_subview(dom_lab)
        view.add_subview(quitbuttondom)
        remove_subview_all(sender)


dombutton = ui.Button(title = '7,9,11,13 (dominant)')
dombutton.frame = (25, 380, 150, 50)
dombutton.border_color = '#0000ff'
dombutton.border_width = 5 
dombutton.action = dom

quitbuttonmaj = ui.Button(title = 'EXIT')
quitbuttonmaj.frame = (140, 200, 100, 50)
quitbuttonmaj.border_color = '#0000ff'
quitbuttonmaj.border_width = 10

def majquit(sender):
         view.remove_subview(quitbuttonmaj)
         view.remove_subview(maj_lab)
         add_subview_all(sender)

quitbuttonmaj.action = majquit

maj_lab = ui.Label(text = major_7_9_11_13_txt, number_of_lines = 0)
maj_lab.frame=(20,30,350,100)

def maj(sender):                                                                     ender):
        view.add_subview(maj_lab)
        view.add_subview(quitbuttonmaj)
        remove_subview_all(sender)

majbutton = ui.Button(title = 'maj7,9,11,13 (major 7)')
majbutton.frame = (20, 430, 160, 50)
majbutton.border_color = '#0000ff'
majbutton.border_width = 5 
majbutton.action = maj

quitbuttonadd = ui.Button(title = 'EXIT')
quitbuttonadd.frame = (140, 200, 100, 50)
quitbuttonadd.border_color = '#0000ff'
quitbuttonadd.border_width = 10

def addquit(sender):
         view.remove_subview(quitbuttonadd)
         view.remove_subview(add_lab)
         add_subview_all(sender)
         
quitbuttonadd.action = addquit

add_lab = ui.Label(text = add_txt, number_of_lines = 0)
add_lab.frame=(20,30,350,100)

def add(sender):                                                                       ender):
        view.add_subview(add_lab)
        view.add_subview(quitbuttonadd)
        remove_subview_all(sender)

addbutton = ui.Button(title = 'add')
addbutton.frame = (20, 480, 160, 50)
addbutton.border_color = '#0000ff'
addbutton.border_width = 5 
addbutton.action = add

quitbuttonaug = ui.Button(title = 'EXIT')
quitbuttonaug.frame = (140, 200, 100, 50)
quitbuttonaug.border_color = '#0000ff'
quitbuttonaug.border_width = 10

def augquit(sender):
         view.remove_subview(quitbuttonaug)
         view.remove_subview(aug_lab)
         add_subview_all(sender)
         
quitbuttonaug.action = augquit

aug_lab = ui.Label(text = aug_txt, number_of_lines = 0)
aug_lab.frame=(20,30,350,100)

def aug(sender):                                                                       ender):
        view.add_subview(aug_lab)
        view.add_subview(quitbuttonaug)
        remove_subview_all(sender)

augbutton = ui.Button(title = 'aug (augmented)')
augbutton.frame = (20, 530, 160, 50)
augbutton.border_color = '#0000ff'
augbutton.border_width = 5 
augbutton.action = aug

quitbuttondim = ui.Button(title = 'EXIT')
quitbuttondim.frame = (140, 200, 100, 50)
quitbuttondim.border_color = '#0000ff'
quitbuttondim.border_width = 10

def dimquit(sender):
         view.remove_subview(quitbuttondim)
         view.remove_subview(dim_lab)
         add_subview_all(sender)
         
quitbuttondim.action = dimquit

dim_lab = ui.Label(text = dim_txt, number_of_lines = 0)
dim_lab.frame=(20,30,350,100)

def dim(sender):                                                                       ender):
        view.add_subview(dim_lab)
        view.add_subview(quitbuttondim)
        remove_subview_all(sender)

dimbutton = ui.Button(title = 'dim (diminished)')
dimbutton.frame = (20, 580, 160, 50)
dimbutton.border_color = '#0000ff'
dimbutton.border_width = 5 
dimbutton.action = dim

quitbuttonsharpflat = ui.Button(title = 'EXIT')
quitbuttonsharpflat.frame = (140, 200, 100, 50)
quitbuttonsharpflat.border_color = '#0000ff'
quitbuttonsharpflat.border_width = 10

def sharpflatquit(sender):
         view.remove_subview(quitbuttonsharpflat)
         view.remove_subview(sharpflat_lab)
         add_subview_all(sender)
         
quitbuttonsharpflat.action = sharpflatquit

sharpflat_lab = ui.Label(text = sharp_flat_txt, number_of_lines = 0)
sharpflat_lab.frame=(20,30,350,100)

def sharpflat(sender):                                                                       ender):
        view.add_subview(sharpflat_lab)
        view.add_subview(quitbuttonsharpflat)
        remove_subview_all(sender)

sharpflatbutton = ui.Button(title = 'dim (diminished)')
sharpflatbutton.frame = (20, 630, 160, 50)
sharpflatbutton.border_color = '#0000ff'
sharpflatbutton.border_width = 5 
sharpflatbutton.action = sharpflat 

quitbuttonminorthird = ui.Button(title = 'EXIT')
quitbuttonminorthird.frame = (140, 200, 100, 50)
quitbuttonminorthird.border_color = '#0000ff'
quitbuttonminorthird.border_width = 10

def minorthirdquit(sender):
         view.remove_subview(quitbuttonminorthird)
         view.remove_subview(minorthird_lab)
         add_subview_all(sender)
         
quitbuttonminorthird.action = minorthirdquit

minorthird_lab = ui.Label(text = minor_third_txt, number_of_lines = 0)
minorthird_lab.frame=(20,30,350,100)

def minorthird(sender):                                                                       ender):
        view.add_subview(minorthird_lab)
        view.add_subview(quitbuttonminorthird)
        remove_subview_all(sender)

minorthirdbutton = ui.Button(title = 'minor third')
minorthirdbutton.frame = (20, 630, 160, 50)
minorthirdbutton.border_color = '#0000ff'
minorthirdbutton.border_width = 5 
minorthirdbutton.action = minorthird 

add_subview_all(sender)
view.present(hide_title_bar = True)

