import random
import Tkinter as tk 

root = ['A', 'Ab', 'A#', 'B', 'Bb', 'C', 'C#', 'D','Db', 'D#', 'E','Eb', 'F', 'F#', 'G', 'Gb', 'G#']
scale = [ '', 'm',  '7',  'maj7', '6', 'm6', '5', '9', 'm9', 'maj9', '11', 'm11', '13', 'm13', 'add2', '11dim9','13dim11','13dim9','6/9','6aug5', '6dim5', '7#5', '7#9', '7+5','7-5','7-9', '7aug', '7aug5', '7b5', '7b9','7dim5', '7dim9', '7sus', '7sus2', '9aug5', '9dim5','9sus', 'add2','add4','add9', '6add9', 'aug','dim','dim11','dim13','dim7','dim9','m11dim9','m13dim11','m13dim9','m6','m7','m7b5','m7dim5','m7dim9','m9','maj11','maj13','maj9','mb5','mdim11','mdim13','mdim9','mmaj7','sus','sus2']
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

root = tk.Tk()

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

def refresh():
    global chordtxt
    chordtxt.pack_forget()
    global chordarrayindex
    chordarrayindex = chordarrayindex + 1
    chord = chordarray[chordarrayindex]
    chordtxt = tk.Label(root, width=25, height=3, text=chord, fg='blue',font='Verdana 14 bold')
    chordtxt.pack_configure(before = resetbutton) 

resetbutton = tk.Button(root, width=50, height=3, text='GENERATE', command=refresh)
resetbutton.pack()

chordtxt = tk.Label(root, width=25, height=3, text=chord, fg='blue',font='Verdana 14 bold')
chordtxt.pack_configure(before=resetbutton)

quitbutton = tk.Button(root, width=50, height=3, text='QUIT', command=root.destroy)
quitbutton.pack()

def create_window_minor():
    window = tk.Toplevel(root)
    definition = tk.Label(window, text = minor_txt)
    definition.pack()
    exit = tk.Button(window, text='EXIT', command=window.destroy)
    exit.pack()

minor = tk.Button(root, text='m (minor)', command=create_window_minor)
minor.pack()

def create_window_dom():
    window = tk.Toplevel(root)
    definition = tk.Label(window, text = dom_txt)
    definition.pack()
    exit = tk.Button(window, text='EXIT', command=window.destroy)
    exit.pack()

dom = tk.Button(root, text='7,9,11,13 (dominant 7,9,11,13)', command=create_window_dom)
dom.pack()

def create_window_maj():
    window = tk.Toplevel(root)
    definition = tk.Label(window, text = major_7_9_11_13_txt)
    definition.pack()
    exit = tk.Button(window, text='EXIT', command=window.destroy)
    exit.pack()

major_7_9_11_13 = tk.Button(root, text='maj7,9,11,13 (major 7)', command=create_window_maj)
major_7_9_11_13.pack()

def create_window_add():
    window = tk.Toplevel(root)
    definition = tk.Label(window, text = add_txt)
    definition.pack()
    exit = tk.Button(window, text='EXIT', command=window.destroy)
    exit.pack()
    

add = tk.Button(root, text='add', command=create_window_add)
add.pack()

def create_window_aug():
    window = tk.Toplevel(root)
    definition = tk.Label(window, text = aug_txt)
    definition.pack()
    exit = tk.Button(window, text='EXIT', command=window.destroy)
    exit.pack()

aug = tk.Button(root, text='aug (augmented)', command=create_window_aug)
aug.pack()

def create_window_dim():
    window = tk.Toplevel(root)
    definition = tk.Label(window, text = dim_txt)
    definition.pack()
    exit = tk.Button(window, text='EXIT', command=window.destroy)
    exit.pack()

dim = tk.Button(root, text='dim (diminished)', command=create_window_dim)
dim.pack()

def create_window_sharp_flat():
    window = tk.Toplevel(root)
    definition = tk.Label(window, text = sharp_flat_txt)
    definition.pack()
    exit = tk.Button(window, text='EXIT', command=window.destroy)
    exit.pack()

sharp_flat = tk.Button(root, text= '+,-,#,b (sharp,flat)', command=create_window_sharp_flat)
sharp_flat.pack()

def create_window_minor_third():
    window = tk.Toplevel(root)
    definition = tk.Label(window, text = minor_third_txt)
    definition.pack()
    exit = tk.Button(window, text='EXIT', command=window.destroy)
    exit.pack()

minor_third = tk.Button(root, text='minor third', command=create_window_minor_third)
minor_third.pack()

def create_window_major_third():
    window = tk.Toplevel(root)
    definition = tk.Label(window, text = major_third_txt)
    definition.pack()
    exit = tk.Button(window, text='EXIT', command=window.destroy)
    exit.pack()

major_third = tk.Button(root, text='major third', command=create_window_major_third)
major_third.pack()

def create_window_perfect_fourth():
    window = tk.Toplevel(root)
    definition = tk.Label(window, text = perfect_fourth_txt)
    definition.pack()
    exit = tk.Button(window, text='EXIT', command=window.destroy)
    exit.pack()

perfect_fourth = tk.Button(root, text='perfect fourth', command=create_window_perfect_fourth)
perfect_fourth.pack()

def create_window_flattened_fifth():
    window = tk.Toplevel(root)
    definition = tk.Label(window, text = flattened_fifth_txt)
    definition.pack()
    exit = tk.Button(window, text='EXIT', command=window.destroy)
    exit.pack()

flattened_fifth = tk.Button(root, text='flattened fifth', command=create_window_flattened_fifth)
flattened_fifth.pack()

def create_window_perfect_fifth():
    window = tk.Toplevel(root)
    definition = tk.Label(window, text = perfect_fifth_txt)
    definition.pack()
    exit = tk.Button(window, text='EXIT', command=window.destroy)
    exit.pack()

perfect_fifth = tk.Button(root, text='perfect fifth', command=create_window_perfect_fifth)
perfect_fifth.pack()

def create_window_augmented_fifth():
    window = tk.Toplevel(root)
    definition = tk.Label(window, text = augmented_fifth_txt)
    definition.pack()
    exit = tk.Button(window, text='EXIT', command=window.destroy)
    exit.pack()

augmented_fifth = tk.Button(root, text='augmented fifth', command=create_window_augmented_fifth)
augmented_fifth.pack()

def create_window_sixth():
    window = tk.Toplevel(root)
    definition = tk.Label(window, text = sixth_txt)
    definition.pack()
    exit = tk.Button(window, text='EXIT', command=window.destroy)
    exit.pack()

sixth = tk.Button(root, text='sixth', command=create_window_sixth)
sixth.pack()

def create_window_minor_seventh():
    window = tk.Toplevel(root)
    definition = tk.Label(window, text = minor_seventh_txt)
    definition.pack()
    exit = tk.Button(window, text='EXIT', command=window.destroy)
    exit.pack()

minor_seventh = tk.Button(root, text='minor seventh', command=create_window_minor_seventh)
minor_seventh.pack()

def create_window_major_seventh():
    window = tk.Toplevel(root)
    definition = tk.Label(window, text = major_seventh_txt)
    definition.pack()
    exit = tk.Button(window, text='EXIT', command=window.destroy)
    exit.pack()

major_seventh = tk.Button(root, text='major seventh', command=create_window_major_seventh)
major_seventh.pack()

root.mainloop()



