# FacialVote
Facial recognition-based voting system

# Facial Recognition-Based Voting System

This project is a facial recognition-based voting system written in Python. It utilizes a CMake-based facial recognition library and employs the Eel framework to connect the backend Python code with the HTML and JavaScript frontend.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Sample Images](#Sample-Images)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Facial Recognition-Based Voting System aims to provide a secure and user-friendly voting platform. Users can register and vote using facial recognition technology, ensuring that each vote is unique and legitimate. The system includes advanced anti-spoofing measures to detect and prevent fraudulent attempts using photos or videos.

## Features

- User registration with facial recognition
- Secure voting process with facial verification
- Anti-spoofing technology to detect fake faces
- Real-time feedback and user interface
- Easy to use web-based frontend

## Installation

### Prerequisites

- Anaconda
- CMake
- Node.js and npm (for frontend dependencies)

### Steps

1. **Clone the repository**
    ```bash
    git clone https://github.com/Gokuls-lab/FacialVote.git
    cd FacialVote
    ```

2. **Create and activate the Anaconda environment**
    ```bash
    conda create -n FacialVote python=3.8
    conda activate FacialVote
    ```

3. **Install backend dependencies**
    ```bash
    pip install -r requirements.txt
    ```


## Usage

1. **Start the backend server**
    ```bash
    python main.py
    ```

2. **Access the frontend**
    Open a web browser and navigate to `http://localhost:8000`

# Sample-Images
## Register Page
![Sample register page image](https://github.com/Gokuls-lab/FacialVote/blob/main/ReadMe/register.png)
## Login Page
![Sample Login page image](https://github.com/Gokuls-lab/FacialVote/blob/main/ReadMe/login.png)
![Sample Login page image](https://github.com/Gokuls-lab/FacialVote/blob/main/ReadMe/login_face.png)
# Voting page
![Sample Login page image](https://github.com/Gokuls-lab/FacialVote/blob/main/ReadMe/vote.png)
## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any bugs, feature requests, or improvements.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


