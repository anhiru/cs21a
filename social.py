# ----------------------------------------------------------------------------
# Name:         social
# Purpose:      describe a social profile
#
# Author:       Andrew Tran
# Date:         06/19/2019
# ----------------------------------------------------------------------------
"""
Module to outline a Profile class
"""


class Profile(object):
    """
    Represent a person's social profile

    Argument:
    name: a person's name -- assumed to uniquely identify a person (string)

    Attributes:
    name: a person's name -- assumed to uniquely identify a person (string)
    statuses: a list containing a person's statuses (list)
    friends: set of friends for the given person.
            It is the set of profile objects representing these friends. (set)
    """

    def __init__(self, name):
        self.name = name
        self.statuses = []
        self.friends = set()

    def add_friend(self, friend_profile):
        """
        Establish a mutual friendship

        :param friend_profile: profile object (Profile)
        :return: None
        """
        self.friends.add(friend_profile)
        friend_profile.friends.add(self)

    def get_friends(self):
        """
        Return an alphabetical list of names of the person's friends

        :return: names of the person's friends in alphabetical order (list)
        """
        names = set()
        for profile in self.friends:
            names.add(profile.name)
        return sorted(names)
