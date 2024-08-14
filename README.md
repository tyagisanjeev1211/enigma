# enigma
A cryptographic tool called the Enigma machine was created and used during the early to mid-20th century to safeguard military, diplomatic, and commercial communications.

![center text](https://ds055uzetaobb.cloudfront.net/brioche/uploads/8lhMEciVlk-enigma.jpg "enigma")

First this was invented and used to safeguard bank communications, the device was created in 1918. Later the German military forces adopted and improved it because it ran on batteries and was therefore portable.

# How Enigma operated 
Enigma was a novel type of encryption that did not rely on codebooks or hand ciphers, but rather on **electro-machines**. With an electro-mechanical cipher machine, it could produce 159 million million million different configurations of cipher. 
- Encrypted text was produced by first **mumbling characters** from a **plug board** of electrical circuits using the inputs then that character entered into the moving **mechanical rotors**. 
The rotors' starting positions—which could be changed in any order—were what determined ciphering. 
- Unless the recipient understood the rotor and plug board settings on the day the enciphered text was produced, the text the machine produced was unreadable. The Germans reset their Enigma machines at midnight every night to preserve security, since understanding the machine's settings was essential to decoding the communications.
- Different configurations and marginally different machines were used by each network.
- Enigma machine operators received a key sheet printed with their network's settings.

# How this code works 
There are three classes written for different functionalities 

- Plugboard
- Wheel
- Rotor

#### Plugboard 
To incorporate the features of the Enigma machine's electric plugboard, the Plugboard class was developed. You must create a simple file in the **plug_board folder** with naming standards such as the index of **input character** and the index of **output character** from the plugboard in order to enable a plug for any character. The input character appears as single charater only in the first line of that file.
The encryption and decryption operations both utilize this file.
##### Example 
If a user want that alphabet "a" would be changed to "s" then the file name would be 119 (index of "a" is one and index of "s" is 19), and "a" would appear as a single character in the file's first line. 

#### Wheel 
The purpose of the Wheel class is to initialize the Rotors wheel. Every wheel has an initial code, which can be modified, with an initial character serving as the starting point. The original code that was used to encrypt the text must match in order to decrypt it.

#### Rotors
The wheels must be initialized by the **Roters class**. 
- The rotors of a mechanical enigma machine have three wheels; however, this code allows the wheel count can be modified by specifying the count of **levels**, with three being the minimum number of levels.
- The mechanical enigma machine can go forward one step once each character is cyphered. This code also allows to configure it with the class parameter **steps**. One is the default value.
- The Enter wheel's default position is "d," but you may adjust it by passing the beginning character to the class parameter **position**.  
- Using temp_position, internal logic has been built to set the position of other wheels.

## Example 
```
input_str = 'Sanjeev Tyagi'
# creating a Roters class with entry wheel position as 'j', parameter levels has a default value of 3, and parameter steps has a default value of 3.
rotor   = Rotors(position='j')

rotor.init_wheels()                           ## Initializing wheels in Rotors 

pb_obj  = pb.Plugboard()                      ## Initializing 
pb_str  = pb_obj.exchange_plugged_chars(input_str)    ## processed charaters from Plugboard 
ret     = rotor.process_line(pb_str)          ##  Get encrypted value from Roters 


## Decrypting for same string 
rotor   = Rotors(position='j')               ## reinitializing Rotors            
rotor.init_wheels()                          ## Wheels with same value as used to encrypt string  
de_ret     = rotor.process_line(ret,encripted=True)    ## additional parameter as encripted string is passed 

de_pb_str  = pb_obj.exchange_plugged_chars(de_ret)     ## changed Plugged characters
```


