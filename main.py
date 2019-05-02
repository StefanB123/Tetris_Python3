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

        # save all blocks
        self.blocks_down = []

        # start the game
        self.clock()

    # moves the piece automatic down
    def clock(self):
        # set the actual clock and save it
        self.after_id = self.after(self.clock_timer, self.clock)
        self.check_block()





    # to do:
    # implement that check_block
    # returns an bool
    # and the methods which call it
    # should then chose







    # checks if the block hits an other block / bottom
    def check_block(self):
        # get the position of the block
        block_x = self.frame_block.winfo_x()
        block_y = self.frame_block.winfo_y()

        # move the block down; if the block is at the bottom make a new one
        if block_y < (self.height - self.block_size):
            block_y += self.block_size

            # check if the block falls on a block
            for block_d in self.blocks_down:
                # get the position of the stopped block
                block_d_x = block_d.winfo_x()
                block_d_y = block_d.winfo_y()

                print(block_d_y)
                print(block_d_x)

                if (block_x == block_d_x) & (block_y == block_d_y):
                    print('k')
                    # set a new block
                    self.new_block()

                    # set the position of the new block
                    block_x = 0
                    block_y = 0

        else:
            # set the new block
            self.new_block()

            # set the positions of the new block
            block_x = 0
            block_y = 0

        # place the (new) block
        self.frame_block.place(x=block_x, y=block_y)

    # creates an new block
    def new_block(self):
        self.blocks_down.append(self.frame_block)
        self.frame_block = Frame(self.frame_game, height=self.block_size, width=self.block_size, bg='#ff0000')

    # moves the pieces to the players input
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
                self.check_block()

        # place the frame at the new position
        self.frame_block.place(x=block_x, y=block_y)


Main().mainloop()
