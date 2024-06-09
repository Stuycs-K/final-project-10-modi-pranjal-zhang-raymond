[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ecp4su41)
# THIS DOCUMENT IS REQUIRED
## Group Info

### Group Name: Rayjal
### Period: 10

## Overview

### SHA-512

SHA-512 is a hash function that helps encode important and sensitive data, like passwords, by turning input into hash digests. These hash digests have a fixed length. In the case of SHA-512, a 512-bit hash is created; compared to its predecessor SHA-256 which only creates hashes of 256 bits, SHA-512 is more secure. Designed by the NSA (National Security Agency), it was published in 2002. 

### Algorithm

1. Data is inputted. SHA-512 aims to turn this input into an output, the hash digest, of fixed length (512 bits). This hash digest needs to be uniformly distributed. If there is a fixed length, it is certain that there will be duplicate hash digests for certain different inputs. Uniform distribution ensures that each possible output value is equally likely given an input. Strong collision resistance is also important; it should not be feasible to find more than one input that results in the same hash digest.

## Instructions

To run the program, first determine whether or not a file or individual message needs to be hashed. Also, make sure to be in the **main directory** of the repository, rather than the `src` directory, when running the code. To hash a file, run the command `make hashFile ARGS="fileName"`, in which the `fileName` is a full path to the desired file with the extension included. To hash a message, use the command `make hashMessage ARGS="message"`. In both situations. the output hash will be directed into the command line. No libraries or other ancillary code pieces are required to run this hashing algorithm; using the command formats above will provide the correct output. 