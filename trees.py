class Story:
    def __init__(self, story, isGood):
        self.story = story
        self.isGood = isGood
        self.level = 1
    
    def update_story(self, level):
        self.level = level
        
      
class Tree:
    def __init__(self, initial_story):
        self.initial_story = Story(initial_story, True)

        self.left = Story("", False)
        self.left.level += 1
        self.right = Story("", True)
        self.right.level += 1

        self.left.left = Story("", False)
        self.left.left.level += 1
        self.left.right = Story("", True)
        self.left.right.level += 1
        
        self.right.left = Story("", False)
        self.right.left.level += 1
        self.right.right = Story("", True)
        self.right.right.level += 1
        
    def add_stories(self, stories): # List of stories, all 8 in order
        pass