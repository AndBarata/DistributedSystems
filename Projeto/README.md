# real Semaphore Clock Syncronization

This project demonstrates the concept of semaphore synchronization using Raspberry Pi 4 devices. Multiple semaphores, represented by individual Raspberry Pi 4s, are programmed to transition between red, yellow, and green states without any direct communication between them. Each semaphore's decision is based solely on its internal timer. The syncronization is ensure by Network Time Protocol - NTP, where the master clock is one of the nodes 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

- Connect the rasps to the same network by using the hotspot in one of them
- Run the NTPserver.py on the master and NTPclient.py on the slaves. Note that a sigle rasp can be slave and master
- 




