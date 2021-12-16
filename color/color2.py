#!/usr/bin/env python3

# import librarys
import crayons

def main():
    """run time code. Always indent under function"""

    # print 'red string' in red
    print(crayons.red('red string'))

    # Red White and Blue Text
    print(f"{crayons.red('red')} white {crayons.blue('blue')}")

    crayons.disable()

    # this line should NOT have color as crayons is disabled
    print(f"{crayons.red('red')} white {crayons.blue('blue')}")

    crayons.DISABLE_COLOR = False

    # this line will print in color because color is enabled
    print(f"{crayons.red('red')} white {crayons.blue('blue')}")

    # print 'red string' in red
    print(crayons.red('red string', bold=True))

    # print 'yellow string' in yellow
    print(crayons.yellow('yellow string', bold=True))

    # print magenta string in magenta
    print(crayons.magenta('magenta string', bold=True))

    # print 'white string' in white
    print(crayons.white('white string', bold=True))

# this condition is only true if our script is run directly
# it is NOT true if our code is impoted from another script

if __name__ == "__main__":
    main()
