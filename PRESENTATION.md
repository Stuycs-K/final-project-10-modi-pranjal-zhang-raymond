# SHA-512

### SHA-512 General Facts

SHA-512 is a hash function that was designed by the National Security Agency (NSA) and published by the National Institute of Standards and Technology (NIST) in 2001 as a Federal Information Processing Standard (FIPS).

SHA-512 helps encode important and sensitive data, like passwords, by turning input (SHA-512 is designed for input messages of up to $`2^128 - 1`$ bits) into hash digests. The algorithm is commonly used for email addresses, passwords, and digital record verification, but it is also used in blockchain technology. The hash digests have a fixed length of 512 bits, or 64 bytes. In the case of SHA-512, a 512-bit hash is created; compared to its predecessor SHA-256 which only creates hashes of 256 bits (32 bytes), SHA-512 is more secure. 

The strengths of SHA-512 include:

* **Resistance to many cryptographic attacks**
  For each of the 128 characters in the output of a SHA-512 hash digest, there are 16 possible characters (0-9 and a-f). 
  This yields $`16^128 \approx 1.34 * 10^154`$ possibilities.

* **Irreversible**
  Modular addition and bitwise rotation ensure that a hash digest cannot be traced back to the original message (without a rainbow table). 

* **Iterative Structure**
  Multiple rounds of processing (80, to be precise) that use specific mathematical functions amplify the *diffusion* and *avalanche* effects. This means that small changes in an input will generate completely different hashes.

* **Versatile** 
  Not only can SHA-512 be used for cryptography, it can also be used in many other information security and data management fields, like checksum verifications as well as checks for data integrity. 






### Algorithm

1. Data is inputted. SHA-512 aims to turn this input into an output, the hash digest, of fixed length (512 bits). This hash digest needs to be uniformly distributed. If there is a fixed length, it is certain that there will be duplicate hash digests for certain different inputs. Uniform distribution ensures that each possible output value is equally likely given an input. Strong collision resistance is also important; it should not be feasible to find more than one input that results in the same hash digest.


### Sources

https://komodoplatform.com/en/academy/sha-512/#:~:text=SHA%2D512%2C%20or%20Secure%20Hash,hashing%2C%20and%20digital%20record%20verification. 