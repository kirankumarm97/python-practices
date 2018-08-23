class a(Exception):
      pass
def call():
      raise a("if youcall i will raise")
try:
      call()
except a as e:
      print(e)
