"""This module contains password generation classes and functionality"""

from password_generator import utils

import datetime
import random

random.seed(datetime.datetime.now())

class LeftHand(object):
    INDEX = [
        ['$', 'R', 'F', 'V', '%', 'T', 'G', 'B', '^'],
        ['4', 'r', 'f', 'v', '5', 't', 'g', 'b', '6']
    ]

    MIDDLE = [
        ['#', 'E', 'D', 'C'],
        ['3', 'e', 'd', 'c']
    ]

    RING = [
        ['@', 'W', 'S', 'X'],
        ['2', 'w', 's', 'x']
    ]

    PINKY = [
        ['!', 'Q', 'A', 'Z'],
        ['1', 'q', 'a', 'z']
    ]

    def index_finger(self, is_capitalized):
        return self.__finger(self.INDEX, is_capitalized)

    def middle_finger(self, is_capitalized):
        return self.__finger(self.MIDDLE, is_capitalized)

    def ring_finger(self, is_capitalized):
        return self.__finger(self.RING, is_capitalized)

    def pinky_finger(self, is_capitalized):
        return self.__finger(self.PINKY, is_capitalized)

    def __finger(self, collection, is_capitalized):
        if is_capitalized:
            array = collection[0]
        else:
            array = collection[1]

        return array[random.randint(0, len(array) - 1)]


class RightHand(object):
    INDEX = [
        ['&', 'Y', 'H', 'N', '*', 'U', 'J', 'M'],
        ['7', 'y', 'h', 'n', '8', 'u', 'j', 'm']
    ]

    MIDDLE = [
        ['(', 'I', 'K', '<'],
        ['9', 'i', 'k', ',']
    ]

    RING = [
        ['(', 'O', 'L', '>'],
        ['9', 'o', 'l', '.']
    ]

    PINKY = [
        [')', 'P', ':', '?', '_', '{', '"', '+', '}'],
        ['0', 'p', ';', '/', '-', '[', '\'', '=', ']']
    ]

    def index_finger(self, is_capitalized):
        return self.__finger(self.INDEX, is_capitalized)

    def middle_finger(self, is_capitalized):
        return self.__finger(self.MIDDLE, is_capitalized)

    def ring_finger(self, is_capitalized):
        return self.__finger(self.RING, is_capitalized)

    def pinky_finger(self, is_capitalized):
        return self.__finger(self.PINKY, is_capitalized)

    def __finger(self, collection, is_capitalized):
        if is_capitalized:
            array = collection[0]
        else:
            array = collection[1]

        return array[random.randint(0, len(array) - 1)]

class Generator(object):
    FINGERS = {
        'f': LeftHand().index_finger,
        'd': LeftHand().middle_finger,
        's': LeftHand().ring_finger,
        'a': LeftHand().pinky_finger,
        'j': RightHand().index_finger,
        'k': RightHand().middle_finger,
        'l': RightHand().ring_finger,
        ';': RightHand().pinky_finger,
        ':': RightHand().pinky_finger,
    }

    @staticmethod
    def generate(pattern):
        output = ""
        for character in pattern:
            func = Generator.FINGERS[character.lower()]

            if not func:
                print "unknown pattern character: " + character
                continue
            
            is_capitalized = character <= 'a' or character == ':'

            output_character = func(is_capitalized)

            print character, is_capitalized, output_character

            output += output_character

        return output
