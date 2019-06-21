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
        self.width = 40
        self.block_size = 10

        # save all blocks which are fixed
        self.blocks_down = []

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

                # create new blocks
                self.new_blocks()

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

        # check if it goes out of the border
        if (block_x < 0) | (block_x > (self.width - self.block_size)):

            return False

        # check if the block can move down; if the block is at the bottom return false
        if block_y >= self.height:

            return False

        # check if the block falls on a block
        for block_d in self.blocks_down:

            # get the position of the stopped block
            block_d_x = block_d.winfo_x()
            block_d_y = block_d.winfo_y()

            # return False if there is already another block at that position
            if (block_x == block_d_x) & (block_y == block_d_y):

                return False

        # return True if it run until here
        return True

    # creates new blocks
    def new_blocks(self):

        ##########################################################################################################
        # Try to make the possible tetris peaces
        ##########################################################################################################

        # add the old blocks to the blocks which are down; only if blocks already exist
        if self.frame_blocks:
            for j in range(0, 4):

                # add the values to the list
                self.blocks_down.append(self.frame_blocks[j])
        # clear the lines
        self.clear_line()

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

            # print(self.blocks_position)

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

        # make a list for the changes; also create a bool if it's successful
        successful = True
        changes = []

        # do this for all tetris pieces
        for i in range(0, 4):

            # get the position of the block
            block_x = self.blocks_position[i][0]
            block_y = self.blocks_position[i][1]

            # create a new piece when the piece is at the bottom
            if block_y >= (self.height - self.block_size):

                # set successful to false
                successful = False

                # create a new block
                self.new_blocks()

                # break out of the loop
                break

            # set the new position
            if event.keysym == 'a':

                # check if the block goes out of the left side
                if block_x > 0:

                    # calculate the new x
                    block_x -= self.block_size

                    # check if it hits another block; if yes don't commit changes
                    if not self.check_block(block_x=block_x, block_y=block_y):

                        # set successful to False
                        successful = False

                        break

                # if one block is at the border, the entirety of the piece shouldn't move!!!!
                else:

                    # set successful to False
                    successful = False

            elif event.keysym == 'd':

                # check if the block goes out of the right side
                if block_x < (self.width - self.block_size):

                    # calculate the new x
                    block_x += self.block_size

                    # check if it hits another block; if yes don't commit changes
                    if not self.check_block(block_x=block_x, block_y=block_y):

                        # set successful to False
                        successful = False

                        break

                # if one block is at the border, the entirety of the piece shouldn't move!!!!
                else:

                    # set successful to False
                    successful = False

            elif event.keysym == 's':

                if block_y < (self.height - self.block_size):

                    # calculate the new y
                    block_y += self.block_size

                    # check if it hits another block
                    if not self.check_block(block_x=block_x, block_y=block_y):

                        # set successful to False
                        successful = False

                        # make a new block
                        self.new_blocks()

            # save the changes
            changes.append([block_x, block_y])

        # write the changes back if it was successful
        if successful:

            # write the changes back
            for i in range(0, 4):

                # write back to the corresponding position
                self.blocks_position[i] = changes[i]

        # place the blocks
        self.place_blocks()

    # checks if any lines can get cleared
    def clear_line(self):

        # create a list for all the positions of the blocks (includes the block itself)
        positions = []

        # put the positions of the blocks into the position list, also add the block to it
        for block in self.blocks_down:
            block_position = [block.winfo_x(), block.winfo_y(), block]
            positions.append(block_position)

        # go from the bottom upwards
        for clear_y in range(self.height - self.block_size, 0, self.block_size * -1):

            # create a list for the blocks in the line
            line_blocks = []

            # get how many blocks fit into the span of the game field
            missing_blocks = self.width / self.block_size

            # save all blocks with that height to the line_blocks list; also reduce the amount of missing blocks
            for position in positions:

                if position[1] == clear_y:
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
