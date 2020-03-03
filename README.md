# ProxySplit

A python script to convert different types of proxy lists to other formats

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What you need to run the script

```
Python3 installed
A proxylist in any of the following formats

<Proxy XX 1.00s [TYPE] XX.X.XXX.XX:PORT> (format from proxybroker)

TYPE    XX.X.XXX.XX:XX  PORT (format from proxychains)

type(s)://XX.X.XXX.XX:PORT

```

### Usage

You run the program with 3 command line arguments
1. input list
2. name of the output list
3. output list type/export type which currently has two options: 1 for 'TYPE   xx.xxx.xx.x PORT' or 2 for 'type://xx.xxx.xx.x:port (more types to be added in the future!)

Example: ./proxysplit.py proxybrokerlist chainsfriendlylist 1



## Stuff to add

* export multiple formats at once
* several inputs at once
* add more formats
* fix the problems that occur if proxybroker output has more than 1 type(for example: <Proxy XX 1.00s [HTTP,HTTPS]...> )



* **LazyLucy** [PurpleBooth](https://github.com/lazylucy)


## License

This project is licensed under the GNU GPL v3.0 License - see the [LICENSE.md](LICENSE.md) file for details
