import random
import ui 

root = ['A', 'Ab', 'A#', 'B', 'Bb', 'C', 'C#', 'D','Db', 'D#', 'E','Eb', 'F', 'F#', 'G', 'Gb', 'G#']

scale = [ '', '-','°','ø','b5', 'sus2','sus4','sus2b5','add2','add9','madd2','madd9','-2', 'sus2b5','6','-6','6/9','△7sus2','△7sus','maj7sus','△7sus24', '7#9','△7#9', '-7#9','7b9','△7b9','-7b9','-△7b9','+△7b9','+7b9','Øb9','°9','°b9','+7#9','△11','-11','-△11','7#9#11','11','△13','-13','13','-△13', '7', '△7','-#7','-△7','-7','+7','+△7','7#5','7+5','ø','-7b5','°7','7b5']

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

major_txt = 'root, major third, perfect fifth. EX: C'      
minor_txt = 'root, minor third, perfect fifth. EX: C-'
dom_txt = 'root, major third, pefect fifth, minor seventh, (add 9), (add 9,11), (add 9,11,13). EX: C13'
major_7_9_11_13_txt = 'root, major third, perfect fifth, major seventh, (add 9), (add 9+11), (add 9+11+13). EX: C△13'
add_txt = 'take the root triad and add the desired note in the scale. EX: Cadd2'
sus_txt = 'root add"2,4,24" perfect fifth. EX: Csus2, Note: Csus is implied Csus4.'
aug_txt = 'root, major third, augmented fifth. EX: C+'
dim_txt = 'root, minor third, flattened fifth. EX: C°'
halfdim_txt = 'root, minor third, flattened fifth, minor seventh. EX: Cø'
sharp_flat_txt = 'sharp (#) or flat (b) the desired note and add it to the root triad. EX: Cb5'
minor_third_txt = 'An interval consisting of three semitones. '
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
        view.remove_subview(augbutton)
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
        view.remove_subview(majorbutton)
        view.remove_subview(susbutton)
        view.remove_subview(halfdimbutton)

def add_subview_all(sender):
        view.add_subview(chordtxt)
        view.add_subview(quitbutton)
        view.add_subview(resetbutton)
        view.add_subview(minorbutton)
        view.add_subview(dombutton)
        view.add_subview(majbutton)
        view.add_subview(addbutton)
        view.add_subview(augbutton)
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
        view.add_subview(majorbutton)
        view.add_subview(susbutton)
        view.add_subview(halfdimbutton)

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
chordtxt.frame = (90,40,200,75)
chordtxt.alignment = ui.ALIGN_CENTER

def quit(sender):
        view.close()

quitbutton = ui.Button(title = 'QUIT')
quitbutton.frame = (140,170,100,50)
quitbutton.border_color = '#0000ff'
quitbutton.border_width = 10
quitbutton.action = quit   

resetbutton = ui.Button(title = 'GENERATE')
resetbutton.frame = (140, 120, 100, 50)
resetbutton.border_color = '#0000ff'
resetbutton.border_width = 10
resetbutton.action = reset

quitbuttonmajor = ui.Button(title = 'EXIT')
quitbuttonmajor.frame = (140, 200, 100, 50)
quitbuttonmajor.border_color = '#0000ff'
quitbuttonmajor.border_width = 10

def majorquit(sender):
         view.remove_subview(quitbuttonmajor)
         view.remove_subview(major_lab)
         add_subview_all(sender)

quitbuttonmajor.action = majorquit

major_lab = ui.Label(text = major_txt)
major_lab.frame=(20,30,400,100)

def major(sender):
        view.add_subview(major_lab)
        view.add_subview(quitbuttonmajor)
        remove_subview_all(sender)

majorbutton = ui.Button(title = 'M (major)')
majorbutton.frame = (20, 200, 160, 50)
majorbutton.border_color = '#0000ff'
majorbutton.border_width = 5 
majorbutton.action = major

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

minorbutton = ui.Button(title = '- (minor)')
minorbutton.frame = (20, 250, 160, 50)
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
dombutton.frame = (20, 300, 160, 50)
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

def maj(sender):                                                                    
        view.add_subview(maj_lab)
        view.add_subview(quitbuttonmaj)
        remove_subview_all(sender)

majbutton = ui.Button(title = '△7,9,11,13 (major 7)')
majbutton.frame = (20, 350, 160, 50)
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

def add(sender):                                                                      
        view.add_subview(add_lab)
        view.add_subview(quitbuttonadd)
        remove_subview_all(sender)

addbutton = ui.Button(title = 'add')
addbutton.frame = (20, 400, 160, 50)
addbutton.border_color = '#0000ff'
addbutton.border_width = 5 
addbutton.action = add

quitbuttonsus = ui.Button(title = 'EXIT')
quitbuttonsus.frame = (140, 200, 100, 50)
quitbuttonsus.border_color = '#0000ff'
quitbuttonsus.border_width = 10

def susquit(sender):
         view.remove_subview(quitbuttonsus)
         view.remove_subview(sus_lab)
         add_subview_all(sender)

quitbuttonsus.action = susquit

sus_lab = ui.Label(text = sus_txt, number_of_lines = 0)
sus_lab.frame=(20,30,350,100)

def sus(sender):                                                                      
        view.sus_subview(sus_lab)
        view.sus_subview(quitbuttonsus)
        remove_subview_all(sender)

susbutton = ui.Button(title = 'sus (suspended)')
susbutton.frame = (20, 650, 160, 50)
susbutton.border_color = '#0000ff'
susbutton.border_width = 5 
susbutton.action = sus

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

def aug(sender):                                                                      
        view.add_subview(aug_lab)
        view.add_subview(quitbuttonaug)
        remove_subview_all(sender)

augbutton = ui.Button(title = '+ (augmented)')
augbutton.frame = (20, 450, 160, 50)
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

def dim(sender):                                                                      
        view.add_subview(dim_lab)
        view.add_subview(quitbuttondim)
        remove_subview_all(sender)

dimbutton = ui.Button(title = '° (diminished)')
dimbutton.frame = (20, 500, 160, 50)
dimbutton.border_color = '#0000ff'
dimbutton.border_width = 5 
dimbutton.action = dim

quitbuttonhalfdim = ui.Button(title = 'EXIT')
quitbuttonhalfdim.frame = (140, 200, 100, 50)
quitbuttonhalfdim.border_color = '#0000ff'
quitbuttonhalfdim.border_width = 10

def halfdimquit(sender):
         view.remove_subview(quitbuttonhalfdim)
         view.remove_subview(halfdim_lab)
         add_subview_all(sender)

quitbuttonhalfdim.action = halfdimquit

halfdim_lab = ui.Label(text = halfdim_txt, number_of_lines = 0)
halfdim_lab.frame=(20,30,350,100)

def halfdim(sender):                                                                      
        view.add_subview(halfdim_lab)
        view.add_subview(quitbuttonhalfdim)
        remove_subview_all(sender)

halfdimbutton = ui.Button(title = 'ø (half diminished)')
halfdimbutton.frame = (200, 650, 160, 50)
halfdimbutton.border_color = '#0000ff'
halfdimbutton.border_width = 5 
halfdimbutton.action = halfdim

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

def sharpflat(sender):                                                                      
        view.add_subview(sharpflat_lab)
        view.add_subview(quitbuttonsharpflat)
        remove_subview_all(sender)

sharpflatbutton = ui.Button(title = '#,b (sharp,flat)')
sharpflatbutton.frame = (20, 550, 160, 50)
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

def minorthird(sender):                                                                       
        view.add_subview(minorthird_lab)
        view.add_subview(quitbuttonminorthird)
        remove_subview_all(sender)

minorthirdbutton = ui.Button(title = 'minor third')
minorthirdbutton.frame = (20, 600, 160, 50)
minorthirdbutton.border_color = '#0000ff'
minorthirdbutton.border_width = 5 
minorthirdbutton.action = minorthird 

quitbuttonmajorthird = ui.Button(title = 'EXIT')
quitbuttonmajorthird.frame = (140, 200, 100, 50)
quitbuttonmajorthird.border_color = '#0000ff'
quitbuttonmajorthird.border_width = 10

def majorthirdquit(sender):
         view.remove_subview(quitbuttonmajorthird)
         view.remove_subview(majorthird_lab)
         add_subview_all(sender)

quitbuttonmajorthird.action = majorthirdquit

majorthird_lab = ui.Label(text = major_third_txt, number_of_lines = 0)
majorthird_lab.frame=(20,30,350,100)

def majorthird(sender):                                                                       
        view.add_subview(majorthird_lab)
        view.add_subview(quitbuttonmajorthird)
        remove_subview_all(sender)

majorthirdbutton = ui.Button(title = 'major third')
majorthirdbutton.frame = (200, 250, 160, 50)
majorthirdbutton.border_color = '#0000ff'
majorthirdbutton.border_width = 5 
majorthirdbutton.action = majorthird 

quitbuttonperfectfourth = ui.Button(title = 'EXIT')
quitbuttonperfectfourth.frame = (140, 200, 100, 50)
quitbuttonperfectfourth.border_color = '#0000ff'
quitbuttonperfectfourth.border_width = 10

def perfectfourthdquit(sender):
         view.remove_subview(quitbuttonperfectfourth)
         view.remove_subview(perfectfourth_lab)
         add_subview_all(sender)

quitbuttonperfectfourth.action = perfectfourthdquit

perfectfourth_lab = ui.Label(text = perfect_fourth_txt, number_of_lines = 0)
perfectfourth_lab.frame=(20,30,350,100)

def perfectfourth(sender):                                                                       
        view.add_subview(perfectfourth_lab)
        view.add_subview(quitbuttonperfectfourth)
        remove_subview_all(sender)

perfectfourthbutton = ui.Button(title = 'perfect fourth')
perfectfourthbutton.frame = (200, 300, 160, 50)
perfectfourthbutton.border_color = '#0000ff'
perfectfourthbutton.border_width = 5 
perfectfourthbutton.action = perfectfourth

quitbuttonflatfifth = ui.Button(title = 'EXIT')
quitbuttonflatfifth.frame = (140, 200, 100, 50)
quitbuttonflatfifth.border_color = '#0000ff'
quitbuttonflatfifth.border_width = 10

def flatfifthquit(sender):
         view.remove_subview(quitbuttonflatfifth)
         view.remove_subview(flatfifth_lab)
         add_subview_all(sender)

quitbuttonflatfifth.action = flatfifthquit

flatfifth_lab = ui.Label(text = flattened_fifth_txt, number_of_lines = 0)
flatfifth_lab.frame=(20,30,350,100)

def flatfifth(sender):                                                                       
        view.add_subview(flatfifth_lab)
        view.add_subview(quitbuttonflatfifth)
        remove_subview_all(sender)

flatfifthbutton = ui.Button(title = 'flattened fifth')
flatfifthbutton.frame = (200, 350, 160, 50)
flatfifthbutton.border_color = '#0000ff'
flatfifthbutton.border_width = 5 
flatfifthbutton.action = flatfifth 

quitbuttonperfectfifth = ui.Button(title = 'EXIT')
quitbuttonperfectfifth.frame = (140, 200, 100, 50)
quitbuttonperfectfifth.border_color = '#0000ff'
quitbuttonperfectfifth.border_width = 10

def perfectfifthquit(sender):
         view.remove_subview(quitbuttonperfectfifth)
         view.remove_subview(perfectfifth_lab)
         add_subview_all(sender)

quitbuttonperfectfifth.action = perfectfifthquit

perfectfifth_lab = ui.Label(text = perfect_fifth_txt, number_of_lines = 0)
perfectfifth_lab.frame=(20,30,350,100)

def perfectfifth(sender):                                                                       
        view.add_subview(perfectfifth_lab)
        view.add_subview(quitbuttonperfectfifth)
        remove_subview_all(sender)

perfectfifthbutton = ui.Button(title = 'perfect fifth')
perfectfifthbutton.frame = (200, 400, 160, 50)
perfectfifthbutton.border_color = '#0000ff'
perfectfifthbutton.border_width = 5 
perfectfifthbutton.action = perfectfifth 

quitbuttonaugfifth = ui.Button(title = 'EXIT')
quitbuttonaugfifth.frame = (140, 200, 100, 50)
quitbuttonaugfifth.border_color = '#0000ff'
quitbuttonaugfifth.border_width = 10

def augfifthquit(sender):
         view.remove_subview(quitbuttonaugfifth)
         view.remove_subview(augfifth_lab)
         add_subview_all(sender)

quitbuttonaugfifth.action = augfifthquit

augfifth_lab = ui.Label(text = augmented_fifth_txt, number_of_lines = 0)
augfifth_lab.frame=(20,30,350,100)

def augfifth(sender):                                                                     
        view.add_subview(augfifth_lab)
        view.add_subview(quitbuttonaugfifth)
        remove_subview_all(sender)

augfifthbutton = ui.Button(title = 'augmented fifth')
augfifthbutton.frame = (200, 450, 160, 50)
augfifthbutton.border_color = '#0000ff'
augfifthbutton.border_width = 5 
augfifthbutton.action = augfifth 

quitbuttonsixth = ui.Button(title = 'EXIT')
quitbuttonsixth.frame = (140, 200, 100, 50)
quitbuttonsixth.border_color = '#0000ff'
quitbuttonsixth.border_width = 10

def sixthquit(sender):
         view.remove_subview(quitbuttonsixth)
         view.remove_subview(sixth_lab)
         add_subview_all(sender)

quitbuttonsixth.action = sixthquit

sixth_lab = ui.Label(text = sixth_txt, number_of_lines = 0)
sixth_lab.frame=(20,30,350,100)

def sixth(sender):                                                                      
        view.add_subview(sixth_lab)
        view.add_subview(quitbuttonsixth)
        remove_subview_all(sender)

sixthbutton = ui.Button(title = 'sixth')
sixthbutton.frame = (200, 500, 160, 50)
sixthbutton.border_color = '#0000ff'
sixthbutton.border_width = 5 
sixthbutton.action = sixth

quitbuttonminorseventh = ui.Button(title = 'EXIT')
quitbuttonminorseventh.frame = (140, 200, 100, 50)
quitbuttonminorseventh.border_color = '#0000ff'
quitbuttonminorseventh.border_width = 10

def minorseventhquit(sender):
         view.remove_subview(quitbuttonminorseventh)
         view.remove_subview(minorseventh_lab)
         add_subview_all(sender)

quitbuttonminorseventh.action = minorseventhquit

minorseventh_lab = ui.Label(text = minor_seventh_txt, number_of_lines = 0)
minorseventh_lab.frame=(20,30,350,100)

def minorseventh(sender):                                                                      
        view.add_subview(minorseventh_lab)
        view.add_subview(quitbuttonminorseventh)
        remove_subview_all(sender)

minorseventhbutton = ui.Button(title = 'minor seventh')
minorseventhbutton.frame = (200, 550, 160, 50)
minorseventhbutton.border_color = '#0000ff'
minorseventhbutton.border_width = 5 
minorseventhbutton.action = minorseventh

quitbuttonmajorseventh = ui.Button(title = 'EXIT')
quitbuttonmajorseventh.frame = (140, 200, 100, 50)
quitbuttonmajorseventh.border_color = '#0000ff'
quitbuttonmajorseventh.border_width = 10

def majorseventhquit(sender):
         view.remove_subview(quitbuttonmajorseventh)
         view.remove_subview(majorseventh_lab)
         add_subview_all(sender)

quitbuttonmajorseventh.action = majorseventhquit

majorseventh_lab = ui.Label(text = major_seventh_txt, number_of_lines = 0)
majorseventh_lab.frame=(20,30,350,100)

def majorseventh(sender):                                                                      
        view.add_subview(majorseventh_lab)
        view.add_subview(quitbuttonmajorseventh)
        remove_subview_all(sender)

majorseventhbutton = ui.Button(title = 'major seventh')
majorseventhbutton.frame = (200, 600, 160, 50)
majorseventhbutton.border_color = '#0000ff'
majorseventhbutton.border_width = 5 
majorseventhbutton.action = majorseventh

view.add_subview(chordtxt)
view.add_subview(quitbutton)
view.add_subview(resetbutton)
view.add_subview(minorbutton)
view.add_subview(dombutton)
view.add_subview(majbutton)
view.add_subview(addbutton)
view.add_subview(augbutton)
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
view.add_subview(majorbutton)
view.add_subview(susbutton)
view.add_subview(halfdimbutton)
view.present(hide_title_bar = True)
