class Node:
    def __init__(self, img, val, level, state = None):
        self.image = img    # img_path
        self.caption = ''
        self.val = val      # string/story for this image
        self.level = level  # depth [0, 1, or 2]
        self.state = state  # win/lose for all levels except 0
        self.left = None    # lose
        self.right = None   # win