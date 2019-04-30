from tkinter import *


class Main(Tk):

    def __init__(self):
        super().__init__()

        # set some values
        self.clock_timer = 1000
        self.after_id = None
        self.height = 500
        self.width = 100
        self.block_size = 10

        # create an frame for the game and the block
        self.frame_game = Frame(self, height=self.height, width=self.width, bg='#484848')
        self.frame_block = Frame(self.frame_game, height=self.block_size, width=self.block_size, bg='#ff0000')

        # place those frames
        self.frame_game.pack()
        self.frame_block.place(x=0, y=0)

        # start the game
        self.clock()

    def clock(self):
        # set the actual clock and save it
        self.after_id = self.after(self.clock_timer, self.clock)

        # get the height of the block
        height = self.frame_block.winfo_y()

        # replace the block if it didn't hit the bottom
        if height < (self.height - self.block_size):
            height += self.block_size
            self.frame_block.place(x=0, y=height)


Main().mainloop()
