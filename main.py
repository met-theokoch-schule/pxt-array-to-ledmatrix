strip = neopixel.create(DigitalPin.C8, 64, NeoPixelMode.RGB)
strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
strip.set_pixel_color(9, neopixel.colors(NeoPixelColors.RED))
strip.show()

def on_forever():
    basic.show_icon(IconNames.HEART)
basic.forever(on_forever)
