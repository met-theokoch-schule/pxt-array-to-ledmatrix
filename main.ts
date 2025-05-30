let strip = neopixel.create(DigitalPin.C8, 64, NeoPixelMode.RGB)
strip.showColor(neopixel.colors(NeoPixelColors.Black))
strip.setPixelColor(9, neopixel.colors(NeoPixelColors.Red))
strip.show()

basic.forever(function on_forever() {
    basic.showIcon(IconNames.Heart)
})
