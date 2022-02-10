# Format War
Idelogy: merological-universalism (yes I have near to no knowledge of the meaning behind this word :D )

## Instructions
* '+' - increment Value at carret
* '-' - decrement Value at carret
* '<' - reverse address pointer
* '>' - traverse address pointer
### Standard
* '\{' - beginning of scope, check if carret value is non-zero, otherwise go past end of scope to the preceding instruction
### Beginner
* '\{' - beginning of scope, always enter scope, but exit the scope when it's at a new range
* '}' - end of scope, return to beginning of newest scope

## Deviations
* '?' - reads the content of the oppnent's carret and writes to the players carret
* '!' - reads from the player's carret and writes to the oppnents carret

## Rules
### Standard
* Each Player is allowed 32 states
* Every state has to be unique
* Each player has a total of 512 steps
* Each player has 8 bytes, storing a value between 0-63
* Each one of the player's state has a distinct value assigned to it

### Beginner
* Each Player is allowed 6 rules
* Each player has a total of steps every turn that is the total sum total of the buffer
* Each player has 8 bytes, storing a value between 0-255
* Each one of the player's rules has a range of value assigned to it

## Logic
### Standard
* Overflowing/underflowing of array indices and byte values is permitted
* bytes has to be picked by the player, and the state with corresponding value runs
* The carret does not reset between turns
* every instruction run on that cost 1 step, including repeats
* open scope instructions are automatically closed the end of the file

### Beginner
* Overflowing/underflowing of array indices and byte values is not permitted, and attempting one will cost the player a step
* bytes has to be picked by the player, and the rule with corresponding value range runs
* The carret does not reset between turns
* every instruction run on that cost 1 step, including repeats
* open scope instructions are automatically closed the end of the file

## Varations
* Make it possible by extra commands, to read buffer index
* Have a rule be drawn from a pool of random rules, every turn
* Make other players byte accessable by your carret
* Have underflows pop bytes, and overflows append them
* formula for max value: number of cells Max Value=4^(2+numCell), stepCap=2^(7+numCell)
   Example of how it could scale:
   4 / 128
   16 16 / 256
   64 64 64 / 512
   256 256 256 256 / 1024
   
## Initial arrangment
### Standard
1. Each player pick what values will represent what state (between 0-255)
2. Player swap half their states at random, and place their state in the closest Fit (rounding)
3. The values of the bytes are randomized for both players

### Beginner
1. Each player pick what values will represent what rules (between 0-255)
2. Player swap half their states at random, and place their state in the corresponding range
3. The values of the bytes at the beginning is assigned and is capped at 50 for the sum of the values om the buffer


## Termination
### Standard
* If a player has no bytes that represent a state left, they lose
* If a player has no steps left, they lose
### Beginner
* If a player reaches the final range (224-255) for their entire buffer, they win on their turn

* If a player reaches the Initial range (0-31) for their entire buffer, they lose on their turn
