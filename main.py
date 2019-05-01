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

        # bind the game inputs to the game frame
        self.frame_game.bind('<a>', self.shift)
        self.frame_game.bind('<d>', self.shift)
        self.frame_game.bind('<s>', self.shift)
        self.frame_game.focus()

        # place those frames
        self.frame_game.pack()
        self.frame_block.place(x=0, y=0)

        # start the game
        self.clock()

    def clock(self):
        # set the actual clock and save it
        self.after_id = self.after(self.clock_timer, self.clock)

        # get the position of the block
        block_x = self.frame_block.winfo_x()
        block_y = self.frame_block.winfo_y()

        # replace the block if it didn't hit the bottom
        if block_y < (self.height - self.block_size):
            block_y += self.block_size
            self.frame_block.place(x=block_x, y=block_y)

    def shift(self, event):
        # get the position of the block
        block_x = self.frame_block.winfo_x()
        block_y = self.frame_block.winfo_y()

        # return when the block is at the bottom
        if block_y >= (self.height - self.block_size):
            return

        # set the new position
        if event.keysym == 'a':
            if block_x > 0:
                block_x -= self.block_size

        elif event.keysym == 'd':
            if block_x < (self.width - self.block_size):
                block_x += self.block_size

        elif event.keysym == 's':
            if block_y < (self.height - self.block_size):
                block_y += self.block_size

        # place the frame at the new position
        self.frame_block.place(x=block_x, y=block_y)


Main().mainloop()
