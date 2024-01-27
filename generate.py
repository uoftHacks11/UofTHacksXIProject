import cohere
import os
from image_captioning import predict_step
from dotenv import load_dotenv
from binary_tree import *
load_dotenv()

api_key = os.getenv('COHERE_API_KEY')
co = cohere.Client(api_key)


def generate_text(captions, temp=0):
  
    prompt=f"""Predict what I experienced based on these captions in order using first person narrative (I):
        {captions[0]},
        {captions[1]},
        {captions[2]}

        Ensure that for each caption, you generate exactly 4 sentences. Separate the output for each caption based
        on the format below. Strictly adhere to the format and ensure you don't generate anything that strays from the 
        format below. Ensure that the storyline between the outputs for the captions is consistent.

        Strictly adhere to the folling output format and don't deviate from it:
        "
        [sentences for caption 1]
        ###
        [sentences for caption 2]
        ###
        [sentences for caption 3]
        "
        """

    # chat_hist = []
    response = co.generate(
        model='command',
        prompt=prompt,
        temperature=0.0,
    )
    # chat_hist.append(response.generations[0].text)
    return response.generations[0].text


def generate_text_level_two(captions, prev, temp=0):
  
    prompt=f"""Predict what I experienced based on these captions in order using first person narrative (I):
        {captions[0]},
        {captions[1]},
        {captions[2]}

        The output for the first caption is: {prev[0]}

        Ensure that for the remaining captions, you generate exactly 4 sentences. Separate the output for each caption based
        on the format below. Strictly adhere to the format and ensure you don't generate anything that strays from the 
        format below. Ensure that the storyline between the outputs for the remaining captions is consistent with the
        story introduced by the first caption.

        Strictly adhere to the folling output format and don't deviate from it:
        "
        {prev[0]}
        ###
        [sentences for caption 2]
        ###
        [sentences for caption 3]
        "
        """

    # chat_hist = []
    response = co.generate(
        model='command',
        prompt=prompt,
        temperature=0.0,
    )
    # chat_hist.append(response.generations[0].text)
    return response.generations[0].text



def generate_text_level_three(captions, prev, temp=0):
  
    prompt=f"""Predict what I experienced based on these captions in order using first person narrative (I):
        {captions[0]},
        {captions[1]},
        {captions[2]}

        The output for the first caption is: {prev[0]}
        The output for the second caption is: {prev[1]}

        Ensure that for the remaining captions, you generate exactly 4 sentences. Separate the output for each caption based
        on the format below. Strictly adhere to the format and ensure you don't generate anything that strays from the 
        format below. Ensure that the storyline between the outputs for the remaining captions is consistent with the
        story introduced by the first caption.

        Strictly adhere to the folling output format and don't deviate from it:
        "
        {prev[0]}
        ###
        {prev[1]}
        ###
        [sentences for caption 3]
        "
        """

    # chat_hist = []
    response = co.generate(
        model='command',
        prompt=prompt,
        temperature=0.0,
    )
    # chat_hist.append(response.generations[0].text)
    return response.generations[0].text

'''
class Node:
    def __init__(self, img, val, level, state = None):
        self.image = img    # img
        self.val = val      # string/story for this image
        self.level = level  # depth [0, 1, or 2]
        self.state = state  # win/lose for all levels except 0
        self.left = None 
        self.right = None
'''

def create_game_tree(img, root_val, max_level):
    root = Node(img, root_val, 1, 'start')

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


if __name__ == "__main__":
    image_paths_3 = ['./images/biking.jpg', './images/monke.jpg', './images/rohan.jpeg']

    captions = predict_step(image_paths_3)

    coo = generate_text(captions)
    coo = [s.replace('\n', '').replace('"', '') for s in coo.split('###')]
    print(coo)
