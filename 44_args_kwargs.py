def f(*args, **kwargs):
  print("positional:", kwargs)

#f(10, 50, 25)
f(men=10, women=50, prefered_not_to_say=25)