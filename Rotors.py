import Plugboard as pb

class Wheel():
    """
    Rotor is a main component in Enigma machine and Rotor has three wheels. This Wheel class is responsible to create wheels for Rotor.   
    ...

    Attributes
    ----------
    position : str
        a alphabet to set the starting position of Entry Wheel. Default is "d" 
    steps : int
        wheel need to change position after every character using this steps attribute, Default value is 1
    Wheel : list
        listed 26 alphabet 

    Methods
    ----------
    move()
    move wheel from its current position to next position using steps attribute 
    
    Exception
    ----------
    No Exception need to be handle 
    """

    def __init__(self, position='d', steps=1):
        self.position = position
        if (steps < 1):
            steps = 1
        self.steps    = int(steps)
        wheel = [chr( ord('a') + i ) for i in range(26)]
        
        self.position = self.position % len(wheel)
        self.wheel = wheel[self.position:] + wheel[:self.position]

    def move(self):
        self.wheel = self.wheel[self.steps:] + self.wheel[:self.steps]

    def __repr__(self):
        return "['"+"', '".join(self.wheel) + "']"


    def __str__(self):
        return "['"+"', '".join(self.wheel) + "']"

class Rotors():

    """
    Rotor is a main component in Enigma machine, which is made by wheels of characters. 
    this class takes list of characters and process those characters
    """
    position : str
    def __init__(self, position='d', levels=3, steps=1):
        self.position  = ord(position) - 96
        self.steps     = steps
        
        self.start_pos = []
        self.wheels    = []
        if(levels < 3): 
            levels = 3

        self.levels    = levels + levels
        
    def init_wheels(self):
        """
        Initialization of wheels in Rotor. 
        Usually there are three wheel exists in one Enigma machine and with both side input, it has 6 faces
        """
        temp_position = 9
        for i in range(self.levels):
            #print(self.position, "->", temp_position)

            self.wheels.append( Wheel(position=self.position, steps=self.steps) )
            self.start_pos.append(self.wheels[i].wheel[0])
            self.position, temp_position = temp_position + self.position, self.position
            self.position = self.position - 26 if (self.position > 26) else self.position
            ##print(self.wheels[i].wheel) 

    def process_line(self, line,encripted=False):
        """
            This method is used to encript or decript the line in Roter 
            while it encripting the value then this method used the output string of plugboard and
            while it decripting the value then it produce string that need to process in plugboard 
        """
        line = line.lower()
        self.encripted = encripted
        ret_val        = []

        for char in line:
            if( char.isalpha()):
                char_num = ''
                if(self.encripted):
                    x = self.wheels[-1].wheel.index(char)
                    ret_val.append(chr(ord('a') + x))
                else:
                    char_num = ord(char) - 97
                    ret_val.append( self.wheels[-1].wheel[char_num])

                self.wheels[0].move()
                self.wheels[-1].move()

                other_wheel_move_i = int(len(ret_val) / 26) + 1
                if ( len(ret_val) % 26 == 0 and other_wheel_move_i <= (len(self.wheels)/2) ):
                    for i in range(1, other_wheel_move_i): 
                        self.wheels[i].move() 
                        self.wheels[ -(i+1) ].move()
            else:
                ret_val.append(char)
        return ''.join(ret_val)


if __name__ == '__main__':

    #input_str = 'zkertmfdjtidlstrv1a5bcd efghii--zkertmfdjtidlstrvabcdefghii'
    input_str = 'Sanjeev Tyagi'
    wheel   = Rotors(position='j')
    wheel.init_wheels()
    print(f"{'Input Str': <15}: {input_str}" )
    pb_obj  = pb.Plugboard()
    pb_str  = pb_obj.exchange_plugged_chars(input_str)
    print(f"{'Plugboard Str': <15}: {pb_str}")
    ret     = wheel.process_line(pb_str)
    print(f"{'Output Str': <15}: {ret}")

    print("\n\n")
    wheel   = Rotors(position='j')
    wheel.init_wheels()
    de_ret     = wheel.process_line(ret,encripted=True)
    print(f"{'processed Str': <15}: {ret}")

    de_pb_str  = pb_obj.exchange_plugged_chars(de_ret)
    print(f"{'final output Str': <15}: {de_pb_str}")

