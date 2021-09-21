#!/usr/bin/env python3

#         Python Stream Deck Library
#      Released under the MIT license
#
#   dean [at] fourwalledcubicle [dot] com
#         www.fourwalledcubicle.com
#

# Example script showing basic library usage - updating key images with new
# tiles generated at runtime, and responding to button state change events.

import os
import threading

from PIL import Image, ImageDraw, ImageFont
from StreamDeck.DeviceManager import DeviceManager
from StreamDeck.ImageHelpers import PILHelper

# Folder location of image assets used by this example.
ASSETS_PATH = os.path.join(os.path.dirname(__file__), "Assets")


# Generates a custom tile with run-time generated text and custom image via the
# PIL module.
def render_key_image(deck, icon_filename, font_filename, label_text):
    # Resize the source image asset to best-fit the dimensions of a single key,
    # leaving a margin at the bottom so that we can draw the key title
    # afterwards.
    icon = Image.open(icon_filename)
    image = PILHelper.create_scaled_image(deck, icon, margins=[0, 0, 20, 0])

    # Load a custom TrueType font and use it to overlay the key index, draw key
    # label onto the image a few pixels from the bottom of the key.
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_filename, 14)
    draw.text((image.width / 2, image.height - 5), text=label_text, font=font, anchor="ms", fill="white")

    return PILHelper.to_native_format(deck, image)


# Returns styling information for a key based on its position and state.
def get_key_style(deck, key, state):
    # Last button in the example application is the exit button.
# exit_key_index = deck.key_count() - 1

    keyA1 = 0
    keyA2 = 8
    keyA3 = 16
    keyA4 = 24

    keyB1 = 1
    keyB2 = 9
    keyB3 = 17
    keyB4 = 25

    keyC1 = 2
    keyC2 = 10
    keyC3 = 18
    keyC4 = 26

    keyD1 = 3
    keyD2 = 11
    keyD3 = 19
    keyD4 = 27

    keyE1 = 4
    keyE2 = 12
    keyE3 = 20
    keyE4 = 28

    keyF1 = 5
    keyF2 = 13
    keyF3 = 21
    keyF4 = 29

    keyG1 = 6
    keyG2 = 14
    keyG3 = 22
    keyG4 = 30

    keyH1 = 7
    keyH2 = 15
    keyH3 = 23
    keyH4 = 31

    if key == keyH4:

        name = "exit"

        icon = "{}.png".format("Exit")

        font = "Roboto-Regular.ttf"

        label = "Bye" if state else "Exit"

    elif key == keyA1:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyA2:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyA3:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyA4:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyB1:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyB2:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyB3:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyB4:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyC1:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyC2:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyC3:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyC4:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyD1:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyD2:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyD3:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyD4:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyE1:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyE2:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyE3:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyE4:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyF1:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyF2:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyF3:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyF4:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyG1:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyG2:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyG3:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyG4:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyH1:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyH2:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    elif key == keyH3:

        name = "emoji"

        icon = "{}.png".format("Pressed" if state else "Released")

        font = "Roboto-Regular.ttf"

        label = "Pressed!" if state else "Key {}".format(key)

    return {

        "name": name,

        "icon": os.path.join(ASSETS_PATH, icon),

        "font": os.path.join(ASSETS_PATH, font),

        "label": label

    }


# Creates a new key image based on the key index, style and current key state
# and updates the image on the StreamDeck.
def update_key_image(deck, key, state):
    # Determine what icon and label to use on the generated key.
    key_style = get_key_style(deck, key, state)

    # Generate the custom key with the requested image and label.
    image = render_key_image(deck, key_style["icon"], key_style["font"], key_style["label"])

    # Use a scoped-with on the deck to ensure we're the only thread using it
    # right now.
    with deck:
        # Update requested key with the generated image.
        deck.set_key_image(key, image)


# Prints key state change information, updates rhe key image and performs any
# associated actions when a key is pressed.
def key_change_callback(deck, key, state):
    # Print new key state
    print("Deck {} key {} = {}".format(deck.id(), key, state), flush=True)

    # Update the key image based on the new key state.
    update_key_image(deck, key, state)

    # Check if the key is changing to the pressed state.
    if state:
        key_style = get_key_style(deck, key, state)

        # When an exit button is pressed, close the application.
        if key_style["name"] == "exit":
            # Use a scoped-with on the deck to ensure we're the only thread
            # using it right now.
            with deck:
                # Reset deck, clearing all button images.
                deck.reset()

                # Close deck handle, terminating internal worker threads.
                deck.close()


if __name__ == "__main__":
    streamdecks = DeviceManager().enumerate()

    print("Found {} Stream Deck(s).\n".format(len(streamdecks)))

    for index, deck in enumerate(streamdecks):
        deck.open()
        deck.reset()

        print("Opened '{}' device (serial number: '{}')".format(deck.deck_type(), deck.get_serial_number()))

        # Set initial screen brightness to 30%.
        deck.set_brightness(30)

        # Set initial key images.
        for key in range(deck.key_count()):
            update_key_image(deck, key, False)
        

        # Register callback function for when a key state changes.
        deck.set_key_callback(key_change_callback)

        # Wait until all application threads have terminated (for this example,
        # this is when all deck handles are closed).
        for t in threading.enumerate():
            if t is threading.currentThread():
                continue

            if t.is_alive():
                t.join()
