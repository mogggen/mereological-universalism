# The duel of the State-machines

## Instructions
* '+' - increment Value at carret
* '-' - decrement Value at carret
* '<' - reverse address pointer
* '>' - traverse address pointer
* '\[' - beginning of scope, check if carret value is non-zero, otherwise go past end of scope to the preceding instruction
* ']' - end of scope, return to beginning of newest scope

## Deviations
* '.' - reads the content of the oppnent's carret and writes to the players carret
* ',' - reads from the player's carret and writes to the oppnents carret

## Rules
* Each Player is allowed 32 states
* Every state has to be unique
* Each player has a total of 512 steps
* Each player has 8 bytes, storing a value between 0-255
* Each one of the player's state has a distinct value assigned to it

## Logic
* Overflowing/underflowing of array indices and byte values is permitted
* bytes has to be picked by the player, and the state with corresponding value runs
* The carret does not return between turns
* every instruction run on that cost 1 step, including repeats
* open scope instructions are automatically closed the end of the file

## Initial arrangment
1. Each player pick what values will represent what state (between 0-255)
2. Player swap half their states at random, and place their state in the closest Fit (rounding down)
3. The values of the bytes are randomized for both players
4. The Player that goes second, gets one extra state starting at the board

## Termination
* If a player has no bytes that represent a state left, they lose
* If a player has no steps left, they lose
