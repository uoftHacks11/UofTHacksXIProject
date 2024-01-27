import cohere
import os
from dotenv import load_dotenv
from binary_tree import *
load_dotenv()

api_key = os.getenv('COHERE_API_KEY')
co = cohere.Client(api_key)

prompt="""Predict what I experienced based on these captions in order using first person narrative (I):
    a large jetliner sitting on top of an airport tarmac,
    a computer science guy coding on the phone
"   tasteful spaghetti
    "For each caption output, keep it 3 sentences, and seperate each caption output,
    but ensure that the storyline between caption outputs is consistent. Only return the 3 captions and nothing else.
    Use this format for the output:
    [sentences for caption 1]
    [sentences for caption 2]
    [sentences for caption 3]"""

def generate_text(prompt, temp=0):
  chat_hist = []
  response = co.generate(
    model='command',
    prompt=prompt,
    temperature=0.0,
    # chat_history=[
    #     {"role": "Chatbot", "message": {response.generations[0].text}}
    # ]
    )
  chat_hist.append(response.generations[0].text)
  return response.generations[0].text


response_text = generate_text(prompt)
story_parts = response_text.split("\n")
story_parts = [part for part in story_parts if part.strip()]


# print(response.generations[0].text)


def create_game_tree(root_val, max_level):
    root = Node(root_val, 1, 'start')
    _expand_tree(root, 2, max_level)
    return root

def _expand_tree(node, current_level, max_level):
    if current_level == max_level:
        return

    win_story = generate_text(f"Win story for level {current_level - 1}")
    lose_story = generate_text(f"Lose story for level {current_level - 1}")

    node.left = Node(generate_text(prompt + ""), current_level + 1, 'win')
    node.right = Node(generate_text(prompt + ""), current_level + 1, 'lose')

    # _expand_tree(node.left, current_level + 1, max_level)
    # _expand_tree(node.right, current_level + 1, max_level)

def print_game_tree(node, path=[]):
    if node:
        path.append((node.val, node.state))
        if node.left is None and node.right is None:
            print("".join([f"{p[0]}" for p in path]))
        else:
            print_game_tree(node.left, path.copy())
            print_game_tree(node.right, path.copy())

root_story = "Original story"
max_game_level = 3
game_tree = create_game_tree(root_story, max_game_level)
print_game_tree(game_tree)
