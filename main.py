import os
import discord
from dotenv import load_dotenv
import keep_alive

load_dotenv()
token = os.getenv('discordbottoken')

client = discord.Client()

def fetch_role(m):
  author_roles = [r.id for r in m.author.roles]
  for i, n in enumerate([985750157607985153, 987232675221868604]):
    if n in author_roles:
      return i
  return None

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')
@client.event
async def on_message(message):
  if message.channel.id == 985752337710723163 and not message.content.startswith("$"):
    counting_team = fetch_role(message)
    if counting_team is None:
      return None
    try:
      entry_count = int(message.content)
      wrong_counting = False
    except ValueError:
      wrong_counting = True
        
    f = open('number.txt', 'r')
    current_count = int(f.readline())
    correct_lst = f.readline()[:-1].split(",")
    error_lst = f.readline().split(",")
    f.close()
        
    if not wrong_counting and entry_count == current_count + 1:
      current_count += 1
      correct_lst[counting_team] = str(int(correct_lst[counting_team]) + 1)
    else:
      error_lst[counting_team] = str(int(error_lst[counting_team]) + 1)
    
    f = open('number.txt', 'w')
    f.writelines([str(current_count) + "\n", ",".join(correct_lst) + "\n", ",".join(error_lst)])
    f.close()
      
  if message.content.startswith("$score"):
    f = open('number.txt', 'r')
    f.readline()
    correct_lst = f.readline()[:-1].split(",")
    error_lst = f.readline().split(",")
    f.close()
    output = "This command is used for debugging and testing, not to be actually implemented"
    for i, name in enumerate(["Team Kusanali", "Team Yaoyao"]):
      output += f"\n{name}: has {correct_lst[i]} correct entries and {error_lst[i]} wrong entries"
    await message.channel.send(output)



keep_alive.keep_alive()
client.run(token)
