if __name__ == "__main__":
  # Introduction to the set union

  s1 = { "Python", "Java" }
  s2 = { "C#", "Java" }

  print(s1)
  print(s2)
  print(s1.union(s2))

  # Union sets using union() method

  """
  new_set = set.union(another_set, ...)
  """

  s1 = { "Python", "Java" }
  s2 = { "C#", "Java" }
  s = s1.union(s2)

  print(s1)
  print(s2)
  print(s)

  # Union sets using the | operator

  """
  new_set = set1 | set2
  """

  s1 = { "Python", "Java" }
  s2 = { "C#", "Java" }
  s = s1 | s2

  print(s1)
  print(s2)
  print(s)

  # The union() method vs. set union operator

  """
  In fact, the union() method accepts one or more iterables, converts the iterables to sets, and performs the union.
  The following examples show how to pass a list to the union() method:
  """

  rates = {1, 2, 3}
  ranks = [2, 3, 4]
  ratings = rates.union(ranks)
  print(ratings)

  """
  However, the union operator (|) only allows sets, not iterables like the union() method.
  The following examples causes an error:
  """

  rates = {1, 2, 3}
  ranks = [2, 3, 4]
  # ratings = rates.union(ranks)
  # TypeError
