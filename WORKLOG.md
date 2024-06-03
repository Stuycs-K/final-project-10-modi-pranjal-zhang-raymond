# Work Log

## Pranjal Modi

### 5/22/24

- Created a git branch 'pmodi'.
- Continued looking into previous deployments of the SHA-256 algorithm as an example for SHA-512 implementations.

### 5/23/24

- Created a 'src' folder to hold all of the code (for now, a helper file and the main file, both in Python).
- Coded some helper functions regarding bitstrings, message padding, and zeros padding into the helper file.
- Finished entire message padding functionality (preparation of message *mainly* done).

### 5/24/24

- Implemented a binary adder, which has an implemented carry-in bit, of two bitstrings of the same length.
- Added some elementary bitstring manipulation operations, including right and left-rotation.
- Planned a bit ahead as to integration of these helper functions into the main algorithm.

### 5/27/24

- Continued research into SHA-512 algorithm, along with possible ways to employ the recently-created bit rotators.
- Sketched out in a separate doc a play-by-play for the algorithm.

### 5/28/24

- Started working on the body of the SHA512 algorithm, implementing chunk processing, some manipulation of constants, and the framework for the rest of it.
- Continued clarifying constant creation in byteFunc.
- Researched into how to cycle variables in the SHA512 main loop.

### 5/29/24

- Completed a rudimentary form of the SHA512 algorithm in SHA512.py. Began debugging the various errors that cropped up, including type mismatches and unexpected length changes.
- Implemented the final for loop in the SHA512 algorithm, which updates the constants of the program repeatedly.

## Raymond Zhang

### 5/22/24

- created git branch 'raymond'
- started writing README with information about SHA-512

### 5/23/24

- wrote helper function splitIntoBlocks
- imported constants into SHA512 file
- currently in the process of learning more about how the hashes are processed so that I can write the processBlock function

### 5/24/24

- helper functions merged into src/byteFunc.py
- researched hash function with the 80 iterations
- spent time researching and thoroughly understanding the processing blocks section of the SHA-512 algorithm
- outlined the steps needed for the processing function

### 5/27/24

- completed large and small sigma functions
- found conflicting algorithms for implementation of SHA-512, will investigate

### 5/28/24

- merged sigma functions onto main
- peer programmed with Pranjal on process function
- completed ch and maj functions

### 5/29/24

- peer programmed with Pranjal on finishing process function & debugging (at this point, working on separate branches is less conducive to workflow)
- more research into clarifying types of inputs and outputs of helper functions (we believe that's our main issue)

### 5/30/24 

- peer programming: we worked out all the syntax errors, now we need to figure out why our hash is so long (and therefore incorrect)
- spent ~20 minutes at home looking through logic, didn't find anything so far

### 5/31/24 

- peer programming yielded problem with surroundZero function, fixed, so we now have correct array of binaries

### 6/2/24

- started detailing the README