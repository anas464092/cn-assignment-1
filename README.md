# Distributed File Download System

This assignment demonstrates a distributed file download system using Python. A large file is split into smaller fragments, hosted on multiple servers, and downloaded by a client application that recombines the fragments into the original file. The system is designed to simulate fault tolerance by handling random server failures.

---

## Table of Contents

1. [Overview](#overview)
2. [Modules](#modules)
3. [Setup](#setup)
4. [Usage](#usage)
5. [How It Works](#how-it-works)

---

## Overview

The system includes:

-   A **file generator** to create a large dummy file for testing.
-   A **file splitter** to divide the large file into smaller fragments.
-   Three **servers**, each hosting a single fragment of the file.
-   A **client application** that downloads file fragments concurrently and recombines them into the original file.

---

## Modules

### 1. `large_file_creater.py`

Generates a large file with repeating English text.

-   **Inputs:**
    -   `file_path`: Path where the file will be saved.
    -   `size_in_mb`: Size of the file in MB.
-   **Output:** A file of the specified size.

### 2. `split_file.py`

Splits the large file into smaller fragments.

-   **Inputs:**
    -   `file_path`: Path to the large file.
    -   `chunk_size`: Size of each chunk in bytes.
-   **Output:** Fragment files (`file_fragment_1.dat`, `file_fragment_2.dat`, etc.).

### 3. `server1.py`, `server2.py`, `server3.py`

Servers that host file fragments.

-   **Inputs:**
    -   `fragment_file`: The file fragment to serve.
    -   `port`: The port on which the server listens.
-   **Output:** Serves file fragments to connected clients.

### 4. `client.py`

Downloads file fragments from servers and recombines them.

-   **Inputs:**
    -   List of server IPs, ports, and file fragments.
-   **Output:** The original recombined file (`recombined_large_file.dat`).

---

## Setup

### Prerequisites

-   Python 3.x installed on your system.
-   Basic knowledge of Python sockets and threading.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/anas464092/cn-assignment-1.git
    cd cn-assignment-1
    ```

### Usage

1. Generate a Large File:

    Run the large_file_creater.py script to generate a large test file.

    ```bash
    python large_file_creater.py
    ```

    Edit the script to specify the desired file size in MB.

2. Split the Large File:

    Run the split_file.py script to divide the large file into smaller fragments.

    ```bash
    python split_file.py
    ```

    Adjust the chunk size in the script as needed.

### Start Servers

Run each server script in separate terminals.

-   For `server1.py`:
    ```bash
    python server1.py
    ```
-   For `server2.py`:
    ```bash
    python server2.py
    ```
-   For `server3.py`:
    ```bash
    python server3.py
    ```

### Run the Client:

-   Run the client.py script to download fragments and recombine them.

    ```bash
    python client.py
    ```

## How It Works

### 1. File Creation

The `large_file_creater.py` script generates a large file containing repeating English text. This file is used for testing purposes.

### 2. File Splitting

The `split_file.py` script splits the large file into smaller chunks. These fragments are named `file_fragment_1.dat`, `file_fragment_2.dat`, etc.

### 3. Server Hosting

-   Each server script (`server1.py`, `server2.py`, etc.) hosts one file fragment.
-   Servers are implemented using TCP sockets to handle client requests.

### 4. Client Download

-   The `client.py` script connects to each server and downloads the corresponding file fragment.
-   Downloads are performed concurrently using Python's `threading` module.

### 5. File Recombination

Once all fragments are downloaded, the `client.py` script recombines them into the original file named `recombined_large_file.dat`.
