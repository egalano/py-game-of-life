#!/usr/bin/env python
# E.G. Galano

import argparse
import curses
from pygameoflife.game import Game

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("board_width", type=int,help="Width of the game board")
    parser.add_argument("board_height", type=int,help="Height of the game board")
    parser.add_argument("--sleep", type=float, default=0.2, help="Amount of time between refresh (seconds)")
    parser.add_argument("--seed", type=str,default='rand', help="Inital seed pattern")
    parser.add_argument("-d", "--debug", action='store_true', help="Enables the game's debug view")
    args = parser.parse_args()

    gol = Game(height=args.board_height,
               width=args.board_width,
               sleep_time=args.sleep,
               debug=args.debug)
               
    gol.seed(args.seed)
    curses.wrapper(gol.draw)

if __name__ == '__main__':
    main()
