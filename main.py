from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

textures = ['white_cube', 'grass', 'brick']
selected_texture = 0

app = Ursina()
window.borderless = False
window.exit_button.visible = False

class Voxel(Button):
    def __init__(self, position=(0,0,0), texture='white_cube'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color.white,
            highlight_color=color.lime
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                Voxel(position=self.position + mouse.normal, texture=textures[selected_texture % len(textures)])

            if key == 'right mouse down':
                destroy(self)

for z in range(20):
    for x in range(20):
        Voxel((x, 0, z))

player = FirstPersonController()

def update():
    if held_keys['escape']:
        mouse.locked = False

    if held_keys['left mouse']:
        mouse.locked = True

# this is better for detecting a key pressed, not held down
def input(key):
    global selected_texture

    if key == 'tab':
        selected_texture += 1

app.run()
