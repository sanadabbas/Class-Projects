from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:
    def __init__(self, food, game, property):
        self.food = food
        self.game = game
        self.property = property
        self.body = [(GAME_WIDTH // 2, GAME_HEIGHT // 2)]
        self.direction = 'down'

    def move(self, direction):
        self.direction = direction
        x, y = self.body[0]
        
        if direction == 'up':
            y -= SPACE_SIZE
        elif direction == 'down':
            y += SPACE_SIZE
        elif direction == 'left':
            x -= SPACE_SIZE
        elif direction == 'right':
            x += SPACE_SIZE
        
        self.body.insert(0, (x, y))
        self.body.pop()

    def grow(self):
        x, y = self.body[-1]
        self.body.append((x, y))


class Food:
    def __init__(self):
        self.x = (random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE)
        self.y = (random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE)

    def next_turn(self):
        self.x = (random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE)
        self.y = (random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE)


def change_direction(new_direction):
    global direction
    if new_direction != direction and not is_opposite(direction, new_direction):
        direction = new_direction


def is_opposite(current, new):
    opposites = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}
    return opposites.get(current) == new


def check_collisions(snake, food, canvas):
    global score
    
    head_x, head_y = snake.body[0]
    
    # Check collision with food
    if head_x == food.x and head_y == food.y:
        score += 1
        snake.grow()
        food.next_turn()
        return False
    
    # Check collision with walls
    if head_x < 0 or head_x >= GAME_WIDTH or head_y < 0 or head_y >= GAME_HEIGHT:
        return True
    
    # Check collision with self
    if (head_x, head_y) in snake.body[1:]:
        return True
    
    return False


def update_game():
    global direction, score, game_over
    
    if not game_over:
        snake.move(direction)
        
        if check_collisions(snake, food, canvas):
            game_over = True
            canvas.create_text(GAME_WIDTH // 2, GAME_HEIGHT // 2, 
                             text=f"Game Over! Score: {score}", 
                             font=('consolas', 30), fill="white")
        else:
            # Redraw canvas
            canvas.delete("all")
            
            # Draw snake
            for x, y in snake.body:
                canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, 
                                      fill=SNAKE_COLOR, outline="white")
            
            # Draw food
            canvas.create_rectangle(food.x, food.y, food.x + SPACE_SIZE, food.y + SPACE_SIZE,
                                  fill=FOOD_COLOR, outline="white")
            
            # Update label
            label.config(text=f"Score: {score}")
    
    canvas.after(SPEED, update_game)


def on_key_press(event):
    key = event.keysym.lower()
    if key == 'up':
        change_direction('up')
    elif key == 'down':
        change_direction('down')
    elif key == 'left':
        change_direction('left')
    elif key == 'right':
        change_direction('right')


# Initialize game
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'
game_over = False

label = Label(window, text=f"Score: {score}", font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.bind("<Key>", on_key_press)

# Create game objects
snake = Snake(food="apple", game="arcade", property="green")
food = Food()

# Center window on screen
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")

# Start game loop
update_game()
window.mainloop()