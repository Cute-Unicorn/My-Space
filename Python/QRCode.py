import qrcode

img = qrcode.make('https://www.instagram.com/p/Cd1fcT1paAE/')
type(img)  # qrcode.image.pil.PilImage
img.save("Morgana.png")