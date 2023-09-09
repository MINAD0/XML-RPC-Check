# XML-RPC Vulnerability Checker and Directory Fuzzer

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

This repository contains a versatile Bash script for assessing web application security. It offers two primary functionalities: XML-RPC vulnerability checking and directory fuzzing using the powerful "ffuf" tool.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

### XML-RPC Vulnerability Check
- Quickly assess whether a given URL is vulnerable to XML-RPC exploits.
- Detects if the target's XML-RPC server accepts POST requests only.
- Provides clear and informative results for each operation.

### Directory Fuzzing with ffuf
- Utilizes the powerful "ffuf" tool to perform directory and page fuzzing.
- Discover hidden directories, files, and endpoints on web servers.
- Ideal for reconnaissance and identifying potential attack vectors.
- Supports customizable wordlists for directory fuzzing.

## Getting Started

### Prerequisites
- A Linux-based operating system (tested on Ubuntu).
- The "curl" and "ffuf" tools installed on your system.
- Basic knowledge of web security and directory fuzzing.

### Installation
1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/MINAD0/XML-RPC-Check.git
   cd XML-RPC-Check
   chmod +x xmlrpc.sh
