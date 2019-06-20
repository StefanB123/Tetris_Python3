from tkinter import *
from random import randint
import time


class Main(Tk):

    def __init__(self):
        super().__init__()

        # set some values
        self.clock_timer = 1000
        self.after_id = None
        self.height = 200
        self.width = 30
        self.block_size = 10

        # save the positions of the blocks
        self.blocks_position = []

        # create an frame for the game and the block
        self.frame_game = Frame(self, height=self.height, width=self.width, bg='#484848')

        # changed this line on purpose => rework all references!!!!!
        self.frame_blocks = []
        self.new_blocks()

        # bind the game inputs to the game frame
        self.frame_game.bind('<a>', self.shift)
        self.frame_game.bind('<d>', self.shift)
        self.frame_game.bind('<s>', self.shift)
        self.frame_game.focus()

        # place those frames; place the frame in the middle of the screen
        self.frame_game.pack()

        # place the frames
        self.place_blocks()

        # save all blocks
        self.blocks_down = []

        # start the game
        self.clock()

    # is the clock of this game
    def clock(self):

        # set the actual clock and save it
        self.after_id = self.after(self.clock_timer, self.clock)
        self.move_blocks()

    # moves the block down
    def move_blocks(self):

        # make a list of the changes if it's successful; also create the bool to check if it's successful
        y_changes = []
        successful = True

        for i in range(0, 4):

            # calculate the new position of the block
            block_x = self.blocks_position[i][0]
            block_y = self.blocks_position[i][1] + self.block_size

            # check if the block hits the bottom
            if not self.check_block(block_x=block_x, block_y=block_y):

                # set successful as false
                successful = False

                # add the blocks to the blocks which are down
                for j in range(0, 4):
                    self.blocks_down.append(self.frame_blocks[j])

                # create new blocks
                self.new_blocks()

                # check if the line(s) should get cleared
                self.clear_line()

                # break out of the loops; if not then it will have corrupted information (since new blocks got generated)!!!!
                break

            else:
                y_changes.append(block_y)

        # write the changes back if they were successful
        if successful:

            for i in range(0, 4):

                # write those back; just needs the y-changes
                self.blocks_position[i][1] = y_changes[i]

        # place the block
        self.place_blocks()

    # places all blocks
    def place_blocks(self):

        # get the frames and place them
        for i in range(0, 4):

            # place it on the according spot
            self.frame_blocks[i].place(x=self.blocks_position[i][0], y=self.blocks_position[i][1])

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

    # creates new blocks
    def new_blocks(self):

        ##########################################################################################################
        # Try to make the possible tetris peaces
        ##########################################################################################################

        # remove all the entries of self.frame_blocks; same goes with the positions
        self.frame_blocks = []
        self.blocks_position = []

        # append 4 blocks to the list
        for i in range(0, 4):

            # create the frame for it
            frame_block = Frame(self.frame_game, height=self.block_size, width=self.block_size, bg='#ff0000')
            self.frame_blocks.append(frame_block)

        # create an random integer
        rn = randint(0, 6)

        # following integers make the pieces
        # 0 = O-Piece
        # 1 = z-Piece
        # 2 = s-Piece
        # 3 = L-Piece
        # 4 = J-Piece
        # 5 = T-Piece
        # 6 = I-Piece

        # TESTING!!!!!!!
        rn = 0

        # create O-Piece
        if rn == 0:

            # calculate the positions

            # in the middle at the top
            x0 = self.block_size * int(self.width / self.block_size / 2)
            y0 = 0

            # on the left side of the first block
            x1 = x0 + self.block_size
            y1 = y0

            # beneath the first block
            x2 = x0
            y2 = y0 + self.block_size

            # beneath the second block
            x3 = x1
            y3 = y2

            # set the positions for the blocks
            self.blocks_position.append([x0, y0])
            self.blocks_position.append([x1, y1])
            self.blocks_position.append([x2, y2])
            self.blocks_position.append([x3, y3])

            print(self.blocks_position)

        # create z-Piece
        elif rn == 1:
            pass

        # create s-Piece
        elif rn == 2:
            pass

        # create L-Piece
        elif rn == 3:
            pass

        # create J-Piece
        elif rn == 4:
            pass

        # create T-Piece
        elif rn == 5:
            pass

        # create I-Piece
        elif rn == 6:
            pass

        # place the blocks
        self.place_blocks()

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
