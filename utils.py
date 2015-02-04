class Map(object):

    def __init__(self, name = None, mapping = {}, 
            width = 10, height = 9, bank = None):

        self.name  = name
        self.width = width
        self.height = width

        self.bank =  mapping.get(name)[2]
        self.start = int(mapping.get(name)[0], 16)
        self.end   = int(mapping.get(name)[1], 16)

        self.sprite = "banks/" + str(self.bank) +".png"

        self.blocks = []

    def generate_block_css(self, b):
        output = ""
        output += "#block{} {{\n".format(b.block_id)
        output += "left : {}px;\n".format(b.x)
        output += "top : {}px;\n".format(b.y)
        output += "background: url('{}') ".format(self.sprite)
        output += "0px {}px\n".format(8192 - (b.width * b.contents))
        output += "}"
        
        return output

    def generate_block_html(self, b):
        output = ""
        output += '<li id="block{}"></a></li>'.format(b.block_id)
        return output

    def html(self):
        block_css = '\n'.join([self.generate_block_css(b) for b in self.blocks])
        block_html = '\n'.join([self.generate_block_html(b) for b in self.blocks])
        
        output = """
        <!DOCTYPE html>
        <html>
        <head>
        <style>
        
        #navlist {{
            position: relative;
        }}

        #navlist li {{
            margin: 0;
            padding: 0;
            list-style: none;
            position: absolute;
            width: 32px;
            height: 32px;
        }}

        #navlist li, #navlist a {{
            display: block;
        }}

        {0}
    
        </style>
        </head>
        <body>

        <ul id="navlist">
        {1}
        </ul>

        </body>
        </html>
        """.format(block_css, block_html)

        return output
        

    def add_block(self, block):
        self.blocks.append(block)


class Block(object):
    ''' self.contents has already been converted to decimal '''
    def __init__(self, x, y, contents, block_id = 0, width=32):
        self.x = x
        self.y = y
        self.contents = contents
        self.width = width
        self.block_id = block_id


    def __repr__(self):
        return "{} at ({}, {}) ".format(self.contents, self.x, self.y)


    
