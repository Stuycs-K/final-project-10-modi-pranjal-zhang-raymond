[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ecp4su41)
# THIS DOCUMENT IS REQUIRED
## Group Info

### Group Name: Rayjal

### Group Members: Pranjal Modi, Raymond Zhang

### Period: 10

## Overview

### SHA-512

We decided to implement SHA-512 in Python for our project. Belonging to the SHA-2 cryptographic hash functions family, SHA-512 is a hash function that helps encode important and sensitive data, like passwords, by turning input into fixed-length hash digests. These functions are well known for being versatile, collision-resistant, and irreversible. Although SHA-256 is most prevalently used, SHA-512 offers better security and is starting to become implemented more. That was one of our deciding factors in choosing to implement SHA-512 over SHA-256.

## Instructions

To run the program, first determine whether or not a file or individual message needs to be hashed. Also, make sure to be in the **main directory** of the repository, rather than the `src` directory, when running the code. To hash a file, run the command `make hashFile ARGS="fileName"`, in which the `fileName` is a full path to the desired file with the extension included. To hash a message, use the command `make hashMessage ARGS="message"`. In both situations. the output hash will be directed into the command line. No libraries or other ancillary code pieces are required to run this hashing algorithm; using the command formats above will provide the correct output. 

## Presentation

