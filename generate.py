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

        Strictly adhere to the following output format and don't deviate from it:
        "
        [sentences for caption 1]
        ###
        [sentences for caption 2]
        ###
        [sentences for caption 3]
        "

        The output should be parse-able using [s.replace('\n', '').replace('"', '') for s in coo.split('###')].
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

        Strictly adhere to the following output format and don't deviate from it:
        "
        {prev[0]}
        ###
        [sentences for caption 2]
        ###
        [sentences for caption 3]
        "

        The output should be parse-able using [s.replace('\n', '').replace('"', '') for s in coo.split('###')].
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
        on the format below. Generate only the sentences. Strictly adhere to the format and don't generate any additional
        text asking acknowledging the instructions or asking if the output is satisfactory. Ensure that the storyline between 
        the outputs for the remaining captions is consistent with the story introduced by the first caption and the second caption.

        Strictly adhere to the following output format and don't deviate from it:
        "
        {prev[0]}
        ###
        {prev[1]}
        ###
        [sentences for caption 3]
        "

        The output should be parse-able using [s.replace('\n', '').replace('"', '') for s in coo.split('###')].
        """

    # chat_hist = []
    response = co.generate(
        model='command',
        prompt=prompt,
        temperature=0.0,
    )
    # chat_hist.append(response.generations[0].text)
    return response.generations[0].text


def process_co_output(coo):
    print(coo)
    return [s.replace('\n', '').replace('"', '') for s in coo.split('###')]


def create_game_tree(imgs):
    root = Node(imgs[0], '', 0)

    # level 1
    root.left = Node(imgs[1], '', 1, 'lose')
    root.right = Node(imgs[1], '', 1, 'right')
    
    # level 2
    root.left.left, root.left.right = Node(imgs[2], '', 2, 'lose'), Node(imgs[2], '', 2, 'right')
    root.right.left, root.right.right = Node(imgs[2], '', 2, 'lose'), Node(imgs[2], '', 2, 'right')

    return root


'''
class Node:
    def __init__(self, img, val, level, state = None):
        self.image = img    # img_path
        self.caption = ''
        self.val = val      # string/story for this image
        self.level = level  # depth [0, 1, or 2]
        self.state = state  # win/lose for all levels except 0
        self.left = None    # lose
        self.right = None   # win
'''

def populate_tree(root, captions):
    # assume generate_text generates winning text
    gen = process_co_output(generate_text(captions))

    root.caption, root.val = captions[0], gen[0]
    root.right.caption, root.right.val = captions[1], gen[1]
    root.right.right.caption, root.right.right.val = captions[2], gen[2]

    gen2 = process_co_output(generate_text_level_three(captions, gen[:2]))
    root.right.left.caption, root.right.left.val = captions[2], gen2[2]

    gen_left_from_root = process_co_output(generate_text_level_two(captions, gen[:1]))
    root.left.caption, root.left.val = captions[1], gen_left_from_root[1]
    root.left.right.caption, root.left.right.val = captions[2], gen_left_from_root[2]

    gen_remaining = process_co_output(generate_text_level_three(captions, gen_left_from_root[:2]))
    root.left.left.caption, root.left.left.val = captions[2], gen_remaining[2]

# def _expand_tree(node, current_level, max_level):
#     if current_level == max_level:
#         return

#     win_story = generate_text(f"Win story for level {current_level - 1}")
#     lose_story = generate_text(f"Lose story for level {current_level - 1}")

#     node.left = Node(generate_text(prompt + ""), current_level + 1, 'win')
#     node.right = Node(generate_text(prompt + ""), current_level + 1, 'lose')

#     # _expand_tree(node.left, current_level + 1, max_level)
#     # _expand_tree(node.right, current_level + 1, max_level)

def print_tree(root, level=0, prefix="Root: ", state=""):
    if root is not None:
        if level == 0:
            print(f"{prefix}{root.caption} - {root.state} ({root.level})")
        else:
            print(f"{' ' * (level * 4)}|-- {root.caption} - {root.state} ({root.level})")

        print_tree(root.left, level + 1, "Left: ", root.state)
        print_tree(root.right, level + 1, "Right: ", root.state)


if __name__ == "__main__":
    image_paths_3 = ['./images/biking.jpg', './images/monke.jpg', './images/rohan.jpeg']

    captions = predict_step(image_paths_3)

    root = create_game_tree(image_paths_3)
    populate_tree(root, captions)
    print_tree(root)
