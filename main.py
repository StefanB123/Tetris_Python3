from tkinter import *


class Main(Tk):

    def __init__(self):
        super().__init__()

        # set some values
        self.clock_timer = 1000
        self.after_id = None
        self.height = 200
        self.width = 30
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
        self.move_block()

    def move_block(self):
        # calculate the new position of the block
        block_x = self.frame_block.winfo_x()
        block_y = self.frame_block.winfo_y() + self.block_size

        # check if the block hits the bottom
        if not self.check_block(block_x=block_x, block_y=block_y):

            # make a new block
            self.new_block()

            block_x = 0
            block_y = 0

        # place the block
        self.frame_block.place(x=block_x, y=block_y)

    # checks if the block hits an other block / bottom
    def check_block(self, block_x: int, block_y: int):

        # move the block down; if the block is at the bottom return false
        if block_y < self.height:

            # check if the block falls on a block
            for block_d in self.blocks_down:
                # get the position of the stopped block
                block_d_x = block_d.winfo_x()
                block_d_y = block_d.winfo_y()

                if (block_x == block_d_x) & (block_y == block_d_y):
                    return False

        else:
            return False

        return True

    # creates an new block
    def new_block(self):
        self.blocks_down.append(self.frame_block)
        self.clear_line()
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
                """
                # calculate the new position of the block
                block_x = self.frame_block.winfo_x()
                block_y = self.frame_block.winfo_y() + self.block_size

                # check if the block hits the bottom
                if not self.check_block(block_x=block_x, block_y=block_y):

                    # make a new block
                    self.new_block()

                    block_x = 0
                    block_y = 0

                # place the block
                self.frame_block.place(x=block_x, y=block_y)
                
                """

                block_y += self.block_size

                if not self.check_block(block_x=block_x, block_y=block_y):

                    # make a new block
                    self.new_block()

                    block_x = 0
                    block_y = 0

        # place the frame at the new position
        self.frame_block.place(x=block_x, y=block_y)

    # checks if any lines can get cleared
    def clear_line(self):

        # go from the bottom upwards
        for clear_y in range(self.height - self.block_size, 0, self.block_size * -1):

            # create a list for all the positions of the blocks (includes the block itself)
            positions = []

            # put the positions of the blocks into the position list, also add the block to it
            for block in self.blocks_down:
                block_position = [block.winfo_x(), block.winfo_y(), block]
                positions.append(block_position)

            # get how many blocks fit into the span of the game field
            missing_blocks = self.width / self.block_size

            # create a list for the blocks in the line
            line_blocks = []

            # save all blocks with that height to the line_blocks list; also reduce the amount of missing blocks
            for position in positions:

                if position[2].winfo_y() == clear_y:
                    missing_blocks -= 1
                    line_blocks.append(position[2])

            # check if there are no more missing blocks => line is full
            if missing_blocks == 0:

                # go through the list and delete all of them
                for line in line_blocks:
                    line.place_forget()
                    self.blocks_down.remove(line)
                    line.destroy()


Main().mainloop()
