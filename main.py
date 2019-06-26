from tkinter import *
from random import randint


class Main(Tk):

    def __init__(self):
        super().__init__()

        # set some values
        self.clock_timer = 1000
        self.after_id = None
        self.height = 200
        self.width = 100
        self.block_size = 10

        # save all blocks which are fixed
        self.blocks_down = []

        # save the positions of the blocks
        self.blocks_position = []

        # save the type of the piece
        self.piece_type = ''

        # save the rotation degree; 0 = standard; 1 = once to the right; 2 = upside down; 3 = once to the left
        self.rotation = 0

        # create an frame for the game and the block
        self.frame_game = Frame(self, height=self.height, width=self.width, bg='#484848')

        # changed this line on purpose
        self.frame_blocks = []
        self.new_blocks()

        # bind the game inputs to the game frame
        self.frame_game.bind('<a>', self.shift)
        self.frame_game.bind('<d>', self.shift)
        self.frame_game.bind('<s>', self.shift)
        self.frame_game.bind('<k>', self.rotate)
        self.frame_game.bind('<l>', self.rotate)
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
        if (block_x < 0) | (block_x > (self.width - self.block_size)) | (block_y >= self.height) | (block_y < 0):

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

        # TEST
        rn = 5

        # following integers make the pieces
        # 0 = O-Piece
        # 1 = z-Piece
        # 2 = s-Piece
        # 3 = L-Piece
        # 4 = J-Piece
        # 5 = T-Piece
        # 6 = I-Piece

        # create the variables
        x0 = 0
        x1 = 0
        x2 = 0
        x3 = 0
        y0 = 0
        y1 = 0
        y2 = 0
        y3 = 0

        # create O-Piece
        if rn == 0:

            # set the type
            self.piece_type = 'O'

            # calculate the positions

            # in the middle at the top
            x0 = int(self.width / 2)
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

        # create z-Piece
        elif rn == 1:

            # set the type
            self.piece_type = 'Z'

            # calculate the positions

            # create the first block in the middle
            x0 = int(self.width / 2)
            y0 = 0

            # to the left of the first block
            x1 = x0 - self.block_size
            y1 = y0

            # below the first block
            x2 = x0
            y2 = y0 + self.block_size

            # to the right of the third block
            x3 = x2 + self.block_size
            y3 = y2

        # create s-Piece
        elif rn == 2:

            # set the type
            self.piece_type = 'S'

            # calculate the positions

            # create the first block in the middle
            x0 = int(self.width / 2)
            y0 = 0

            # the second block to the right side of the first
            x1 = x0 + self.block_size
            y1 = y0

            # the third below the first
            x2 = x0
            y2 = y0 + self.block_size

            # the fourth to the left of the third
            x3 = x2 - self.block_size
            y3 = y2

        # create L-Piece
        elif rn == 3:

            # set the type
            self.piece_type = 'L'

            # calculate the position

            # create the first block in the middle
            x0 = int(self.width / 2)
            y0 = 0

            # the second to the right of the first
            x1 = x0 + self.block_size
            y1 = y0

            # the third piece to the left of the first
            x2 = x0 - self.block_size
            y2 = y0

            # the fourth piece below the third
            x3 = x2
            y3 = y2 + self.block_size

        # create J-Piece
        elif rn == 4:

            # set the type
            self.piece_type = 'J'

            # calculate the position

            # create the first block in the middle
            x0 = int(self.width / 2)
            y0 = 0

            # the second to the left of the first
            x1 = x0 - self.block_size
            y1 = y0

            # the third piece to the right of the first
            x2 = x0 + self.block_size
            y2 = y0

            # the fourth piece below the third
            x3 = x2
            y3 = y2 + self.block_size

        # create T-Piece
        elif rn == 5:

            # set the type
            self.piece_type = 'T'

            # calculate the position

            # create the first block in the middle
            x0 = int(self.width / 2)
            y0 = 0

            # the second to the right of the first
            x1 = x0 + self.block_size
            y1 = y0

            # the third piece to the left of the first
            x2 = x0 - self.block_size
            y2 = y0

            # the fourth piece below the first
            x3 = x0
            y3 = y0 + self.block_size

        # create I-Piece
        elif rn == 6:

            # set the type
            self.piece_type = 'I'

            # calculate the position

            # create the first block in the middle
            x0 = int(self.width / 2)
            y0 = 0

            # the second block to the right of the first
            x1 = x0 + self.block_size
            y1 = y0

            # the third block to the left of the first
            x2 = x0 - self.block_size
            y2 = y0

            # the fourth block to the left of the third
            x3 = x2 - self.block_size
            y3 = y2

        # set the positions for the blocks
        self.blocks_position.append([x0, y0])
        self.blocks_position.append([x1, y1])
        self.blocks_position.append([x2, y2])
        self.blocks_position.append([x3, y3])

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

        # go from the bottom upwards
        for clear_y in range(self.height - self.block_size, 0, self.block_size * -1):

            # create a list for all the positions of the blocks (includes the block itself)
            positions = []

            # put the positions of the blocks into the position list, also add the block to it; has to be in the loop so that it works when moving down the pieces
            for block in self.blocks_down:
                block_position = [block.winfo_x(), block.winfo_y(), block]
                positions.append(block_position)

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

                # delete the blocks
                for line in line_blocks:

                    # delete the blocks
                    line.place_forget()
                    self.blocks_down.remove(line)
                    line.destroy()

                # create a list to save all the blocks above
                above = []

                # get a list of all the blocks above
                for block in self.blocks_down:

                    # check if the block is above the cleared height
                    if block.winfo_y() < clear_y:

                        # append the block to the list
                        above.append(block)

                # move all of them down
                for a_block in above:

                    # get and calculate the new position
                    a_x = a_block.winfo_x()
                    a_y = a_block.winfo_y() + self.block_size

                    # place the block
                    a_block.place(x=a_x, y=a_y)

    # rotates the pieces
    def rotate(self, event):

        # THOUGHT!!!!!!
        # maybe i should implement a self.block so i know which block is which => looks like it's the best way to identify it. => also prob. outside of the k and l check cause less if ( i think)

        # set a bool to check if it changed already
        changed = False

        # declare the positions
        x0 = self.blocks_position[0][0]
        y0 = self.blocks_position[0][1]
        x1 = self.blocks_position[1][0]
        y1 = self.blocks_position[1][1]
        x2 = self.blocks_position[2][0]
        y2 = self.blocks_position[2][1]
        x3 = self.blocks_position[3][0]
        y3 = self.blocks_position[3][1]

        # O-Piece doesn't rotate
        if self.piece_type == 'O':
            return

        # check it's an I-Piece; I piece is the same for both rotations
        elif self.piece_type == 'I':

            # set changed to True
            changed = True

            # check the rotation size
            if self.rotation == 0:

                # get and recalculate the position of the blocks

                # the first block stays the same; so no changes

                # place the second block below the first block
                x1 = x0
                y1 = y0 + self.block_size

                # place the third above the first
                x2 = x0
                y2 = y0 - self.block_size

                # place the third above the third
                x3 = x2
                y3 = y2 - self.block_size

            else:

                # the first block stays the same

                # the second block to the right of the first
                x1 = x0 + self.block_size
                y1 = y0

                # the third block to the left of the first
                x2 = x0 - self.block_size
                y2 = y0

                # the fourth block to the left of the third
                x3 = x2 - self.block_size
                y3 = y2

        # check the Z-piece
        elif self.piece_type == 'Z':

            # set changed to True
            changed = True

            # turn it once to the left from the base position
            if self.rotation == 0:

                # recalculate the new positions

                # the first piece stays the same

                # the second piece on top of the first
                x1 = x0
                y1 = y0 - self.block_size

                # the third block to the left of the first
                x2 = x0 - self.block_size
                y2 = y0

                # the fourth block below the third
                x3 = x2
                y3 = y2 + self.block_size

            # turn it upside down from the base position
            elif self.rotation == 1:

                # create the first block in the middle

                # the first block stays the same

                # to the left of the first block
                x1 = x0 - self.block_size
                y1 = y0

                # below the first block
                x2 = x0
                y2 = y0 + self.block_size

                # to the right of the third block
                x3 = x2 + self.block_size
                y3 = y2

        elif self.piece_type == 'S':

            # set changed to True
            changed = True

            # turn it upwards
            if self.rotation == 0:

                # first block stays the same

                # second block below first
                x1 = x0
                y1 = y0 + self.block_size

                # third block to the left of the first one
                x2 = x0 - self.block_size
                y2 = y0

                # fourth block above the third
                x3 = x2
                y3 = y2 - self.block_size

            elif self.rotation == 1:

                # first block stays the same

                # the second block to the right side of the first
                x1 = x0 + self.block_size
                y1 = y0

                # the third below the first
                x2 = x0
                y2 = y0 + self.block_size

                # the fourth to the left of the third
                x3 = x2 - self.block_size
                y3 = y2

        # check if the turning is possible
        if not (self.check_block(x1, y1) & self.check_block(x2, y2) & self.check_block(x3, y3)):
            return

        # change the rotation accordingly
        if (self.rotation == 0) & changed:
            self.rotation = 1

        elif (self.rotation == 1) & changed:
            self.rotation = 0

        if not changed:

            # check the T-Piece
            # NOTE: locks like it doesn't stay at the same place but does... maybe fix?
            if self.piece_type == 'T':

                # from the standard position to the right; or from upside down to the left
                if ((self.rotation == 0) & (event.keysym == 'l')) | ((self.rotation == 2) & (event.keysym == 'k')):

                    # first block stays the same

                    # second block below the first
                    x1 = x0
                    y1 = y0 + self.block_size

                    # third block on top of the first
                    x2 = x0
                    y2 = y0 - self.block_size

                    # fourth block to the left of the first
                    x3 = x0 - self.block_size
                    y3 = y0

                    # check if the turning is possible
                    if not (self.check_block(x1, y1) & self.check_block(x2, y2) & self.check_block(x3, y3)):
                        print('k')
                        return

                    # set the rotation
                    self.rotation = 1

                # upside down from the standard position
                elif ((self.rotation == 1) & (event.keysym == 'l')) | ((self.rotation == 3) & (event.keysym == 'k')):

                    # first block stays the same

                    # second block to the left of the first
                    x1 = x0 - self.block_size
                    y1 = y0

                    # third block to the right of the first
                    x2 = x0 + self.block_size
                    y2 = y0

                    # fourth block on top of the first
                    x3 = x0
                    y3 = y0 - self.block_size

                    # check if the turning is possible
                    if not (self.check_block(x1, y1) & self.check_block(x2, y2) & self.check_block(x3, y3)):
                        return

                    # set the rotation
                    self.rotation = 2

                # turn it to the right of the upside down position; left from the standard position
                elif ((self.rotation == 2) & (event.keysym == 'l')) | ((self.rotation == 0) & (event.keysym == 'k')):

                    # first block stays the same

                    # second block on top of the first
                    x1 = x0
                    y1 = y0 - self.block_size

                    # third block below the first
                    x2 = x0
                    y2 = y0 + self.block_size

                    # fourth block to the right of the first
                    x3 = x0 + self.block_size
                    y3 = y0

                    # check if the turning is possible
                    if not (self.check_block(x1, y1) & self.check_block(x2, y2) & self.check_block(x3, y3)):

                        print(x1, y1)
                        print(x2, y2)
                        print(x3, y3)
                        return

                    # set the rotation
                    self.rotation = 3

                # turn it to the standard position
                else:

                    # first block stays the same

                    # the second to the right of the first
                    x1 = x0 + self.block_size
                    y1 = y0

                    # the third piece to the left of the first
                    x2 = x0 - self.block_size
                    y2 = y0

                    # the fourth piece below the first
                    x3 = x0
                    y3 = y0 + self.block_size

                    # check if the turning is possible
                    if not (self.check_block(x1, y1) & self.check_block(x2, y2) & self.check_block(x3, y3)):
                        return

                    # set the rotation
                    self.rotation = 0

        # turn to the left
        if (event.keysym == 'k') & (not changed):

            print('no')
            pass

        # turn to the right
        elif (event.keysym == 'l') & (not changed):
            pass

        # write the changes back
        self.blocks_position[0] = [x0, y0]
        self.blocks_position[1] = [x1, y1]
        self.blocks_position[2] = [x2, y2]
        self.blocks_position[3] = [x3, y3]

        # place the blocks
        self.place_blocks()


Main().mainloop()
