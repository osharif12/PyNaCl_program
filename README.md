# PyNaCl_program
Encrypting files using PyNaCla

This repo consists of pynacl-test.py, config.json, and text files that are used for encryption. The program pynacl takes user input to generate private keys and public keys to create shared keys. Once shared keys are created they will be used to encrypt files and decrypt files. The library that is used is PyNaCl which is based off of Nacl and replicates public key cryptography. 

In this example I am looking for all text files in a given directory and given the user input, I will either encrypt all the files or decrypt all the files. The encryption keys that are generated will be stored in config.json. The purpose of this project is to better understand public key cryptography, elliptic curves, hashing algorithms, and the field of cryptography in general. It is also to understand how Ransomware attacks are carried out. 