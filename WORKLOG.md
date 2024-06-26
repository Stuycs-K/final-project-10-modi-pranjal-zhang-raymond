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

### 5/30/24

- Worked out the bugs to get a working SHA512 program, though the results don't match the calculator.
- Primarily focused on debugging and fixing type errors throughout the code.
- Focused on getting the output length to match 128.

### 5/31/24

- Continued debugging, using a completed Java version to see what certain values were *supposed* to be via println commands.
- Fixed the padding functionality, which incorrectly added the length to the end of the binary message.
- Decided on the correct functionality for filling out the list of all components.

### 6/3/24

- Started debugging the main part of the SHA512 function.
- Started converting the main datatype of the program into integers.

### 6/4/24

- Looked into the accumulation of integers in our sigma values, which were hurting the accuracy of the function.
- Researched bitwise operations to figure out how to rework our full binary adder for integers.

### 6/5/24

- Debugged rotateRight and sigma functions.
- Figured out summation errors in the constant addition during the algorithm.

### 6/6/24 - 6/7/24

- Rewrote entire body of the code to use lists instead of other representations.
- Got to correct hash length, focused on debugging rotateRight.
- Made strides on finding the exact iteration (#23) where the program breaks.

### 6/7/24

- Completed the SHA-512 algorithm (on call with Raymond), by fixing an incorrect constant.
- Fully debugged and cleaned up print statements from the code.
- Ran some test cases.
- Made a driver file to provide simple strings from the command line to hash (file capabilities possibly coming soon).

### 6/9/24

- Added a file hashing functionality for the algorithm, based on command line arguments.
- Added a makefile regarding code implementation, and updated the README accordingly.
- Completed video, finalized README and WORKLOG.

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

### 6/3/24

- peer programming yielded problems with signed & unsigned ints, more logical problems

### 6/4/24

- found and fixed an error in the rotate_right function that could be one of the causes of producing an extremely long hash

### 6/5/24

- peer programming yielded problems with signs

### 6/6/24

- peer programmed and rewrote much of our code together
- length of the hash is correct, trying to find out why iterations are going wrong (starts on 24th iteration)

### 6/7/24

- debugged rotate function with Pranjal in class
- turns out the problem was not any of the functions but the constant list
- after much debugging and the above realization, we've finished our SHA512 implementation

### 6/9/24

- created and recorded video

## References and Resources (Also in [PRESENTATION.MD](https://github.com/Stuycs-K/final-project-10-modi-pranjal-zhang-raymond/blob/main/PRESENTATION.md))

[General Facts link](https://komodoplatform.com/en/academy/sha-512/#:~:text=SHA%2D512%2C%20or%20Secure%20Hash,hashing%2C%20and%20digital%20record%20verification.)

[Medium article we used for the Algorithm](https://medium.com/@zaid960928/cryptography-explaining-sha-512-ad896365a0c1)

[Link to the Java implementation of SHA-512 that we used to help debug (trittimo)](https://github.com/trittimo/SHA512)