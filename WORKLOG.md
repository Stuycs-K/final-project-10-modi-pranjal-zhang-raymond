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

## Raymond Zhang

### 5/22/24

- created git branch 'raymond'
- started writing README with information about SHA-512

### 5/23/24

- wrote helper function splitIntoBlocks
- imported constants into SHA512 file
- currently in the process of learning more about how the hashes are processed so that I can write the processBlock function

### 5/24/24

- spent time researching and thoroughly understanding the processing blocks section of the SHA-512 algorithm
- outlined the steps needed for the processing function

### 5/27/24

- completed large and small sigma functions
- found conflicting algorithms for implementation of SHA-512, will investigate