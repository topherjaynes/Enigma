I'm curious in how the Enigma machine works. I think it would be fun to try and implement the mechanics in Python to learn the process and a little about the math. This is a journey to code it up and understand early cryptography. Phase II would be building a way to "break" the code. Yes, this was inpired by watching 'Imitation Game'

# Enigma

The machine was invented by German engineer Arthur Scherbius at the end of World War I and was commercially available for businesses to secure communication. The most complext version of the cipher machine were employed by the military, and they featured a plug board at the front to add extra complexity. 

The machine was a mix of mechanical and electrical. It looked like a bulky typewriter, that had an extra display of letters that would light up as a key was pressed on the mechanical keyboard. While complex, the basic idea was that when a key was pressed it would complete a circuit and light up the corresponding letter. The electrical path would go through the 3 rotors and wires to scramble the letters. The rotors and cables would be changed daily with new settings.


# Mathmatical Concepts
[Numberphile](https://youtu.be/G2_Q9FoD-oQ?si=vmdR90ubA5kDCcRI)

The machine scrambles the letters upon typing, but how does that secure the output? Because of the sheer number of settings it was thought to be nearly impossible break the code. You'd have to try each setting combination, decrypt the message, and then see if it made sense. 


# Flaws or hacks
An inputted letter couldn't be encrypted as itself. There was standard communication so would be able to look for common words to align on.


