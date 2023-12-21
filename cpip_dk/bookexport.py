Password Picker (page 52)
import random
import string
adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'fluffy', 
'white', 'proud', 'brave'] 
nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon', 'hammer', 'duck', 'panda'] 
print('Welcome to Password Picker!') 
while True: adjective = random.choice(adjectives) noun = random.choice(nouns) number = random.randrange(0, 100) special_char = random.choice(string.punctuation)
 password = adjective + noun + str(number) + special_char print('Your new password is: %s' % password)
 response = input('Would you like another password? Type y or n: ') if response == 'n': break 

Nine Lives (page 60) 
import random 
lives = 9 words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane'] secret_word = random.choice(words) clue = list('?????') heart_symbol = u'\u2764' guessed_word_correctly = False 
def update_clue(guessed_letter, secret_word, clue): index = 0 while index < len(secret_word): 
if guessed_letter == secret_word[index]: clue[index] = guessed_letter index = index + 1 
while lives > 0: print(clue) print('Lives left: ' + heart_symbol * lives) guess = input('Guess a letter or the whole word: ')
 if guess == secret_word: guessed_word_correctly = True break
 if guess in secret_word: update_clue(guess, secret_word, clue) else: 
print('Incorrect. You lose a life') lives = lives � 1 
if guessed_word_correctly: print('You won! The secret word was ' \ 
+
 secret_word) 

else: print('You lost! The secret word was ' \ 

+
 secret_word) 



Robot Builder (page 72) 
import turtle as t 
def rectangle(horizontal, vertical, color): t.pendown() t.pensize(1) t.color(color) t.begin_fill() for counter in range(1, 3):
 t.forward(horizontal) t.right(90) t.forward(vertical) t.right(90)
 t.end_fill() t.penup() 
t.penup() t.speed('slow') t.bgcolor('Dodger blue') 
# feet t.goto(�100, �150) rectangle(50, 20, 'blue') t.goto(�30, �150) rectangle(50, 20, 'blue') 
# legs t.goto(�25, �50) rectangle(15, 100, 'grey') t.goto(�55, �50) rectangle(�15, 100, 'grey') 
# body t.goto(�90, 100) rectangle(100, 150, 'red') 
# arms t.goto(�150, 70) rectangle(60, 15, 'grey') 
t.goto(�150, 110) rectangle(15, 40, 'grey') 
t.goto(10, 70) rectangle(60, 15, 'grey') t.goto(55, 110) rectangle(15, 40, 'grey') 
# neck t.goto(�50, 120) rectangle(15, 20, 'grey') 
# head t.goto(�85, 170) rectangle(80, 50, 'red') 
# eyes t.goto(�60, 160) rectangle(30, 10, 'white') t.goto(�55, 155) rectangle(5, 5, 'black') t.goto(�40, 155) rectangle(5, 5, 'black') 
# mouth t.goto(�65, 135) rectangle(40, 5, 'black') 
t.hideturtle() 

Kaleido-spiral (page 82) 
import turtle from itertools import cycle 
colors = cycle(['red', 'orange', 'yellow', \ 'green', 'blue', 'purple']) 
def draw_circle(size, angle, shift): turtle.pencolor(next(colors)) turtle.circle(size) turtle.right(angle) turtle.forward(shift) draw_circle(size + 5, angle + 1, shift + 
1) 
turtle.bgcolor('black') turtle.speed('fast') turtle.pensize(4) draw_circle(30, 0, 1) 

Starry Night (page 90) 
import turtle as t from random import randint, random 
def draw_star(points, size, col, x, y): t.penup() t.goto(x, y) t.pendown angle = 180 � (180 / points) t.color(col) t.begin_fill() for i in range(points):
 t.forward(size) t.right(angle) t.end_fill() 
# Main code t.Screen().bgcolor('dark blue') 
while True: ranPts = randint(2, 5) * 2 + 1 ranSize = randint(10, 50) ranCol = (random(), random(), random()) ranX = randint(�350, 300) ranY = randint(�250, 250)
 draw_star(ranPts, ranSize, ranCol, ranX, ranY) 

Mutant Rainbow (page 98) 
import random import turtle as t 
def get_line_length(): choice = input('Enter line length (long, medium, short): ') if choice == 'long':
 line_length = 250 elif choice == 'medium': line_length = 200
 else: line_length = 100 return line_length 
def get_line_width(): choice = input('Enter line width (superthick, thick, thin): ') if choice == 'superthick':
 line_width = 40 elif choice == 'thick': line_width = 25 
else:
 line_width = 10
 return line_width 
def inside_window():
 left_limit = (�t.window_width() / 2) + 100
 right_limit = (t.window_width() / 2) � 100
 top_limit = (t.window_height() / 2) � 100
 bottom_limit = (�t.window_height() / 2) + 100
 (x, y) = t.pos()
 inside = left_limit < x < right_limit and bottom_limit < y < top_limit
 return inside 
def move_turtle(line_length):
 pen_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
 t.pencolor(random.choice(pen_colors))
 if inside_window():
 angle = random.randint(0, 180)
 t.right(angle)
 t.forward(line_length)
 else:
 t.backward(line_length) 
line_length = get_line_length() line_width = get_line_width() 
t.shape('turtle') t.fillcolor('green') t.bgcolor('black') t.speed('fastest') t.pensize(line_width) 
while True: move_turtle(line_length) 

Countdown Calendar (page 110) 
from tkinter import Tk, Canvas from datetime import date, datetime 
def get_events():
 list_events = []
 with open('events.txt') as file:
 for line in file:
 line = line.rstrip('\n')
 current_event = line.split(',')
 event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
 current_event[1] = event_date
 list_events.append(current_event)
 return list_events 
def days_between_dates(date1, date2): time_between = str(date1 � date2) number_of_days = time_between.split(' ') return number_of_days[0] 
root = Tk() c = Canvas(root, width=800, height=800, bg='black') c.pack() c.create_text(100, 50, anchor='w', fill='orange', font='Arial 28 bold underline', \
 text='My Countdown Calendar') 
events = get_events() today = date.today() 
vertical_space = 100 
for event in events: event_name = event[0] days_until = days_between_dates(event[1], today) display = 'It is %s days until %s' % (days_until, event_name) c.create_text(100, vertical_space, anchor='w', fill='lightblue', \
 font='Arial 28 bold', text=display)
 vertical_space = vertical_space + 30 

Ask the Expert (page 120) 
from tkinter import Tk, simpledialog, messagebox 
def read_from_file(): with open('capital_data.txt') as file:
 for line in file: line = line.rstrip('\n') country, city = line.split('/') the_world[country] = city 
def write_to_file(country_name, city_name): with open('capital_data.txt', 'a') as file: file.write('\n' + country_name + '/' + city_name) 
print('Ask the Expert � Capital Cities of the World') root = Tk() root.withdraw() the_world = {} 
read_from_file() 
while True: query_country = simpledialog.askstring('Country', 'Type the name of a country:')
 if query_country in the_world: 
result = the_world[query_country] messagebox.showinfo('Answer', 'The capital city of ' + query_country + ' is ' + result + '!') else:
 new_city = simpledialog.askstring('Teach me', 'I don\'t know! ' + 'What is the capital city of ' + query_country + '?')
 the_world[query_country] = new_city write_to_file(query_country, new_city) 
root.mainloop() 

Secret Messages (page 130) 
from tkinter import messagebox, simpledialog, Tk 
def is_even(number): return number % 2 == 0 
def get_even_letters(message): even_letters = [] for counter in range(0, len(message)):
 if is_even(counter): even_letters.append(message[counter]) return even_letters 
def get_odd_letters(message): odd_letters = [] for counter in range(0, len(message)):
 if not is_even(counter): odd_letters.append(message[counter]) return odd_letters 
def swap_letters(message): letter_list = [] if not is_even(len(message)):
 message = message + 'x' even_letters = get_even_letters(message) odd_letters = get_odd_letters(message) for counter in range(0, int(len(message)/2)):
 letter_list.append(odd_letters[counter])
 letter_list.append(even_letters[counter]) new_message = ''.join(letter_list) return new_message 
def get_task(): task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?') return task def get_message(): message = simpledialog.askstring('Message', 'Enter the secret message: ') return message 
root = Tk() 
while True: task = get_task() if task == 'encrypt':
 message = get_message() encrypted = swap_letters(message) messagebox.showinfo('Ciphertext of the secret message is:', encrypted)
 elif task == 'decrypt': message = get_message() decrypted = swap_letters(message) messagebox.showinfo('Plaintext of the secret message is:', decrypted)
 else: break root.mainloop() 

Screen Pet (page 142) 
from tkinter import HIDDEN, NORMAL, Tk, Canvas 
def toggle_eyes(): current_color = c.itemcget(eye_left, 'fill') new_color = c.body_color if current_color == 'white' else 'white' current_state = c.itemcget(pupil_left, 'state') new_state = NORMAL if current_state == HIDDEN else HIDDEN c.itemconfigure(pupil_left, state=new_state) c.itemconfigure(pupil_right, state=new_state) c.itemconfigure(eye_left, fill=new_color) c.itemconfigure(eye_right, fill=new_color) 
def blink(): toggle_eyes() root.after(250, toggle_eyes) root.after(3000, blink) 
def toggle_pupils():
 if not c.eyes_crossed: c.move(pupil_left, 10, �5) c.move(pupil_right, �10, �5) c.eyes_crossed = True
 else: c.move(pupil_left, �10, 5) c.move(pupil_right, 10, 5) c.eyes_crossed = False 
def toggle_tongue():
 if not c.tongue_out: c.itemconfigure(tongue_tip, state=NORMAL) c.itemconfigure(tongue_main, state=NORMAL) c.tongue_out = True
 else: c.itemconfigure(tongue_tip, state=HIDDEN) c.itemconfigure(tongue_main, state=HIDDEN) c.tongue_out = False 
def cheeky(event): toggle_tongue() toggle_pupils() hide_happy(event) root.after(1000, toggle_tongue) root.after(1000, toggle_pupils) return 
def show_happy(event):
 if (20 <= event.x and event.x <= 350) and (20 <= event.y and event.y <= 350): c.itemconfigure(cheek_left, state=NORMAL) c.itemconfigure(cheek_right, state=NORMAL) c.itemconfigure(mouth_happy, state=NORMAL) c.itemconfigure(mouth_normal, state=HIDDEN) c.itemconfigure(mouth_sad, state=HIDDEN) c.happy_level = 10
 return 
def hide_happy(event): c.itemconfigure(cheek_left, state=HIDDEN) c.itemconfigure(cheek_right, state=HIDDEN) c.itemconfigure(mouth_happy, state=HIDDEN) c.itemconfigure(mouth_normal, state=NORMAL) c.itemconfigure(mouth_sad, state=HIDDEN) return 
def sad():
 if c.happy_level == 0: c.itemconfigure(mouth_happy, state=HIDDEN) c.itemconfigure(mouth_normal, state=HIDDEN) c.itemconfigure(mouth_sad, state=NORMAL)
 else: c.happy_level �= 1 root.after(5000, sad) 
root = Tk() c = Canvas(root, width=400, height=400) c.configure(bg='dark blue', highlightthickness=0) c.body_color = 'SkyBlue1' 
body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color) ear_left = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.body_color, fill=c.body_color) ear_right = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.body_color, fill=c.body_color) foot_left = c.create_oval(65, 320, 145, 360, outline=c.body_color, fill=c.body_color) foot_right = c.create_oval(250, 320, 330, 360, outline=c.body_color, fill=c.body_color) 
eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white') pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black') eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white') pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black') 
mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL) mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN) mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN) tongue_main = c.create_rectangle(170, 250, 230, 290, outline='red', fill='red', state=HIDDEN) tongue_tip = c.create_oval(170, 285, 230, 300, outline='red', fill='red', state=HIDDEN) 
cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN) cheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN) 
c.pack() 
c.bind('<Motion>', show_happy) c.bind('<Leave>', hide_happy) c.bind('<Double�1>', cheeky) 
c.happy_level = 10 c.eyes_crossed = False c.tongue_out = False 
root.after(1000, blink) root.after(5000, sad) root.mainloop() 

Caterpillar (page 158) 
import random import turtle as t 
t.bgcolor('yellow') 
caterpillar = t.Turtle() caterpillar.shape('square') caterpillar.color('red') caterpillar.speed(0) caterpillar.penup() caterpillar.hideturtle() 
leaf = t.Turtle() 
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14)) t.register_shape('leaf', leaf_shape) leaf.shape('leaf') leaf.color('green') leaf.penup() leaf.hideturtle() leaf.speed(0) 
game_started = False text_turtle = t.Turtle() text_turtle.write('Press SPACE to start', align='center', font=('Arial', 16, 'bold')) text_turtle.hideturtle() 
score_turtle = t.Turtle() score_turtle.hideturtle() score_turtle.speed(0) 
def outside_window(): left_wall = �t.window_width() / 2 right_wall = t.window_width() / 2 top_wall = t.window_height() / 2 bottom_wall = �t.window_height() / 2 (x, y) = caterpillar.pos() outside = \
 x< left_wall or \
 x> right_wall or \ y< bottom_wall or \
 y> top_wall return outside 
def game_over(): caterpillar.color('yellow') leaf.color('yellow') t.penup() t.hideturtle() t.write('GAME OVER!', align='center', font=('Arial', 30, 'normal')) 
def display_score(current_score): score_turtle.clear() score_turtle.penup() x = (t.window_width() / 2) � 50 y = (t.window_height() / 2) � 50 score_turtle.setpos(x, y) score_turtle.write(str(current_score), align='right', font=('Arial', 40, 'bold')) 
def place_leaf(): leaf.ht() leaf.setx(random.randint(�200, 200)) 
leaf.sety(random.randint(�200, 200)) leaf.st() 
def start_game(): global game_started if game_started:
 return game_started = True
 score = 0 text_turtle.clear()
 caterpillar_speed = 2 caterpillar_length = 3 caterpillar.shapesize(1, caterpillar_length, 1) caterpillar.showturtle() display_score(score) place_leaf()
 while True: caterpillar.forward(caterpillar_speed) if caterpillar.distance(leaf) < 20:
 place_leaf() caterpillar_length = caterpillar_length + 1 caterpillar.shapesize(1, caterpillar_length, 1) caterpillar_speed = caterpillar_speed + 1 score = score + 10 display_score(score)
 if outside_window(): game_over() break 
def move_up(): if caterpillar.heading() == 0 or caterpillar.heading() == 180: caterpillar.setheading(90) 
def move_down(): if caterpillar.heading() == 0 or caterpillar.heading() == 180: caterpillar.setheading(270) 
def move_left(): if caterpillar.heading() == 90 or caterpillar.heading() == 270: caterpillar.setheading(180) 
def move_right(): if caterpillar.heading() == 90 or caterpillar.heading() == 270:
 caterpillar.setheading(0) t.onkey(start_game, 'space') t.onkey(move_up, 'Up') t.onkey(move_right, 'Right') 
t.onkey(move_down, 'Down') t.onkey(move_left, 'Left') t.listen() t.mainloop() 

Snap (page 168) 
import random import time from tkinter import Tk, Canvas, HIDDEN, NORMAL 
def next_shape(): global shape global previous_color global current_color
 previous_color = current_color
 c.delete(shape)
 if len(shapes) > 0: shape = shapes.pop() c.itemconfigure(shape, state=NORMAL) current_color = c.itemcget(shape, 'fill') root.after(1000, next_shape)
 else: c.unbind('q') c.unbind('p') if player1_score > player2_score:
 c.create_text(200, 200, text='Winner: Player 1') elif player2_score > player1_score: c.create_text(200, 200, text='Winner: Player 2') else: c.create_text(200, 200, text='Draw') c.pack() 
def snap(event): global shape global player1_score global player2_score valid = False
 c.delete(shape) if previous_color == current_color: valid = True
 if valid: if event.char == 'q': player1_score = player1_score + 1 else: 
player2_score = player2_score + 1 shape = c.create_text(200, 200, text='SNAP! You score 1 point!') else: if event.char == 'q': player1_score = player1_score � 1 else: player2_score = player2_score � 1
 shape = c.create_text(200, 200, text='WRONG! You lose 1 point!') c.pack() root.update_idletasks() time.sleep(1) 
root = Tk() root.title('Snap') c = Canvas(root, width=400, height=400) 
shapes = [] 
circle = c.create_oval(35, 20, 365, 350, outline='black', fill='black', state=HIDDEN) shapes.append(circle) circle = c.create_oval(35, 20, 365, 350, outline='red', fill='red', state=HIDDEN) shapes.append(circle) circle = c.create_oval(35, 20, 365, 350, outline='green', fill='green', state=HIDDEN) shapes.append(circle) circle = c.create_oval(35, 20, 365, 350, outline='blue', fill='blue', state=HIDDEN) shapes.append(circle) 
rectangle = c.create_rectangle(35, 100, 365, 270, outline='black', fill='black', state=HIDDEN) shapes.append(rectangle) rectangle = c.create_rectangle(35, 100, 365, 270, outline='red', fill='red', state=HIDDEN) shapes.append(rectangle) rectangle = c.create_rectangle(35, 100, 365, 270, outline='green', fill='green', state=HIDDEN) shapes.append(rectangle) rectangle = c.create_rectangle(35, 100, 365, 270, outline='blue', fill='blue', state=HIDDEN) shapes.append(rectangle) 
square = c.create_rectangle(35, 20, 365, 350, outline='black', fill='black', state=HIDDEN) shapes.append(square) square = c.create_rectangle(35, 20, 365, 350, outline='red', fill='red', state=HIDDEN) shapes.append(square) square = c.create_rectangle(35, 20, 365, 350, outline='green', fill='green', state=HIDDEN) shapes.append(square) square = c.create_rectangle(35, 20, 365, 350, outline='blue', fill='blue', state=HIDDEN) shapes.append(square) c.pack() 
random.shuffle(shapes) 
shape = None 
previous_color = '' current_color = '' player1_score = 0 player2_score = 0 
root.after(3000, next_shape) c.bind('q', snap) c.bind('p', snap) c.focus_set() 
root.mainloop() 

Matchmaker (page 180) 
import random import time from tkinter import Tk, Button, DISABLED 
def show_symbol(x, y): global first global previousX, previousY buttons[x, y]['text'] = button_symbols[x, y] buttons[x, y].update_idletasks()
 if first: previousX = x previousY = y first = False
 elif previousX != x or previousY != y:
 if buttons[previousX, previousY]['text'] != buttons[x, y]['text']: time.sleep(0.5) buttons[previousX, previousY]['text'] = '' buttons[x, y]['text'] = ''
 else: buttons[previousX, previousY]['command'] = DISABLED buttons[x, y]['command'] = DISABLED
 first = True 
root = Tk() root.title('Matchmaker') root.resizable(width=False, height=False) buttons = {} first = True previousX = 0 previousY = 0 button_symbols = {} symbols = [u'\u2702', u'\u2702', u'\u2705', u'\u2705', u'\u2708', u'\u2708',
 u'\u2709', u'\u2709', u'\u270A', u'\u270A', u'\u270B', u'\u270B', 
u'\u270C', u'\u270C', u'\u270F', u'\u270F', u'\u2712', u'\u2712', u'\u2714', u'\u2714', u'\u2716', u'\u2716', u'\u2728', u'\u2728'] random.shuffle(symbols) 
for x in range(6):
 for y in range(4): button = Button(command=lambda x=x, y=y: show_symbol(x, y), width=3, height=3) button.grid(column=x, row=y) buttons[x, y] = button button_symbols[x, y] = symbols.pop() 
root.mainloop() 

Egg Catcher (page 190) 
from itertools import cycle from random import randrange from tkinter import Canvas, Tk, messagebox, font 
canvas_width = 800 canvas_height = 400 
root = Tk() c = Canvas(root, width=canvas_width, height=canvas_height, background='deep sky blue') c.create_rectangle(�5, canvas_height � 100, canvas_width + 5, canvas_height + 5, \
 fill='sea green', width=0) c.create_oval(�80, �80, 120, 120, fill='orange', width=0) c.pack() 
color_cycle = cycle(['light blue', 'light green', 'light pink', 'light yellow', 'light cyan']) egg_width = 45 egg_height = 55 egg_score = 10 egg_speed = 500 egg_interval = 4000 difficulty_factor = 0.95 
catcher_color = 'blue' catcher_width = 100 catcher_height = 100 catcher_start_x = canvas_width / 2 � catcher_width / 2 catcher_start_y = canvas_height � catcher_height � 20 catcher_start_x2 = catcher_start_x + catcher_width catcher_start_y2 = catcher_start_y + catcher_height 
catcher = c.create_arc(catcher_start_x, catcher_start_y, \ catcher_start_x2, catcher_start_y2, start=200, extent=140, \ style='arc', outline=catcher_color, width=3) game_font = font.nametofont('TkFixedFont') game_font.config(size=18) 
score = 0 score_text = c.create_text(10, 10, anchor='nw', font=game_font, fill='darkblue', \ text='Score: ' + str(score)) 
lives_remaining = 3 lives_text = c.create_text(canvas_width � 10, 10, anchor='ne', font=game_font, fill='darkblue', \ text='Lives: ' + str(lives_remaining)) 
eggs = [] 
def create_egg(): x = randrange(10, 740) y = 40 new_egg = c.create_oval(x, y, x + egg_width, y + egg_height, fill=next(color_cycle), width=0) eggs.append(new_egg) root.after(egg_interval, create_egg) 
def move_eggs():
 for egg in eggs: (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg) c.move(egg, 0, 10) if egg_y2 > canvas_height:
 egg_dropped(egg) root.after(egg_speed, move_eggs) 
def egg_dropped(egg): eggs.remove(egg) c.delete(egg) lose_a_life() if lives_remaining == 0:
 messagebox.showinfo('Game Over!', 'Final Score: ' + str(score)) root.destroy() 
def lose_a_life(): global lives_remaining lives_remaining �= 1 c.itemconfigure(lives_text, text='Lives: ' + str(lives_remaining)) 
def check_catch(): (catcher_x, catcher_y, catcher_x2, catcher_y2) = c.coords(catcher) for egg in eggs:
 (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)
 if catcher_x < egg_x and egg_x2 < catcher_x2 and catcher_y2 � egg_y2 < 40: eggs.remove(egg) c.delete(egg) increase_score(egg_score) 
root.after(100, check_catch) 
def increase_score(points): global score, egg_speed, egg_interval score += points egg_speed = int(egg_speed * difficulty_factor) egg_interval = int(egg_interval * difficulty_factor) c.itemconfigure(score_text, text='Score: ' + str(score)) 
def move_left(event): (x1, y1, x2, y2) = c.coords(catcher) if x1 > 0:
 c.move(catcher, �20, 0) 
def move_right(event): (x1, y1, x2, y2) = c.coords(catcher) if x2 < canvas_width:
 c.move(catcher, 20, 0) 
c.bind('<Left>', move_left) c.bind('<Right>', move_right) c.focus_set() 
root.after(1000, create_egg) root.after(1000, move_eggs) root.after(1000, check_catch) root.mainloop() 
