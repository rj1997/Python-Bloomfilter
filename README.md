
# Python-Bloomfilter

Bloomfilters are a space and time efficient way to tell whether an object is present in a set or not. They are probabilistic in nature, can give **false positives** *(BloomFilter says present, but not actually present)* but never give **false negatives** *(BloomFilter says not present, but actually the item is present)*. 

A quick example will be, whenever you signup for a website, you need to input a username for your avatar. This username should not be taken up by any other user. 

In the Bloomfilter approach a set is made consisting of all the usernames already taken in the system. When we apply bloomfilters, the object even if it gives false positives, still will not allow username already taken to be submitted by the user. Though some non-present usernames in DB might get wasted,  bit we can trade-off that. Bloomfilters are much better than conventional methods like tries and hash-tables.

More about bloomfilters : [Bloomfilters](https://en.wikipedia.org/wiki/Bloom_filter)

# About the Project
The project allows three types of functionalities:
1. Using user given string query, tell the correct guess rate of bloomfilter vs set.
2. Simulates the queries for big data testing.
3. Implements a FIFO cache using bloomfilter to speedup the search from a conventional cache system.
 
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
Clone the repo using 
```
git clone https://github.com/rj1997/Python-Bloomfilter.git
```

### Prerequisites

Python3 along with pip is the requirement to run this project. Apart from that, you need the following packages:

```
mmh3
bitarray
```
Install them using pip from terminal.

### Installing

In the terminal, use these commands to install dependencies.

```
sudo pip install mmh3
sudo pip install bitarray
```

## Running the tests

To run each simulation use the following commands from terminal:

Using user given string query, tell the correct guess rate of bloomfilter vs set.
```
python3 basic_bloomfilter.py basic
```

Simulates the queries for big data testing.
```
python3 basic_bloomfilter.py simulation
```

Implements a FIFO cache using bloomfilter to speedup the search from a conventional cache system.
```
python3 basic_bloomfilter.py remote-cache-simulation
```


## Contributing

The work is still in progression, I will add more functionalities to this bloomfilter in some time.
But you are free to make pull requests and start commiting.


## Authors

* **Rishabh Jain** - *LinkedIn* - [rj1997](https://www.linkedin.com/in/rj1997/)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

