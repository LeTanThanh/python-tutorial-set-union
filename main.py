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
