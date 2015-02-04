from mapping import town_to_hex
from utils import Map, Block
import os
import sys

ROM_PATH = "gold.gbc"
SQUARE_SIZE = 32

##TODO ADD VERTICAL TILES
if __name__ == '__main__':

    with open(ROM_PATH, 'rb') as gold_rom:

        # Let's try to create your Bedroom in Pallet Town
        # 'Ash's Room', 'Pallet Town' width 10, "Viridian City" 18

        current_map = Map(name = "Pallet Town", mapping = town_to_hex,
                width = 10)

        print(current_map.bank)


        bytes_to_read = current_map.end - current_map.start 


        # Skip to where pallet_town is stored on the ROM
        ### NEED TO DOUBLE CHECK THE ADDING 1 HERE

        all_data = gold_rom.read()
        relevant_hex_data = all_data[ current_map.start : current_map.end + 1 ]

        i = i_ = j = block_id = 0
        
        for h in relevant_hex_data:
            
            offset = hex(current_map.end - bytes_to_read)
            d = (int(offset,0))
            bytes_to_read -= 1

            contents = all_data[d]
            b = Block(i, j, contents, width=SQUARE_SIZE, block_id = block_id)
            current_map.add_block(b)
            #print(current_map.generate_block_html(b))
            #print(current_map.generate_block_css(b))

            i  += SQUARE_SIZE
            i_ += 1
            block_id += 1

            if (i_ % current_map.width == 0):
                i_ = i = 0
                j += SQUARE_SIZE

            '''
            FSP_repr = hex_to_FSP[current_map.bank].get(h)
            b = Block(FSP_repr, i, j)
            
            current_map.add_block(b)
    
            i += 16 
            i_ += 1
            if (i_ % current_map.width == 0):
                i_ = 0
                i -= 16 * current_map.width
                j += 16 



        '''
        html =(current_map.html())
        f = open('JoeMap.html', 'w')
        f.write(html)
        print("written")
        


        #print(pallet_town.name, pallet_town.start, pallet_town.end)


