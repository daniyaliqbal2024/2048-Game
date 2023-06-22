"""import tkinter as tk
import random 


class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")
        self.main_grid = tk.Frame(
            self, bg="#92877d", bd=5, width=800, height=800
        )
        self.main_grid.grid(pady=(110, 0))
        
        self.make_GUI()
        self.start_game()
        
        self.master.bind("<Left>", self.left)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Up>", self.up)
        self.master.bind("<Down>", self.down)
        
        self.mainloop()

    Color_EmptyCell = "#ffd5b5"
    Font_ScoreLabel = ("Verdana", 24)
    Font_Score = ("Helvetica", 48, "bold")
    Font_GameOver = ("Helvetica", 48, "bold")
    Font_Color_GameOver = "#ffffff"
    Winner_BG = "#ffcc00"
    Color_Background = "#a39489"
    Color_FG = "#ffffff"
 
    Color_Cells = {
        2: "#fcefe6",
        4: "#f2e8cb",
        8: "#f5b682",
        16: "#f29446",
        32: "#ff775c",
        64: "#e64c2e",
        128: "#ede291",
        256: "#fce130",
        512: "#ffdb4a",
        1024: "#f0b922",
        2048: "#fad74d"    
    }
 
    Color_CellNumber = {
        2: "#695c57",
        4: "#695c57",
        8: "#ffffff",
        16: "#ffffff",
        32: "#ffffff",
        64: "#ffffff",
        128: "#ffffff",
        256: "#ffffff",
        512: "#ffffff",
        1024: "#ffffff",
        2048: "#ffffff"
    }
 
    Fonts_CellNumber = {
        2: ("Helvetica", 55, "bold"),
        4: ("Helvetica", 55, "bold"),
        8: ("Helvetica", 55, "bold"),
        16: ("Helvetica", 50, "bold"),
        32: ("Helvetica", 50, "bold"),
        64: ("Helvetica", 50, "bold"),
        128: ("Helvetica", 45, "bold"),
        256: ("Helvetica", 45, "bold"),
        512: ("Helvetica", 45, "bold"),
        1024: ("Helvetica", 40, "bold"),
        2048: ("Helvetica", 40, "bold"),
    }

    def make_GUI (self): 
        self.cells= []
        for i in range(4):
            row=[]
            for j in range(4):
                cell_frame= tk.Frame(
                    self.main_grid,
                    bg=self.Color_EmptyCell,
                    width= 150,
                    height=150
                )
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number= tk.Label(self.main_grid, bg=self.Color_EmptyCell)
                cell_number.grid(row=i, column=j)
                cell_data= {"frame":cell_frame, "number":cell_number}
                row.append(cell_data)
            self.cells.append(row)

        score_frame=tk.Frame(self)
        score_frame.place(relx=0.5, y=45, anchor="center")
        tk.Label(
            score_frame,
            text= "Score",
            font= self.Font_ScoreLabel 
        ).grid(row=0)
        self.score_label= tk.Label(score_frame, text="0", font=self.Font_score)
        self.score_label.grid(row=1)

    def start_game(self):
        self.matrix = [[0]*4 for _ in range(4)]
        row= random.randint(0,3)
        col= random.randint(0,3)
        self.matrix[row][col] = 2
        self.cells[row][col]["frame"].configure(bg=self.Color_Cells[2])
        self.cells[row][col]["number"].configure(
            bg=self.Color_Cells[2], 
            fg= self.Color_CellNumber[2],
            font= self.Fonts_CellNumber[2], 
            text= "2"
        )

        while(self.matrix[row][col] != 0):
            row= random.randint(0,3)
            col= random.randint(0,3)
        self.matrix[row][col] = 2
        self.cells[row][col]["frame"].configure(bg=self.Color_Cells[2])
        self.cells[row][col]["number"].configure(
            bg=self.Color_Cells[2], 
            fg= self.Color_CellNumber[2],
            font= self.Fonts_CellNumber[2], 
            text= "2"
        )

        self.score=0

    def stack (self): 
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            fill_position= 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    new_matrix[i][fill_position] = self.matrix[i][j]
                    fill_position+=1
        self.matrix= new_matrix
    
    def combine(self):
        for i in range(4):
            for j in range (3):
                if self.matrix[i][j] !=0 and self.matrix[i][j] == self.matrix[i][j+1]:
                    self.matrix[i][j] *=2
                    self.matrix[i][j+1] =0
                    self.score += self.matrix[i][j]

    def reverse(self):
        new_matrix= []
        for i in range(4):
            new_matrix.append([])
            for j in range(4):
                new_matrix[i].append(self.matrix[i][3-j])
        self.matrix = new_matrix

    def transpose (self):
        new_matrix= [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range (4):
                new_matrix[i][j]= self.matrix[j][i]
        self.matrix= new_matrix
         
    def add_new_tile(self):
        row= random.randint(0,3)
        col= random.randint(0,3)

        while(self.matrix[row][col] != 0):
            row= random.randint(0,3)
            col= random.randint(0,3)
        self.matrix[row][col] = random.choice([2,4])

    def update_GUI(self):
        for i in range(4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.cells[i][j]["frame"].configure(bg=self.Color_EmptyCell)
                    self.cells[i][j]["number"].configure(
                        bg= self.Color_EmptyCell,
                        text=""
                    )
                else:
                    self.cells[i][j]["frame"].configure(
                        bg=self.Color_Cells[cell_value])
                    self.cells[i][j]["number"].configure(
                        bg= self.Color_Cells[cell_value],
                        fg= self.Color_CellNumber[cell_value],
                        font= self.Fonts_CellNumber[cell_value],
                        text= str(cell_value)
                    )
        self.score_label.configure(text= self.score)
        self.update_idletasks()

    def left(self, event):
        self.stack()
        self.combine()
        self.stack()
        self.add_new_tile()
        self.update_GUI()

    def right(self, event):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.add_new_tile()
        self.update_GUI()
        
    def up(self, event):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()

    def down(self, event):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()

    def horizontal_move_exists(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j+1]:
                    return True
        return False
    
    def vertical_move_exists(self):
        for i in range(3):
            for j in range (4):
                if self.matrix[i][j] == self.matrix[i+1][j]:
                    return True
        return False

    def game_over(self):
        if any(2048 in row for row in self.matrix):
            game_over_frame = tk.Frame(self, border= 2)
            game_over_frame.place(relx= 0.5, rely=0.5, anchor="center")
            tk.Label(
                game_over_frame,
                text= "You win!!", 
                bg= self.Color_Background, 
                fg= self.Color_FG, 
                font= self.Font_GameOver
            ).pack()
        
        elif not any(0 in row for row in self.matrix) and not self.horizontal_move_exists() and not self.vertical_move_exists:
            game_over_frame = tk.Frame(self, border= 2)
            game_over_frame.place(relx= 0.5, rely=0.5, anchor="center")
            tk.Label(
                game_over_frame,
                text= "Game Over", 
                bg= self.Color_Background, 
                fg= self.Color_FG, 
                font= self.Font_GameOver
            ).pack()


def main():
    Game()

if __name__== "_main_":
    main()
"""

# 2048 Game
import tkinter as tk
import random

class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")
        self.main_grid = tk.Frame(
            self, bg="#92877d", bd=5, width=800, height=800
        )
        self.main_grid.grid(pady=(110, 0))
        
        self.make_GUI()
        self.start_game()
        
        self.master.bind("<Left>", self.left)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Up>", self.up)
        self.master.bind("<Down>", self.down)
        
        self.mainloop()

    Color_EmptyCell = "#ffd5b5"
    Font_ScoreLabel = ("Verdana", 24)
    Font_Score = ("Helvetica", 48, "bold")
    Font_GameOver = ("Helvetica", 48, "bold")
    Font_Color_GameOver = "#ffffff"
    Winner_BG = "#ffcc00"
    Color_Background = "#a39489"
    Color_FG = "#ffffff"
 
    Color_Cells = {
        2: "#fcefe6",
        4: "#f2e8cb",
        8: "#f5b682",
        16: "#f29446",
        32: "#ff775c",
        64: "#e64c2e",
        128: "#ede291",
        256: "#fce130",
        512: "#ffdb4a",
        1024: "#f0b922",
        2048: "#fad74d"    
    }
 
    Color_CellNumber = {
        2: "#695c57",
        4: "#695c57",
        8: "#ffffff",
        16: "#ffffff",
        32: "#ffffff",
        64: "#ffffff",
        128: "#ffffff",
        256: "#ffffff",
        512: "#ffffff",
        1024: "#ffffff",
        2048: "#ffffff"
    }
 
    Fonts_CellNumber = {
        2: ("Helvetica", 55, "bold"),
        4: ("Helvetica", 55, "bold"),
        8: ("Helvetica", 55, "bold"),
        16: ("Helvetica", 50, "bold"),
        32: ("Helvetica", 50, "bold"),
        64: ("Helvetica", 50, "bold"),
        128: ("Helvetica", 45, "bold"),
        256: ("Helvetica", 45, "bold"),
        512: ("Helvetica", 45, "bold"),
        1024: ("Helvetica", 40, "bold"),
        2048: ("Helvetica", 40, "bold"),
    }

    def make_GUI(self):
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg=self.Color_EmptyCell,
                    width=150,
                    height=150
                )
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.main_grid, bg=self.Color_EmptyCell)
                cell_number.grid(row=i, column=j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)
 
        score_frame = tk.Frame(self)
        score_frame.place(relx=0.5, y=45, anchor="center")
        tk.Label(
            score_frame,
            text="Score",
            font=self.Font_ScoreLabel
        ).grid(row=0)
        self.score_label = tk.Label(score_frame, text="0", font=self.Font_Score)
        self.score_label.grid(row=1)

    def start_game(self):
        self.matrix = [[0] * 4 for _ in range(4)]
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        self.matrix[row][col] = 2
        self.cells[row][col]["frame"].configure(bg=self.Color_Cells[2])
        self.cells[row][col]["number"].configure(
            bg=self.Color_Cells[2],
            fg=self.Color_CellNumber[2],
            font=self.Fonts_CellNumber[2],
            text="2"
        )
        while(self.matrix[row][col] != 0):
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        self.matrix[row][col] = 2
        self.cells[row][col]["frame"].configure(bg=self.Color_Cells[2])
        self.cells[row][col]["number"].configure(
            bg=self.Color_Cells[2],
            fg=self.Color_CellNumber[2],
            font=self.Fonts_CellNumber[2],
            text="2"
        )
        self.score = 0

    def stack(self):
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            fill_position = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    new_matrix[i][fill_position] = self.matrix[i][j]
                    fill_position += 1
        self.matrix = new_matrix

    def combine(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0
                    self.score += self.matrix[i][j]

    def reverse(self):
        new_matrix = []
        for i in range(4):
            new_matrix.append([])
            for j in range(4):
                new_matrix[i].append(self.matrix[i][3 - j])
        self.matrix = new_matrix

    def transpose(self):
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new_matrix[i][j] = self.matrix[j][i]
        self.matrix = new_matrix

    def add_new_tile(self):
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        while(self.matrix[row][col] != 0):
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        self.matrix[row][col] = random.choice([2, 4])

    def update_GUI(self):
        for i in range(4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.cells[i][j]["frame"].configure(bg=self.Color_EmptyCell)
                    self.cells[i][j]["number"].configure(
                        bg=self.Color_EmptyCell,
                        text=""
                    )
                else:
                    self.cells[i][j]["frame"].configure(
                        bg=self.Color_Cells[cell_value]
                    )
                    self.cells[i][j]["number"].configure(
                        bg=self.Color_Cells[cell_value],
                        fg=self.Color_CellNumber[cell_value],
                        font=self.Fonts_CellNumber[cell_value],
                        text=str(cell_value)
                    )
        self.score_label.configure(text=self.score)
        self.update_idletasks()

    def left(self, event):
        self.stack()
        self.combine()
        self.stack()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def right(self, event):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def up(self, event):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def down(self, event):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def horizontal_move_exists(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j + 1]:
                    return True
        return False
    
    def vertical_move_exists(self):
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i + 1][j]:
                    return True
        return False
    
    def game_over(self):
        if any(2048 in row for row in self.matrix):
            game_over_frame = tk.Frame(self, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(
                game_over_frame,
                text="You win!",
                bg=self.Color_Background,
                fg=self.Color_FG,
                font=self.Font_GameOver
            ).pack()

        elif not any(0 in row for row in self.matrix) and not self.horizontal_move_exists() and not self.vertical_move_exists():
            game_over_frame = tk.Frame(self, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(
                game_over_frame,
                text="Game over!",
                bg=self.Color_Background,
                fg=self.Color_FG,
                font=self.Font_GameOver
            ).pack()

def main():
    Game()

if __name__ == "__main__":
    main()
