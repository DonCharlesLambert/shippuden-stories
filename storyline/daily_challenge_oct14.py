from storyline.common import Story, Scene
from characters.character import Naruto, Sasuke, Kakashi
from screens.background import TrainingGround, Forest

# Daily Challenge Story - October 14, 2025
# A story about a ninja training challenge

story = Story("Training Challenge")

# Scene 1: The Training Begins
scene1 = Scene(
    background=TrainingGround,
    narrator="It's a bright morning at the training ground. Naruto is excited for today's challenge!"
)
scene1.add_character(Naruto, position="center", expression="excited")
scene1.add_dialogue(Naruto, "Alright! I'm ready for any challenge! Believe it!")
scene1.add_character(Kakashi, position="right", expression="calm")
scene1.add_dialogue(Kakashi, "Good energy, Naruto. Today's training will test your teamwork and strategy.")

# Scene 2: Sasuke Arrives
scene2 = Scene(
    background=TrainingGround,
    narrator="Sasuke arrives at the training ground, ready for the challenge."
)
scene2.add_character(Naruto, position="left", expression="happy")
scene2.add_character(Sasuke, position="right", expression="serious")
scene2.add_dialogue(Sasuke, "Let's get this over with. I don't have time to waste.")
scene2.add_dialogue(Naruto, "Hey! We're teammates today, so let's work together!")

# Scene 3: The Challenge Begins
scene3 = Scene(
    background=Forest,
    narrator="Kakashi explains the mission: retrieve a scroll hidden deep in the forest."
)
scene3.add_character(Kakashi, position="center", expression="serious")
scene3.add_dialogue(Kakashi, "Your objective is to retrieve the scroll before sunset. You must work together.")
scene3.add_character(Naruto, position="left", expression="determined")
scene3.add_character(Sasuke, position="right", expression="confident")
scene3.add_dialogue(Naruto, "Leave it to us, Sensei!")

# Scene 4: Working Together
scene4 = Scene(
    background=Forest,
    narrator="In the forest, Naruto and Sasuke must combine their skills to overcome obstacles."
)
scene4.add_character(Naruto, position="left", expression="thinking")
scene4.add_character(Sasuke, position="right", expression="serious")
scene4.add_dialogue(Naruto, "There's a trap ahead. We need to be careful.")
scene4.add_dialogue(Sasuke, "I'll use my Sharingan to see through it. You create a distraction.")
scene4.add_dialogue(Naruto, "Got it! Shadow Clone Jutsu!")

# Scene 5: Success
scene5 = Scene(
    background=TrainingGround,
    narrator="Naruto and Sasuke return with the scroll, having completed the challenge together."
)
scene5.add_character(Kakashi, position="center", expression="proud")
scene5.add_character(Naruto, position="left", expression="excited")
scene5.add_character(Sasuke, position="right", expression="satisfied")
scene5.add_dialogue(Kakashi, "Well done. You both learned the value of teamwork today.")
scene5.add_dialogue(Naruto, "That was awesome! We make a great team!")
scene5.add_dialogue(Sasuke, "Hmph. Not bad... for today.")

# Add all scenes to the story
story.add_scene(scene1)
story.add_scene(scene2)
story.add_scene(scene3)
story.add_scene(scene4)
story.add_scene(scene5)

# Export the story
if __name__ == "__main__":
    story.play()
