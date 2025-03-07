# Python Project

## Description

This project was made just for fun—it's kind of a mini-game.

## Why Did I Make This Project?

I wanted to learn about Python libraries and some aspects of cybersecurity and encryption, and I learned a lot in the process.

## What Did You Learn?

1. Cryptography: One of the best encryption libraries. It allows you to generate random keys for encrypting data and offers many more features related to security.

2. PyArmor: This library is used to encrypt Python code, making it unreadable. While it might be possible to decrypt the code somehow, it adds a good layer of safety.

3. Argon2: This is used to prevent dictionary attacks and attacks that require significant computing power. It's one of the best password hashing algorithms currently available.

4. Salt: This is basically some random characters added to a password to protect against dictionary attacks, especially if your password is weak.

5. TPM (Trusted Platform Module): This is a chip on the motherboard made for security reasons. It holds a main encryption key that no one can access and is used to generate and store encrypted keys. There's a library to use the TPM, but it works only on Linux. There are ways to use it on Windows, but it's more complicated by using the Windows API.

6. Managing Dependencies: Learned how to install and manage external libraries, ensuring my project has all the necessary requirements to run properly.

7. Open Source Contribution: Understood the importance of sharing projects on platforms like GitHub to exchange knowledge and benefit from others' feedback.

8. Improving Coding Skills: Enhanced my programming skills and problem-solving abilities through this project.

## Why Don't You Include Those Libraries in Your Code?

Because it's not necessary for this project. As you can see, my code does not use any passwords, and I have actually included some of those libraries I mentioned.

## Why Did You Publish It on GitHub?

Because I want my friends to see and edit the code. Also, I want it to be my first open-source project, allowing me to contribute to the developer community and receive feedback and improvements.

## How Can I Download the Project? Or I Downloaded It but It's Not Working

To download the project, I recommend downloading the .zip file from the repository. You will find three main files:

1. data (folder): Contains necessary data for the project.
2. tea_pot.png: An image used within the project.
3. main.py: The main Python script containing the code.

If any of these files are missing or corrupted, the project might not run correctly. Also, it might not work because you need to download the required libraries mentioned in the code.

## Requirements

You need to install the cryptography library to run the project. You can install it using the following commands:

If Python is not added to your system variables:

python -m pip install cryptography


Or, if you have Python added to your system variables:

pip install cryptography


Make sure you're using the appropriate version of Python and that all other required libraries are installed.
