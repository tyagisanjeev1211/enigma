import os
import glob

class Plugboard():

    def __init__(self):
        self.config_path = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'pair_plug' + os.path.sep
        
        os.makedirs(self.config_path, exist_ok=True)

    def exchange_plugged_chars(self, line):
        self.line = line.lower()

        if(not line):
            print("String is empty")
            return None 

        self.plugged_config = self._read_pluged_config()

        temp_line = list(self.line)
        for i, self.char in enumerate(temp_line):
            if( self.char in self.plugged_config):
                    
                temp_line[i] = self.plugged_config[self.char]
            else:
                temp_line[i] = self.char
        return ''.join(temp_line)


    def _file_list(self):
        
        files = glob.glob(self.config_path + '*')

        return files


    def _read_pluged_config(self):
        files = self._file_list()
        
        plugged_config = {}
        for plugged_file in files:
            with open(plugged_file) as fh:
                char = fh.readline().strip()

                if (char == '' or not char.isalpha() ):
                    pass
                else:
                    num = str(ord(char) - 96)
            
                    map_char = chr(int(os.path.basename(plugged_file)[len(num):]) + 96)
                    plugged_config[char]     = map_char
                    plugged_config[map_char] = char

        return plugged_config


if __name__ == '__main__':
    
    test = '5aa-bzkt=b1'
    #test = '545'
    #test = '#$'
    #test = False
    plugboard_obj = Plugboard()
    plugged_str    = plugboard_obj.exchange_plugged_chars(test)
    
    unplugged_str  = plugboard_obj.exchange_plugged_chars(plugged_str)

    print("    Original String : ", test, ",\n    encripted string: " , plugged_str)
    print("    Decripted string: " , unplugged_str)

