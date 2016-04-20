#!/usr/bin/env python3


def sleep_in(weekday, vacation):
	"""
	The parameter weekday is True if it is a weekday, and the parameter
	vacation is True if we are on vacation. We sleep in if it is not a
	weekday or we're on vacation. Return True if we sleep in.

	sleep_in(False, False) → True
	sleep_in(True, False) → False
	sleep_in(False, True) → True
	"""
	return False


def monkey_trouble(a_smile, b_smile):
	"""
	We have two monkeys, a and b, and the parameters a_smile and b_smile
	indicate if each is smiling. We are in trouble if they are both smiling or
	if neither of them is smiling. Return True if we are in trouble.

	monkey_trouble(True, True) → True
	monkey_trouble(False, False) → True
	monkey_trouble(True, False) → False
	"""
	return False


def sum_double(a, b):
	"""
	Given two int values, return their sum. Unless the two values are the same,
	then return double their sum.

	sum_double(1, 2) → 3
	sum_double(3, 2) → 5
	sum_double(2, 2) → 8
	"""
	return 0


def diff21(n):
	"""
	Given an int n, return the absolute difference between n and 21, except
	return double the absolute difference if n is over 21.

	diff21(19) → 2
	diff21(10) → 11
	diff21(21) → 0
	"""
	return 0


def count_evens(nums):
	"""
	Return the number of even ints in the given array. Note: the % "mod"
	operator computes the remainder, e.g. 5 % 2 is 1.

	count_evens([2, 1, 2, 3, 4]) → 3
	count_evens([2, 2, 0]) → 3
	count_evens([1, 3, 5]) → 0
	"""
	return 0


def xyz_there(s):
	"""
	Return True if the given string contains an appearance of "xyz" where the
	xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz"
	does not.

	xyz_there('abcxyz') → True
	xyz_there('abc.xyz') → False
	xyz_there('xyz.abc') → True
	"""
	return False


def is_prime(n):
	"""
	Return True if the given number is prime.

	is_prime(2) → True
	is_prime(4) → False
	is_prime(11) → True
	"""
	return False
